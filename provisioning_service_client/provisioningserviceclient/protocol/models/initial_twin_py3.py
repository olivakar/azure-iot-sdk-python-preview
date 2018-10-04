# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InitialTwin(Model):
    """Initial device twin. Contains a subset of the properties of Twin.

    :param tags: Twin tags.
    :type tags: ~protocol.models.TwinCollection
    :param properties: Twin desired properties.
    :type properties: ~protocol.models.InitialTwinProperties
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': 'TwinCollection'},
        'properties': {'key': 'properties', 'type': 'InitialTwinProperties'},
    }

    def __init__(self, *, tags=None, properties=None, **kwargs) -> None:
        super(InitialTwin, self).__init__(**kwargs)
        self.tags = tags
        self.properties = properties
