FROM python:3.9-alpine

WORKDIR ./user/new

COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk update && apk upgrade && apk add bash


ENTRYPOINT ["python",  "./runner.py"]