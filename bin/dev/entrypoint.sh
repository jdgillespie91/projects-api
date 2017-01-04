#!/bin/bash

pip install -e .
gunicorn projects.app:app --bind 0.0.0.0:8000
