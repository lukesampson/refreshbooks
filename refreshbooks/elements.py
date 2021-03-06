from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
from lxml import etree

def field(name, value):
    field_element = etree.Element(name)
    field_element.text = value
    return field_element

def type(name, fields):
    type_element = etree.Element(name)
    
    for field in fields:
        type_element.append(field)
    
    return type_element

def request(name, parameters, _element_name='request'):
    request_element = type(_element_name, parameters)
    request_element.attrib.update(dict(method=name))
    return request_element
