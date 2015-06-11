## Process

1. Get version for latest, testing, and local versions
1. Get changelog version (local and remote)
1. Sync files from one to another
1. Full sync from one to another
1. Full files deploy
1. Check DB connection
1. Create DB conection
1. Dump sql
1. Upload sql
1. Sync DB from one to another 



### Examples for ntdr_ls.py
    ansible -i inventory/cottage-servers br --module-path modules -m ntdr_ls.py
    ansible -i inventory/cottage-servers br --module-path modules -m ntdr_ls.py -a "/var/www/latest"
    ansible -i inventory/cottage-servers br --module-path modules -m ntdr_ls.py -a "/var/www/testing"
