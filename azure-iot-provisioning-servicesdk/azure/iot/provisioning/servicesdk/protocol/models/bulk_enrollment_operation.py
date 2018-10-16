# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BulkEnrollmentOperation(Model):
    """Bulk operation.

    All required parameters must be populated in order to send to Azure.

    :param enrollments: Required. Enrollment items
    :type enrollments: list[~protocol.models.IndividualEnrollment]
    :param mode: Required. Operation mode. Possible values include: 'create',
     'update', 'updateIfMatchETag', 'delete'
    :type mode: str or ~protocol.models.enum
    """

    _validation = {
        'enrollments': {'required': True},
        'mode': {'required': True},
    }

    _attribute_map = {
        'enrollments': {'key': 'enrollments', 'type': '[IndividualEnrollment]'},
        'mode': {'key': 'mode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BulkEnrollmentOperation, self).__init__(**kwargs)
        self.enrollments = kwargs.get('enrollments', None)
        self.mode = kwargs.get('mode', None)