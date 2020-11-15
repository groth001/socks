# Pull base image.
FROM python:3
ENV PYTHONUNBUFFERED 1

# Setup linkages to code repositories and add to image

WORKDIR /var/www/socks

#Python packages
RUN pip3 install Django
RUN pip3 install djangorestframework==3.12.2
RUN pip3 install markdown
RUN pip3 install django-filter==1.1
RUN pip3 install psycopg2-binary
RUN pip3 install requests
RUN pip3 install gunicorn==19.6.0
RUN pip3 install pygments
RUN pip3 install django-guardian
