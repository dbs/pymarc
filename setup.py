def get_version():
    """
    Parse the version from __init__

    Avoids dependency hell due to __init__ requiring the "six" module,
    while maintaining the convenience of specifying version just once.
    """

    import re
    with open('pymarc/__init__.py', 'r') as f:
        content = f.readlines()
    for line in content:
        if line.startswith('__version__'):
            version = re.sub(r'^__version__\s*=\s*([\'"])(.+?)\1', r'\2', line)
    return version

from setuptools import setup, find_packages

install_requires = ['six']
try:
    import xml.etree
except ImportError:
    install_requires.append('elementtree>=1.2.6')

import sys
if sys.version_info < (2 , 6):
    install_requires.append('simplejson>=1.7.3')
del sys

classifiers = """
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: BSD License
Programming Language :: Python
Topic :: Text Processing :: General
"""

setup( 
    name = 'pymarc',
    version = get_version(),
    url = 'http://github.com/edsu/pymarc',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    license = 'http://www.opensource.org/licenses/bsd-license.php',
    packages = find_packages(),
    install_requires = install_requires,
    description = 'read, write and modify MARC bibliographic data',
    classifiers = filter(None, classifiers.split('\n')),
    test_suite = 'test',
)
