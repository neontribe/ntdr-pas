#! /usr/bin/env python

# Find changelog vesion

import sys, os, json, shlex, glob, subprocess


def get_sudo_info():
    get_info = ['env']
    process_return= subprocess.check_output(get_info, universal_newlines=True)
    sudo_enviroment = {}
    process_return = process_return.split('\n')
    temp_list = []
    for element in process_return:    
        element = element.split('=')
        if len(element) >=2:
	    sudo_enviroment[element[0]] = element[1]
    return sudo_enviroment



def recursive_file_permissions(path,uid=-1,gid=-1):
    '''
     Recursively updates file permissions on a given path.
     UID and GID default to -1, and mode is required
    '''
    for item in glob.glob(path+'/*'):
        if os.path.isdir(item):
	    os.chmod(os.path.join(path,item),0775)
            recursive_file_permissions(os.path.join(path,item),uid,gid)
            os.chown(path,uid, gid)
        else:
            try:
                os.chmod(os.path.join(path,item),0664)
		os.chown(path,uid,gid)
            except:
                print 'error'
    	
    files = []
    start_dir = path
    pattern   = "/sites/*/files"
    for dir,_,_ in os.walk(start_dir):
        files.extend(glob.glob(os.path.join(dir,pattern)))

    for element in files:
    	os.chown(element,'www-data','www-data')

    
    files = []
    start_dir = path
    pattern   = "/sites/default"
    for dir,_,_ in os.walk(start_dir):
        files.extend(glob.glob(os.path.join(dir,pattern)))
    
    for element in files:
        os.chmod(element,0755)
    

    
    files = []
    start_dir = path
    pattern   = "/sites/default/*.php"
    for dir,_,_ in os.walk(start_dir):
        files.extend(glob.glob(os.path.join(dir,pattern)))
    
    for element in files:
        os.chmod(element,0644)
    
    return files

def main():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True),
            version = dict(default='no', type='bool'),
        ),
        supports_check_mode = True
    )
    sudo_info = get_sudo_info()
    path = module.params.get('path')
    path = os.path.expanduser(path)

    if not os.path.isfile(path+'/sites/default/settings.php'):
	failure_message = 'failure but: '+path+'/sites/default/settings.php' 
        module.fail_json(msg=failure_message)
    else:
	recursive_file_permissions(path,int(sudo_info['SUDO_UID']),int(sudo_info['SUDO_GID']))
	
    d = {
        'status':'done'
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
