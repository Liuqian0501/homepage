# homepage
This is source for my personal website and all my project, This website is developed in django platform

This project is going to use docker, supersior, nginx, gunicorn, django and javascript. for database, I will use redis.
I will deploy the website on google compute engine.



# Step 1: Create a user on linux server
1. Log in to your server as the root user
`
adduser username
`

2. Use the usermod command to add the user to the sudo group.
`
usermod -aG sudo username
`
By default, on Ubuntu, members of the sudo group have sudo privileges.

3. setup remote login
in `/etc/ssh/sshd_config`:
    ```
    # Change to no to disable tunnelled clear text passwords
     PasswordAuthentication yes
    ```
4. Login in from remote
    ```
    ssh username@server_ip_address
    ```
    
5. install pip and virtualenv
    ```
    sudo apt-get update
    sudo apt-get install python-pip python-dev build-essential 
    sudo pip install --upgrade pip 
    sudo pip install --upgrade virtualenv 
    ```
6. make a virtualenv of python3.5
    ```
    virtualenv -p python3.5 personalwebsite_env
    source personalwebsite_env/bin/activate
    export PS1="$"
    python --version
    ```
7. clone this reporsitory from github
    ```
    git clone https://github.com/Liuqian0501/personalwebsite.git
    cd personalwebsite
    ```

# Step 2: Create a django project and set up config
1. create project
```
    pip install django
    pip freeze -> requirements.txt
    
    django-admin startproject personalwebsite
    $cd personalwebsite && ls
    manage.py  personalwebsite
    
    $cd personalwebsite/ && ls
    __init__.py  settings.py  urls.py  wsgi.py

    $mkdir setting && cp __init__.py settings/__init__.py && cp settings.py settings/base.py && cp settings.py settings/local.py &&cp settings.py settings/production.py && rm settings.py
    $cd settings/ && ls
    base.py  __init__.py  local.py  production.py
```
2. setup config
```
    setup basic.py, local.py , production.py and __init__.py
    and mkdir static-storage at same dir of managy.py then run
    $python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying sessions.0001_initial... OK
    $python manage.py collectstatic
    $python manage.py runserver 0:8008
    # the server have to open port 8008 in firewall rule
```


