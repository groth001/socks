# Pull base image.
FROM python:3
ENV PYTHONUNBUFFERED 1

# Setup linkages to code repositories and add to image

WORKDIR /var/www/socks

#Python packages
RUN pip install Django
RUN pip install djangorestframework==3.12.2
RUN pip install markdown
RUN pip install django-filter==1.1
RUN pip install psycopg2-binary
RUN pip install requests
RUN pip install gunicorn==19.6.0
