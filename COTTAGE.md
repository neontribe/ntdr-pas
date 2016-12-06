This assumes that the group vars for this host are populated:

    brandcode: wl
    drupal_su_pass: <PASSWORD>
    mysql_root_pw: <PASSWORD>
    ansible_become_pass: <PASSWORD>
    domain_name: wightlocations.co.uk
    var_www: /var/www

The you should be able to run these two:

    ansible-playbook --ask-pass -u root -i inventory/cottage-servers --limit=wl_new --extra-vars="sysuser=neonwl ssh_pub_key=/home/tobias/Desktop/wl_ssh/id_rsa.pub ssh_priv_key=/home/tobias/Desktop/wl_ssh/id_rsa" cottage-preflight.yml
    ansible-playbook -i inventory/cottage-servers --limit=wl_new --extra-vars="local=/home/tobias/workspace/cottaging/sites/wl domain_name=wightlocations.co.uk hostnames=new apache_root=/etc/apache2" provision-cottage.yml

And to run the certbot later:

    ansible-playbook -i inventory/cottage-servers --limit=wl_new --extra-vars="local=/home/tobias/workspace/cottaging/sites/wl domain_name=wightlocations.co.uk hostnames=new apache_root=/etc/apache2" provision-cottage.yml --tags=certbot

