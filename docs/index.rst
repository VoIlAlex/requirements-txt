Pip install to requirements.txt
=======================================

.. meta::
   :description lang=en: Add modules to requirements.txt installing packages with pip.

**to-requirements.txt** allows to automatically add and delete modules to requirements.txt installing
them using **pip**.

Easy to setup
    The installation process include only two steps: install the package using pip
    and setup up it using script provided by the package. That's it.

Customizable
    Customize it the way you like: use it only in git repositories, allow or disallow
    automated requirements.txt file creation, enable or disable the package itself.

Easy to use
    After installing the package, running setup command and (optionally) customizing it
    the package is ready. There is no additional conditions to use. Just install,
    uninstall or upgrade packages using *pip* as you usually do.

Always in sync
    With *to-requirements.txt* the project's requirements.txt will always stay in sync
    with packages that you install using *pip*.


Installation
____________

To install the package run the following command:

.. code-block::

    pip install to-requirements.txt

And after that run the command below to initialize the package:

.. code-block::

    requirements-txt setup

It will update your current *pip* scripts to execute the functionality of
this package.

    The changes made to *pip* scripts will not affect ordinary *pip* workflow after
    uninstalling *to-requirements.txt*.


Instructions
-----------

In this section you will get started with the package.

.. toctree::

    intro/configuration
