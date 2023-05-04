# Roster Rookies

## About

This repository contains the CS 440 Tau Team Application Artifact.

## Database

This project uses `PostgreSQL` and `pgAdmin4`.

### Installation

This project requires python 3. To install this on Ubuntu run the following command:
```bash
apt install python3-pip
```

```bash
pip install -r requirements.txt
```

```bash
./postgres_install.bash
```

You will be prompted for an email address and password for `pgAdmin4`, save these.

### Database User Configuration

1. Access the `postgres` command line.

	```bash
	sudo -u postgres psql postgres
	```

2. Set a password for the postgres superuser. This is required to use `pgAdmin4`.

	```postgres
	ALTER USER postgres WITH PASSWORD '<POSTGRES_PASSWORD_HERE>';
	```

3. Create a new user for this project.

	```postgres
	CREATE USER tau WITH PASSWORD '<TAU_PASSWORD_HERE>';
	```

	You can now exit the `postgres` command line.

	Duplicate `database/resources/config_template.yaml` as `database/resources/config.yaml`,
	and fill in your password. Do not commit this file to the repo.

4. Enable password authentication for the new user.

	```bash
	sudo vim /etc/postgresql/*/main/pg_hba.conf
	```

	At the bottom of the file, below

	```conf
	# TYPE  DATABASE        USER            ADDRESS                 METHOD
	```

	add

	```conf
	# CS 440 Team Tau User
	local   all             tau                                     password
	```

5. Restart `postgressql`.

```bash
sudo systemctl restart postgresql.service
```

### Database Configuration

1. Establish an admin server connection.

	1. Navigate to `http://localhost/pgadmin4` in a browser. Login using the credentials
	you configured earlier.
	2. Right click on `servers` in the left pane. Click `Register > Server`.
	3. Under `General`, set the name to `postgres`.
	4. Under `Connection`, set `Hostname/address`:`localhost`, `Username`:`postgres`,
	`Password`:`<POSTGRES_PASSWORD_HERE>`.
	5. Click `Save`.

2. Set up the project database.

	1. Open the `Servers` dropdown menu and click on `postgres > Databases > postgres`.
	2. In the menu bar, click `Tools > Query Tool`.
	3. Copy `databases/sql/create_db.sql` into the `Query` box, and click the "play" icon.
	4. Right click `Databases` and select `Refresh`. The `tau` database should appear.
	5. Click the `tau` database. Once again, in the menu bar, click `Tools > Query Tool`.
	6. Copy `databases/sql/create_table_colleges.sql` into the `Query` box, and click the "play" icon.
	7. Copy `databases/sql/create_table_users.sql` into the `Query` box, and click the "play" icon.
	8. Copy `databases/sql/create_table_players.sql` into the `Query` box, and click the "play" icon.
	9. Copy `databases/sql/create_table_player_data.sql` into the `Query` box, and click the "play" icon.
	10. Copy `databases/sql/create_table_fantasy_teams.sql` into the `Query` box, and click the "play" icon.

3. Upload the `players` and `colleges` tables' data.

	1. Go to `https://collegefootballdata.com/key` and get an API key.
	2. Add your API key to your `database/resources/config.yaml`.
	3. Run `database/db_populator.py`.
	4. Check that the data is in your database, or if you got an errors.

## Server

### Database Credentials

Duplicate `server/resources/config_template.yaml` as `server/resources/config.yaml`,
and fill in your database password. Do not commit this file to the repo.

### Certificate

From the root directory of the project

```bash
openssl req -x509 -newkey rsa:2048 -addext "subjectAltName = DNS:localhost" -keyout server/resources/key.pem -out server/resources/cert.pem -days 365
cp server/resources/cert.pem client/resources/cert.pem
```

Follow the prompts and put in whatever inputs you want. Example inputs shown below.

**Note that the PEM key must be 4-1024 characters.**.
Add the PEM key(cert password) to `server/resources/config.yaml`

```plaintext
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:West Virginia
Locality Name (eg, city) []:Morgantown
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Roster Rookies 
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:tau
Email Address []:tau@tau.com
```

### Run Server

```bash
python3 server/server.py
```

## Client

The client has been developed with PyQt.

### Run Client

```bash
python3 client/main.py
```
