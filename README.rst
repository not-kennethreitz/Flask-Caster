Flask-Caster: Cast Types to Flask Query Parameters
==================================================

This simple Flask extension allows you to cast the type of (and assign defaults to) request query parameters in Flask.

Example Usage
-------------

::

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


Installation
------------

::

    $ pip install Flask-Caster

✨🍰✨