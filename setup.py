from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'jpegoptim',
    version          = '1.5.0', # Match jpegoptim version 
    description      = 'An app to optimize/compress JPEG/JFIF files',
    long_description = readme,
    author           = 'Benny Rochwerger',
    author_email     = 'brochwer@redhat.com',
    url              = 'https://github.com/tjko/jpegoptim',
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
