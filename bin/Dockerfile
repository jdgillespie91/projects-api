FROM python:3.6-alpine

WORKDIR /workspace

COPY dist/* .
RUN pip install *

ENTRYPOINT ["/entrypoint"]

