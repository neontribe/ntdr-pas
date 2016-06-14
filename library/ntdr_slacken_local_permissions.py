#! /usr/bin/env python

# Find changelog vesion

import sys
import os
import json
import shlex
import glob
import subprocess
from pwd import getpwnam


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
        item = item.split(os.sep)[-1]
        if os.path.isdir(item):
	    os.chmod(path+item,0775) #0775
            recursive_file_permissions(path + item,uid,gid)
            os.chown(path,uid, gid)
        else:
            try:
                os.chmod(path + item,0664) #0664 
		os.chown(path,uid,gid)
            except:
                print 'error'
           	
    files = []
    start_dir = path+'/sites/'
    pattern   = "*/files"
    for dir,_,_ in os.walk(start_dir):
        files.extend(glob.glob(os.path.join(dir,pattern)))

    for element in files:
    	os.chown(element, getpwnam('www-data').pw_uid, getpwnam('www-data').pw_gid)
    



    os.chmod(path+'/sites/default',0755) #0755

   

      
    files = []
    start_dir = path+'/sites/default/'
    pattern   = "*.php"

    for dir,_,_ in os.walk(start_dir):
        files.extend(glob.glob(os.path.join(dir,pattern)))
    
    for element in files:
        os.chmod(element,0644) #0644
    

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
    fh = open('printout','w')
    fh.write(path)
    fh.close()
    if not os.path.isfile(path+'/sites/default/settings.php'):
	failure_message = 'failure but: '+path+'/sites/default/settings.php' 
        module.fail_json(msg=failure_message)
    else:
	return_path = recursive_file_permissions(path,int(sudo_info['SUDO_UID']),int(sudo_info['SUDO_GID']))
	
    d = {
        'status':return_path
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
