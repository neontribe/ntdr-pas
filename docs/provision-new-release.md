push-local-to-remote.yml
========================

## Summary

This clones a remote site, on a remote machine.  It duplicates the source site and increments the minor version number, creates a new DB and clones the source DB into it.

It should do the minor bump for you but currently it will take the version from the target dir name.

## Supported options

 1. source - The source site to use
 1. target - The new site to clone to.

## Quick Examples

    ansible-playbook provision-new-release.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="target=/var/www/zz_0_1 source=/var/www/zz_0_0"
