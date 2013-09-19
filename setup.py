#!/usr/bin/python

# Python imports
import os

try:
    from setuptools import setup, Extension
    has_setuptools = True
except ImportError:
    from distutils.core import setup, Extension
    has_setuptools = False

version_string = '0.0.1'


setup_kwargs = {}

setup(name="openshift.py",
    description="Client library for Openshift REST API",
    keywords='',
    version="0.0.1",
    url='https://github.com/FriendCode/openshift.py.git',
    license='Apache',
    author="Samy Pesse",
    author_email='samy.pesse@friendco.de',
    long_description="""""",
    packages=[
        "openshift"
    ],
    **setup_kwargs
)
