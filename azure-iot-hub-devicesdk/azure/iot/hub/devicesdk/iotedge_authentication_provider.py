# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from . import SymmetricKeyAuthenticationProvider

class IoTEdgeAuthenticationProvider(SymmetricKeyAuthenticationProvider):
    """
    Authentication provider that can authenticate module clients using the Edge daemon, AKA libiothsm.
    Most of the functionality for this class comes from the SymmetricKeyAuthenticationProvider class.
    This object just allows for the creation of a SAS token using the iotedge environment and it
    provides a way for clients to get the CA to use when connecting to edgehub.  All other functionality,
    including sas renewal logic, is inherited.
    """

    def __init__(self):

    @classmethod
    def from_environment(cls):
        pass

    def _sign(self):
        """
        Use the edge daemon to perform a signing operation and create a shared access signature.

        Question for the masses: this method is an override.  How to we indicate that in the code?  Is there
        special syntax or some comment convention we can use?
        """
        pass

    def get_trusted_certificate_authority(self):
        """
        Get the trust bundle from the edge daemon and return it as a string.  This string can be
        passed into the transport as the Certificate Authority (CA) to initiate a server-signed
        connection to edgeHub.
        """
