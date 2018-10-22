# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import types


class InternalClient(object):

    def __init__(self, auth_provider, device_transport):
        """
        Constructor for instantiating an internal client
        :param auth_provider: The authentication provider
        :param device_transport: The device transport that the client will use.
        """
        self._auth_provider = auth_provider
        self._transport = device_transport

        self.state = "initial"

        self.on_connection_state = types.FunctionType

    def connect(self):
        """Connects the client to an Azure IoT Hub.
        The client must call this method as an entry point to getting connected to IoT Hub
        """
        logging.info("connecting to transport")
        self._transport.on_transport_connected = self._get_transport_connected_state_callback
        self._transport.connect()

    def send_event(self, event):
        """
        Sends an actual message/telemetry to the IoT Hub via the message broker.
        The client must call this method to send messages.
        :param event: The actual message to send.
        """
        self._transport.send_event(event)

    def _emit_connection_status(self):
        """
        The connection status is emitted whenever the client on the module gets connected or disconnected.
        """
        logging.info("emit_connection_status")
        if self.on_connection_state:
            self.on_connection_state(self.state)
        else:
            logging.error("No callback defined for sending state")

    def _get_transport_connected_state_callback(self, new_state):
        self.state = new_state
        self._emit_connection_status()
