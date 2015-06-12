## Process

1. <del>Get version for latest, testing, and local versions</del>
1. <del>Get changelog version (local and remote)</del>
1. <del>Fix permissions</del>
1. Sync files from one dir to another
1. Sync files to/from remote host to ntdr-pas server
1. Check DB connection
1. Create DB conection
1. Dump sql
1. Upload sql
1. Sync DB from one to another on same host
1. Sync DB from remote host to ntdr-pas server
1. Sync DB from ntdr-pas server to remote host
1. Full mirror
1. Check robots.txt

## Install

    mkdir ~/.drush

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
    ansible -i inventory/cottage-servers br -m shell -a "sudo ntdrchown /var/www/br_0.1.18"

### Sync files from one dir to another
    ansible -i inventory/cottage-servers br --module-path modules -m shell -a "rsync -a /var/www/br_0.1.16 /home/neonbr"

### Sync files to/from remote host to ntdr-pas server
    rsync -a neon[brand code]@host /local/path
    rsync -a --exclude='.git' neon[brand code]@host /local/path

### Create drushrc.alias on remote
    ansible -i inventory/cottage-servers br --module-path modules -m ntdr_create_drushrc_alias.py -a "/var/www/latest"

### Fetch alias
    rsync -a neon[brand code]@host:/var/www/br_0.1.16/sites/all/drush/ALIAS.alias.drushrc.php ~/.drush

### Check DB connection
    ansible -i inventory/cottage-servers br -m shell -a "drush -r /var/www/latest sqlq 'show tables'>/dev/null"
    ansible -i inventory/cottage-servers br_live -m shell -a "drush -r /var/www/latest sqlq 'show tables'>/dev/null"

### Create DB conection
    ansible -i inventory/cottage-servers br -m shell -a "mysql-create-user-and-db -u XXX -p XXX -m XXX"

### Dump sql
    ssh neon[brand code]@host drush -r /var/www/latest sql-dump --ordered-dump --structure-tables-key=common > dumpfile.sql

### Upload sql
    drush @ALIAS sqlc < /path/to/sql

### Sync DB from one to another on remote host
    ssh neon[brand code]@host drush -r /var/www/latest sql-sync /path/to/src @self
    ssh neon[brand code]@host drush -r /var/www/latest sql-sync @self /path/to/src

### Sync DB from remote host to ntdr-pas server
    drush sql-sync @REMOTE @LOCAL

### Sync DB from ntdr-pas server to remote host
    drush sql-sync @LOCAL @REMOTE

### Check robots.txt
### Check .htaccess
