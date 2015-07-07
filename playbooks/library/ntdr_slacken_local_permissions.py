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

    if not os.path.isfile(path+'/sites/default/settings.php'):
	failure_message = 'failure but: '+path+'/sites/default/settings.php' 
        module.fail_json(msg=failure_message)
    else:
        os.chmod(path, 0775)
        os.chmod(path,0664)
        #os.chown(path, uid, gid)
        d = {
            'status':"successful",
        }

        module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
