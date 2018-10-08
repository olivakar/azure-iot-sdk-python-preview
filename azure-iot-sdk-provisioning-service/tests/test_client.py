# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

import pytest
from pytest_mock import mocker
from azure.iot.sdk.provisioning.service import ProvisioningServiceClient
from azure.iot.sdk.provisioning.service.protocol import ProvisioningServiceClient as BaseProvisioningServiceClient
from azure.iot.sdk.provisioning.service.auth import ConnectionStringAuthentication
from azure.iot.sdk.provisioning.service.models import IndividualEnrollment, EnrollmentGroup, AttestationMechanism

@pytest.fixture(scope="module")
def service_str():
    return "HostName=my.host.name;SharedAccessKeyName=mykeyname;SharedAccessKey=Zm9vYmFy"

@pytest.fixture(scope="module")
def service_client(service_str):
    return ProvisioningServiceClient(service_str)

@pytest.fixture(scope="module")
def attestation_mechanism():
    return AttestationMechanism.create_with_x509_ca_references("my-certificate-name")

@pytest.fixture() #don't scope, so changes aren't saved
def individual_enrollment(attestation_mechanism):
    return IndividualEnrollment(registration_id="registration_id", attestation=attestation_mechanism)

@pytest.fixture() #don't scope, so changes aren't saved
def enrollment_group(attestation_mechanism):
    return EnrollmentGroup(enrollment_group_id="group_id", attestation=attestation_mechanism)

@pytest.fixture(scope="module")
def etag():
    return "my-etag"

def test_create(mocker, service_str):
    """Test that instantiation of the application ProvisioningServiceClient creates a ConnectionStringAuthentication from
    the provided connection string, and then uses it along with an extracted hostname in the __init__ of the
    superclass - the generated ProvisioningServiceClient from .protocol
    """
    mock_parent_init = mocker.patch.object(BaseProvisioningServiceClient, '__init__', autospec=True)
    auth = ConnectionStringAuthentication(service_str)
    mock_auth = mocker.patch('azure.iot.sdk.provisioning.service.client.ConnectionStringAuthentication', return_value=auth, autospec=True)
    client = ProvisioningServiceClient(service_str)
    mock_auth.assert_called_once_with(service_str)
    mock_parent_init.assert_called_once_with(client, mock_auth.return_value, "http://my.host.name")

def test_create_or_update_individual_enrollment_min_args(mocker, service_client, individual_enrollment):
    """Test that create_or_update_individual_enrollment with only required arguments.
    Note that Individual Enrollment has no etag, and thus an etag of None is passed in the inner call
    """
    mock_parent_create = mocker.patch.object(BaseProvisioningServiceClient, 'create_or_update_individual_enrollment', autospec=True)
    service_client.create_or_update_individual_enrollment(
        id=individual_enrollment.registration_id, enrollment=individual_enrollment
    )
    mock_parent_create.assert_called_once_with(
        service_client, individual_enrollment.registration_id, individual_enrollment, None, None, False
    )

def test_create_or_update_individual_enrollment_max_args(mocker, service_client, individual_enrollment, etag):
    """Test that create_or_update_individual_enrollment with all possible arguments.
    Note that Individual Enrollment is given an etag, and that it is automatically extracted for the inner call
    """
    individual_enrollment.etag = etag
    custom_headers = {"key" : "value"}
    mock_parent_create = mocker.patch.object(BaseProvisioningServiceClient, 'create_or_update_individual_enrollment', autospec=True)
    service_client.create_or_update_individual_enrollment(
        id=individual_enrollment.registration_id, enrollment=individual_enrollment, custom_headers=custom_headers, raw=True
    )
    mock_parent_create.assert_called_once_with(
        service_client, individual_enrollment.registration_id, individual_enrollment, etag, custom_headers, True
    )

def test_create_or_update_enrollment_group_min_args(mocker, service_client, enrollment_group):
    """Test create_or_update_enrollment_group with only required arguments.
    Note that Enrollment Group has no etag, and thus an etag of None is passed in the inner call
    """
    mock_parent_create = mocker.patch.object(BaseProvisioningServiceClient, 'create_or_update_enrollment_group', autospec=True)
    service_client.create_or_update_enrollment_group(
        id=enrollment_group.enrollment_group_id, enrollment_group=enrollment_group
    )
    mock_parent_create.assert_called_once_with(
        service_client, enrollment_group.enrollment_group_id, enrollment_group, None, None, False
    )

def test_create_or_update_enrollment_group_max_args(mocker, service_client, enrollment_group, etag):
    """Test create_or_update_enrollment_group with all possible args.
    Note that Enrollment Group is given an etag, and that it is automatically extracted for the inner call
    """
    enrollment_group.etag = etag
    custom_headers = {"key" : "value"}
    mock_parent_create = mocker.patch.object(BaseProvisioningServiceClient, 'create_or_update_enrollment_group', autospec=True)
    service_client.create_or_update_enrollment_group(
        id=enrollment_group.enrollment_group_id, enrollment_group=enrollment_group, custom_headers=custom_headers, raw=True
    )
    mock_parent_create.assert_called_once_with(
        service_client, enrollment_group.enrollment_group_id, enrollment_group, etag, custom_headers, True
    )