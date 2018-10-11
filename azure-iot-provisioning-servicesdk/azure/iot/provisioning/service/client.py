# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

"""Redefine the generated ProvisioningServiceClient class via inheritance to allow for API
customization and authentication logic injection
"""

from .protocol import ProvisioningServiceClient as _ProvisioningServiceClient
from .auth import ConnectionStringAuthentication, HOST_NAME

class ProvisioningServiceClient(_ProvisioningServiceClient):
    """API for service operations with the Azure IoT Hub Device Provisioning Service

    :ivar config: Configuration for client.
    :vartype config: ProvisioningServiceClientConfiguration

    :param str connection_string: Connection String for your Device Provisioning Service hub.
    """

    def __init__(self, connection_string):
        cs_auth = ConnectionStringAuthentication(connection_string)
        super(ProvisioningServiceClient, self).__init__(cs_auth, "https://" + cs_auth[HOST_NAME])


    def create_or_update_individual_enrollment(self, id, enrollment, custom_headers=None, raw=False, **operation_config):
        """Create or update a device enrollment record.

        :param id: The registration ID is alphanumeric, lowercase, and may
         contain hyphens.
        :type id: str
        :param enrollment: The device enrollment record.
        :type enrollment: ~protocol.models.IndividualEnrollment
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: IndividualEnrollment or ClientRawResponse if raw=true
        :rtype: ~protocol.models.IndividualEnrollment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ProvisioningServiceErrorDetailsException<protocol.models.ProvisioningServiceErrorDetailsException>`
        """
        return super(ProvisioningServiceClient, self).create_or_update_individual_enrollment(id, enrollment, enrollment.etag, custom_headers, raw, **operation_config)
    create_or_update_individual_enrollment.metadata = _ProvisioningServiceClient.create_or_update_individual_enrollment.metadata


    def create_or_update_enrollment_group(self, id, enrollment_group, custom_headers=None, raw=False, **operation_config):
        """Create or update a device enrollment group.

        :param id: Enrollment group ID.
        :type id: str
        :param enrollment_group: The device enrollment group.
        :type enrollment_group: ~protocol.models.EnrollmentGroup
        :param if_match: The ETag of the enrollment record.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: EnrollmentGroup or ClientRawResponse if raw=true
        :rtype: ~protocol.models.EnrollmentGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ProvisioningServiceErrorDetailsException<protocol.models.ProvisioningServiceErrorDetailsException>`
        """
        return super(ProvisioningServiceClient, self).create_or_update_enrollment_group(id, enrollment_group, enrollment_group.etag, custom_headers, raw, **operation_config)
    create_or_update_enrollment_group.metadata = _ProvisioningServiceClient.create_or_update_enrollment_group.metadata
