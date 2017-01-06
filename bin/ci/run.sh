#!/bin/bash

docker run -d -l ci -v $PWD:/workspace -w /workspace -p 8000 --entrypoint /workspace/bin/ci/entrypoint.sh python:latest
