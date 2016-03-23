## Playbooks

## Install

    mkdir ~/.drush

Ansible should ab at verion 1.8 or higher, 14.04 ships with 1.5.4:

    $ sudo apt-get install software-properties-common
    $ echo deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main | sudo tee --append /etc/apt/sources.list.d/ansible-ubuntu-ansible-utopic.list
    $ echo deb-src http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main | sudo tee --append /etc/apt/sources.list.d/ansible-ubuntu-ansible-utopic.list
    $ sudo apt-get update
    $ sudo apt-get install ansible

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

    ansible-playbook pull.yml -i inventory/cottage-servers --ask-vault-pass --limit=br_live --extra-vars="local=/$HOME/workspace/br"

Sync just the files folder down

    ansible-playbook pull.yml -i inventory/cottage-servers --ask-vault-pass --limit=br_live --extra-vars="source=/var/www/latest local=/$HOME/workspace/br" --tags="filesync"

Sync files and db down
    ansible-playbook pull.yml -i inventory/cottage-servers --ask-vault-pass --limit=br_live --extra-vars="source=/var/www/latest local=/$HOME/workspace/br" --tags="filesync,db"

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

    ansible-playbook push.yml -i inventory/ansible --ask-vault-pass --limit=ansible --extra-vars="local=/$HOME/workspace/Cottaging/sites/zz target=/var/www/zz"

Same thing but use a vault passwd file stored in your homespace

    ansible-playbook push.yml -i inventory/ansible --vault-password-file ~/.vault_pass.txt --limit=ansible --extra-vars="local=/$HOME/workspace/Cottaging/sites/zz target=/var/www/zz"

Push modules & themes, no DB

    ansible-playbook push.yml -i inventory/ansible --ask-vault-pass --limit=ansible --extra-vars="local=/$HOME/workspace/Cottaging/sites/zz target=/var/www/zz" --tags="modules"

Push just the DB

    ansible-playbook push.yml -i inventory/ansible --ask-vault-pass --limit=ansible --extra-vars="local=/$HOME/workspace/Cottaging/sites/zz target=/var/www/zz" --tags="db"

### Remote functions

#### Send Live

Copies files and db from /var/www/latest to /var/www/testing, runs updb, fixes permissions and installs a robots.txt from the theme. Then it symlinks the source of /var/www/testing to /var/www/latest. Then it creates a whole new drupal and copies the files. module and db from the new /var/www/latest into it and symlinks it as /var/www/testing.

    ansible-playbook sendlive.yml --vault-password-file ~/.vault_pass.txt -i inventory/kvm --limit=kvm

Default values:

    source: /var/www/latest
    target: /var/www/testing

