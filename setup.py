from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from future.builtins import open
setup(
    name='refreshbooks',
    version='1.7.3.dev',
    author='Owen Jacobson',
    author_email='api@freshbooks.com',
    url='http://github.com/freshbooks/refreshbooks',
    download_url='http://pypi.python.org/pypi/refreshbooks/',
    description='A client library for the FreshBooks API',
    
    long_description=open("README.rst").read(),
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    
    packages=[
        'refreshbooks', 'refreshbooks.transports', 'refreshbooks.optional'
    ],
    
    setup_requires=[
        'setuptools-git',
        'nose'
    ],
    tests_require=[
        'nose',
        'mock'
    ],
    install_requires=[
        'lxml',
        'future'
    ],
    extras_require={
        'oauth': ['oauth'],
        'httplib2': ['httplib2 >= 0.7.2'],
        'requests': ['requests >= 0.11.1']
    },
    
    test_suite = 'nose.collector'
)
