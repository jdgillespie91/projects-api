projects
========

A RESTful API describing my personal projects.

Usage
-----

.. code-block:: bash

    $ curl projects.jakegillespie.me
    "Hello, world!"

Development
-----------

*Note that Docker is a prerequisite*

It's possible to run the app in multiple configurations.

.. code-block:: bash

    $ curl localhost:<port>
    "Hello, world!"
    
First is the *dev* environment which runs by default on port 8000.

.. code-block:: bash

    $ ./bin/run-dev.sh

Features include mounted source code and hot reloading, meaning any local changes will be immediately available in the containerised app.

Next is the *ci* environment which runs on port 8001.

.. code-block:: bash

    $ ./bin/run-ci.sh

Features include an isolated distribution build and installation, meaning the running app will have a corresponding wheel that can be used in more production-like environments if appropriate.

Additionally, we have the *qa*, *staging* and *production* environments. These run on ports 8002, 8003 and 8004 respectively.

.. code-block:: bash

    $ ./bin/run-qa.sh
    $ ./bin/run-staging.sh
    $ ./bin/run-prod.sh

Note that the features included here are identical to those in the *ci* environment. The intention is to, at a later date, configure these such that they have a better deployment process.
