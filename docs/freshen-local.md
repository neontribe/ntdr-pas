push-local-to-remote.yml
========================

## Summary

Copies down files and optionaly databse from remote site to a local site.  If this is run against multiple sites the last site in the list will be the open that persist but it really should be limited to a single site.

## Supported options

 1. source - The folder on the local machine holding the Drupal to sync up.
 1. target - The location on the remote machine that the Drupal withs/will live
 1. withdb - If set then the remote database will be replaced with the local database.
 1. mysql_root_pw - The mysql root password for the remote machine.

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

