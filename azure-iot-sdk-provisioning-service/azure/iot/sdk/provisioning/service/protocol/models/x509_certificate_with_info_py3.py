# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class X509CertificateWithInfo(Model):
    """Certificate and Certificate info.

    :param certificate:
    :type certificate: str
    :param info:
    :type info: ~protocol.models.X509CertificateInfo
    """

    _attribute_map = {
        'certificate': {'key': 'certificate', 'type': 'str'},
        'info': {'key': 'info', 'type': 'X509CertificateInfo'},
    }

    def __init__(self, *, certificate: str=None, info=None, **kwargs) -> None:
        super(X509CertificateWithInfo, self).__init__(**kwargs)
        self.certificate = certificate
        self.info = info