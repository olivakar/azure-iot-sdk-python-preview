# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.iot.hub.devicesdk.device_client import DeviceClient
from azure.iot.hub.devicesdk.auth.authentication_provider_factory import from_connection_string
from azure.iot.hub.devicesdk.transport.mqtt.mqtt_transport import MQTTTransport
import pytest

from six import add_move, MovedModule

add_move(MovedModule("mock", "mock", "unittest.mock"))
from six.moves import mock
from mock import MagicMock


connection_string_format = "HostName={};DeviceId={};SharedAccessKey={}"
shared_access_key = "Zm9vYmFy"
hostname = "beauxbatons.academy-net"
device_id = "MyPensieve"


@pytest.fixture
def connection_string():
    connection_string = connection_string_format.format(hostname, device_id, shared_access_key)
    return connection_string


@pytest.fixture
def authentication_provider(connection_string):
    auth_provider = from_connection_string(connection_string)
    return auth_provider


def test_device_client_gets_created_correctly(mocker, authentication_provider):
    mock_transport = MagicMock(spec=MQTTTransport)
    mock_constructor_transport = mocker.patch("azure.iot.hub.devicesdk.device_client.MQTTTransport")
    mock_constructor_transport.return_value = mock_transport
    device_client = DeviceClient.from_authentication_provider(authentication_provider, "mqtt")

    assert device_client._auth_provider == authentication_provider
    assert device_client._transport == mock_transport


def test_raises_on_cretaion_of_device_client_when_transport_is_incorrect(authentication_provider):
    with pytest.raises(NotImplementedError, match="No specific transport can be instantiated based on the choice."):
        DeviceClient.from_authentication_provider(authentication_provider, "floo")




