#! /usr/bin/env python

# Get DB Details from an alias file

import sys, os, json, shlex, re, datetime

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
            autofix = dict(default='no', type='bool'),
        ), 
        supports_check_mode = True
    )

    path = module.params.get('path')
    path = os.path.expanduser(path)
    autofix = module.params.get('autofix')

    dbname = False
    dbpass = False
    dbuser = False

    new_settings = []

    if os.path.isfile(path):
        with open(path, 'rU') as f:
            for line in f:
                if "'database' => " in line:
                    dbname = get_value(line)
                    new_settings.append("      'database' => '" + dbname + "',\n")
                elif "'username' => " in line:
                    dbpass = get_value(line)
                    new_settings.append("      'username' => '" + dbpass + "',\n")
                elif "'password' => " in line:
                    dbuser = get_value(line)
                    new_settings.append("      'password' => '" + dbuser + "',\n")
                else:
                    new_settings.append(line)

    if (autofix):
        os.rename(path, path + '.' + datetime.date.today().strftime("%Y%m%d-%H%S") + '~')
        settings = open(path, 'w')
        for line in new_settings:
            settings.write(line)
        settings.close()

    # back to ansible
    d = {
        'path'    : path,
        'dbname'  : dbname,
        'dbpass'  : dbpass,
        'dbuser'  : dbuser,
        'autofix' : autofix,
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
