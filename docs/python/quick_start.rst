Quick Start
===========

Installation
------------

Python 2.7+ is a prerequisite for using the ThreatConnect Python SDK. Typically, Python comes pre-installed on Linux/OS X/Unix systems, so additional steps to install Python are usually not required. To ensure you have python installed and to check the version, type ``python --version`` into the command line/command prompt.

The ThreatConnect Python SDK can be installed using `python pip <https://pip.pypa.io/en/stable/>`_ as shown below:

.. code-block:: shell

    pip install threatconnect

.. note:: If you get a ``Permission denied`` error, you may have to install the threatconnect package with escalated privileges: ``sudo pip install threatconnect``.

.. warning:: If you are using Python 2, you will also need to install the `enum34 <https://pypi.python.org/pypi/enum34/>`_ package using: ``pip install enum34``.

Configuration
-------------

Any script using the ThreatConnect Python SDK needs access to a configuration file which is laid out as follows:

.. code-block:: text

    [threatconnect]

    # note -- do not use any quotes...

    #
    # api access id - ENTER API ACCESS ID
    #
    api_access_id = 12345678900987654321

    #
    # api org - ENTER API DEFAULT ORG
    #
    api_default_org = Test Owner

    #
    # api secret key - ENTER API SECRET KEY
    #
    api_secret_key = aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz!@#$%^&*()-=

    #
    # api base url - ENTER API BASE URL (e.g. https://api.threatconnect.com)
    #
    api_base_url = https://api.threatconnect.com

Update the configuration file as follows:

1. Replace the ``api_access_id`` and ``api_secret_key`` with your credentials.
2. Update the ``api_default_org`` with your organization's name as it appears in ThreatConnect.
3. Change the ``api_base_url`` as needed (see the note below if you are using the ThreatConnect **sandbox**).

.. note:: If you are working with the ThreatConnect **sandbox**, the ``api_base_url`` should be: ``https://sandbox.threatconnect.com/api/``.

What hath God wrought! (a.k.a. Hello World)
-------------------------------------------

Assuming that you have installed the ThreatConnect Python SDK and have created a configuration file with the correct information, we are now ready to test the SDK. To test the SDK:

1. Create a folder in a convenient location on your computer.
2. Copy the configuration file from the previous, **Configuration** step into the new folder and name it ``tc.conf``.
3. Copy and paste the following code into a file and save it in the new folder with the name ``tc_test.py``. This code will print all of the owners in ThreatConnect which you have permission to see.

.. 
    no-test

.. code-block:: python

    try:
        import ConfigParser
    except:
        import configparser as ConfigParser
    import sys

    from threatconnect import ThreatConnect

    config = ConfigParser.RawConfigParser()
    config.read("./tc.conf")

    try:
        api_access_id = config.get('threatconnect', 'api_access_id')
        api_secret_key = config.get('threatconnect', 'api_secret_key')
        api_default_org = config.get('threatconnect', 'api_default_org')
        api_base_url = config.get('threatconnect', 'api_base_url')
    except ConfigParser.NoOptionError:
        print('Could not read configuration file.')
        sys.exit(1)

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Owners object
    owners = tc.owners()

    try:
        # retrieve the Owners
        owners.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Owners
    for owner in owners:
        print(owner.id)
        print(owner.name)
        print(owner.type)
        print("")

4. In the command line/command prompt, run ``python tc_test.py``. This should print the ID number, name, and type of the owners which you have permission to see.

Standard Script Heading
-----------------------

Every script that communicates to the ThreatConnect Python SDK should begin with the same, basic code:

.. 
    no-test

.. code-block:: python

    try:
        import ConfigParser
    except:
        import configparser as ConfigParser
    import sys

    from threatconnect import ThreatConnect

    config = ConfigParser.RawConfigParser()
    config.read("./tc.conf")

    try:
        api_access_id = config.get('threatconnect', 'api_access_id')
        api_secret_key = config.get('threatconnect', 'api_secret_key')
        api_default_org = config.get('threatconnect', 'api_default_org')
        api_base_url = config.get('threatconnect', 'api_base_url')
    except ConfigParser.NoOptionError:
        print('Could not read configuration file.')
        sys.exit(1)

For the sake of brevity, the configuration code above will be summarized with ``...`` in all of code snippets in this documentation. In other words, any time you see ``...`` in a code snippet, it can be replaced with the code above.

Next Steps
----------

From here, find a topic that interests you and dig in! If you don't know where to start, retrieving indicators is a good place to start.

.. hint:: There are some **good examples** using this SDK here: `https://github.com/ThreatConnect-Inc/threatconnect-python/tree/master/examples <https://github.com/ThreatConnect-Inc/threatconnect-python/tree/master/examples>`__

.. hint:: When using this documentation, it will be helpful to have a basic understanding of the `ThreatConnect Data Model <http://kb.threatconnect.com/customer/en/portal/articles/2092925-the-threatconnect-data-model>`_.
