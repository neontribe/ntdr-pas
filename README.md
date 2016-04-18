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

    See the EXAMPLES.md in this folder.

### Push functions

Push a site to a remotye server

#### Extra vars

  * local - The location of the site on the remote fiule system; **default**: /var/www/latest
  * target - The location of the local site; **default**: /var/tmp/cottage + ansible_hostname
  * mysql_root_pw - The local mysql root passwd; **default**: Ansible will prompt for this
  * includefiles - If set to yes it will push sites/default/files
  * includedb -If set to yes it will push the local DB

#### Examples

    See the EXAMPLES.md in this folder.

### Remote functions

#### Send Live

Copies files and db from /var/www/latest to /var/www/testing, runs updb, fixes permissions and installs a robots.txt from the theme. Then it symlinks the source of /var/www/testing to /var/www/latest. Then it creates a whole new drupal and copies the files. module and db from the new /var/www/latest into it and symlinks it as /var/www/testing.

    ansible-playbook sendlive.yml --vault-password-file ~/.vault_pass.txt -i inventory/kvm --limit=kvm

Default values:

    source: /var/www/latest
    target: /var/www/testing

