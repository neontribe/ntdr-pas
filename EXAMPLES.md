## Push from cottage to rc

    ansible-playbook push-from-neoncottage-to-rc.yml -i inventory/cottage-servers --limit=ch --ask-vault-pass
    ansible-playbook push-from-neoncottage-to-rc.yml --limit=ch --ask-vault-pass

## Pull

    ansible-playbook pull.yml -i inventory/cottage-servers \
        --vault-password-file ~/.vault_pass.txt \
        --extra-vars="local=/var/www/testing/fb/FB-241"

