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

    $mkdir setting && cp __init__.py settings/__init__.py && cp settings.py settings/basic.py && cp settings.py settings/local.py &&cp settings.py settings/production.py && rm settings.py
    $cd settings/ && ls
    basic.py  __init__.py  local.py  production.py
```
2. setup config
```
    setup basic.py, local.py , production.py and __init__.py
    and mkdir static-storage at same dir of managy.py then run
    
```


