FROM ubuntu:24.04

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git gcc g++ make python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev gettext curl redis-server pkg-config

RUN curl -sL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install nodejs && \
    npm install -g sass postcss-cli postcss autoprefixer

RUN apt-get install -y libmysqlclient-dev

WORKDIR /
RUN git clone https://github.com/DMOJ/site.git --recursive --depth 1
WORKDIR /site
RUN pip3 install -r requirements.txt --break-system-packages && \
    pip3 install mysqlclient uwsgi redis --break-system-packages

COPY local_settings.py /site/dmoj/local_settings.py

RUN ./make_style.sh
RUN python3 manage.py collectstatic && \
    python3 manage.py compilemessages && \
    python3 manage.py compilejsi18n
