ARG image
FROM python:${image}-alpine
LABEL author="Bohdan"
LABEL version=1.0

ENV message="It work's!"

RUN pip install pipenv

WORKDIR /app/web_app

COPY __main__.py ./
COPY index.html ./templates/
COPY Pipfile ../
COPY Pipfile.lock ../

RUN pipenv install --system --deploy --clear

EXPOSE 5000

WORKDIR /app

ENTRYPOINT ["python", "web_app"]