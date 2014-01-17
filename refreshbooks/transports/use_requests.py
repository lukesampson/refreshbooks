from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
import requests

from refreshbooks import exceptions as exc

class Transport(object):
    def __init__(self, url, headers_factory):
        self.session = requests.session()
        self.url = url
        self.headers_factory = headers_factory
    
    def __call__(self, entity):
        
        resp = self.session.post(
            self.url,
            headers=self.headers_factory(),
            data=entity
        )
        if resp.status_code >= 400:
            raise exc.TransportException(resp.status_code, resp.content)
        
        return resp.content
