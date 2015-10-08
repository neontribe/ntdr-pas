#! /usr/bin/env python

# Find changelog vesion

import sys, os, json, shlex, re

import logging
logging.basicConfig(filename='/tmp/debug.log',level=logging.DEBUG)

def main():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True),
            version = dict(default=False, type='bool'),
            exists = dict(default=False, type='bool'),
        ),
        supports_check_mode = True
    )

    path = module.params.get('path')
    path = os.path.expanduser(path)
    exists = module.params.get('exists')
    version = module.params.get('version')

    logging.debug('Path: ' + path)
    logging.debug('Exists: ' + str(exists))
    logging.debug('Version: ' + str(version))

    if not version:
        full = os.path.join(path, 'changelog.txt')
        if os.path.isfile(full):
            with open(full, 'r') as f:
                first_line = f.readline()
            parts = first_line.split();
            if len(parts) == 0:
                version = os.path.basename(path)
                found = False
            else:
                version = parts[1]
                found = True
        else:
            version = os.path.basename(path)
            found = False

    parts = re.split('\.|_', version)
    count = len(parts)

    if (count > 0):
        brand = parts[0]
    else:
        raise

    if (count > 1):
        major = parts[1]
    else:
        major = 0

    if (count > 2):
        minor = parts[2]
    else:
        minor = 0
    
    if (count > 3):
        patch = parts[3]
    else:
        patch = 0
    
    major = str(major)
    minor = str(minor)
    patch = str(patch)

    if not major.isdigit():
        major = 0
    if not minor.isdigit():
        minor = 0
    if not patch.isdigit():
        patch = 0
    
    if exists:
        patch = int(patch) + 1
    
    version = brand + '_' + str(major) + '_' + str(minor) + '_' + str(patch)

    # back to ansible
    d = {
        'path'     : path,
        'realpath' : os.path.realpath(path),
        'version'  : version,
        'found'    : found,
        'shortver' : brand + '_' + str(major) + '_' + str(minor),
        'brand'    : brand,
        'major'    : str(major),
        'minor'    : str(minor),
        'patch'    : str(patch),
        'parts'    : parts,
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
