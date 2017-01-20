#!/bin/bash

set -e
set -x

PROJECT_ENV=dev

docker run \
    -d \
    -e PROJECT_ENV=$PROJECT_ENV \
    -l $PROJECT_ENV \
    -p 8000:8000 \
    -v $PWD:/workspace \
    -w /workspace \
    --entrypoint /workspace/bin/entrypoint.sh \
    --name $PROJECT_ENV \
    python:latest \
    $PROJECT_ENV  # Pass $PROJECT_ENV to entrypoint.
