# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .internal_client import InternalClient
from .auth.authentication_provider_factory import from_connection_string
from .transport.mqtt.mqtt_transport import MQTTTransport


class ModuleClient(InternalClient):

    def __init__(self, auth_provider, transport):
        """
        Constructor for instantiating a device client
        :param auth_provider: The authentication provider
        :param transport: The device transport that the client will use
        """
        InternalClient.__init__(self, auth_provider, transport)

    @staticmethod
    def from_authentication_provider(authentication_provider, transport_protocol):
        if transport_protocol == "mqtt":
            transport = MQTTTransport(authentication_provider)
        else:
            transport = NotImplemented
        return ModuleClient(authentication_provider, transport)

    @staticmethod
    def from_connection_string(connection_string, transport_protocol):
        authentication_provider = from_connection_string(connection_string)
        if transport_protocol == "mqtt":
            transport = MQTTTransport(authentication_provider)
        else:
            transport = NotImplemented
        return ModuleClient(authentication_provider, transport)
