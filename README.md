# Visiona - Tech-backend Project

This is built with Flask, Flask-RESTful, MongoDB, Redis and MySql

## Pre-requirements
- [Python 3.x LTS](https://www.python.org/downloads/)
- [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Docker](https://docs.docker.com/desktop/install/windows-install/)

## Recommended IDEAs
 - [VSCode with Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
 - [IntelliJ with Python Plugin](https://plugins.jetbrains.com/plugin/631-python)


### How to install WSL 2 and Docker

- step 1 (PowerShell Admin): 
```bash
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

- step 2 (PowerShell Admin):
```bash
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

- step 3
restart the computer

- step 4 (Download the Linux kernel update package):
https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

- step 5 (PowerShell Admin):
```bash
wsl --set-default-version 2
```

- step 6 (Install Docker):
https://docs.docker.com/docker-for-windows/install/

#### The IDE must load the Python packages from **venv**

## Environment Settings
### Step 1

- Into the local repository folder, run:

```bash
python3 -m venv venv
```

- After activate the Python venv

```bash
source venv/Scripts/activate
```

- Update **pip** package

```bash
python3 -m pip install -U pip
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
- The Flask app will be online in the port 5000
- The Redis Caching will be online in the port 6379 (details in docker-compose.yml file)
- The MSSQL Database will be online in the port 1433

## Running Flask back-end
1. Start Redis with Docker:
```bash
# In the project root folder
cd docker
docker-compose up --force-recreate -d ; docker-compose logs -f
```
To stop docker:
```bash
docker stop
```

2. Open the "flaskr" folder in console with following command:
```bash
cd ../flaskr
```

3. If you want to run in development mode, run these commands in folder flaskr:
```bash
export FLASK_ENV=development
export FLASK_APP=app.py
export FLASK_DEBUG=1
```

4. And finally execute:
```bash
flask run
```