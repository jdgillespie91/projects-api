#!/bin/bash


set -e
set -x


function dev {
    # In development mode, we want to use the source code as the project 
    # source. This enables hot reloading of the application.
    export PROJECT_ENV=dev
    pip install -e .
    gunicorn projects.app:app --bind 0.0.0.0:8000 --reload
}


function local {
    export PROJECT_ENV=local
    gunicorn projects.app:app --bind 0.0.0.0:8000
}


function ci {
    export PROJECT_ENV=ci
    gunicorn projects.app:app --bind 0.0.0.0:8000
}


function qa {
    export PROJECT_ENV=qa
    gunicorn projects.app:app --bind 0.0.0.0:8000
}


function staging {
    export PROJECT_ENV=staging
    gunicorn projects.app:app --bind 0.0.0.0:8000
}


function prod {
    export PROJECT_ENV=prod
    gunicorn projects.app:app --bind 0.0.0.0:8000
}


function main {
    case "$1" in
        dev ) dev ;;
        local ) local ;;
        ci ) ci ;;
        qa ) qa ;;
        staging ) staging ;;
        prod ) prod ;;
    esac
}


main $1
