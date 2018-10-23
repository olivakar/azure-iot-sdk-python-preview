# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import pytest
from azure.iot.hub.devicesdk.transport.mqtt.mqtt_transport import MQTTTransport
from azure.iot.hub.devicesdk.transport.mqtt.mqtt_provider import MQTTProvider
from azure.iot.hub.devicesdk.symmetric_key_authentication_provider import (
    SymmetricKeyAuthenticationProvider,
)
from six import add_move, MovedModule

add_move(MovedModule("mock", "mock", "unittest.mock"))
from six.moves import mock
from mock import MagicMock


connection_string_format = "HostName={};DeviceId={};SharedAccessKey={}"
shared_access_key = "Zm9vYmFy"
hostname = "beauxbatons.academy-net"
device_id = "MyPensieve"


@pytest.fixture(scope="module")
def authentication_provider():
    connection_string = connection_string_format.format(hostname, device_id, shared_access_key)
    auth_provider = SymmetricKeyAuthenticationProvider.create_authentication_from_connection_string(
        connection_string
    )
    return auth_provider


@pytest.fixture(scope="module")
def transport(authentication_provider):
    transport = MQTTTransport(authentication_provider)
    return transport


def test_create():
    connection_string = connection_string_format.format(hostname, device_id, shared_access_key)
    authentication_provider = SymmetricKeyAuthenticationProvider.create_authentication_from_connection_string(
        connection_string
    )
    trans = MQTTTransport(authentication_provider)
    assert trans._auth_provider == authentication_provider
    assert trans._mqtt_provider is None


def test_connect_to_message_broker(mocker, transport):
    mock_mqtt_provider = MagicMock(spec=MQTTProvider)
    mock_mqtt_provider_constructor = mocker.patch(
        "azure.iot.hub.devicesdk.transport.mqtt.mqtt_transport.MQTTProvider"
    )
    mock_mqtt_provider_constructor.return_value = mock_mqtt_provider

    mocker.patch.object(mock_mqtt_provider, "connect")

    transport.connect()
    mock_mqtt_provider.connect.assert_called_once_with()


def test_sendevent(mocker, transport):
    topic = "devices/" + device_id + "/messages/events/"
    event = "Wingardian Leviosa"

    mock_mqtt_provider = MagicMock(spec=MQTTProvider)
    mock_mqtt_provider_constructor = mocker.patch(
        "azure.iot.hub.devicesdk.transport.mqtt.mqtt_transport.MQTTProvider"
    )
    mock_mqtt_provider_constructor.return_value = mock_mqtt_provider
    mocker.patch.object(mock_mqtt_provider, "connect")
    mocker.patch.object(mock_mqtt_provider, "publish")

    transport.connect()
    transport.send_event(event)

    mock_mqtt_provider.connect.assert_called_once_with()
    mock_mqtt_provider.publish.assert_called_once_with(topic, event)


def test_disconnect_from_message_broker(mocker, transport):
    mock_mqtt_provider = MagicMock(spec=MQTTProvider)
    mock_mqtt_provider_constructor = mocker.patch(
        "azure.iot.hub.devicesdk.transport.mqtt.mqtt_transport.MQTTProvider"
    )
    mock_mqtt_provider_constructor.return_value = mock_mqtt_provider
    mocker.patch.object(mock_mqtt_provider, "disconnect")

    transport.connect()
    transport.disconnect()

    mock_mqtt_provider.disconnect.assert_called_once_with()

def test_transport_uses_ca_from_auth_provider_if_available():
    """
    Verify that the transport calls get_trusted_certificate_authority
    on the auth provider (if availalbe) in order to get a CA string and that it
    passes this string into the transport provider.
    """
    pass

def test_transport_doesnt_pass_ca_if_auth_provider_doesnt_provide_it():
    """
    If the auth provider does not have a get_trusted_certificate_authority
    method, then verify that the transport passes None as the CA to the transport
    provider
    """
    pass

def test_transport_fails_connection_if_auth_provider_fails_getting_ca_certificate():
    """
    verify that the transport connection fails if the auth provider raises an exception
    while getting the trust bundle.
    """
    pass

def test_transport_fails_connection_if_auth_provider_does_not_provide_sas_token():
    """
    verify that the transport will fail to connect if the auth provider does not supply
    a sas token for the transport to use.
    """
    pass