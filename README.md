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
  * db - Sync the data base, it's advisable to pull files as well.
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

    ansible-playbook push.yml -i inventory/cottage-servers --ask-sudo-pass --limit=fb_test --extra-vars="local=/$HOME/workspace/Cottaging/fb target=/var/www/fb_1_7_0"

Push modules & themes, no DB

    ansible-playbook push.yml -i inventory/cottage-servers --ask-sudo-pass --limit=neoncottage --extra-vars="local=/$HOME/workspace/Cottaging/sites/br target=/var/www/sites/testing/br/BR-571" --tags="modules"
    
Push just the DB

    ansible-playbook push.yml -i inventory/cottage-servers --ask-sudo-pass --limit=neoncottage --extra-vars="local=/$HOME/workspace/Cottaging/sites/br target=/var/www/sites/testing/br/BR-571" --tags="db"

### Remote functions

#### Extra vars

  * local - The location of the site on the remote fiule system; **default**: /var/www/latest
  * target - The location of the local site; **default**: /var/tmp/cottage + ansible_hostname
  * mysql_root_pw - The local mysql root passwd; **default**: Ansible will prompt for this

#### Tags

  * fixperms - Correct permissions on the source path
  * freshen - Full freshen, module, themes, files and DB from source to target
  * freshendb - Copy DB from source to target
  * freshenmodules - Copy sites/all from source to target
  * freshenfiles - Copy sites/default/files from source to target
  * sendlive - DB & file sync + cheangelog update and symlink swap
  * setro - Put source site into ro
  * setrw - Put target site into rw

#### Examples

Release testing to latest, including a files and DB refresh and a minor version bump

    ansible-playbook remote.yml -i inventory/cottage-servers --ask-sudo-pass --limit=fb_test --tags=sendlive

Update files and DB in testing from latest.

    ansible-playbook remote.yml -i inventory/cottage-servers --ask-sudo-pass --limit=fb_test --tags='freshendb,freshenfiles'
