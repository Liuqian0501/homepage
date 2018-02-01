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


# Step 2: clone this reporsitory from github

