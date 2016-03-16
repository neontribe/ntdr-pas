Push theme and modules
======================

## To all hosts
    ansible-playbook --vault-password-file ~/.vault_pass.txt push.yml -i inventory/cottage-servers --tags=modules

## To Country hideaways testing and live
    ansible-playbook --vault-password-file ~/.vault_pass.txt push.yml -i inventory/cottage-servers --limit=ch --tags=modules
