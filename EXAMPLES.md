## Push

    ansible-playbook push.yml -i inventory/cottage-servers \
        --vault-password-file ~/.vault_pass.txt \
        --limit=lb

## Pull

    ansible-playbook pull.yml -i inventory/cottage-servers \
        --vault-password-file ~/.vault_pass.txt \
        --extra-vars="local=/var/www/testing/fb/FB-241"
