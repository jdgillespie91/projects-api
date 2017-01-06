#!/bin/bash

docker run -d -v $PWD:/workspace -w /workspace -p 8000 --entrypoint /workspace/bin/dev/entrypoint.sh python:latest
