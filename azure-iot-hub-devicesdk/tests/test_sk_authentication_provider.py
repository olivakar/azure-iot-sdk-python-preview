# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import pytest
import threading
from azure.iot.hub.devicesdk.auth.sk_authentication_provider import SymmetricKeyAuthenticationProvider

from six import add_move, MovedModule

add_move(MovedModule("mock", "mock", "unittest.mock"))
from six.moves import mock
from mock import MagicMock
from mock import patch

connection_string_device_sk_format = "HostName={};DeviceId={};SharedAccessKey={}"
connection_string_device_skn_format = (
    "HostName={};DeviceId={};SharedAccessKeyName={};SharedAccessKey={}"
)
connection_string_module_sk_format = (
    "HostName={};DeviceId={};ModuleId={};SharedAccessKey={}"
)

shared_access_key = "Zm9vYmFy"
shared_access_key_name = "alohomora"
hostname = "beauxbatons.academy-net"
device_id = "MyPensieve"
module_id = "Divination"


def test_all_attributes_for_device():
    connection_string = connection_string_device_sk_format.format(
        hostname, device_id, shared_access_key
    )
    sym_key_auth_provider = SymmetricKeyAuthenticationProvider.parse(connection_string)
    assert sym_key_auth_provider.hostname == hostname
    assert sym_key_auth_provider.device_id == device_id
    assert hostname in sym_key_auth_provider.sas_token_str
    assert device_id in sym_key_auth_provider.sas_token_str


def test_all_attributes_for_module():
    connection_string = connection_string_module_sk_format.format(
        hostname, device_id, module_id, shared_access_key
    )
    sym_key_auth_provider = SymmetricKeyAuthenticationProvider.parse(connection_string)
    assert sym_key_auth_provider.hostname == hostname
    assert sym_key_auth_provider.device_id == device_id
    assert sym_key_auth_provider.module_id == module_id
    assert hostname in sym_key_auth_provider.sas_token_str
    assert device_id in sym_key_auth_provider.sas_token_str
    assert module_id in sym_key_auth_provider.sas_token_str


def test_sastoken_keyname_device():
    connection_string = connection_string_device_skn_format.format(
        hostname, device_id, shared_access_key_name, shared_access_key
    )

    sym_key_auth_provider = SymmetricKeyAuthenticationProvider.parse(connection_string)

    assert hostname in sym_key_auth_provider.sas_token_str
    assert device_id in sym_key_auth_provider.sas_token_str
    assert shared_access_key_name in sym_key_auth_provider.sas_token_str


def test_raises_when_auth_provider_created_from_incomplete_connection_string():
    with pytest.raises(ValueError, match="Invalid Connection String - Incomplete"):
        connection_string = "HostName=beauxbatons.academy-net;SharedAccessKey=Zm9vYmFy"
        SymmetricKeyAuthenticationProvider.parse(connection_string)


def test_raises_when_auth_provider_created_from_connection_string_with_duplicatekeys():
    with pytest.raises(ValueError, match="Invalid Connection String - Unable to parse"):
        connection_string = (
            "HostName=beauxbatons.academy-net;HostName=TheDeluminator;HostName=Zm9vYmFy"
        )
        SymmetricKeyAuthenticationProvider.parse(connection_string)


def test_raises_when_auth_provider_created_from_connection_string_without_proper_delimeter():
    with pytest.raises(ValueError):
        connection_string = "HostName+beauxbatons.academy-net!DeviceId+TheDeluminator!"
        SymmetricKeyAuthenticationProvider.parse(connection_string)


def test_raises_when_auth_provider_created_from_connection_string_with_bad_keys():
    with pytest.raises(ValueError, match="Invalid Connection String - Invalid Key"):
        connection_string = "BadHostName=beauxbatons.academy-net;BadDeviceId=TheDeluminator;SharedAccessKey=Zm9vYmFy"
        SymmetricKeyAuthenticationProvider.parse(connection_string)


@patch('threading.Timer')
def test_scheduled_sas_token_update_creates_new_token_calls_event_handler_and_schedules_new_update(MockTimer):
    """
    Verifies that a scheduled sas token update:
    1. happens at the appropriate time
    2. creates new token
    3. calls event handler
    4. schedules the next update
    """
    pass

def test_manual_sas_token_update_creates_new_token_calls_event_handler_and_schedules_new_update():
    """
    Verifies that a manual sas token update:
    1. creates new token
    2. calls event handler
    3. schedules the next update
    """
    pass

def test_token_interval_change_creates_new_token_calls_event_handler_and_schedules_new_update():
    """
    Verifies that a change to the token update interval:
    1. creates new token
    2. calls event handler
    3. schedules the next update
    """
    pass
