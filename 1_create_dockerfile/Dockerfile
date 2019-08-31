ARG image
FROM python:${image}-alpine
LABEL author="Bohdan"
LABEL version=1.0

ENV message="It work's!"
RUN pip install pipenv

COPY __main__.py /app/learn_docker

WORKDIR /app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --system --deploy --clear

ENTRYPOINT ["python", "learn_docker"]