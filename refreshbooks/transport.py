from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
import base64
import http.client

from refreshbooks import exceptions

try:
    from refreshbooks.optional import oauth as os
    
    OAuthAuthorization = os.OAuthAuthorization
except ImportError:
    def OAuthAuthorization(consumer, token, sig_method=None):
        raise NotImplementedError('oauth support requires the "oauth" module.')

try:
    from refreshbooks.transports import use_requests as transport
except ImportError:
    try:
        from refreshbooks.transports import use_httplib2 as transport
    except ImportError:
        import warnings
        warnings.warn(
            "Unable to load requests or httplib2 transports, falling back to urllib2. SSL cert verification disabled."
        )
        from refreshbooks.transports import use_urllib2 as transport

class TokenAuthorization(object):
    """Generates HTTP BASIC authentication headers obeying FreshBooks'
    token-based auth scheme (token as username, password irrelevant).
    
        >>> auth = TokenAuthorization("monkey")
        >>> auth()
        {'Authorization': 'Basic bW9ua2V5Og=='}
    
    Prefer OAuthAuthorization, from refreshbooks.optional.oauth, for new
    development.
    """
    def __init__(self, token):
        # See RFC 2617.
        base64_user_pass = base64.b64encode("%s:" % (token, ))
        
        self.headers = {
            'Authorization': 'Basic %s' % (base64_user_pass, )
        }
    
    def __call__(self):
        return self.headers

class UserAgentHeaders(object):
    def __init__(self, base_headers_factory, user_agent):
        self.base_headers_factory = base_headers_factory
        self.user_agent = user_agent
    
    def __call__(self):
        headers = self.base_headers_factory()
        headers['User-Agent'] = self.user_agent
        return headers

class KeepAliveHeaders(object):
    def __init__(self, base_headers_factory):
        self.base_headers_factory = base_headers_factory
    
    def __call__(self):
        headers = self.base_headers_factory()
        headers['Connection'] = 'Keep-Alive'
        return headers

HttpTransport = transport.Transport
TransportException = exceptions.TransportException
