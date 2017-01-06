#!/bin/bash

pip install --upgrade pip setuptools wheel
python setup.py bdist_wheel
pip install dist/*

gunicorn projects.app:app --bind 0.0.0.0:8000
