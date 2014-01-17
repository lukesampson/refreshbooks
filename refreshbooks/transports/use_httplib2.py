from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
import httplib2

from refreshbooks import exceptions as exc

class Transport(object):
    def __init__(self, url, headers_factory):
        self.client = httplib2.Http()
        self.url = url
        self.headers_factory = headers_factory
    
    def __call__(self, entity):
        
        resp, content = self.client.request(
            self.url,
            'POST',
            headers=self.headers_factory(),
            body=entity
        )
        if resp.status >= 400:
            raise exc.TransportException(resp.status, content)
        
        return content
