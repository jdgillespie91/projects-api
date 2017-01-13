#!/bin/bash


set -e
set -x


function dev {
    # In dev mode, we're happy to use the source code as the project source.
    # Hence, we're happy to remain in the project directory.

    pip install -e .

    gunicorn projects.app:app --bind 0.0.0.0:8000 --reload
}


function ci {
    # In ci mode, we want to ensure we're using the packaged version of the
    # app. Hence, we prepare the distribution, install it, then cd to root to
    # ensure we're using the installed app rather than the source code.

    pip install --upgrade pip setuptools wheel
    python setup.py bdist_wheel
    pip install dist/*
    cd /

    gunicorn projects.app:app --bind 0.0.0.0:8000 --reload
}


function main {
    case "$1" in
        dev ) dev ;;
        ci ) ci ;;
    esac
}


main $1
