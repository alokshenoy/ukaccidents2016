# Use postgresql-alpine 
FROM postgres:latest

# Env Variables (user/pass)
ENV POSTGRES_USER accidentdata
ENV POSTGRES_PASSWORD 2016
ENV POSTGRES_DB ukaccidents_2016

RUN apt-get update && apt-get install -y locales software-properties-common python3-pip && rm -rf /var/lib/apt/lists/* && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN pip3 install sqlalchemy pandas psycopg2

ADD ./data /data
WORKDIR /data

ADD move_data.sh /docker-entrypoint-initdb.d/move_data.sh
