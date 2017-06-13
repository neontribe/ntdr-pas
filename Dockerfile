FROM ubuntu:xenial
MAINTAINER oliver@neontribe.co.uk

ARG brandcode="zz"
ARG ssh_prv_key
ARG ssh_pub_key

ENV BRANDCODE=${brandcode}

WORKDIR /opt/

RUN apt update && apt -y install git ruby-compass php7.0 php7.0-curl php7.0-dev php7.0-gd php7.0-intl php7.0-json php7.0-mbstring php7.0-mcrypt php7.0-readline php7.0-sqlite3 php7.0-tidy php7.0-xml php-apcu php-imagick php-tidy php-xdebug php-xml libapache2-mod-php7.0 php7.0-mysql software-properties-common drush openssh-server

RUN add-apt-repository -y ppa:ansible/ansible
RUN apt-get update
RUN apt-get install -y ansible

RUN git clone https://github.com/neontribe/ntdr-pas

# Here we'll need to allow read-only access to the repo or use some other system for cloning without exposing our ssh privates.
RUN drush make --working-copy "ntdr-pas/files/${BRANDCODE}.make" "./build_${BRANDCODE}"

RUN cp  ntdr-pas/inventory/cottage-servers /etc/ansible/hosts

