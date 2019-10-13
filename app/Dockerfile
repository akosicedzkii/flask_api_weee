FROM ubuntu:latest
MAINTAINER fnndsc "martinezcederic@gmail.com"

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev python-mysqldb libmysqlclient-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

#COPY . /app 
ADD . /app
WORKDIR /app

#RUN pip3 install virtualenv

#RUN virtualenv env
#RUN ls -l

#RUN /bin/bash -c "source env/bin/activate"

RUN pip3 install -r requirements.txt
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
#RUN FLASK_APP=run.py FLASK_DEBUG=1 flask run
#RUN ls -l
CMD ["bash","flask_start.sh"]
#CMD []