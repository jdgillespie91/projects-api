#!/bin/bash

PROJECT_ENV=ci

docker run \
    -d \
    -l $PROJECT_ENV \
    -p 8004:8000 \
    -v $PWD/bin:/workspace/bin \
    -v $PWD/projects:/workspace/projects \
    -v $PWD/setup.py:/workspace/setup.py \
    -v $PWD/setup.cfg:/workspace/setup.cfg \
    -w /workspace \
    --entrypoint /workspace/bin/entrypoint.sh \
    python:latest \
    $PROJECT_ENV  # Pass $PROJECT_ENV to entrypoint.
