#!/bin/bash

docker run --rm -v $PWD:/workspace -w /workspace -p 8000 --entrypoint /workspace/bin/dev/entrypoint.sh python:latest
