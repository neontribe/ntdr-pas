swap-rc-to-live
===============

## Summary

Sends the current RC site live and creates a new RC site by clonig the new live site

## Supported options

 1. latest - The real dir name of the latest (curent live) site
 1. testing - The real dir name of the testing (curent rc) site
 1. newrc - The real dir name of the new (currently non-existent) rc site
 1. mysql_root_pw - The mysql root password for the remote machine.

## Quick Examples

Send live

    ansible-playbook swap-rc-to-live.yml \
      -i inventory/cottage-servers \
      --limit zz_test \
      --extra-vars="latest=/var/www/zz_0_0 testing=/var/www/zz_0_1 newrc=/var/www/zz_0_3"
