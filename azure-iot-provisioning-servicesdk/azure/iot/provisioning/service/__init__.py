# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

from .client import ProvisioningServiceClient
from . import models

#Patch model convenience methods
models._patch_attestation_mechanism()

#Remove query operations from client (they are not currently supported)
delattr(ProvisioningServiceClient, "query_individual_enrollments")
delattr(ProvisioningServiceClient, "query_enrollment_groups")
delattr(ProvisioningServiceClient, "query_device_registration_states")

__all__ = [
    "ProvisioningServiceClient",
    "models",
]