# encoding: utf-8
from setuptools import setup, find_packages

SHORT = "A client for apollo 2.0"

__version__ = "0.1.0"
__author__ = ''
__email__ = ''
__url__=''
readme_path = 'README.md'

setup(
    name='py_apollo_cli',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    url=__url__,
    author=__author__,
    author_email=__email__,
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',        
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    include_package_data=True,
    package_data={'': ['*.py', '*.pyc']},
    zip_safe=False,
    platforms='any',

    description=SHORT,
    long_description=open(readme_path, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)