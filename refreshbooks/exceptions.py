from __future__ import unicode_literals
class TransportException(Exception):
    def __init__(self, status, content):
        self.status = status
        self.content = content
    
    def __str__(self):
        return repr(self)
    
    def __repr__(self):
        return "TransportException(%r, %r)" % (self.status, self.content)
