## Playbooks

## Install

    mkdir ~/.drush

## Cleaning up ZZ

If you have been testing against the ZZ site(s) and you want to reset them:

    mysql-dropuser-and-db -u zz_0.0.2 -m b191wkm && sudo rm -rf /var/www/*

Where the DB name is set correctly.

## Quick Examples

Create a whole new site on a remote site

    ansible-playbook push-local-to-remote.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="target=/var/www/zz_0.0 source=/home/tobias/workspace/Cottaging/sites/zz/ withdb=true"

Freshen a remote site with local files, no DB push/update

    ansible-playbook push-local-to-remote.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="target=/var/www/zz_0.0 source=/home/tobias/workspace/Cottaging/sites/zz/"

Pull a remote site to local, including new DB

    ansible-playbook pull-full-copy.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="source=/var/www/zz_0.0 withdb=true"

Pull a remote site to local, No DB

    ansible-playbook pull-full-copy.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="target=/var/www/zz_0.0"

Freshen local, files folder and DB

    ansible-playbook freshen-local.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="source=/var/www/zz_0.0 withdb=true"

Freshen local, files folder, No DB

    ansible-playbook freshen-local.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="source=/var/www/zz_0.0"

Create a new RC site, minor version bump

    ansible-playbook provision-new-release.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="target=/var/www/zz_0_1 source=/var/www/zz_0_0"

Freshen remote (from live)

    ansible-playbook freshen-remote.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="target=/var/www/zz_0_1 source=/var/www/zz_0_0"

Send live

    ansible-playbook swap-rc-to-live.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="latest=/var/www/zz_0_2 testing=/var/www/foo"
