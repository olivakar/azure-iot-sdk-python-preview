# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TwinCollection(Model):
    """Represents a collection of properties within a Twin.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param version: Version of the TwinCollection
    :type version: long
    :param count: Number of properties in the TwinCollection
    :type count: int
    :param metadata: Metadata for the TwinCollection
    :type metadata: ~protocol.models.Metadata
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'version': {'key': 'version', 'type': 'long'},
        'count': {'key': 'count', 'type': 'int'},
        'metadata': {'key': 'metadata', 'type': 'Metadata'},
    }

    def __init__(self, *, additional_properties=None, version: int=None, count: int=None, metadata=None, **kwargs) -> None:
        super(TwinCollection, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.version = version
        self.count = count
        self.metadata = metadata
