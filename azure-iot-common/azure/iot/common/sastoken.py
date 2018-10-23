# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import base64
import hmac
import hashlib
import time
import six.moves.urllib as urllib

__all__ = ["SasToken", "SasTokenError"]

DELIMITER = "&"
VALUE_SEPARATOR = "="
PARTS_SEPARATOR = " "


SIGNATURE = "sig"
SHARED_ACCESS_KEY = "sk"
SHARED_ACCESS_KEY_NAME = "skn"
RESOURCE_URI = "sr"
EXPIRY = "se"


_valid_keys = [
    SIGNATURE,
    SHARED_ACCESS_KEY,
    SHARED_ACCESS_KEY_NAME,
    RESOURCE_URI,
    EXPIRY
]


class SasTokenError(Exception):
    def __init__(self, message, cause=None):
        super(self.__class__, self).__init__(message)
        self.cause = cause


class SasToken(object):
    """
    Shared Access Signature Token used to authenticate a request
    and securely encapsulate information about a resource on an IoT Hub.
    """

    _encoding_type = "utf-8"
    _service_token_format = "SharedAccessSignature sr={}&sig={}&se={}&skn={}"
    _device_token_format = "SharedAccessSignature sr={}&sig={}&se={}"

    def __repr__(self):
        return self._token

    def refresh(self):
        """
        Refresh the SasToken lifespan, giving it a new expiry time
        """
        self.expiry_time = int(time.time() + self.ttl)
        self._token = self._build_token()

    def _build_token(self):
        """Buid SasToken representation

        Returns:
        String representation of the token
        """
        try:
            message = (self._uri + "\n" + str(self.expiry_time)).encode(self._encoding_type)
            signing_key = base64.b64decode(self._key.encode(self._encoding_type))
            signed_hmac = hmac.HMAC(signing_key, message, hashlib.sha256)
            signature = urllib.parse.quote(base64.b64encode(signed_hmac.digest()))
        except (TypeError, base64.binascii.Error) as e:
            raise SasTokenError("Unable to build SasToken from given values", e)
        if self._key_name:
            token = self._service_token_format.format(
                self._uri, signature, str(self.expiry_time), self._key_name
            )
        else:
            token = self._device_token_format.format(self._uri, signature, str(self.expiry_time))
        return token

    @staticmethod
    def create(uri, key, key_name=None, ttl=3600):
        """
        This method returns a new instance of the SharedAccessSignature token object with sr, sig, and se properties.
        It may optionally have an skn property.

        Parameters:
        uri (str): the resource URI to encode into the token
        key_name (str): an identifier associated with the key
        key (str): a base64-encoded Shared Access Key value
        ttl (int)[default 3600]: Time to live for the token, in seconds

        Data Attributes:
        expiry_time (int): Time that token will expire (in UTC, since epoch)
        ttl (int): Time to live for the token, in seconds

        Raises:
        SasTokenError if trying to build a SasToken from invalid values
        """
        sas_token = SasToken()
        sas_token._uri = urllib.parse.quote_plus(uri)
        sas_token._key = key
        sas_token._key_name = key_name
        sas_token.ttl = ttl
        sas_token.refresh()
        return sas_token

    @staticmethod
    def parse(shared_access_signature):
        """
        This method creates a shared access signature object from a string, and sets properties for each of the parsed
        fields in the string. Also validates the required properties of the shared access signature.
        :param shared_access_signature: The ampersand-delimited string of 'name=value' pairs.
        The input may look like the following formations:-
        SharedAccessSignature sr=<resource_uri>&sig=<signature>&se=<expiry>
        SharedAccessSignature sr=<resource_uri>&sig=<signature>&skn=<keyname>&se=<expiry>
        :return: The shared access signature object constructed from the input string
        """
        parts = shared_access_signature.split(PARTS_SEPARATOR)
        if len(parts) != 2:
            raise ValueError("The shared access signature must be of the format 'SharedAccessSignature sr=<resource_uri>&sig=<signature>&se=<expiry>' or/and it can additionally contain an optional skn=<keyname> name=value pair.")

        sas_args = parts[1].split(DELIMITER)
        d = dict(arg.split(VALUE_SEPARATOR, 1) for arg in sas_args)
        if len(sas_args) != len(d):
            raise ValueError("Invalid Shared Access Signature - Unable to parse")
        if not all(key in _valid_keys for key in d.keys()):
            raise ValueError("Invalid Shared Access Signature - Invalid Key")

        _validate_required_keys(d)

        sas_token = SasToken()
        sas_token._uri = d.get(RESOURCE_URI)
        sas_token.expiry_time = d.get(EXPIRY)
        if d.get(SHARED_ACCESS_KEY_NAME) is not None:
            sas_token._key_name = d.get(SHARED_ACCESS_KEY_NAME)

        sas_token._token = shared_access_signature
        return sas_token


def _validate_required_keys(d):
    """
    Validates that required keys are present.
    Raise ValueError if incorrect combination of keys
    """
    resource_uri = d.get(RESOURCE_URI)
    signature = d.get(SIGNATURE)
    expiry = d.get(EXPIRY)

    # This logic could be expanded to return the category of ConnectionString
    if resource_uri and signature and expiry:
        pass
    else:
        raise ValueError("Invalid Shared Access Signature - Missing some property")