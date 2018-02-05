FROM ubuntu:latest

# Update python, Install virtualenv, nginx, supervisor
RUN apt-get update --fix-missing  \ 
	&& apt-get install -y build-essential git \
	&& apt-get install -y python python-dev python-tk python-setuptools \
	&& apt-get install -y build-essential libblas-dev liblapack-dev \
        && apt-get install -y python-pip python-virtualenv \
 	&& apt-get install -y nginx supervisor

RUN service supervisor stop \
	&& service nginx stop

# create virtual env and install dependencies
RUN virtualenv -p python3.5 /opt/venv  
ADD ./requirements.txt /opt/venv/requirements.txt
RUN /opt/venv/bin/pip install -r /opt/venv/requirements.txt

# expose port
EXPOSE 8080 9001

RUN pip install supervisor-stdout

# Add our config files Add our config files
ADD ./supervisor.conf /etc/supervisor.conf 
ADD ./nginx.conf /etc/nginx/nginx.conf

# Copy our service code
ADD ./personalwebsite /opt/web-app

# start supervisor to run our wsgi server, nginx, supervisor-stdout
CMD supervisord -c /etc/supervisor.conf -n
