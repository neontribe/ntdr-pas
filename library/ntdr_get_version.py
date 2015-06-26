#! /usr/bin/env python

# Find changelog vesion

import sys, os, json, shlex

def main():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True),
            version = dict(default='no', type='bool'),
        ),
        supports_check_mode = True
    )

    path = module.params.get('path')
    path = os.path.expanduser(path)

    full = os.path.join(path, 'changelog.txt')
    if os.path.isfile(full):
        with open(full, 'r') as f:
            first_line = f.readline()
        parts = first_line.split();
        version = parts[1]
        found = True
    else:
        version = os.path.basename(path)
        found = False

    parts = version.split('.')
    count = len(parts)

    if (count > 0):
        major = parts[0]
    else:
        major = 0

    if (count > 1):
        minor = parts[1]
    else:
        minor = 0
    
    if (count > 2):
        patch = parts[2]
    else:
        patch = 0
    
    version = str(major) + '.' + str(minor) + '.' + str(patch)

    # back to ansible
    d = {
        'path'     : path,
        'realpath' : os.path.realpath(path),
        'version'  : version,
        'found'    : found,
        'shortver'   : str(major) + '.' + str(minor),
        'major'    : str(major),
        'minor'    : str(minor),
        'patch'    : str(patch),
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
