#! /usr/bin/env python

# Find changelog vesion

import sys, os, json, shlex, time, commands, re

def main():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True),
        ),
        supports_check_mode = True
    )

    path = module.params.get('path')
    path = os.path.expanduser(path)

    full = os.path.join(path, 'changelog.txt')
    lines = []
    version = False
    if os.path.isfile(full):
        with open(full, 'r') as f:
            contents = f.readlines()
            for line in contents:
                if not version:
                    parts = line.split();
                    if len(parts) >= 1:
                        version = parts[1]
                    else:
                        version = '0_0_0'
                lines.append(line)

    if not version:
        # Get it from the dir
        rp = os.path.realpath(path)
        version = os.path.basename(rp)

    if len(re.split('\.|_', version)) < 3:
        version = '0_0_0'

    parts = re.split('\.|_', version);
    major = parts[0]
    minor = parts[1]
    patch = parts[2]
    patch = int(patch) + 1
    newversion = major + '_' + minor + '_' + str(patch)
    
    if os.path.isfile(full):
        changelog = []
        changelog.append('+----- ' + newversion + ' -----+')
        changelog.append(time.strftime("%Y-%m-%d_%H-%M-%S"))

        branches = ''
        cmd = 'branches -p ' + path
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        while True:
            out = proc.stdout.read(1)
            if out == '' and proc.poll() != None:
                break
            if out != '':
                branches += out

        changelog.append(branches)
        changelog.append('')
        changelog += lines

        outfile = open(full, 'w')
        outfile.write("\n".join(changelog))
        outfile.close()

    # back to ansible
    d = {
        'path'      : path,
        'version'   : version,
        'newversion': newversion
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
