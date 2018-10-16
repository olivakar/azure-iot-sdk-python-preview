# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QuerySpecification(Model):
    """A Json query request.

    All required parameters must be populated in order to send to Azure.

    :param query: Required. The query.
    :type query: str
    """

    _validation = {"query": {"required": True}}

    _attribute_map = {"query": {"key": "query", "type": "str"}}

    def __init__(self, **kwargs):
        super(QuerySpecification, self).__init__(**kwargs)
        self.query = kwargs.get("query", None)
