# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class IndividualEnrollmentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`IndividualEnrollment <protocol.models.IndividualEnrollment>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[IndividualEnrollment]'}
    }

    def __init__(self, *args, **kwargs):

        super(IndividualEnrollmentPaged, self).__init__(*args, **kwargs)
