# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import logging
from azure.iot.hub.devicesdk.device_client import DeviceClient
from azure.iot.hub.devicesdk.iotedge_authentication_provider import IotEdgeAuthenticationProvider
from azure.iot.hub.devicesdk.transport.transport_config import TransportProtocol, TransportConfig

logging.basicConfig(level=logging.INFO)

transport_config = TransportConfig(TransportProtocol.MQTT)
auth = IotEdgeAuthenticationProvider.create_from_environment()
simpleDevice = DeviceClient.create(auth, transport_config)


def connection_state_callback(status):
    print("connection status: " + status)
    if status == "connected":
        simpleDevice.send_event("Mimbulus Mimbletonia")


simpleDevice.on_connection_state = connection_state_callback
simpleDevice.connect()

while True:
    continue
