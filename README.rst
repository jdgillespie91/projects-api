projects
========

An API that provides a description of my personal projects.

Usage
-----

.. code-block:: bash

    $ curl -L projects.jakegillespie.me
    "Hello, world!"

Development
-----------

*Note that Docker is a prerequisite*

Start the application in development mode with

.. code-block:: bash

    $ ./bin/start
    $ curl localhost:8000
    "Hello, world!"

Prepare a release with

.. code-block:: bash

    $ ./bin/build

Deploy the release with

.. code-block:: bash

    $ ./bin/deploy

