#!/bin/bash


set -e
set -x


function setup {
    pip install -e .
    pip install pytest
}


function run {
    gunicorn projects.app:app --bind 0.0.0.0:8000 --reload
}


function unittest {
    pytest tests
}


function main {
    case "$1" in
        dev )
            setup
            run
            ;;
        test )
            setup
            unittest
            ;;
    esac
}


main $1
