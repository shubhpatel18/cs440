# {Application Name}

## About

This repository contains the CS 440 Tau Team Application Artifact.

## Database

This project uses PostgreSQL and pgAdmin4.

### Installation

```bash
./install.bash
```

You will be prompted for an email address and password for pgAdmin4, save these.

### Configuration

Access the postgres command line.

```bash
sudo -u postgres psql postgres
```

Change the password.

```postgres
alter user postgres with password '<YOUR_PASSWORD_HERE>';
```

Duplicate `database_secrets_template.toml` as `database_secrets.toml`, and fill in your password.

### Management (via pgAdmin4)

Navigate to `http://localhost/pgadmin4` in a browser. Login using the credentials you configured earlier.
