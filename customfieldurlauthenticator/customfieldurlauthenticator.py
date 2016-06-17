from urlauthenticator import UrlAuthenticator

from tornado import gen
from traitlets import (
    Unicode,
    Int,
    Dict,
)

import urllib, urllib.request
import json

class CustomFieldUrlAuthenticator(UrlAuthenticator):
    """
    Class for authenticating to jupyterhub against a remote URL and also checking the
    response against a set of configurable fields.
    """

    # config values
    custom_fields = Dict(
        default_value={},
        config=True,
        help='mapping of fields to check from the http response to values to check for during authentication.' # LEFTOFF
    )

    def process_response(self, resp):
        """
        do whatever checks are necessary against the response to determine if
        the user should be authenticated. in this case, we also want to check
        against the fields in the configuration
        """
        d = json.loads(resp.decode())
        username = d.get('username', None)

        if username and self.validate_custom_fields(d):
            return username
        return None

    def validate_custom_fields(self, d):
        """
        check the provided dictonary against the configured fields from the
        config. return True/False
        """
        # see if all the custom keys are in d (d may have extra stuff, but the
        # custom fields cannot)
        if set(self.custom_fields.keys()) > set(d.keys()):
            return False

        for k, v in self.custom_fields.items():
            if d[k] != v:
                # found a bad value, not valid
                return False
        return True
