# Docker file for jpegoptim ChRIS plugin app
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build -t local/pl-jpegoptim .
#
# In the case of a proxy (located at 192.168.13.14:3128), do:
#
#    docker build --build-arg http_proxy=http://192.168.13.14:3128 --build-arg UID=$UID -t local/pl-jpegoptim .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pl-jpegoptim
#
# To pass an env var HOST_IP to container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/pl-jpegoptim
#

FROM python:3.9.1-slim-buster
LABEL maintainer="Benny Rochwerger <brochwer@redhat.com>"

WORKDIR /usr/local/src

RUN apt-get update -y && \
    apt-get install -y jpegoptim

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy flags.json explicitly, so if the file wasn't generated the build will fail
COPY flags.json . 

COPY . .
RUN pip install .

CMD ["jpegoptim", "--help"]
