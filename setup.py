"""
Flask-SQLite3
-------------

This is the description for that library
"""
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