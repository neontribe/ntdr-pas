#! /usr/bin/env python

# Find changelog vesion

import sys, os, json, shlex, re, glob

import logging
logging.basicConfig(filename='/tmp/debug.log',level=logging.DEBUG)



def recursive_file_to_json(file_path_list, version, json):
    if len(file_path_list) >0:
        if file_path_list[0] in json:
             recursive_file_to_json(file_path_list[1:],version,json[file_path_list[0]])
        else:
            json[file_path_list[0]] = {}
            recursive_file_to_json(file_path_list[1:],version,json[file_path_list[0]])
    else:
        json['version'] = version

    return json
    
    





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

    #returns list of file paths to changelogs
    if not version:
        files = []
        start_dir = path
        pattern   = "*/changelog.txt"

        for dir,_,_ in os.walk(start_dir):      
            files.extend(glob.glob(os.path.join(dir,pattern)))

        testList = []
        temp_filetree = {path:{}}
        filetree={}
        filetree['flat'] = []
        tempList= []
        pattern = re.compile("[a/-zA/-Z][a/-zA/-Z]_[0-1000]_[0-1000]_[0-1000]|[a/-zA/-Z][a/-zA/-Z]_[0-1000]_[0-1000]|[a/-zA/-Z][a/-zA/-Z]_[0-1000]")
        
        for filepath in files:
            filepath = filepath.replace(path,'')
            filepathsplit = filepath.split(os.sep)


            if pattern.match(filepathsplit[-2]) or filepathsplit[-2] =='latest' or filepathsplit[-2]=='testing':
                flat_entry = {"name": filepath.replace('/changelog.txt','')}
                filetree['flat'].append(flat_entry)
                if filepathsplit[0] == "":
                    del filepathsplit[0]
                f = open(path+filepath, 'r')
                version =  f.readline()
                version = version.split()[1]
                filepath = filepath.replace(path,'')
                filepath = filepath.replace('/changelog.txt','')
                f.close()
                del filepathsplit[-1]
                tempList.append({'version':version,'filepath':filepathsplit})
                testList.append(filepathsplit)
      
        file_objects = tempList

        for element in file_objects:
            filetree['path'] = recursive_file_to_json(element['filepath'],element['version'],temp_filetree[path])
        



            

        
 

    # back to ansible
    d = {
        'files': filetree
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
