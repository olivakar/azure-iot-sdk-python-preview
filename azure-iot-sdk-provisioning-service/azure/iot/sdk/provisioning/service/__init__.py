# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

from .client import ProvisioningServiceClient
from . import models

models._patch_attestation_mechanism()

__all__ = [
    "ProvisioningServiceClient",
    "models",
]