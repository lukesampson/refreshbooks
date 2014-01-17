from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from future import standard_library

import oauth.oauth as oauth

class OAuthAuthorization(object):
    """Generates headers for an OAuth Core 1.0 Revision A (say that three 
    times fast) request, given an oauth.Consumer and an oauth.Token.
    
        >>> import oauth.oauth as oauth
        >>> consumer = oauth.OAuthConsumer("EXAMPLE", "CONSUMER")
        >>> token = oauth.OAuthToken("EXAMPLE", "TOKEN")
        >>> auth = OAuthAuthorization(consumer, token)
        >>> auth() # doctest:+ELLIPSIS
        {'Authorization': 'OAuth realm="", oauth_nonce="...", oauth_timestamp="...", oauth_consumer_key="EXAMPLE", oauth_signature_method="PLAINTEXT", oauth_version="1.0", oauth_token="EXAMPLE", oauth_signature="CONSUMER%26TOKEN"'}
    
    """
    def __init__(self, consumer, token, sig_method=oauth.OAuthSignatureMethod_PLAINTEXT()):
        self.consumer = consumer
        self.token = token
        self.sig_method = sig_method

    def __call__(self):
        oauth_request = oauth.OAuthRequest.from_consumer_and_token(
            self.consumer,
            token=self.token
        )
        oauth_request.sign_request(self.sig_method, self.consumer, self.token)
        return oauth_request.to_header()

def OAuthClient(
    AuthorizingClient,
    domain,
    consumer_key,
    consumer_secret,
    token,
    token_secret,
    user_agent,
    request_encoder,
    response_decoder
):
    consumer = oauth.OAuthConsumer(consumer_key, consumer_secret)
    token = oauth.OAuthToken(token, token_secret)

    return AuthorizingClient(
        domain,
        OAuthAuthorization(
            consumer,
            token
        ),
        request_encoder,
        response_decoder,
        user_agent=user_agent
    )
