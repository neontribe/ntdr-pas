## Playbooks

## Install

    mkdir ~/.drush

## Cleaning up ZZ

If you have been testing against the ZZ site(s) and you want to reset them:

    mysql-dropuser-and-db -u zz_0.0.2 -m b191wkm && sudo rm -rf /var/www/*

Where the DB name is set correctly.

## Quick Examples

### Pull functions

Pull a remote site to local.

#### Extra vars

  * source - The location of the site on the remote fiule system; **default**: /var/www/latest
  * local - The location of the local site; **default**: /var/tmp/cottage + ansible_hostname
  * devsite - If set to true robots.txt is set to no follow; **default**: true
  * mysql_root_pw - The local mysql root passwd; **default**: Ansible will prompt for this

#### Tags

  * fullsync - Full files sync, whole of drupal
  * db - Full files sync, whole of drupal
  * filesync - Sync the sites/default/files folder down

#### Examples

Pull a whole new copy to my home workspace

    ansible-playbook pull.yml -i inventory/cottage-servers-live --limit=br_live --extra-vars="local=/$HOME/workspace/br"

Sync just the files folder down

    ansible-playbook pull.yml -i inventory/cottage-servers-live --limit=br_live --extra-vars="source=/var/www/latest local=/$HOME/workspace/br" --tags="filesync"

Sync files and db down
    ansible-playbook pull.yml -i inventory/cottage-servers-live --limit=br_live --extra-vars="source=/var/www/latest local=/$HOME/workspace/br" --tags="filesync,db"

### Push functions

Push a site to a remotye server

#### Extra vars

  * local - The location of the site on the remote fiule system; **default**: /var/www/latest
  * target - The location of the local site; **default**: /var/tmp/cottage + ansible_hostname
  * mysql_root_pw - The local mysql root passwd; **default**: Ansible will prompt for this

#### Tags

  * modules - Sync sites/all foilders
  * files - Sync the sites/default/files folder
  * db - Sync up the DB

#### Examples

Full push/new provision

    ansible-playbook push.yml -i inventory/cottage-servers --ask-sudo-pass --limit=neoncottage --extra-vars="local=/$HOME/workspace/Cottaging/sites/br target=/var/www/sites/testing/br/BR-571"

Push modules & themes, no DB

    ansible-playbook push.yml -i inventory/cottage-servers --ask-sudo-pass --limit=neoncottage --extra-vars="local=/$HOME/workspace/Cottaging/sites/br target=/var/www/sites/testing/br/BR-571" --tags="modules"
    
Push just the DB

    ansible-playbook push.yml -i inventory/cottage-servers --ask-sudo-pass --limit=neoncottage --extra-vars="local=/$HOME/workspace/Cottaging/sites/br target=/var/www/sites/testing/br/BR-571" --tags="db"
