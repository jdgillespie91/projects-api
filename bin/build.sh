#!/bin/bash


set -e
set -x


docker build \
    -f bin/Dockerfile \
    -t projects-api:0.1.0-latest \
    --label projects-api \
    .
