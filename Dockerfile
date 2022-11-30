FROM python:3.8

#Basic S.O Libs
RUN apt-get update && apt-get install -y
RUN apt-get install -y --no-install-recommends gettext libcairo2 libffi-dev libpango1.0-0 \
  libgdk-pixbuf2.0-0 libxml2-dev libxslt1-dev shared-mime-info

# Required envs
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=settings.settings \
    TZ=America/Sao_Paulo \
    OAUTHLIB_INSECURE_TRANSPORT=True \
    PYTHONPATH=sec\
    DEBUG=True

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /usr/src/app/project

CMD gunicorn    --bind 0.0.0.0:8007         \
                --reload wsgi:application

