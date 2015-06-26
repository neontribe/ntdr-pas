## Playbooks

## Install

    mkdir ~/.drush

## Quick Examples

Create a whole new site on a remote site

    ansible-playbook push-local-to-remote.yml -i inventory/cottage-servers-zz --limit zz_live --extra-vars="target=/var/www/zz_0.0 source=/home/tobias/workspace/Cottaging/sites/zz/ with_db=true"

Freshen a remote site with local files, no DB push/update

    ansible-playbook push-local-to-remote.yml -i inventory/cottage-servers-zz --limit zz_live --extra-vars="target=/var/www/zz_0.0 source=/home/tobias/workspace/Cottaging/sites/zz/"

Pull a remote site to local, including new DB

    ansible-playbook pull-full-copy.yml -i inventory/cottage-servers-zz --limit zz_live --extra-vars="target=/var/www/zz_0.0"

Pull a remote site to local, No DB

    ansible-playbook pull-full-copy.yml -i inventory/cottage-servers-zz --limit zz_live --extra-vars="target=/var/www/zz_0.0 with_db=true"

Freshen local, files folder and DB

    ansible-playbook freshen-local.yml -i inventory/cottage-servers-zz --limit zz_live --extra-vars="target=/var/www/zz_0.0 with_db=true"

Freshen local, files folder, No DB

    ansible-playbook freshen-local.yml -i inventory/cottage-servers-zz --limit zz_live --extra-vars="target=/var/www/zz_0.0"

Create a new RC site, minor version bump

    ansible-playbook new-rc.yml -i inventory/cottage-servers-zz --limit zz_live --extra-vars="target=/var/www/zz_0.1

Freshen remote (from live)

Send live
