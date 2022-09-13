from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'jpegoptim',
    version          = '0.1',
    description      = 'An app to ...',
    long_description = readme,
    author           = 'Benny Rochwerger',
    author_email     = 'brochwer@redhat.com',
    url              = 'http://wiki',
    packages         = ['jpegoptim'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'jpegoptim = jpegoptim.__main__:main'
            ]
        }
)
