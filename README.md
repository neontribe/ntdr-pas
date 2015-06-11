## Process

1. <del>Get version for latest, testing, and local versions</del>
1. <del>Get changelog version (local and remote)</del>
1. Fix permissions
1. Sync files from one to another
1. Full sync from one to another
1. Full files deploy
1. Check DB connection
1. Create DB conection
1. Dump sql
1. Upload sql
1. Sync DB from one to another 



## Examples

### ntdr_ls.py

    ansible all -i "localhost," -c local --module-path modules -m ntdr_ls.py
    ansible -i inventory/cottage-servers br --module-path modules -m ntdr_ls.py
    ansible -i inventory/cottage-servers br --module-path modules -m ntdr_ls.py -a "/var/www/latest"
    ansible -i inventory/cottage-servers br --module-path modules -m ntdr_ls.py -a "/var/www/testing"

### ntdr_get_version.py
    
    ansible all -i "localhost," -c local --module-path modules -m ntdr_get_version.py -a /home/tobias/workspace/Cottaging/sites/br/
    ansible -i inventory/cottage-servers br --module-path modules -m ntdr_get_version.py
    ansible -i inventory/cottage-servers br --module-path modules -m ntdr_get_version.py -a "/var/www/latest /var/www/testing"

### Fix permissions

http://docs.ansible.com/file_module.html
