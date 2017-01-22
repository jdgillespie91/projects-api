projects
========

A RESTful API describing my personal projects.

Usage
-----

.. code-block:: bash

    $ curl projects.jakegillespie.me
    "Hello, world!"

Running the application
-----------------------

*Note that Docker is a prerequisite*

Pull the latest image with

.. code-block:: bash

    $ docker pull jdgillespie91/jakegillespie.me/projects-0.1.0:latest

Run the image with

.. code-block:: bash

    $ docker run -v ~/.aws:~/.aws -d jdgillespie91/jakegillespie.me/projects-0.1.0:latest local

This will expose the app on a random port (determine which with `docker ps`). Verify the app is running with

.. code-block:: bash

    $ curl localhost:<port>
    "Hello, world!"

It's possible to run the application with its *ci*, *qa*, *staging* or *prod* configurations using the following

.. code-block:: bash

    $ docker run -v ~/.aws:~/.aws -d projects-api:0.1.0-latest ci
    $ docker run -v ~/.aws:~/.aws -d projects-api:0.1.0-latest qa
    $ docker run -v ~/.aws:~/.aws -d projects-api:0.1.0-latest staging
    $ docker run -v ~/.aws:~/.aws -d projects-api:0.1.0-latest prod

Development
-----------

*Note that Docker is a prerequisite*

Clone the repository, then run the application in development mode with

.. code-block:: bash

    $ ./bin/run.sh

The app will be exposed on port 8000. Features include mounted source code and hot reloading, meaning any local changes will be immediately available in the containerised app.
