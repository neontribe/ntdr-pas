freshen-remote-site.yml
========================

## Summary

Copies the files from one remote deployment to another remote deployment, and overwrites the target database.

## Supported options

 1. source - The folder on the local machine holding the Drupal to sync up.
 1. target - The location on the remote machine that the Drupal withs/will live

## Quick Examples

Freshen remote (from live)

    ansible-playbook freshen-remote.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="target=/var/www/zz_0_1 source=/var/www/zz_0_0"
