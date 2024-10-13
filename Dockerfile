FROM python:3.11

EXPOSE 80

ADD ./app .

RUN python3 -m venv /opt/venv

RUN . .venv/bin/activate && pip install -r requirements.txt

ENTRYPOINT ["./.venv/bin/python","test.py"]
