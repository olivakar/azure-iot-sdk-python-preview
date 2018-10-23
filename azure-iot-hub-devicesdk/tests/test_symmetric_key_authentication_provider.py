# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.iot.hub.devicesdk.auth.authentication_provider_factory import from_connection_string
import pytest


connection_string_device_sk_format = "HostName={};DeviceId={};SharedAccessKey={}"
connection_string_device_skn_format = (
    "HostName={};DeviceId={};SharedAccessKeyName={};SharedAccessKey={}"
)
connection_string_module_sk_format = (
    "HostName={};DeviceId={};ModuleId={};SharedAccessKey={}"
)
connection_string_module_gateway_sk_format = (
    "HostName={};DeviceId={};ModuleId={};SharedAccessKey={};GatewayHostName={}"
)

shared_access_key = "Zm9vYmFy"
shared_access_key_name = "alohomora"
hostname = "beauxbatons.academy-net"
device_id = "MyPensieve"
module_id = "Divination"
gateway_name = "EnchantedCeiling"

uri_device = hostname + "/devices/" + device_id
uri_module = hostname + "/devices/" + device_id + "/modules/" + module_id


def test_create_from_incomplete_connection_string():
    with pytest.raises(ValueError, match="Invalid Connection String - Incomplete"):
        connection_string = "HostName=beauxbatons.academy-net;SharedAccessKey=Zm9vYmFy"
        from_connection_string(connection_string)


def test_create_from_duplicatekeys_connection_string():
    with pytest.raises(ValueError, match="Invalid Connection String - Unable to parse"):
        connection_string = (
            "HostName=beauxbatons.academy-net;HostName=TheDeluminator;HostName=Zm9vYmFy"
        )
        from_connection_string(connection_string)

# Without the proper delimiter the dictionary function itself can't take place
def test_create_from_badparsing_connection_string():
    with pytest.raises(ValueError):
        connection_string = "HostName+beauxbatons.academy-net!DeviceId+TheDeluminator!"
        from_connection_string(connection_string)


def test_create_from_badkeys_connection_string():
    with pytest.raises(ValueError, match="Invalid Connection String - Invalid Key"):
        connection_string = "BadHostName=beauxbatons.academy-net;BadDeviceId=TheDeluminator;SharedAccessKey=Zm9vYmFy"
        from_connection_string(connection_string)


def test_all_attributes_for_device():
    connection_string = connection_string_device_sk_format.format(
        hostname, device_id, shared_access_key
    )
    authentication_provider = from_connection_string(connection_string)
    assert authentication_provider.hostname == hostname
    assert authentication_provider.device_id == device_id
    assert authentication_provider.shared_access_key == shared_access_key


def test_all_attributes_for_module():
    connection_string = connection_string_module_sk_format.format(
        hostname, device_id, module_id, shared_access_key
    )
    authentication_provider = from_connection_string(connection_string)
    assert authentication_provider.hostname == hostname
    assert authentication_provider.device_id == device_id
    assert authentication_provider.shared_access_key == shared_access_key
    assert authentication_provider.module_id == module_id


def test_create_from_module_gateway_connection_string():
    connection_string = connection_string_module_gateway_sk_format.format(
        hostname, device_id, module_id, shared_access_key, gateway_name
    )
    authentication_provider = from_connection_string(connection_string)

    assert authentication_provider.hostname == hostname
    assert authentication_provider.device_id == device_id
    assert authentication_provider.shared_access_key == shared_access_key
    assert authentication_provider.module_id == module_id
    assert authentication_provider.gateway_hostname == gateway_name


def test_sastoken_key_device(mocker):
    mock_sastoken = mocker.patch(
        "azure.iot.hub.devicesdk.auth.symmetric_key_authentication_provider.SasToken.create"
    )

    dummy_value = "SharedAccessSignature sr=beauxbatons.academy-net%2Fdevices%2FMyPensieve&sig=zh8pwNIG56yUd3Nna7lyKA2HQAns84U3XwxyFQJqh48%3D&se=1539036534"
    mock_sastoken.return_value.__str__.return_value = dummy_value

    connection_string = connection_string_device_sk_format.format(
        hostname, device_id, shared_access_key
    )
    sym_key_auth_provider = from_connection_string(connection_string)
    sym_key_auth_provider._sign()

    mock_sastoken.assert_called_once_with(uri_device, shared_access_key, None)
    assert sym_key_auth_provider.shared_access_signature_token == dummy_value


def test_sastoken_key_module(mocker):
    mock_sastoken = mocker.patch(
        "azure.iot.hub.devicesdk.auth.symmetric_key_authentication_provider.SasToken.create"
    )
    dummy_value = "SharedAccessSignature sr=beauxbatons.academy-net%2Fdevices%2FMyPensieve%2Fmodules%2FDivination&sig=zh8pwNIG56yUd3Nna7lyKA2HQAns84U3XwxyFQJqh48%3D&se=1539036534"
    mock_sastoken.return_value.__str__.return_value = dummy_value

    connection_string = connection_string_module_sk_format.format(
        hostname, device_id, module_id, shared_access_key
    )
    sym_key_auth_provider = from_connection_string(connection_string)
    sym_key_auth_provider._sign()

    mock_sastoken.assert_called_once_with(uri_module, shared_access_key, None)
    assert sym_key_auth_provider.shared_access_signature_token == dummy_value


def test_sastoken_key_gateway_module(mocker):
    mock_sastoken = mocker.patch(
        "azure.iot.hub.devicesdk.auth.symmetric_key_authentication_provider.SasToken.create"
    )
    dummy_value = "SharedAccessSignature sr=beauxbatons.academy-net%2Fdevices%2FMyPensieve%2Fmodules%2FDivination&sig=fT/nO0NA/25IKl0Ei2upxDDj6KnY6RPVIjlV84/9aR8%3D&se=1539043658"
    mock_sastoken.return_value.__str__.return_value = dummy_value

    connection_string = connection_string_module_gateway_sk_format.format(
        hostname, device_id, module_id, shared_access_key, gateway_name
    )
    sym_key_auth_provider = from_connection_string(connection_string)
    sym_key_auth_provider._sign()

    mock_sastoken.assert_called_once_with(uri_module, shared_access_key, None)
    assert sym_key_auth_provider.shared_access_signature_token == dummy_value


def test_sastoken_keyname_device(mocker):
    mock_sastoken = mocker.patch(
        "azure.iot.hub.devicesdk.auth.symmetric_key_authentication_provider.SasToken.create"
    )
    dummy_value = "SharedAccessSignature sr=beauxbatons.academy-net%2Fdevices%2FMyPensieve&sig=fT/nO0NA/25IKl0Ei2upxDDj6KnY6RPVIjlV84/9aR8%3D&se=1539043658&skn=alohomora"
    mock_sastoken.return_value.__str__.return_value = dummy_value

    connection_string = connection_string_device_skn_format.format(
        hostname, device_id, shared_access_key_name, shared_access_key
    )
    sym_key_auth_provider = from_connection_string(connection_string)
    sym_key_auth_provider._sign()

    mock_sastoken.assert_called_once_with(uri_device, shared_access_key, shared_access_key_name)
    assert sym_key_auth_provider.shared_access_signature_token == dummy_value
