#!/bin/bash

PROJECT_ENV=dev

docker run \
    -d \
    -l $PROJECT_ENV \
    -p 8000:8000 \
    -v $PWD:/workspace \
    -w /workspace \
    --entrypoint /workspace/bin/entrypoint.sh \
    python:latest \
    $PROJECT_ENV  # Pass $PROJECT_ENV to entrypoint.
