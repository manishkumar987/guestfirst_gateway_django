# Project Setup Guide

## Create a Virtual Environment
To create a virtual environment named `myenv`, run the following command:

```sh
python -m venv myenv
```

## Activate the Virtual Environment
First, navigate to the `myenv` directory:

```sh
cd myenv
```

Then, activate the virtual environment:

- **For Linux or macOS:**

  ```sh
  source bin/activate
  ```

- **For Windows:**

  ```sh
  .\Scripts\activate
  ```

## Clone the Project Repository
Clone the project's GitHub repository using:

```sh
git clone git@github.com:manishkumar987/guestfirst_gateway_django.git
```

## Install Project Dependencies
Navigate to the project directory and install the required dependencies:

```sh
python -m pip install -r requirements.txt
```

## install postgres 
### for linux wsl
To install PostgreSQL on a Debian-based Linux distribution running in WSL (Windows Subsystem for Linux), follow these steps:

### 1. Update your package lists

```bash
sudo apt update
```

### 2. Install PostgreSQL

```bash
sudo apt install postgresql postgresql-contrib
```

* `postgresql` is the core database package.
* `postgresql-contrib` includes useful extensions.

### 3. Start the PostgreSQL service

If you're using WSL, you may need to start PostgreSQL manually:

```bash
sudo service postgresql start
```

To enable it every time you start WSL, you can add this line to your `~/.bashrc` or `~/.profile`:

```bash
sudo service postgresql start
```

If you want to avoid entering a password each time, consider allowing passwordless sudo for that command (not recommended unless you understand the risks).

### 4. Switch to the postgres user and open the PostgreSQL prompt

```bash
sudo -i -u postgres
psql
```

### 5. (Optional) Set a password for the postgres role

```sql
\password postgres
```

### 6. Exit psql and the postgres user shell

```sql
\q
exit
```

 2. Create a PostgreSQL Database & User
Switch to the postgres user and access the PostgreSQL shell:

sudo -i -u postgres
psql
Then run:

sql
-- Create a database
CREATE DATABASE gfg_db;

-- Create a user
CREATE USER gfg_user WITH PASSWORD 'gfg_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE gfg_db TO gfg_user;



## Update Project Dependencies
After installing a new package, update the `requirements.txt` file with:

```sh
pip freeze > requirements.txt
```
