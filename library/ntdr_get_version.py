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
    else:
        version = False

    # back to ansible
    d = {
        'path'     : path,
        'version'  : version,
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
