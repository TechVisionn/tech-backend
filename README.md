# Visiona - Tech-backend Project

This is built with Flask, Flask-RESTful, Flask-SQLAlchemy and Pandas

## Pre-requirements
- [Python 3.x LTS](https://www.python.org/downloads/)

## Recommended IDEAs
 - [VSCode with Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
 - [IntelliJ with Python Plugin](https://plugins.jetbrains.com/plugin/631-python)

#### The IDE must load the Python packages from **venv**

## Environment Settings
### Step 1

- Into the local repository folder, run:

```bash
python -m venv venv
```

- After activate the Python venv

```bash
source venv/Scripts/activate
```

- Update **pip** package

```bash
python -m pip install -U pip
```

### Step 2

- Installing the Python project's dependency packages

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Important Notes
- If new or updated dependency package was added in the project structure, the **requirements.txt** must be updated

```bash
pip freeze > requirements.txt
```

#### Notes
- You will need to declare the database connection information in the config_app.py and mongo_serve in folder db file before running the application.

- If you change models, you need to migrate to the bank, step by step will be in the next topics

- The Flask app will be online in the port 5000

## Running Flask back-end

  1. Open the "flaskr" folder in console with following command:
  ```bash
  cd flaskr
  ```

  2. If you want to run in development mode, run these commands in folder flaskr:
 ```bash
  export FLASK_ENV=development
  export FLASK_APP=app.py
  export FLASK_DEBUG=1
  ```
  3. And finally execute:
  ```bash
  flask run
  ```
## Executing Database Migrations using Flask-Migrate

### For you to control changes in the database follow the instructions below:
  
  1. Open the "flaskr" folder in console with following command:
  ```bash
  cd flaskr
  ```

  2. Create a migration repository. If the **migrations** folder already exists this command is not necessary.
  ```bash
    python -m flask db init
  ```
  3. To build a new migration, for example, "Initial migration"
  ```bash
    python -m flask db migrate -m "Initial migration."
  ```

  4. Then you can apply the migration to the database:
  ```bash
    python -m flask db upgrade
  ```

**Notes**: To see all the commands that are available run this command:
  ```bash
    python -m flask db --help
  ```

  Official documentation for [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)


