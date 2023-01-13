FROM python

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD ["uwsgi", "app.ini"]