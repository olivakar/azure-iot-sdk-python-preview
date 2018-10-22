# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import pytest

def test_iotedge_auth_provider_calls_into_edge_daemon_to_sign_for_connection_string():
    """
    Verify that the iotedge authentication provider calls into the edge daemon using
    HTTP with a propertly constructed REST calls in order to do a signing operation.
    Also verify that the result of the signing operation is used to create a valid
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
