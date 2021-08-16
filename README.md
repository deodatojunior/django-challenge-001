# News API

### Author

- Developer: Deodato Silva
- Email: deodatojunior999@gmail.com

#### Frameworks

- [Python 3.9.6](https://www.python.org/doc/)
- [Docker](https://docs.docker.com/)
- [Django 3.2.6](https://www.djangoproject.com)
- [Django Rest Framework 3.12.4](https://www.django-rest-framework.org)
- [PostgreSQL 12](https://www.postgresql.org)

## In Development Environment

### Python 3.9:

For Windows
- [Python 3.9.6](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe)

For Linux Ubuntu 20.04

First of all, install essential packages for compiling source code. Open a terminal and execute following commands:
```
sudo apt install build-essential checkinstall 
sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev 
```

Now, download the Python 3.9 source code from the official download site. Switch to a relevant directory and use wget to download the source file.
```
cd /opt 
sudo wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz 
```

Next, extract the downloaded archive file and prepare the source for the installation.
```
tar xzf Python-3.9.6.tgz 
cd Python-3.9.6 
sudo ./configure --enable-optimizations 
```

Python source is ready to install. Execute make altinstall command to install Python 3.9 on your system.
```
sudo make altinstall 
make altinstall is used to prevent replacing the default python binary file /usr/bin/python.
```
The Python 3.9 has been installed on Ubuntu 20.04 system. Verify the installed version:
```
python3.9 -V 

Python 3.9.6
```

## Docker

 [Link para download](https://www.docker.com/products/docker-desktop)

### Windows
 *The executable for windows already contains the two dependencies*.

Be sure to install the Linux kernel update for Windows.

https://docs.microsoft.com/pt-br/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package.

If you have any obstacles with the installation, just follow the [Manual](https://docs.docker.com/docker-for-windows/install/).


### Ubuntu 
First, update your existing package list:
```
sudo apt update
```
Then install some prerequisite packages that let apt use packages over HTTPS:
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common

```

Then add the GPG key to the official Docker repository on your system:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

```

Add the Docker repository to APT sources:
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

```


Then update the package database with the Docker packages from the newly added repository:
```
sudo apt update

```
Make sure you are about to install from the Docker repository instead of the default Ubuntu repository:

```
apt-cache policy docker-ce
```

Finally, install Docker:

```
sudo apt install docker-ce

```

Docker should now be installed, the daemon started and the process enabled to start at boot. Check if it is working:
```
sudo systemctl status docker
```

And now, install the Docker Compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

```

Then set the correct permissions for the docker-compose command to be executable:
```
sudo chmod +x /usr/local/bin/docker-compose

```

To verify that the installation was successful, run:
```
docker-compose --version
```
## Git
### Ubuntu
```
sudo apt-get install git-all
```
### Windows
[Git for Windows](https://git-scm.com/download/win)

Clone the remote repository into the desired folder
```
git clone https://github.com/deodatojunior/django-challenge-001
```

## Virtualenv
To create a virtual environment, after install Python 3.9, choose a directory where you want to place it and run the venv module as a script with the directory path:
```
py -m venv path/to/dir
```

Once your virtual environment is created, you must activate it.

In Windows, execute:
```
tutorial-env\Scripts\activate.bat
```

In Ubuntu or MacOS, execute:
```
source path/to/dir/Scripts/activate.bat
```

After activating virtualenv, go to the folder where you cloned the remote repository, run:
```
cd jungle_test
```

Install all requirements.txt dependencies into virtualenv:
```
pip install -r requirements.txt
```

Create an .env file with the .env.example development parameters and set the DATABASE_URL to your local PostgreSQL:
```
if is deployment:
SECRET_KEY='...an example...'
DEBUG=on
ALLOWED_HOSTS=*
DATABASE_URL=psql://postgres:postgres@localhost:5432/postgres

```
  

After creating the .env with the development parameters, run these commands to configure the migrations:

```
python manage.py makemigrations jungle_test
python manage.py migrate
```


Before running, create an admin user and enter the name, email and password.
```
python manage.py createsuperuser
```


So, run the API locally:
```
python manage.py runserver
```


## In Production Environment

## Docker

 [Link for download](https://www.docker.com/products/docker-desktop)

### Windows
 *The executable for windows already contains the two dependencies*.

Be sure to install the Linux kernel update for Windows.

https://docs.microsoft.com/pt-br/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package.

If you have any obstacles with the installation, just follow the [Manual](https://docs.docker.com/docker-for-windows/install/).


### Ubuntu 
First, update your existing package list:
```
sudo apt update
```
Then install some prerequisite packages that let apt use packages over HTTPS:
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common

```

Then add the GPG key to the official Docker repository on your system:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

```

Add the Docker repository to APT sources:
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

```


Then update the package database with the Docker packages from the newly added repository:
```
sudo apt update

```
Make sure you are about to install from the Docker repository instead of the default Ubuntu repository:

```
apt-cache policy docker-ce
```

Finally, install Docker:

```
sudo apt install docker-ce

```

Docker should now be installed, the daemon started and the process enabled to start at boot. Check if it is working:
```
sudo systemctl status docker
```

And now, install the Docker Compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

```

Then set the correct permissions for the docker-compose command to be executable:
```
sudo chmod +x /usr/local/bin/docker-compose

```

To verify that the installation was successful, run:
```
docker-compose --version
```

## Git
Now, install Git:

### Ubuntu
```
sudo apt-get install git-all
```
### Windows

[Git for Windows](https://git-scm.com/download/win)


Clone the remote repository into the desired folder
```
git clone https://github.com/deodatojunior/django-challenge-001
```

After clone the remote repository, go to the folder where you cloned the remote repository, run:
```
cd jungle_test
```

Create an .env file with the .env.example development parameters and set the DATABASE_URL to your local PostgreSQL:
```
if is production

SECRET_KEY='...an example...'
DEBUG=
ALLOWED_HOSTS=*
DATABASE_URL=psql://postgres:challenge@db:5432/challenge
```
  
After creating the .env with the required parameters for the production environment, run this command:
```
docker-compose up
```

The API and PostgreSQL will be built. After the database is built and displays these logs:
```
db_1   | PostgreSQL init process complete; ready for start up.
db_1   |
db_1   | 2021-08-16 20:28:50.037 UTC [1] LOG:  starting PostgreSQL 12.8 (Debian 12.8-1.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-b
it
db_1   | 2021-08-16 20:28:50.038 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db_1   | 2021-08-16 20:28:50.038 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db_1   | 2021-08-16 20:28:50.420 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1   | 2021-08-16 20:28:51.331 UTC [76] LOG:  database system was shut down at 2021-08-16 20:28:49 UTC
db_1   | 2021-08-16 20:28:51.501 UTC [1] LOG:  database system is ready to accept connections
```

...the API will complete the migrations and run the API with the following logs:
```
web_1  | Operations to perform:
web_1  |   Apply all migrations: admin, auth, authtoken, contenttypes, jungle_test, knox, sessions
web_1  | Running migrations:
web_1  |   Applying contenttypes.0001_initial... OK
web_1  |   Applying auth.0001_initial... OK
web_1  |   Applying admin.0001_initial... OK
web_1  |   Applying admin.0002_logentry_remove_auto_add... OK
web_1  |   Applying admin.0003_logentry_add_action_flag_choices... OK
web_1  |   Applying contenttypes.0002_remove_content_type_name... OK
web_1  |   Applying auth.0002_alter_permission_name_max_length... OK
web_1  |   Applying auth.0003_alter_user_email_max_length... OK
web_1  |   Applying auth.0004_alter_user_username_opts... OK
web_1  |   Applying auth.0005_alter_user_last_login_null... OK
web_1  |   Applying auth.0006_require_contenttypes_0002... OK
web_1  |   Applying auth.0007_alter_validators_add_error_messages... OK
web_1  |   Applying auth.0008_alter_user_username_max_length... OK

   Applying auth.0010_alter_group_name_max_length... OK
web_1  |   Applying auth.0011_update_proxy_permissions... OK
web_1  |   Applying auth.0012_alter_user_first_name_max_length... OK
web_1  |   Applying authtoken.0001_initial... OK
web_1  |   Applying authtoken.0002_auto_20160226_1747... OK
web_1  |   Applying authtoken.0003_tokenproxy... OK
web_1  |   Applying jungle_test.0001_initial... OK
web_1  |   Applying jungle_test.0002_rename_first_paragraph_article_firstparagraph... OK
web_1  |   Applying knox.0001_initial... OK
web_1  |   Applying knox.0002_auto_20150916_1425... OK
web_1  |   Applying knox.0003_auto_20150916_1526... OK
web_1  |   Applying knox.0004_authtoken_expires... OK
web_1  |   Applying knox.0005_authtoken_token_key... OK
web_1  |   Applying knox.0006_auto_20160818_0932... OK
web_1  |   Applying knox.0007_auto_20190111_0542... OK
web_1  |   Applying sessions.0001_initial... OK
web_1  | Performing system checks...
web_1  |
web_1  | System check identified no issues (0 silenced).
web_1  | August 16, 2021 - 16:30:01
web_1  | Django version 3.2.6, using settings 'jungle_test.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.
```

# API Links:
- ```http://localhost/api/admin/authors/``` ou ```http://127.0.0.1/api/admin/authors/``` GET, POST, HEAD ou OPTIONS - Authors
- ```http://localhost/api/admin/articles/``` ou ```http://127.0.0.1/api/admin/articles/``` GET, POST, HEAD ou OPTIONS - Articles
- ```http://localhost/api/login``` ou ```http://127.0.0.1/api/login```  POST, HEAD ou OPTIONS - Login
- ```http://localhost/api/sign-up``` ou ```http://127.0.0.1/api/sign-up```  POST, HEAD ou OPTIONS - Sign Up
- ```http://localhost/api/admin/authors/{id}/``` ou ```http://127.0.0.1/api/admin/authors/{id}/``` GET, PUT, PATCH, DELETE, HEAD ou OPTIONS - Authors
- ```http://localhost/api/admin/articles/{id}/``` ou ```http://127.0.0.1/api/admin/articles/{id}/``` GET, PUT, PATCH, DELETE, HEAD ou OPTIONS - Articles

# Specials requests
- ```http://localhost/api/articles/?category={category}/``` ou ```http://127.0.0.1/api/articles/?category={category}/``` GET, HEAD ou OPTIONS - Articles
- ```http://localhost/api/articles/{id}/``` ou ```http://127.0.0.1/api/articles/{id}/``` GET, HEAD ou OPTIONS - Articles


