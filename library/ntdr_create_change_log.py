#! /usr/bin/env python

# Find changelog vesion

import sys, os, json, shlex, time, json, glob , subprocess, git, math


def touch(fname, times=None):
    fhandle = open(fname, 'a')
    try:
        os.utime(fname, times)
    finally:
        fhandle.close()


'''
full list of options for branches function:
{f:Boolean,p:Boolean,l:Boolean,b:Boolean,a:Boolean}

f  Fetch origin
p  Plain out put, supress colours. Use to create a changelog entry.
l  Show latest tag. If colours are enabled then tag that have different
   content to the current branch are coloured red.
b branch
      If specified and the remote branch exists then a the branch is checked out
      and pulled. Existing chang
      es will be stashed, and then applied.
a  Auto tag. If used in conjuction with -l then drupal-tag will be called with
   a patch level bump.
'''



class Prepender:

    def __init__(self, fname, mode='a'):
        self.__write_queue = []
        self.__f = open(fname, mode)

    def write(self, s):
        self.__write_queue.insert(0, s)

    def close(self):
        self.__exit__(None, None, None)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self.__write_queue: 
            self.__f.writelines(self.__write_queue)
        self.__f.close()


def branches(pathname,options):

    fetch_origin = False
    plain_output = False
    latest_tag = False
    new_branch = False
    autotag = False

    for key in options.keys():
        if key == 'f':
            fetch_origin = options[key]
        if key == 'p':
            plain_output = options[key]
        if key == 'l':
            latest_tag = options[key]
        if key == 'b':
            new_branch = options[key]
        if key == 'a':
            autotag = options[key]



    files = []
    start_dir = pathname#os.getcwd()
    pattern   = "*/.git"

    for dir,_,_ in os.walk(start_dir):      
        files.extend(glob.glob(os.path.join(dir,pattern)))
    

    returnObject =[]
    temp_files=[]
    for element in files:
        branch_list = []
        repo = git.Repo(element)
        assert not repo.bare


        if not str(element)[-20:-5] == 'tabs-api-client':

            if fetch_origin:
                fetch_command = ['git', '-C', element[:-5],'fetch','origin']
                run_process= subprocess.check_output(fetch_command, universal_newlines=True)

            branch_full_path = element[:-5]
            repo_name = branch_full_path.split('/')[-1]
            branches = [repo.active_branch]
            for branch in branches:
                branch_list.append(branch.name)
            

            if latest_tag !=False:

                for branch in branch_list:
                    #feature not currently implemented in the git module
                    latest_tag_command = ['git', '-C', branch_full_path,'describe','--abbrev=0','--tags']
                    lt = subprocess.check_output(latest_tag_command, universal_newlines=False).strip()
                    temp_files.append(lt)

                    #will be used if needed
                    '''
                    diff_command = ['git', '-C', element[:-5],'diff','refs/heads/'+branch+'..refs/tags/'+lt]
                    diff = subprocess.check_output(diff_command, universal_newlines=True)
                    temp_files.append(diff_command)
                    '''
                    
                    returnObject.append({'Name':repo_name,'Branch':branch,'Tag':lt,'Path':branch_full_path})
            


    return returnObject
    

def main():
    module = AnsibleModule(
    argument_spec = dict(
            path = dict(required=True),
            version = dict(required=True),
        ),
        supports_check_mode = True
    )
    path = module.params.get('path')
    version = module.params.get('version')

    touch(path+'/changelog.txt')
    touch(path+'/testlog2.txt')
   
     
    f = open(path+'/testlog2.txt','a+')
    f.write('+----- '+version+' -----+\n')
    f.write(time.strftime("%y-%m-%d_%H-%M\n"))
    titles = '\n%-25s %-20s %-10s %s\n' %('Name','Branch','Tag','Path')
    f.write(titles)
    
    branches_info=branches(path,{'l':True})
    for info in branches_info:
        infomation = '\n%-25s %-20s %-10s %s\n' %(info['Name'],info['Branch'],info['Tag'],info['Path'])
        f.write(infomation)

    f.write('\n')
    
    f1 = open(path+'/changelog.txt','r')
    lines = f1.readlines()
    f.writelines(lines)
    f1.close()
    f.close()
    os.remove(path+'/changelog.txt')
    os.rename(path+'/testlog2.txt',path+'/changelog.txt')
    d = {
        'path':path,
        'version': version,
        'number':path
    }

    module.exit_json(changed=False, stat=d)

# import module snippets
from ansible.module_utils.basic import *

main()
