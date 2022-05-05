Configurations
==============

.. meta::
   :description lang=en: Configuring to-requirements.txt to deal with requirements.txt the way you like.

Configurations of *to-requirements.txt* allows you to customize the way the package
deal with requirements.txt the way you like.


There is two sets of configs: local and global. Local settings applies to your current folder.
Global settings are used as default as local settings are not specified.

View the config
_______________

The following command will output the local config or to-requirements.txt:

.. code-block::

     requirements-txt config


The following command will output the global config or to-requirements.txt:

.. code-block::

     requirements-txt config --global



Enable / Disable the package
____________________________

* Name: **disable**
* Values: **0, 1**
* Default: **0**

To disable the package use the following command:

.. code-block::

    requirements-txt config disable 1


To enable the package use the following command:

.. code-block::

    requirements-txt config disable 0


Only git repository
___________________

* Name: **only_git**
* Values: **0, 1**
* Default: **0**

**Enable only git repositories**

Enable saving to requirements.txt only in git repositories:

.. code-block::

    requirements-txt config only_git 1


Enable saving to requirements.txt only in git repositories globally:

.. code-block::

    requirements-txt config --global only_git 1

**Disable only git repositories**

Disable saving to requirements.txt only in git repositories:

.. code-block::

    requirements-txt config only_git 1


Disable saving to requirements.txt only in git repositories globally:

.. code-block::

    requirements-txt config --global only_git 1



Allow create requirements.txt
___________________

* Name: **allow_create**
* Values: **0, 1**
* Default: **0**

**Allow requirements.txt creation**

To allow the package to create requirements.txt if it does not exist:

.. code-block::

    requirements-txt config allow_create 1


To allow the package to create requirements.txt if it does not exist globally:

.. code-block::

    requirements-txt config --global allow_create 1

**Disallow requirements.txt creation**

To disallow the package to create requirements.txt if it does not exist:

.. code-block::

    requirements-txt config allow_create 0


To disallow the package to create requirements.txt if it does not exist globally:

.. code-block::

    requirements-txt config --global allow_create 0


Config files
____________

Local settings are stored in the current directory.

.. code-block::

    ./.to-requirements.txt/default.ini


Global settings are stored in the user folder. For Linux:

.. code-block::

    /home/<user>/.to-requirements.txt/default.ini
