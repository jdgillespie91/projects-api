projects
========

A RESTful API describing my personal projects.

Usage
-----

.. code-block:: bash

    $ curl projects.jakegillespie.me
    "Hello, world!"

Running the app
---------------

*Note that Docker is a prerequisite*

Pull the latest image with

.. code-block:: bash

    $ docker pull jdgillespie91/jakegillespie.me/projects-0.1.0:latest

Start the container with

.. code-block:: bash

    $ ./bin/run-local.sh

The app will be exposed on port 8001.

.. code-block:: bash

    $ curl localhost:8001
    "Hello, world!"

To run with *ci*, *qa*, *staging* or *prod* configurations, use the following. Note that these apps will be exposed on port 8002, 8003, 8004 and 8005 respectively.

.. code-block:: bash

    $ ./bin/run-ci.sh
    $ ./bin/run-qa.sh
    $ ./bin/run-staging.sh
    $ ./bin/run-prod.sh

Development
-----------

*Note that Docker is a prerequisite*

Run the application in development mode with

.. code-block:: bash

    $ ./bin/run-dev.sh

The app will be exposed on port 8000. Features include mounted source code and hot reloading, meaning any local changes will be immediately available in the containerised app.
