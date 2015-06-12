#! /usr/bin/env python

# Find changelog vesion
# Arguments are directories to search; default is /var/www/latest
# No recursion.

import sys, os, json, shlex

def get_version(name):
    full = os.path.join(name, 'changelog.txt')
    if os.path.isfile(full):
        with open(full, 'r') as f:
            first_line = f.readline()
        parts = first_line.split();
        return parts[1]
    return False

def get_versions(arguments):
    data = {}
    for name in arguments:
        data[name] = get_version(name)
    return data

if __name__ == "__main__":
    ''' Ansible uploads the args as a fil '''
    args_file = sys.argv[1]
    args_data = file(args_file).read()

    arguments = shlex.split(args_data)
    if not arguments: arguments = ['/var/www/latest']

    data = get_versions(arguments)
    print json.dumps(data)
    sys.exit(0)

