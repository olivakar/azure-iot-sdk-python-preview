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


class SymmetricKeyAuthenticationProvider(object):
    """
    A provider for authentication mechanism based on known authentication mechanisms ,
    including x509 and SAS based authentication.
    """
    def __init__(self, parsed_connection_string):
        """
        Constructor for SymmetricKey Authentication Provider
        :param parsed_connection_string: The already parsed connection string.
        """
        self.device_id = parsed_connection_string[DEVICE_ID]
        self.hostname = parsed_connection_string[HOST_NAME]

        self.module_id = None
        self.gateway_hostname = None
        self.shared_access_keyname = None
        self.shared_access_key = None
        self.shared_access_signature_token = None

        if parsed_connection_string.get(MODULE_ID) is not None:
            self.module_id = parsed_connection_string[MODULE_ID]
        if parsed_connection_string.get(GATEWAY_HOST_NAME) is not None:
            self.gateway_hostname = parsed_connection_string[GATEWAY_HOST_NAME]
        if parsed_connection_string.get(SHARED_ACCESS_KEY) is not None:
            self.shared_access_key = parsed_connection_string[SHARED_ACCESS_KEY]
        if parsed_connection_string.get(SHARED_ACCESS_KEY_NAME) is not None:
            self.shared_access_keyname = parsed_connection_string[SHARED_ACCESS_KEY_NAME]

    @classmethod
    def create_authentication_from_connection_string(cls, connection_string):
        """
        Parses the connection string and instantiates an authentication provider with the parsed connection string.
        :param connection_string: The connection string of the client as set by the user.
        :return: An authentication provider.
        """
        connection_string_obj = ConnectionString(connection_string)
        return cls(connection_string_obj)

    def _sign(self):
        if self.module_id:
            uri = self.hostname + "/devices/" + self.device_id + "/modules/" + self.module_id
        else:
            uri = self.hostname + "/devices/" + self.device_id

        sas_token = None
        if self.shared_access_keyname is not None:
            sas_token = SasToken(uri, self.shared_access_key, self.shared_access_keyname)
        elif self.shared_access_key is not None:
            sas_token = SasToken(uri, self.shared_access_key)
        else:
            pass
        self.shared_access_signature_token = str(sas_token)

    def get_current_sas_token(self):
        """
        :return: The current shared access signature token
        """
        self._sign()
        return self.shared_access_signature_token
