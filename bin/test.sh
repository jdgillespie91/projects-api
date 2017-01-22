#!/bin/bash


set -e
set -x


PROJECT_ENV=test


docker run \
    -e PROJECT_ENV=$PROJECT_ENV \
    -l $PROJECT_ENV \
    -v $PWD:/workspace \
    -w /workspace \
    --entrypoint /workspace/bin/entrypoint.sh \
    --name $PROJECT_ENV \
    python:latest \
    $PROJECT_ENV
