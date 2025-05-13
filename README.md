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

## Install and Set Up MySQL Database
### Start MySQL (if not running)
If MySQL is not running, you can start it with:

```sh
sudo mysqld --user=mysql &
```

### Create Database and User
Log in to your MySQL server and execute the following commands to create a new database and user:

```sql
CREATE DATABASE gfg_db;
CREATE USER 'gfg_user' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON gfg_db.* TO 'gfg_user';
```

## Apply Database Migrations
Run the following command to apply database migrations:

```sh
python manage.py migrate
```

## Update Project Dependencies
After installing a new package, update the `requirements.txt` file with:

```sh
pip freeze > requirements.txt
```
