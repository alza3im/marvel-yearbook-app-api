FROM python:3.7.2

ADD . /flask-deploy

WORKDIR /flask-deploy

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app --log-level info