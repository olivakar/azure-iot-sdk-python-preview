# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import sys

from azure.iot.common.connection_string import (
    ConnectionString,
    HOST_NAME,
    SHARED_ACCESS_KEY_NAME,
    SHARED_ACCESS_KEY,
    SHARED_ACCESS_SIGNATURE,
    DEVICE_ID,
    MODULE_ID,
    GATEWAY_HOST_NAME,
)
from azure.iot.common.sastoken import SasToken

# Length of time, in seconds, that a SAS token is valid for.
DEFAULT_TOKEN_RENEWAL_INTERVAL = 3600

# Length of time, in seconds, before a token expires that we want to begin renewing it.
DEFAULT_TOKEN_RENEWAL_MARGIN = 120


class SymmetricKeyAuthenticationProvider(object):
    """
    A provider for authentication mechanism based on known authentication mechanisms ,
    including x509 and SAS based authentication.
    """

    def __init__(self, connection_string, token_renewal_interval = DEFAULT_TOKEN_RENEWAL_INTERVAL, token_renewal_margin = DEFAULT_TOKEN_RENEWAL_MARGIN):

        self.hostname = connection_string[HOST_NAME]
        self.device_id = connection_string[DEVICE_ID]

        if connection_string._dict.get(MODULE_ID) is not None:
            self.module_id = connection_string[MODULE_ID]
        if connection_string._dict.get(GATEWAY_HOST_NAME) is not None:
            self.gateway_hostname = connection_string[GATEWAY_HOST_NAME]

        self.shared_access_signature_token = None
        self._shared_access_keyname = None
        self._shared_access_key = None
        self.on_sas_token_updated = None

    @classmethod
    def create_authentication_from_connection_string(cls, connection_string):
        connection_string_obj = ConnectionString(connection_string)
        auth_provider = cls(connection_string_obj)
        uri = auth_provider.hostname + "/devices/" + auth_provider.device_id

        if connection_string_obj._dict.get(SHARED_ACCESS_KEY_NAME) is not None:
            auth_provider.shared_access_signature_token = SasToken(
                uri,
                connection_string_obj[SHARED_ACCESS_KEY],
                connection_string_obj[SHARED_ACCESS_KEY_NAME],
            )
        elif connection_string_obj._dict.get(SHARED_ACCESS_KEY) is not None:
            auth_provider.shared_access_signature_token = SasToken(
                uri, connection_string_obj[SHARED_ACCESS_KEY]
            )
        else:
            pass

        return auth_provider

    def get_current_sas_token(self):
        """
        :return: The current shared access signature token.  This returns a cached value
        and does not cause any token creation or re-creation to take place.  If the client
        wishes to update the sas token, they should call trigger_sas_token_update.
        """
        return self.shared_access_signature_token

   def generate_new_sas_token(self):
        """
        Force the SAS token to update itself.  This will cause a new sas token to be
        created, and self.on_sas_token_updated to be called.  The token update will
        be rescheduled based on the current time.
        """
        pass

    def cancel_token_update_timer(self):
        """
        Cancel any future token update operations.  This is typically done as part of a
        teardown operation
        """
        pass

    def _schedule_token_update(self, seconds_until_update):
        """
        Schedule an automatic sas token update to take place seconds_until_update seconds in
        the future.  If an update was previously scheduled, this method shall cancel the
        previously-scheduled update and schedule a new update.
        """
        pass

     def _notify_token_updated(self):
        """
        Notify clients that the SAS token has been updated by calling self.on_sas_token_updated.
        In response to this event, clients should re-initiate their connection in order to use
        the updated sas token.
        """
        pass

    def _update_sas_token(self):
        """
        Generate a new sas token and notify the client that the token has been updated.
        """
        pass

