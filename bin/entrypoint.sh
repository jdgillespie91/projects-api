#!/bin/bash


set -e
set -x


function setup_dev {
    setup dev
    pip install -e .
}


function run_dev {
    gunicorn projects.app:app --bind 0.0.0.0:8000 --reload
}


function setup {
    aws s3 cp s3://settings-$1/settings.sh /tmp/settings.sh
    source /tmp/settings.sh
    rm /tmp/settings.sh
}


function run {
    gunicorn projects.app:app --bind 0.0.0.0:8000
}


function main {
    case "$1" in
        dev )
            # In development mode, we want to use the source code as the 
            # project source. This enables hot reloading of the application.
            setup_dev
            run_dev
            ;;
        local )
            setup $1
            run
            ;;
        ci )
            setup $1
            run
            ;;
        qa )
            setup $1
            run
            ;;
        staging )
            setup $1
            run
            ;;
        prod )
            setup $1
            run
            ;;
    esac
}


main $1
