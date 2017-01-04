"""
    pai-db
    ~~~~~~

    Persistent storage of defined resources/relations.
"""

import ast
import re

try:
    from setuptools import setup
except ImportError:
    from distutils import setup


version_regex = re.compile(r'__version__\s+=\s+(.*)')


def get_version():
    with open('pai_db/__init__.py', 'r') as f:
        return str(ast.literal_eval(version_regex.search(f.read()).group(1)))


setup(
    name='pai-db',
    version=get_version(),
    author='Andrew Hawker',
    author_email='andrew.r.hawker@gmail.com',
    url='https://github.com/ahawker/pai-db',
    license='Apache 2.0',
    description='Persistent storage of defined resources/relations.',
    long_description=__doc__,
    packages=['pai_db'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]

)
