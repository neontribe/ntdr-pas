#! /usr/bin/env python

# Find symbolic links and show where they point to.
# Arguments are directories to search; default is /var/www
# No recursion.

import sys, os, json, shlex

''' Ansible uploads the args as a fil '''
args_file = sys.argv[1]
args_data = file(args_file).read()

arguments = shlex.split(args_data)
if not arguments: arguments = ['/var/www/']

data = {}
for arg in arguments:
    for name in os.listdir(arg):
        if name not in (os.curdir, os.pardir):
            full = os.path.join(arg, name)
            if os.path.islink(full):
                data[name] =  os.readlink(full)

print json.dumps(data)
sys.exit(0)
