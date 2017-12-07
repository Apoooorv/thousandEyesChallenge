FROM centos:centos7

RUN yum -y update &&\
    yum clean all &&\
    yum -y install epel-release &&\
    yum -y install python-pip python-django MySQL-python python-gunicorn &&\
    yum clean all &&\
    mkdir -p /home/src/

ADD reverseProxy /home/src/

RUN cd /home/src/ &&\
    pip install -r requirements.txt &&\
    touch proxy.logs &&\
    chmod 0777 /home/src/validate.sh 
    
EXPOSE 8080

ENTRYPOINT /home/src/validate.sh
#ENTRYPOINT bash /home/src/run.sh && gunicorn --bind 0.0.0.0:8080 --access-logfile=/home/src/proxy.logs --pythonpath /home/src/ reverseProxy.wsgi
