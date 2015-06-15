## Playbooks

1. Create new RC site from live site. Minor version bump
    1. Sync Live to RC
    1. Sync DB into RC
    1. Run up and updb
    1. Set testing symlink to point at RC
    1. Set robots.txt to no follow
    1. Fix remote permissions
1. Push staging site to RC
    1. Fix rc permissions
    1. Fix staging permissions
    1. Sync down sites/default/files
    1. Sync up full file system
    1. Run up and dbup
    1. Set robots.txt to no follow
    1. Create change log and patch bump
    1. Run tests on RC
1. Freshen staging
    1. Fix permissions on latest
    1. Fix Permissions on staging
    1. Sync down latest sites/default/files
    1. Sync down database
1. Pull a copy of remote (Latest, RC or Staging)
    1. Fix permissions on latest
    1. If local exists fix permissions on local
    1. Full fs sync from latest to Local
    1. Sync DB latest to local
1. Send RC live
    1. Put latest into read only
    1. Remote file sync from latest to RC
    1. Remote DB sync from latest to RC
    1. Run up and updb on RC
    1. Set robots.txt to crawl on RC
    1. Set robots.txt to no follow on latest
    1. Rewrite latest symlink to point at RC
    1. Send (new) latest live
    1. Remove testing symlink
    1. Fix latest permission
    1. Create new RC site from live site. Minor version bump

## Install

    mkdir ~/.drush

## Examples

### ntdr_ls.py
    ansible all -i "localhost," -c local -m ntdr_ls.py
    ansible -i inventory/cottage-servers br -m ntdr_ls.py
    ansible -i inventory/cottage-servers br -m ntdr_ls.py -a "/var/www/latest"
    ansible -i inventory/cottage-servers br -m ntdr_ls.py -a "/var/www/testing"

### ntdr_get_version.py
    ansible all -i "localhost," -c local -m ntdr_get_version.py -a /home/tobias/workspace/Cottaging/sites/br/
    ansible -i inventory/cottage-servers br -m ntdr_get_version.py
    ansible -i inventory/cottage-servers br -m ntdr_get_version.py -a "/var/www/latest /var/www/testing"

### Fix permissions
    ansible -i inventory/cottage-servers br -m shell -a "sudo ntdrchown /var/www/br_0.1.18"

### Sync files from one dir to another
    ansible -i inventory/cottage-servers br -m shell -a "rsync -a /var/www/br_0.1.16 /home/neonbr"

### Sync files to/from remote host to ntdr-pas server
    ansible all -i "localhost," -c local -m shell -a "rsync -a neon{{ brand code }}@host:/local/path /remote/path"
    ansible all -i "localhost," -c local -m shell -a "rsync -a neon{{ brand code }}@host:/local/path /remote/path"

### Create drushrc.alias on remote
    ansible -i inventory/cottage-servers br -m ntdr_create_drushrc_alias.py -a "/var/www/latest"

### Fetch alias
    ansible all -i "localhost," -c local -m shell -a "rsync -a neon{{ brand code }}@host:/var/www/br_0.1.16/sites/all/drush/ALIAS.alias.drushrc.php ~/.drush"

### Check DB connection
    ansible -i inventory/cottage-servers br -m shell -a "drush -r /var/www/latest sqlq 'show tables'>/dev/null"
    ansible -i inventory/cottage-servers br_live -m shell -a "drush -r /var/www/latest sqlq 'show tables'>/dev/null"

### Create DB conection
    ansible -i inventory/cottage-servers br -m shell -a "mysql-create-user-and-db -u XXX -p XXX -m XXX"

### Dump sql
    ssh neon{{ brand code }}@host drush -r /var/www/latest sql-dump --ordered-dump --structure-tables-key=common --result-file={{ brand code }}-latest.sql

### Upload sql
    drush @ALIAS sqlc < /path/to/sql

### Sync DB from one to another on remote host
    ssh neon{{ brand code }}@host drush -r /var/www/latest sql-sync /path/to/src @self
    ssh neon{{ brand code }}@host drush -r /var/www/latest sql-sync @self /path/to/src

### Sync DB from remote host to ntdr-pas server
    drush sql-sync @REMOTE @LOCAL

### Sync DB from ntdr-pas server to remote host
    drush sql-sync @LOCAL @REMOTE

### Check robots.txt
### Check .htaccess
