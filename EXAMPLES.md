    ansible-playbook pull.yml -i inventory/cottage-servers --ask-vault-pass --limit=fb_live \
        --extra-vars="local=/var/www/testing/fb/FB-241"
