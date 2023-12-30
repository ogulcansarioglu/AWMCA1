##
## Dockerfile to generate a Docker image from a GeoDjango project
##

# Start from an existing image with Miniconda installed
FROM continuumio/miniconda3

# Set the maintainer of the Docker image
MAINTAINER Ogulcan

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=CA1.settings

# Update the system packages and Conda
RUN apt-get -y update && apt-get -y upgrade
RUN conda update -n base conda && conda update -n base --all

# Create and set the working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#RUN apt-get update || (cat /var/log/apt/*.log && false)
#RUN apt-get -y install build-essential python-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info || (cat /var/log/apt/*.log && false)
COPY ENV.yml /usr/src/app
RUN conda env create -n ca1 --file ENV.yml

# Install packages not available in Conda using Pip
RUN conda run -n ca1 pip install django-pwa==1.1.0


RUN echo "conda activate ca1" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

RUN conda config --add channels conda-forge && conda config --set channel_priority strict
RUN cat ~/.condarc
RUN conda install uwsgi

COPY ./CA1/uwsgi.ini /usr/src/app/uwsgi.ini

COPY . /usr/src/app

RUN python manage.py collectstatic --no-input

EXPOSE 8001

CMD uwsgi --ini uwsgi.ini
