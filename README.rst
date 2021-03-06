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

Testing
~~~~~~~

Run the test suite with

.. code-block:: bash

    $ ./bin/test

Deployment
~~~~~~~~~~

Prepare a release with

.. code-block:: bash

    $ ./bin/build

Deploy this release locally for testing purposes with

.. code-block:: bash

    $ ./bin/deploy local $(git rev-parse --short HEAD)
    $ curl localhost:8001
    "Hello, world!"

In general, deploy with

.. code-block:: bash

    $ ./bin/deploy <environment> <version>

where environment is one of *local*, *staging* or *prod*.

