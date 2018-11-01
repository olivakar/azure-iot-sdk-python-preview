# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import types
import logging
from azure.iot.hub.devicesdk.transport.abstract_transport import AbstractTransport
from .mqtt_provider import MQTTProvider

logger = logging.getLogger(__name__)

class MQTTTransport(AbstractTransport):
    def __init__(self, auth_provider):
        """
        Constructor for instantiating a transport
        :param auth_provider: The authentication provider
        """
        logger.info("using MQTT transport")
        AbstractTransport.__init__(self, auth_provider)
        self._mqtt_provider = None
        self.on_transport_connected = types.FunctionType

        if hasattr(auth_provider, "on_token_updated"):
            auth_provider.on_token_updated = self._on_sas_token_updated

        self._create_provider()

    def connect(self):
        logger.info("connecting")
        self._mqtt_provider.connect()
        logger.info("done connecting")

    def send_event(self, event):
        topic = self._get_telemetry_topic()
        self._mqtt_provider.publish(topic, event)

    def disconnect(self):
        logger.info("disconnecting")
        self._mqtt_provider.disconnect()
        logger.info("done disconnecting")

    def _create_provider(self):
        logger.info("creating provider object")
        client_id = self._auth_provider.device_id

        if self._auth_provider.module_id is not None:
            client_id += "/" + self._auth_provider.module_id

        username = self._auth_provider.hostname + "/" + client_id + "/" + "?api-version=2018-06-30"

        if hasattr(self._auth_provider, 'gateway_hostname'):
            hostname = self._auth_provider.gateway_hostname
        else:
            hostname = self._auth_provider.hostname

        if hasattr(self._auth_provider, "ca_cert"):
            ca_cert = self._auth_provider.ca_cert
        else:
            ca_cert = None

        self._mqtt_provider = MQTTProvider(client_id, hostname, username,
                                           self._auth_provider.get_current_sas_token(), ca_cert=ca_cert)
        self._mqtt_provider.on_mqtt_connected = self._handle_provider_connected_state

    def _handle_provider_connected_state(self, machine_state):
        return self.on_transport_connected(machine_state)

    def _on_sas_token_updated(self):
        """
        Handle the case where the authentication provider has recently updated the sas
        token and the transport needs update its connection in order to use the new
        token.  In response to this event, the transport will call into the authentication
        provider to retrieve the new credentials and then the transport will disconnect
        and reconnect itself in order to use the new credentials.  If the transport is not
        currently connected, this event will not trigger a connection operation.
        """
        logger.info("SAS token updated.  Reconnecting.")
        self._mqtt_provider.update_password(self._auth_provider.get_current_sas_token())

    def _get_telemetry_topic(self):
        topic = "devices/" + self._auth_provider.device_id

        if self._auth_provider.module_id is not None:
            topic += "/modules/" + self._auth_provider.module_id

        topic += "/messages/events/"
        return topic
