# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import time
import abc
import logging
import math
from threading import Timer
import six.moves.urllib as urllib
from .authentication_provider import AuthenticationProvider

logger = logging.getLogger(__name__)

_device_keyname_token_format = "SharedAccessSignature sr={}&sig={}&se={}&skn={}"
_device_token_format = "SharedAccessSignature sr={}&sig={}&se={}"

# Length of time, in seconds, that a SAS token is valid for.
DEFAULT_TOKEN_RENEWAL_INTERVAL = 3600

# Length of time, in seconds, before a token expires that we want to begin renewing it.
DEFAULT_TOKEN_RENEWAL_MARGIN = 120


class SelfSignAuthenticationProviderBase(AuthenticationProvider):
    """
    A base class for authentication providers which are able to sign themselves
    """

    def __init__(self, hostname, device_id, module_id):
        """
        Constructor for SymmetricKey Authentication Provider
        """
        logger.info(
            "Using symetric key authentication for (%s,%s)", device_id, module_id
        )

        AuthenticationProvider.__init__(self, hostname, device_id, module_id)
        self._token_update_timer = None
        self.token_renewal_interval = DEFAULT_TOKEN_RENEWAL_INTERVAL
        self.token_renewal_margin = DEFAULT_TOKEN_RENEWAL_MARGIN
        self.shared_access_key_name = None
        self.on_token_updated = None
        self.sas_token_str = None

    def __del__(self):
        self._cancel_token_update_timer()

    def generate_new_sas_token(self):
        """
        Force the SAS token to update itself.  This will cause a new sas token to be
        created, and self.on_sas_token_updated to be called.  The token update will
        be rescheduled based on the current time.
        """
        logger.info(
            "Generating new SAS token for (%s,%s) that expires %d seconds in the future",
            self.device_id,
            self.module_id,
            self.token_renewal_interval,
        )
        expiry = int(math.floor(time.time()) + self.token_renewal_interval)
        resource_uri = self.hostname + "/devices/" + self.device_id
        if self.module_id:
            resource_uri += "/modules/" + self.module_id
        quoted_resource_uri = urllib.parse.quote_plus(resource_uri)

        signature = self._do_sign(resource_uri, expiry)

        if self.shared_access_key_name:
            token = _device_keyname_token_format.format(
                quoted_resource_uri, signature, str(expiry), self.shared_access_key_name
            )
        else:
            token = _device_token_format.format(
                quoted_resource_uri, signature, str(expiry)
            )

        self.sas_token_str = str(token)
        self._schedule_token_update(
            self.token_renewal_interval - self.token_renewal_margin
        )
        self._notify_token_updated()

    def set_token_renewal_interval(self, token_renewal_interval, token_renewal_margin):
        """
        Update the token reneal interval for this authorization object.
        Thie method has the side-effect of generating a new token and restarting
        the token renewal timer.
        """
        logger.info(
            "changing renewal interval for (%s,%s) to (%d,%d)",
            self.device_id,
            self.module_id,
            token_renewal_interval,
            token_renewal_margin,
        )
        self.token_renewal_interval = token_renewal_interval
        self.token_renewal_margin = token_renewal_margin
        self.generate_new_sas_token()

    def _cancel_token_update_timer(self):
        """
        Cancel any future token update operations.  This is typically done as part of a
        teardown operation
        """
        if hasattr(self, "_token_update_timer") and self._token_update_timer:
            logger.info(
                "Canceling token update timer for (%s,%s)",
                self.device_id,
                self.module_id,
            )
            self._token_update_timer.cancel()
            self._token_update_timer = None

    def _schedule_token_update(self, seconds_until_update):
        """
        Schedule an automatic sas token update to take place seconds_until_update seconds in
        the future.  If an update was previously scheduled, this method shall cancel the
        previously-scheduled update and schedule a new update.
        """
        self._cancel_token_update_timer()
        logger.info(
            "Scheduleing token update for (%s,%s) for %d seconds in the future",
            self.device_id,
            self.module_id,
            seconds_until_update,
        )
        self._token_update_timer = Timer(
            seconds_until_update, self.generate_new_sas_token
        )
        self._token_update_timer.start()

    def _notify_token_updated(self):
        """
        Notify clients that the SAS token has been updated by calling self.on_sas_token_updated.
        In response to this event, clients should re-initiate their connection in order to use
        the updated sas token.
        """
        if self.on_token_updated:
            logger.info(
                "sending token update notification for (%s, %s)",
                self.device_id, 
                self.module_id,
            )
            # pylint: disable=not-callable
            self.on_token_updated()
        else:
            logger.info("_notify_token_updated: nobody to notify")

    def get_current_sas_token(self):
        """
        :return: The current shared access signature token
        """
        return self.sas_token_str

    @abc.abstractmethod
    def _do_sign(self, resource_uri, expiry):
        """
        Create and return a new signature for this object.  Caller is responsible for placing the
        signature inside the context of a SAS token string.
        """
        pass
