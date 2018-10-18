from azure.iot.hub.devicesdk.internal_client import InternalClient
from azure.iot.hub.devicesdk.symmetric_key_authentication_provider import SymmetricKeyAuthenticationProvider
from azure.iot.hub.devicesdk.transport.mqtt.mqtt_transport import MQTTTransport
from azure.iot.hub.devicesdk.transport.transport_config import TransportConfig, TransportProtocol
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
    auth_provider = SymmetricKeyAuthenticationProvider.create_authentication_from_connection_string(
        connection_string
    )
    return auth_provider


@pytest.fixture
def mqtt_transport_config():
    return TransportConfig(TransportProtocol.MQTT)


def test_connect(mocker, authentication_provider, mqtt_transport_config):
    mocker.patch.object(InternalClient, "_emit_connection_status")
    mocker.patch.object(MQTTTransport, "connect")

    internal_client = InternalClient(authentication_provider, mqtt_transport_config)
    assert internal_client.state == "initial"
    assert internal_client._transport is None

    internal_client.connect()

    assert isinstance(internal_client._transport, MQTTTransport)

    MQTTTransport.connect.assert_called_once_with()
    InternalClient._emit_connection_status.assert_called_once_with()


def test_get_transport_state(mocker, mqtt_transport_config):
    stub_on_connection_state = mocker.stub(name="on_connection_state")

    internal_client = InternalClient(authentication_provider, mqtt_transport_config)
    internal_client.on_connection_state = stub_on_connection_state

    new_state = "apparating"
    internal_client._get_transport_connected_state_callback(new_state)

    stub_on_connection_state.assert_called_once_with(new_state)


def test_emit_connection_status(mocker, mqtt_transport_config):
    stub_on_connection_state = mocker.stub(name="on_connection_state")

    internal_client = InternalClient(authentication_provider, mqtt_transport_config)
    internal_client.on_connection_state = stub_on_connection_state
    new_state = "apparating"
    internal_client.state = new_state

    internal_client._emit_connection_status()

    stub_on_connection_state.assert_called_once_with(new_state)


def test_send_event_magic_mock(mocker, authentication_provider, mqtt_transport_config):
    mock_transport = MagicMock(spec=MQTTTransport)
    mock_transport_config = mocker.patch.object(TransportConfig, "get_specific_transport")
    mock_transport_config.return_value = mock_transport

    mocker.patch.object(mock_transport, "send_event")
    mocker.patch.object(InternalClient, "_emit_connection_status")

    event = "Caput Draconis"
    internal_client = InternalClient(authentication_provider, mqtt_transport_config)
    assert internal_client.state == "initial"
    assert internal_client._transport is None
    internal_client.state = "connected"
    internal_client.connect()
    internal_client.send_event(event)

    TransportConfig.get_specific_transport.assert_called_once_with(authentication_provider)
    mock_transport.send_event.assert_called_once_with(event)
    InternalClient._emit_connection_status.assert_called_once_with()


def test_send_event_error(mocker, authentication_provider, mqtt_transport_config):
    mocker.patch.object(TransportConfig, "get_specific_transport")
    mocker.patch.object(InternalClient, "_emit_connection_status")

    with pytest.raises(ValueError, match="No connection present to send event."):
        event = "Caput Draconis"
        internal_client = InternalClient(authentication_provider, mqtt_transport_config)
        assert internal_client.state == "initial"
        assert internal_client._transport is None
        internal_client.state = "disconnected"
        internal_client.connect()
        internal_client.send_event(event)

    TransportConfig.get_specific_transport.assert_called_once_with(authentication_provider)
