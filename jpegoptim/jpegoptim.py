#
# jpegoptim ds ChRIS plugin app
#
# (c) 2022 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp

import json

Gstr_title = r"""
   _                              _   _           
  (_)                            | | (_)          
   _ _ __   ___  __ _  ___  _ __ | |_ _ _ __ ___  
  | | '_ \ / _ \/ _` |/ _ \| '_ \| __| | '_ ` _ \ 
  | | |_) |  __/ (_| | (_) | |_) | |_| | | | | | |
  | | .__/ \___|\__, |\___/| .__/ \__|_|_| |_| |_|
 _/ | |          __/ |     | |                    
|__/|_|         |___/      |_|                    
"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS and TS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       jpegoptim

    SYNOPSIS

        docker run --rm fnndsc/pl-jpegoptim jpegoptim                     \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-jpegoptim jpegoptim                        \
                /incoming /outgoing

    DESCRIPTION

        `jpegoptim` ...

    ARGS

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
"""


class Jpegoptim(ChrisApp):
    """
    An app to ...
    """
    PACKAGE                 = __package__
    TITLE                   = 'The ChRIS jpegoptim plugin'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 2000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 8000  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    #maxquality = 100

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        # self.add_argument("--max", type=int, help='Maximum image quality, valid values are 0-100', dest='maxquality', optional=True, default=100)

        with open('flags.json') as fd:
            flags = json.load(fd)

        for f,v in flags.items():
            helpmsg = v['help'].replace("%", "")
            flag = "--"+f
            # if v['type'] != 'bool':
            #     self.add_argument(flag, type=eval(v['type']), help=v['help'], dest=f, optional=True, default=v['default'])
            if v['type'] == 'int':
                self.add_argument(flag, type=int,  help=helpmsg, dest=f, optional=True, default=v['default'])
            elif v['type'] == 'str':
                self.add_argument(flag, type=str,  help=helpmsg, dest=f, optional=True, default=v['default'])
            elif v['type'] == 'bool':
                self.add_argument(flag, type=bool, help=helpmsg, dest=f, optional=True, default=v['default'], action=v['action'])

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        print(options.maxquality)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
