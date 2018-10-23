# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import pytest

def test_iotedge_auth_provider_calls_into_edge_daemon_to_sign_for_connection_string():
    """
    Verify that the iotedge authentication provider calls into the edge daemon using
    HTTP with a propertly constructed REST calls in order to do a signing operation.
    """
    pass

def test_iotedge_auth_provider_fails_if_http_signing_operation_fails():
    """
    Verify that the iotedge authentication provider fails if the http call for the
    signing operation fails.
    """
    pass

def test_iotedge_auth_provider_signature_creates_valid_sas_token():
    """
    Verify that the result of the signing operation is used to create a valid
    SAS token.
    """
    pass

def test_iotedge_auth_provider_returns_correct_ca_from_iotedge_trust_bundle():
    """
    Verify that the iotedge authentication provider calls into the edge daemon using
    HTTP with a propertly constructed REST call in order to retrieve and return the
    trust bundle.
    """
    pass

def test_iotedge_auth_provider_fails_if_http_call_to_get_trust_bundle_fails():
    """
    Verify that an HTTP failure getting the trust bundle will cause the call to
    get_trusted_certificate_authority to fail.
    """
    pass
