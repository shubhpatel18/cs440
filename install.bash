### 1 | Install PostgreSQL ###################################################

# https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart
sudo apt install -y postgresql postgresql-contrib
sudo systemctl start postgresql.service

### 2 | Install pgAdmin4 #####################################################

# https://www.pgadmin.org/download/pgadmin-4-apt/
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
sudo apt install -y pgadmin4

### 2.1 | Configure pgAdmin4 web server ######################################

sudo /usr/pgadmin4/bin/setup-web.sh
