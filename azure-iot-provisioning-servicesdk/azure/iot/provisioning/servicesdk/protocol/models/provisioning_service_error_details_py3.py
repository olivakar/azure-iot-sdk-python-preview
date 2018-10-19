# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class ProvisioningServiceErrorDetails(Model):
    """Contains the properties of an error returned by the Azure IoT Hub
    Provisioning Service.

    :param error_code:
    :type error_code: int
    :param tracking_id:
    :type tracking_id: str
    :param message:
    :type message: str
    :param info:
    :type info: dict[str, str]
    :param timestamp_utc:
    :type timestamp_utc: datetime
    """

    _attribute_map = {
        'error_code': {'key': 'errorCode', 'type': 'int'},
        'tracking_id': {'key': 'trackingId', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'info': {'key': 'info', 'type': '{str}'},
        'timestamp_utc': {'key': 'timestampUtc', 'type': 'iso-8601'},
    }

    def __init__(self, *, error_code: int=None, tracking_id: str=None, message: str=None, info=None, timestamp_utc=None, **kwargs) -> None:
        super(ProvisioningServiceErrorDetails, self).__init__(**kwargs)
        self.error_code = error_code
        self.tracking_id = tracking_id
        self.message = message
        self.info = info
        self.timestamp_utc = timestamp_utc


class ProvisioningServiceErrorDetailsException(HttpOperationError):
    """Server responsed with exception of type: 'ProvisioningServiceErrorDetails'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ProvisioningServiceErrorDetailsException, self).__init__(deserialize, response, 'ProvisioningServiceErrorDetails', *args)
