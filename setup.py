#!/usr/bin/env python

from setuptools import setup
from codecs import open
import os
import re
import sys

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'namesilo', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

packages = ['namesilo']

requires = [
    'requests>=2.19.1',
    'lxml>=4.2.2',
    'beautifulsoup4>=4.6.0'
]

setup(
    name=about['name'],
    version=about['version'],
    description=about['description'],
    url=about['url'],
    author=about['author'],
    author_email=about['author_email'],
    packages=packages,
    install_requires=requires,
    package_dir={'namesilo': 'namesilo'},
    license=about['license'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)