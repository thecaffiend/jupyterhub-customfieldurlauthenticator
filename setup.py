#!/usr/bin/env python
from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

install_reqs = parse_requirements('requirements.txt', session=PipSession())
requirements = [str(ir.req) for ir in install_reqs]

__version__ = '0.1.0'

setup(
    name='jupyterhub-customfieldurlauthenticator',
    version=__version__,
    description='Authenticator for JupyterHub that authenticates against a remote URL and allows customization of the fields checked in the response',
    long_description=open('README.md').read(),
    keywords='jupyterhub jupyter jupyternotebook authentication',
    author='L. Drew Pihera',
    author_email='dpihera@gmail.com',
    url='https://github.com/thecaffiend/jupyterhub-customfieldurlauthenticator',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: MIT License',
                 'Environment :: Web Environment',
                 'Natural Language :: English',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Topic :: System :: Systems Administration :: Authentication/Directory',
                 'Environment :: Plugins',
                 'Framework :: Jupyter',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3 :: Only',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Science/Research',
                 'Intended Audience :: System Administrators',],
)
