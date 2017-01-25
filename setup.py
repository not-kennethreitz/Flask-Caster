# -*- coding: utf-8 -*-
"""
Flask-Caster: Cast Types of Flask Query Parameters
==================================================

This simple Flask extension allows you to cast the type of (and assign defaults to) request query parameters in Flask.

Example Usage
-------------

::

    from flask import Flask
    from flask_caster import FlaskCaster

    app = Flask(__name__)

    caster = FlaskCaster(app)
    caster.ints = ['size']
    caster.booleans = ['json']
    caster.always = ['json']

This will do a few things:

- Assure that the ``size`` query parameter is always an integer.
- Assure that the ``json`` query parameter is always an boolean.
- Assure that the ``json`` query parameter is always present, even if
  if it wasn't provided by the end-user.

Assignable properties include ``ints``, ``booleans``, ``always``, and ``always_default``. The ``always_default`` property can be set to any value,
or to a callable, which will receive one keyword argument: ``arg_name``.

For boolean casting, ``0``, ``false``, ``f``, and ``null`` will
automatically be converted to ``False``.

Installation
------------

::

    $ pip install Flask-Caster

✨🍰✨
"""
import sys
import os
from setuptools import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()


setup(
    name='Flask-Caster',
    version='0.1.0',
    url='http://github.com/kennethreitz/Flask-Caster',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.org',
    description='A simple Flask extension for automatically casting the type of query arguments.',
    long_description=__doc__,
    py_modules=['flask_caster'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)