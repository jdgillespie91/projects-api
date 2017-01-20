#!/bin/bash


set -e
set -x


PROJECT_ENV=qa


docker run \
    -d \
    -e PROJECT_ENV=$PROJECT_ENV \
    -l $PROJECT_ENV \
    -p 8003:8000 \
    projects-api:0.1.0-latest \
    $PROJECT_ENV
