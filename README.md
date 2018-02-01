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
    
5. and for fun
`export PS1=":-)"`

6. install pip and virtualenv
    ```
    sudo apt-get update
    sudo apt-get install python-pip python-dev build-essential 
    sudo pip install --upgrade pip 
    sudo pip install --upgrade virtualenv 
    ```
7. make a virtualenv of python3.5
    ```
    virtualenv -p python3.5 personalwebsite_env
    source personalwebsite_env/bin/activate
    python --version
    ```
8. clone this reporsitory from github
    ```
    git clone https://github.com/Liuqian0501/personalwebsite.git
    cd personalwebsite
    ```

# Step 2: Create a django project and set up config

```
pip install django
pip freeze -> requirements.txt

django-admin startproject personalwebsite

```



