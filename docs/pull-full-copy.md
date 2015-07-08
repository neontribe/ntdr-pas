push-local-to-remote.yml
========================

## Summary

I pull a full copy of a remote site and set it up locally.  Default location is /var/tmp/cottage_VERSION

## Supported options

 1. source - The folder on the local machine holding the Drupal to sync up.
 1. local - The location on the remote machine that the Drupal withs/will live
 1. withdb - If set then the remote database will be replaced with the local database.
 1. mysql_root_pw - The mysql root password for the remote machine.

## Quick Examples

Pull a remote site to local, including new DB

    ansible-playbook pull-full-copy.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="source=/var/www/zz_0.0 withdb=true"

Pull a remote site to local, No DB

    ansible-playbook pull-full-copy.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="source=/var/www/zz_0.0 local=/home/tobias/foo"
