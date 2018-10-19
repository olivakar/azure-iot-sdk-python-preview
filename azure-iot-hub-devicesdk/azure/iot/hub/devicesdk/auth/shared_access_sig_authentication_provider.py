# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .authentication_provider import AuthenticationProvider
import six.moves.urllib as urllib


class SharedAccessSigAuthenticationProvider(AuthenticationProvider):
    def __init__(self, shared_access_token):

        self.shared_access_signature_token = shared_access_token._token
        resource_uri = shared_access_token._uri
        unqouted_resource_uri = urllib.parse.unquote_plus(resource_uri)
        url_segments = unqouted_resource_uri.split('/')

        self.module_id = None
        self.hostname = url_segments[0]

        if len(url_segments) > 4:
            self.module_id = url_segments[len(url_segments)-1]
            self.device_id = url_segments[len(url_segments)-3]
        else:
            self.device_id = url_segments[len(url_segments)-1]

    def get_current_sas_token(self):
        return self.shared_access_signature_token

