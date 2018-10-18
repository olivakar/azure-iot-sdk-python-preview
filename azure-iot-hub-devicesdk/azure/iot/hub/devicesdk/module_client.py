# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .internal_client import InternalClient
from .sk_authentication_provider import SymmetricKeyAuthenticationProvider


class ModuleClient(InternalClient):

    def __init__(self, auth_provider, transport_config):
        """
        Constructor for instantiating a module client
        :param auth_provider: The authentication provider
        :param transport_config: The transport config
        """
        InternalClient.__init__(self, auth_provider, transport_config)

    @staticmethod
    def create_from_connection_string(connection_string, transport_config):
        return ModuleClient(SymmetricKeyAuthenticationProvider.create_authentication_from_connection_string(connection_string), transport_config)