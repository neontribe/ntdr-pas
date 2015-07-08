#! /usr/bin/env python

# Get DB Details from an alias file

import sys, os, json, shlex, re

def get_value(text):
    pattern = "(?<=')(.*?)(?=')"
    matches = re.findall(pattern, text)
    value = matches[2]
    return value.strip("'").replace('.', '_')

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

    dbname = False
    dbpass = False
    dbuser = False

    if os.path.isfile(path):
        with open(path, 'rU') as f:
            for line in f:
                if "'database' => " in line:
                    dbname = get_value(line)
                if "'username' => " in line:
                    dbpass = get_value(line)
                if "'password' => " in line:
                    dbuser = get_value(line)

    # back to ansible
    d = {
        'path'    : path,
        'dbname'  : dbname,
        'dbpass'  : dbpass,
        'dbuser'  : dbuser,
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
