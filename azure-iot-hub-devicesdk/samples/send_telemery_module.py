# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import logging
from azure.iot.hub.devicesdk.module_client import ModuleClient

logging.basicConfig(level=logging.INFO)

# This is just a simple module on the simple device. Connection string is of the format
# HostName=<SomeHostName>;DeviceId=<SomeDeviceId>;ModuleId=<SomeModuleIdOnSomeDevice>;SharedAccessKey=<SomeSharedAccessKey>
conn_str = os.getenv("IOTHUB_MODULE_CONNECTION_STRING")
logging.info(conn_str)

simpleModule = ModuleClient.from_connection_string(conn_str, "mqtt")


def connection_state_callback(status):
    print("connection status: " + status)
    if status == "connected":
        simpleModule.send_event("Aguamenti")


simpleModule.on_connection_state = connection_state_callback
simpleModule.connect()

while True:
    continue
