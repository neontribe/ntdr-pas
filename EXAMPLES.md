## Push from cottage to rc

    ansible-playbook push-from-neoncottage-to-rc.yml -i inventory/cottage-servers --limit=ch --ask-vault-pass
    ansible-playbook push-from-neoncottage-to-rc.yml --limit=ch --ask-vault-pass

## Pull

    ansible-playbook pull.yml -i inventory/cottage-servers \
        --vault-password-file ~/.vault_pass.txt \
        --extra-vars="local=/var/www/testing/fb/FB-241"

## Provision from local

In this example I override a lot of features:

 * brandcode - The brandcode of the install, this has NO effect on the DB settings.
 * mysql_root_pw - The root password for the mysql on the target machine
 * local -
 * theme_folder - The path inside the drupal that holds the active theme, we need this for a compass compile and robots.txt
 * var_www - Where to install on the target machine
 * sql_file - The sql file to provision with
 * files_bundle - The tar gzip of the files folder.  The root of the tar should INCLUDE the file folder.

    ansible-playbook -i inventory/intranet \
        --limit=tobias provision-from-local.yml \
        --ask-become-pass \
        --extra-vars="brandcode=br mysql_root_pw=password theme_folder=sites/all/themes/ntbr_theme var_www=/tmp/ansible sql_file=/tmp/br.sql files_bundle=/tmp/br.tgz"

    ansible-playbook -i inventory/intranet --limit=tobias provision-from-remote.yml --ask-become-pass --extra-vars="brandcode=br mysql_root_pw=PASSWORD theme_folder=sites/all/themes/ntbr_theme source=/tmp/ansible/br_0_5" -v

## Releaseing

Bosh!

    ansible-playbook --limit=fb sendlive.yml

(Now remeber to tag changes and update the make file)

    ansible-playbook --limit=fb provision-from-remote.yml

