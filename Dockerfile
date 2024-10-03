FROM --platform=linux/amd64 python:3.12-bookworm
ADD . /app
WORKDIR /app
RUN pip install build setuptools
CMD tail -f /dev/null