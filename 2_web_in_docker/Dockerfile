ARG pass_value="Deafault"
FROM python:3.7.4-alpine
LABEL author="Bohdan"
LABEL version=1.0

ENV message=$pass_value
RUN pip install pipenv

WORKDIR /app/web_app

COPY __main__.py ./
COPY index.html ./templates/

COPY Pipfile ../
COPY Pipfile.lock ../

RUN pipenv install --system --deploy --clear

EXPOSE 5000

ENTRYPOINT ["python", "web_app"]