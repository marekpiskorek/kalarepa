FROM python:3.7

RUN pip install pipenv

RUN groupadd -r kalarepa --gid=999 && \
    useradd -r -g kalarepa -d /kalarepa/ --uid=999 -s /sbin/nologin -c "Docker image user" kalarepa

COPY --chown=kalarepa:kalarepa . /kalarepa/

USER kalarepa

WORKDIR /kalarepa

RUN pipenv run pip install pip==18.0
RUN pipenv install --pre --dev
