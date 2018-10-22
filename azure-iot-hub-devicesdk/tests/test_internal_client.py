from azure.iot.hub.devicesdk.internal_client import InternalClient
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


def test_connect(authentication_provider):
    mock_transport = MagicMock(spec=MQTTTransport)

    device_client = InternalClient(authentication_provider, mock_transport)
    assert device_client.state == "initial"

    device_client.connect()

    mock_transport.connect.assert_called_once_with()


def test_get_transport_state(mocker, authentication_provider):
    stub_on_connection_state = mocker.stub(name="on_connection_state")

    mock_transport = MQTTTransport(authentication_provider)
    device_client = InternalClient(authentication_provider, mock_transport)
    device_client.on_connection_state = stub_on_connection_state

    new_state = "apparating"
    device_client._get_transport_connected_state_callback(new_state)

    stub_on_connection_state.assert_called_once_with(new_state)


def test_emit_connection_status(mocker, authentication_provider):
    stub_on_connection_state = mocker.stub(name="on_connection_state")

    mock_transport = MQTTTransport(authentication_provider)
    device_client = InternalClient(authentication_provider, mock_transport)
    device_client.on_connection_state = stub_on_connection_state
    new_state = "apparating"
    device_client.state = new_state

    device_client._emit_connection_status()

    stub_on_connection_state.assert_called_once_with(new_state)


def test_send_event_magic_mock(authentication_provider):
    mock_transport = MagicMock(spec=MQTTTransport)

    event = "Caput Draconis"
    device_client = InternalClient(authentication_provider, mock_transport)
    assert device_client.state == "initial"
    device_client.state = "connected"
    device_client.connect()
    device_client.send_event(event)

    mock_transport.send_event.assert_called_once_with(event)
