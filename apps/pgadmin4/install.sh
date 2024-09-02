#!/bin/bash

wget --no-check-certificate --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

RELEASE=$(lsb_release -cs)
# curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
apt-key add packages_pgadmin_org.pub
echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/${RELEASE}" pgadmin4 main | sudo tee /etc/apt/sources.list.d/pgadmin4.list

sudo apt update
sudo apt -y install pgadmin4
sudo apt -y install pgadmin4-web 
PGADMIN_SETUP_PASSWORD=password PGADMIN_SETUP_EMAIL=admin@admin.pg /usr/pgadmin4/bin/setup-web.sh --yes
