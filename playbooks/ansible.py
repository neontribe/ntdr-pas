
import os
import subprocess
import re

def Playbook(folder_path=None,
             playbook=None,
             host_list=None,
             limit=None,
             extra_vars={}):
    
    os.chdir(folder_path)

   #ansible-playbook pull-full-copy.yml -i inventory/cottage-servers  --limit zz_test --extra-vars="source=/var/www/zz_0.0 local=/var/tmp mysql_root_pw=cuffhattieslipper"
   

    playbook_command = ['ansible-playbook', 'pull-full-copy.yml', '-i', 'inventory/cottage-servers','--limit','zz_test', '--extra-vars="source=/var/www/zz_0.0 local=/var/tmp mysql_root_pw=cuffhattieslipper"']
    playbook_command = ['printenv']
    
    playbook_command = ['cd /home/vagrant/ansible/ntdr-pas/playbooks; ansible-playbook pull-full-copy.yml -i inventory/cottage-servers  --limit zz_test --extra-vars="source=/var/www/zz_0.0 local=/var/tmp mysql_root_pw=cuffhattieslipper"']

    '''
    if (limit):
        basic_command=['--limit',limit]
        playbook_command.extend(basic_command)



    if bool(extra_vars):
        basic_command ='--extra-vars="'
        for key in extra_vars.keys():
            if extra_vars.keys().index(key) == 0:
                basic_command += key+'='+extra_vars[key]
            else:
                basic_command += ' '+key+'='+extra_vars[key]
        playbook_command.append(basic_command+'"')
    '''


    playbookResult  = subprocess.Popen(playbook_command,shell=True)
    return playbookResult


#print 
Playbook(folder_path='/home/vagrant/ansible/ntdr-pas/playbooks',
               playbook='pull-full-copy.yml',
               limit = 'zz_test',
               host_list='cottage-servers',
               extra_vars={'target':'/var/www/zz_0.0','withdb':'true'})

