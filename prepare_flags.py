#! /bin/env python
# 
# prepare_flags.py: Utility to create the list of flags supported by target progrem (jpegoptim in this case).
#
# Usage: invoke this program PRIOR to building container image, edit the result and then build container image
# 
# Note: The resulting file (flags.json) needs to be manually tuned to properly fit the target program; in particular, defaults need to be set
# This utility could be extended to fully automate the process of creating the flags but the effort to create a generic tool that properly 
# handles all the special cases is not worth it for a single target program. 
#
#  

import argparse
import subprocess
import re
import json

ignore_flags = ['dest', 'stdout', 'stdin', 'overwrite', 'help', 'threshold', 'version']

def main(args):
    cmd = ('jpegoptim', '--help')
    cp = subprocess.run(cmd, capture_output=True, text=True)
    # lines = cp.stderr.split('\n')
    lines = cp.stderr.split('--')
    flags = {}
    for line in lines[1:]:
        values = {}
        key,help = re.split('-.+,',line,maxsplit=1)[0].split(maxsplit=1)
        if key.find('=') != -1:
            key = key.split('=')[0]
            values['type'] = 'int'
            values['default'] = 999
        else:
            values['type'] = 'bool'
            values['action'] = 'store_true'
            values['default'] = False

        if key not in ignore_flags:
            values['help'] = re.subn('\n *', ' ', help)[0].rstrip()
            values['dest'] = key
            flags[key] = values

    if args.doc:
        for f,v in flags.items():
            print('    [--{}]'.format(f))
            print('    {}'.format(v['help']))
    else:
        with open('flags.json', 'w') as fp:
            json.dump(flags, fp, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--doc", action='store_true', help="Generate documentation in format appropiate to add to README.rst")
    args = parser.parse_args()
    main(args)