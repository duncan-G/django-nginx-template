FROM python:3.6-alpine3.6

COPY ./src/requirements*.txt /srv/app/

RUN apk add --no-cache --update \
      bash \
      gcc \
      gettext \
      musl-dev \
      postgresql-client \
      postgresql-dev \
      curl-dev \

RUN pip install --no-cache-dir -r /srv/app/requirements.txt -r /srv/app/requirements-dev.txt

WORKDIR /srv/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
