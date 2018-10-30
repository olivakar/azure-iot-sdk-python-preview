# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from .transport.mqtt.mqtt_transport import MQTTTransport
from .internal_client import InternalClient


class DeviceClient(InternalClient):
    def __init__(self, auth_provider, transport):
        """
        Constructor for instantiating a device client
        :param auth_provider: The authentication provider
        :param transport: The device transport that the client will use
        """
        InternalClient.__init__(self, auth_provider, transport)

    @staticmethod
    def from_authentication_provider(authentication_provider, transport_name):
        """Creates a device client with the specified authentication provider and transport protocol"""
        if transport_name == "mqtt":
            transport = MQTTTransport(authentication_provider)
        else:
            raise NotImplementedError("No specific transport can be instantiated based on the choice.")
        return DeviceClient(authentication_provider, transport)
