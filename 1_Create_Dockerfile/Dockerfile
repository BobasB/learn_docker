FROM python:3.7.4-stretch

ENV message="It work's!"
RUN pip install pipenv

COPY __main__.py /app/learn_docker

WORKDIR /app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --system --deploy --clear

ENTRYPOINT ["python", "learn_docker"]