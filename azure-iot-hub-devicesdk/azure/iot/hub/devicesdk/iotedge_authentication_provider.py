# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import sys
import time
from .iotedge_hsm import IotEdgeHsm


class IotEdgeAuthenticationProvider(object):
    """
    A provider for authentication mechanism based on the IotEdge HSM
    """

    _token_format = "SharedAccessSignature sr={}&sig={}&se={}"

    def __init__(self):
        self.hsm = IotEdgeHsm()
        self.sas_ttl = 3600
        self.hostname = os.environ["IOTEDGE_IOTHUBHOSTNAME"]
        self.device_id = os.environ["IOTEDGE_DEVICEID"]
        self.module_id = os.environ["IOTEDGE_MODULEID"]
        self.gateway_hostname = os.environ["IOTEDGE_GATEWAYHOSTNAME"]
        self.shared_access_signature = self._renew_shared_access_signature()
        self.trusted_ca = self.hsm.get_trust_bundle()
        self._renew_shared_access_signature()

    @classmethod
    def create_from_environment(cls):
        auth_provider = cls()
        return auth_provider

    def _renew_shared_access_signature(self):
        # TODO: URI encode
        resource_uri = (
            self.hostname + "/devices/" + self.device_id + "/modules/" + self.module_id
        )
        expiry = math.floor(time.time) + self.sas_ttl
        string_to_sign = resource_uri + "\n" + expiry
        sig = hsm.sign(string_to_sign)
        self.shared_access_signature = _token_format.format(resource_uri, sig, expiry)
