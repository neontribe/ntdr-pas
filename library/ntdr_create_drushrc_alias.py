#! /usr/bin/env python

# Find changelog vesion
# Arguments are directories to search; default is /var/www/latest
# No recursion.

import sys, os, json, shlex, subprocess, errno, getpass, socket

def main():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(default='/var/www/latest', type='str'),
            name = dict(default='no', type='str'),
            shortver = dict(default='no', type='str'),
            user = dict(default='no', type='str'),
            host = dict(default='no', type='str'),
        ), 
        supports_check_mode = True
    )

    path = module.params.get('path')
    path = os.path.expanduser(path)
    name = module.params.get('name')
    shortver = module.params.get('shortver')
    user = module.params.get('user')
    host = module.params.get('host')

    drpath = path.rstrip("/")

    dirname = os.path.join(drpath, 'sites/all/drush')
    aliaspath = os.path.join(dirname, shortver + '.alias.drushrc.php')

    with open(aliaspath, 'w') as f:
        f.write("<?php\n")
        f.write("$aliases['" + name + "'] = array (\n")
        f.write("  'structure-tables' => \n")
        f.write("  array (\n")
        f.write("    'common' => \n")
        f.write("    array (\n")
        f.write("      0 => 'cach*',\n")
        f.write("      1 => 'history',\n")
        f.write("      2 => 'sessions',\n")
        f.write("      3 => 'watchdog',\n")
        f.write("    ),\n")
        f.write("  ),\n")
        f.write("  'root' => '" + path + "',\n")
        f.write("  'uri' => 'http://default',\n")
        f.write("  '#name' => '" + name + "',\n")
        if user != 'no':
            f.write("  'remote-user' => '" + user + "',\n")
        if host != 'no':
            f.write("  'remote-host' => '" + host + "',\n")
        f.write("  'databases' => \n")
        f.write("  array (\n")
        f.write("    'default' => \n")
        f.write("    array (\n")
        f.write("      'default' => \n")
        f.write("      array (\n")
        f.write("        'database' => '" + shortver + "',\n")
        f.write("        'username' => '" + shortver + "',\n")
        f.write("        'password' => '" + shortver + "',\n")
        f.write("        'host' => 'localhost',\n")
        f.write("        'port' => '',\n")
        f.write("        'driver' => 'mysql',\n")
        f.write("        'prefix' => '',\n")
        f.write("      ),\n")
        f.write("    ),\n")
        f.write("  ),\n")
        f.write(");\n")
    f.close()

    d = {
        'path':      path,
        'aliaspath': aliaspath,
        'name':      name,
        'shortver':     shortver,
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
