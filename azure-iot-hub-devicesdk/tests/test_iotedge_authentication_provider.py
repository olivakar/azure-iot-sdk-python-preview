# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import pytest

class TestSignatureOperation(object):
    def signing_operation_fails_if_environment_variables_are_missing(self):
        """
        verify that signature operations fail if the needed environment variables are missing.
        """
        pass

    def signing_operation_calls_into_edge_daemon_to_sign_for_connection_string(self):
        """
        Verify that the iotedge authentication provider calls into the edge daemon using
        HTTP with a propertly constructed REST calls in order to do a signing operation.
        """
        pass

    def signing_operation_fails_if_http_signing_operation_fails(self):
        """
        Verify that the iotedge authentication provider fails if the http call for the
        signing operation fails.
        """
        pass

    def signing_operation_creates_valid_sas_token(self):
        """
        Verify that the result of the signing operation is used to create a valid
        SAS token.
        """
        pass

class TestGetCaCert(object):
    def get_fails_if_environment_variables_are_missing(self):
        """
        verify that signature operations fail if the needed environment variables are missing.
        """
        pass


    def get_returns_correct_ca_from_iotedge_trust_bundle(self):
        """
        Verify that the iotedge authentication provider calls into the edge daemon using
        HTTP with a propertly constructed REST call in order to retrieve and return the
        trust bundle.
        """
        pass

    def get_fails_if_http_call_to_get_trust_bundle_fails(self):
        """
        Verify that an HTTP failure getting the trust bundle will cause the call to
        get_trusted_certificate_authority to fail.
        """
        pass
