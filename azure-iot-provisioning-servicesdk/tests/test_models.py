# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

import pytest
from azure.iot.provisioning.servicesdk.models import AttestationMechanism

@pytest.fixture(scope="module")
def dummy_value_1():
    return "foo"

@pytest.fixture(scope="module")
def dummy_value_2():
    return "bar"

class TestAttestationMechanismCustomMethods(object):

    def test_create_with_tpm_min(self, dummy_value_1):
        """Create an Attestation using TPM with minimum values
        """
        am = AttestationMechanism.create_with_tpm(endorsement_key=dummy_value_1)
        assert am.type == "tpm"
        assert am.x509 == None
        assert am.tpm.endorsement_key == dummy_value_1
        assert am.tpm.storage_root_key == None
    
    def test_create_with_tpm_max(self, dummy_value_1, dummy_value_2):
        """Create an Attestation using TPM with all values
        """
        am = AttestationMechanism.create_with_tpm(endorsement_key=dummy_value_1, storage_root_key=dummy_value_2)
        assert am.type == "tpm"
        assert am.x509 == None
        assert am.tpm.endorsement_key == dummy_value_1
        assert am.tpm.storage_root_key == dummy_value_2

    def test_create_with_x509_client_certificates_min(self, dummy_value_1):
        """Create an Attestation using X509 Client Certificates with minimum values
        """
        am = AttestationMechanism.create_with_x509_client_certificates(dummy_value_1)
        assert am.type == "x509"
        assert am.tpm == None
        assert am.x509.signing_certificates == None
        assert am.x509.ca_references == None
        assert am.x509.client_certificates.primary.certificate == dummy_value_1
        assert am.x509.client_certificates.primary.info == None
        assert am.x509.client_certificates.secondary == None

    def test_create_with_x509_client_certificates_max(self, dummy_value_1, dummy_value_2):
        """Create an Attestation using X509 Client Certificates with all values
        """
        am = AttestationMechanism.create_with_x509_client_certificates(dummy_value_1, dummy_value_2)
        print(am)
        assert am.type == "x509"
        assert am.tpm == None
        assert am.x509.signing_certificates == None
        assert am.x509.ca_references == None
        assert am.x509.client_certificates.primary.certificate == dummy_value_1
        assert am.x509.client_certificates.primary.info == None
        assert am.x509.client_certificates.secondary.certificate == dummy_value_2
        assert am.x509.client_certificates.secondary.info == None

    def test_create_with_x509_signing_certificates_min(self, dummy_value_1):
        """Create an Attestation using X509 Signing Certificates with minimum values
        """
        am = AttestationMechanism.create_with_x509_signing_certificates(dummy_value_1)
        assert am.type == "x509"
        assert am.tpm == None
        assert am.x509.client_certificates == None
        assert am.x509.ca_references == None
        assert am.x509.signing_certificates.primary.certificate == dummy_value_1
        assert am.x509.signing_certificates.primary.info == None
        assert am.x509.signing_certificates.secondary == None

    def test_create_with_x509_signing_certificates_max(self, dummy_value_1, dummy_value_2):
        """Create an Attestation using X509 Signing Certificates with all values
        """
        am = AttestationMechanism.create_with_x509_signing_certificates(dummy_value_1, dummy_value_2)
        assert am.type == "x509"
        assert am.tpm == None
        assert am.x509.client_certificates == None
        assert am.x509.ca_references == None
        assert am.x509.signing_certificates.primary.certificate == dummy_value_1
        assert am.x509.signing_certificates.primary.info == None
        assert am.x509.signing_certificates.secondary.certificate == dummy_value_2
        assert am.x509.signing_certificates.secondary.info == None

    def test_create_with_x509_ca_references_min(dummy_value_1):
        """Create an Attestation using X509 CA References with minimum values
        """
        am = AttestationMechanism.create_with_x509_ca_references(dummy_value_1)
        assert am.type == "x509"
        assert am.tpm == None
        assert am.x509.client_certificates == None
        assert am.x509.signing_certificates == None
        assert am.x509.ca_references.primary == dummy_value_1
        assert am.x509.ca_references.secondary == None

    def test_create_with_x509_ca_references_max(dummy_value_1, dummy_value_2):
        """Create an Attestation using X509 CA References with all values
        """
        am = AttestationMechanism.create_with_x509_ca_references(dummy_value_1, dummy_value_2)
        assert am.type == "x509"
        assert am.tpm == None
        assert am.x509.client_certificates == None
        assert am.x509.signing_certificates == None
        assert am.x509.ca_references.primary == dummy_value_1
        assert am.x509.ca_references.secondary == dummy_value_2