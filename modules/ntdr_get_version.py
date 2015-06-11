#! /usr/bin/env python

# Find changelog vesion
# Arguments are directories to search; default is /var/www/latest
# No recursion.

import sys, os, json, shlex

''' Ansible uploads the args as a fil '''
args_file = sys.argv[1]
args_data = file(args_file).read()

arguments = shlex.split(args_data)
if not arguments: arguments = ['/var/www/latest']

data = {}
for name in arguments:
    if name not in (os.curdir, os.pardir):
        full = os.path.join(name, 'changelog.txt')
        if os.path.isfile(full):
            with open(full, 'r') as f:
                first_line = f.readline()
            parts = first_line.split();
            data[name] = parts[1]
        else:
            data[name] = False

print json.dumps(data)
sys.exit(0)
