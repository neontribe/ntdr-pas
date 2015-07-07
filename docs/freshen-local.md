freshen-local.yml
=================

## Summary

Copies down files and optionaly databse from remote site to a local site.  If this is run against multiple sites the last site in the list will be the open that persist but it really should be limited to a single site.

## Supported options

 1. source - The folder on the local machine holding the Drupal to sync up.
 1. target - The location on the remote machine that the Drupal withs/will live
 1. withdb - If set then the remote database will be replaced with the local database.

## Quick Examples

Freshen local, files folder and DB

    ansible-playbook freshen-local.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="source=/var/www/zz_0.0 target=/var/www/zz_0_0 withdb=true"

Freshen local, files folder, No DB

    ansible-playbook freshen-local.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="source=/var/www/zz_0.0 target=/var/www/zz_0_0"

