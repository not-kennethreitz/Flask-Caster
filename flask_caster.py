from flask import Flask, request, jsonify
from werkzeug.datastructures import ImmutableMultiDict

from flask import current_app

class FlaskCaster(object):
    """A simple type-caster for Flask query arguments.

    Basic usage:

      caster = FlaskCaster(app)
      caster.ints = ['size']
      caster.booleans = ['json']
      caster.always = ['json']

    This will do a few things:
     - Assure that the 'size' query parameter is always an integer.
     - Assure that the 'json' query parameter is always an boolean.
     - Assure that the 'json' query parameter is always present, even if
       if it wasn't provided by the end-user.
    """
    def __init__(self, app=None, default=None):
        self.app = app
        self.ints = []
        self.floats = []
        self.bools = []
        self.always = []
        self.always_default = default

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.before_request(self.caster)

    def caster(self):
        # Add parameters that always need to be there.
        for a in self.always:
            if a not in request.args:
                # Call default if it's a callable.
                if callable(self.always_default):
                    # Pass in the key name to the callable.
                    value = self.always_default(arg_name=a)
                else:
                    value = self.always_default

                self.replace_arg(a, value)

        # Replace ints.
        for i in self.ints:
            self.cast_to_type(i, int)

        # Replace floats.
        for f in self.floats:
            self.cast_to_type(f, float)

        # Replace booleans.
        for b in self.bools:
            if b in request.args:
                # Special case for false-like strings.
                if isinstance(request.args[b], basestring):
                    if request.args[b].lower() in ['0', 'false', 'f', 'null']:
                        self.replace_arg(b, False)

            self.cast_to_type(b, bool)

    def replace_arg(self, name, value):
        """Replaces a request query parameter with the given value."""
        new = request.args.copy()
        new[name] = value
        request.args = ImmutableMultiDict(new)

    def cast_to_type(self, name, t):
        """Casts a given argument to a given type."""
        try:
            self.replace_arg(name, t(request.args[name]))
        except KeyError:
            pass
