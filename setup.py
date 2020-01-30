#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
import re


with open('encrypted_fields/__init__.py', 'r') as init_file:
    version = re.search(
        '^__version__ = [\'"]([^\'"]+)[\'"]',
        init_file.read(),
        re.MULTILINE,
    ).group(1)


setup(
    name='django-encrypted-fields',
    description=(
        'This is a collection of Django Model Field classes '
        'that are encrypted using a Keyczar compatibility layer to the cryptography module.'
    ),
    url='http://github.com/stuarta0/django-encrypted-fields/',
    license='BSD',
    author='Stuart Attenborrow',
    author_email='stuarta0@gmail.com',
    packages=['encrypted_fields'],
    version=version,
    install_requires=[
        'Django>=1.4',
        'cryptography>=2.8',
    ],
)
