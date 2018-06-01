FROM python:3.6-alpine

WORKDIR /workspace

COPY dist/* .
RUN pip install *

ENTRYPOINT ["gunicorn", "projects.app:app", "--workers", "3", "--bind", "0.0.0.0:8000"]

