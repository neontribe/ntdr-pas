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
            dbver = dict(default='no', type='str'),
        ), 
        supports_check_mode = True
    )

    drpath = path.rstrip("/")

    dirname = os.path.join(drpath, 'sites/all/drush')
    aliaspath = os.path.join(dirname, dbver + '.alias.drushrc.php')

    with open(aliaspath, 'w') as f:
        f.write("<?php")
        f.write("$aliases['" + name + "'] = array (")
        f.write("  'structure-tables' => ")
        f.write("  array (")
        f.write("    'common' => ")
        f.write("    array (")
        f.write("      0 => 'cach*',")
        f.write("      1 => 'history',")
        f.write("      2 => 'sessions',")
        f.write("      3 => 'watchdog',")
        f.write("    ),")
        f.write("  ),")
        f.write("  'root' => '" + path + "',")
        f.write("  'uri' => 'http://default',")
        f.write("  '#name' => '" + name + "',")
        f.write("  'databases' => ")
        f.write("  array (")
        f.write("    'default' => ")
        f.write("    array (")
        f.write("      'default' => ")
        f.write("      array (")
        f.write("        'database' => '" + dbver + "',")
        f.write("        'username' => '" + dbver + "',")
        f.write("        'password' => '" + dbver + "',")
        f.write("        'host' => 'localhost',")
        f.write("        'port' => '',")
        f.write("        'driver' => 'mysql',")
        f.write("        'prefix' => '',")
        f.write("      ),")
        f.write("    ),")
        f.write("  ),")
        f.write(");")
    f.close()

    d = {
        'path':      path,
        'aliaspath': aliaspath,
        'name':      name,
        'dbver':     dbver,
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
