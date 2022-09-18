pl-jpegoptim
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-jpegoptim?sort=semver
    :target: https://hub.docker.com/r/fnndsc/pl-jpegoptim

.. image:: https://img.shields.io/github/license/fnndsc/pl-jpegoptim
    :target: https://github.com/FNNDSC/pl-jpegoptim/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-jpegoptim/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/pl-jpegoptim/actions


.. contents:: Table of Contents


Abstract
--------

An app to optimize/compress JPEG/JFIF files.


Description
-----------


``jpegoptim`` is a *ChRIS ds-type* application that takes in directory of JPEG/JFIF files
and optimizes them by invoking the jpegoptim utility. More information available at:

'https://manpages.ubuntu.com/manpages/trusty/man1/jpegoptim.1.html'


Usage
-----

.. code::

    docker run --rm fnndsc/pl-jpegoptim jpegoptim
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [--version]
        [--force] [--noaction] [--csv] [--quiet] 
        [--totals] [--verbose]
        [--max=<###>]
        [--size=<###>]
        [--preserve] [--preserve-perms]
        [--strip-all] [--strip-none] [--strip-com] 
        [--strip-exif] [--strip-iptc] [--strip-icc] 
        [--strip-xmp]
        [--all-normal] [--all-progressive]

        <inputDir> <outputDir>


Arguments
~~~~~~~~~

.. code::

    [-h] [--help]
    If specified, show help message and exit.
    
    [--json]
    If specified, show json representation of app and exit.
    
    [--man]
    If specified, print (this) man page and exit.

    [--meta]
    If specified, print plugin meta data and exit.
    
    [--savejson <DIR>] 
    If specified, save json representation file to DIR and exit. 
    
    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.
    
    [--version]
    If specified, print version number and exit. 

    [--force]
    force optimization

    [--max]
    set maximum image quality factor (disables lossless optimization mode, which is by default on) Valid quality values: 0 - 100

    [--noaction]
    don't really optimize files, just print results

    [--size]
    Try to optimize file to given size (disables lossless optimization mode). Target size is specified either in kilo bytes (1 - n) or as percentage (1% - 99%)

    [--csv]
    print progress info in CSV format

    [--preserve]
    preserve file timestamps

    [--preserve-perms]
    preserve original file permissions by overwriting it

    [--quiet]
    quiet mode

    [--totals]
    print totals after processing all files

    [--verbose]
    enable verbose mode (positively chatty)

    [--strip-all]
    strip all markers from output file

    [--strip-none]
    do not strip any markers

    [--strip-com]
    strip Comment markers from output file

    [--strip-exif]
    strip Exif markers from output file

    [--strip-iptc]
    strip IPTC/Photoshop (APP13) markers from output file

    [--strip-icc]
    strip ICC profile markers from output file

    [--strip-xmp]
    strip XMP markers markers from output file

    [--all-normal]
    force all output files to be non-progressive

    [--all-progressive]
    force all output files to be progressive



Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-jpegoptim jpegoptim --man

Run
~~~

You need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                             \
        -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
        fnndsc/pl-jpegoptim jpegoptim                        \
        /incoming /outgoing


Development
-----------

Create initial flags.json file using the utility script provided:

.. code:: bash

    python ./prepare_flags.py

Edit the resulting flags.json to match the target program (in particular, check defaults and types):

.. code:: bash 

    vi flags.json 

Build the Docker container:

.. code:: bash

    docker build -t local/pl-jpegoptim .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-jpegoptim nosetests

Examples
--------

Reduce input images to images half the size:

.. code:: docker run -v $INPUTDIR:/input -v $OUTPUTDIR:/outdir --rm fnndsc/pl-jpegoptim --size=50% /indir /outdir

Remove ALL metadata from input images:

.. code:: docker run -v $INPUTDIR:/input -v $OUTPUTDIR:/outdir --rm fnndsc/pl-jpegoptim --strip-all /indir /outdir

Remove IPTC metadata from input images:

.. code:: docker run -v $INPUTDIR:/input -v $OUTPUTDIR:/outdir --rm fnndsc/pl-jpegoptim --strip-iptc /indir /outdir

.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstor