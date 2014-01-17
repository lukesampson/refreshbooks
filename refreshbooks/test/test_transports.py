from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
from mock import patch, Mock, sentinel
from nose.tools import raises
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from refreshbooks.exceptions import TransportException

@attr('integration')
@raises(TransportException)
def test_urllib2_transport_exception():
    from refreshbooks.transports.use_urllib2 import Transport
    Transport('http://httpstat.us/400', dict)(b"foo")

@attr('integration')
def test_urllib2():
    from refreshbooks.transports.use_urllib2 import Transport
    assert len(Transport('http://httpstat.us/200', dict)(b"foo")) > 0

@attr('integration')
@raises(TransportException)
def test_httplib2_transport_exception():
    try:
        import httplib2
    except ImportError:
        raise SkipTest("module 'httplib2' not installed")
    from refreshbooks.transports.use_httplib2 import Transport
    Transport('http://httpstat.us/400', dict)("foo")

@attr('integration')
def test_httplib2():
    try:
        import httplib2
    except ImportError:
        raise SkipTest("module 'httplib2' not installed")
    from refreshbooks.transports.use_httplib2 import Transport
    assert len(Transport('http://httpstat.us/200', dict)("foo")) > 0

@attr('integration')
@raises(TransportException)
def test_requests_transport_exception():
    try:
        import requests
    except ImportError:
        raise SkipTest("module 'requests' not installed")
    from refreshbooks.transports.use_requests import Transport
    Transport('http://httpstat.us/400', dict)("foo")

@attr('integration')
def test_requests():
    try:
        import requests
    except ImportError:
        raise SkipTest("module 'requests' not installed")
    from refreshbooks.transports.use_requests import Transport
    assert len(Transport('http://httpstat.us/200', dict)("foo")) > 0
