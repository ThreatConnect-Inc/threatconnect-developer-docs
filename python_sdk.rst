Python SDK
==========

About This Document

This section explains the process of coding Python applications, and the
implementation of the Python SDK, using the ThreatConnect API. The
Python SDK offers coverage of all features in version 2.0 of the
ThreatConnect API—including the ability to write data to ThreatConnect.

The goal of this Python SDK library is to provide a programmatic
abstraction layer around the ThreatConnect API without losing functional
coverage over the available API resources. This abstraction layer
enables developers to focus on writing enterprise functionality without
worrying about low-level RESTful calls and authentication management.

This document is not a replacement for the official ThreatConnect API
documentation. This document serves as a companion to the official
documentation for the REST API. Read the official documentation to gain
a further understanding of the functional aspects of using the
ThreatConnect API.

How to Use This Document

This document explains how to create Groups, Indicators, Associations,
Tags, Security Labels, and Victims. Along with creating data elements, a
developer will learn how to create, update, delete, and request data
from the API using Python. This document assumes the reader knows the
Python programming language.

All code examples will be to the right in the code column in a separate
box with a monospaced font to facilitate explanation of code
functionality.

Getting Started
---------------

Python SDK Installation:

.. code:: shell

    unzip threatconnect-python.zip
    cd threatconnect-python
    python setup.py install

Example of using ConfigParser to read API configuration values:

.. code:: python

    try:
        import ConfigParser
    except:
        import configparser as ConfigParser

    # read configuration file
    config = ConfigParser.RawConfigParser()
    config.read('tc.conf')

    try:
        api_access_id = config.get('threatconnect', 'api_access_id')
        api_secret_key = config.get('threatconnect', 'api_secret_key')
        api_default_org = config.get('threatconnect', 'api_default_org')
        api_base_url = config.get('threatconnect', 'api_base_url')
    except ConfigParser.NoOptionError:
        print('Could not read configuration file.')
        sys.exit(1)

The configuration file should contain the following lines at a minimum:

::

     [threatconnect]
     api_access_id = 12345678900987654321
     api_default_org = Test Owner
     api_secret_key = aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz!@#$%^&*()-=
     api_base_url = https://api.threatconnect.com

The following examples illustrates a typical initialization of the
ThreatConnect Class:

.. code:: python

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

Installation of Python 2.7+, along with the Python SDK, is a
prerequisite. Typically, Python comes pre-installed on Linux/OS X/Unix
systems, so additional steps to install Python are not required. This
section will also highlight the basic configuration to connect to the
ThreatConnect API. While an IDE will facilitate development of
larger-scale systems, it is not required to follow the examples in this
document.

To use the RESTful API for ThreatConnect, an API user must be
provisioned. See the official ThreatConnect API documentation for
details on how to create an API user as it is out of scope for this
document.

The Python SDK will need to be configured with an Access ID and Secret
Key. One way to achieve this is to use the ``ConfigParser`` module,
which is part of the Python Standard Library. Another option is to use
``ArgParse`` and pass the configuration items via CLI (command-line
interface) arguments. For this example, ConfigParser is used.

Once the configuration has been set up, the developer should be able to
run the examples in this document as long as the Python SDK has been
installed.

Third-Party Dependencies

+------------+-----------+--------------------------------------------------------------------+
| Name       | Version   | Link                                                               |
+============+===========+====================================================================+
| requests   | 2.7.0     | `Python Requests <http://docs.python-requests.org/en/latest/>`__   |
+------------+-----------+--------------------------------------------------------------------+
| enum34     | 1.0.4     | `Python Enum34 <https://pypi.python.org/pypi/enum34>`__            |
+------------+-----------+--------------------------------------------------------------------+

Technical Design

The Python SDK for ThreatConnect was designed with a focus on
abstracting the API REST calls while enabling the developer to use an
enterprise-level programming language. The abstraction layer provides a
platform that makes cumbersome API requests simple and provides a
powerful filtering feature that minimizes the results returned from the
API, when possible, and otherwise utilizes post-API filters.

Supported Resource Types

The Python SDK supports the Resource Types listed below. There is also a
mechanism to do manual API requests to cover any API calls that are not
provided with the core functionality.

+-------------------------+-----------------------------------+
| Object                  | Description                       |
+=========================+===================================+
| ``adversaries()``       | Adversary container object        |
+-------------------------+-----------------------------------+
| ``bulk_indicators()``   | Bulk Indicator container object   |
+-------------------------+-----------------------------------+
| ``documents()``         | Document container object         |
+-------------------------+-----------------------------------+
| ``emails()``            | Email container object            |
+-------------------------+-----------------------------------+
| ``groups()``            | Group container object            |
+-------------------------+-----------------------------------+
| ``incidents()``         | Incident container object         |
+-------------------------+-----------------------------------+
| ``indicators()``        | Indicator container object        |
+-------------------------+-----------------------------------+
| ``owners()``            | Owner container object            |
+-------------------------+-----------------------------------+
| ``signatures()``        | Signature container object        |
+-------------------------+-----------------------------------+
| ``tasks()``             | Task container object             |
+-------------------------+-----------------------------------+
| ``threats()``           | Threat container object           |
+-------------------------+-----------------------------------+
| ``victims()``           | Victim container object           |
+-------------------------+-----------------------------------+

Example Python App
------------------

Example of Python SDK writing to the ThreatConnect API:

.. code:: python

    try:
        import ConfigParser
    except:
        import configparser as ConfigParser

    from threatconnect import ThreatConnect

    config = ConfigParser.RawConfigParser()
    config.read(config_file)

    try:
        api_access_id = config.get('threatconnect', 'api_access_id')
        api_secret_key = config.get('threatconnect', 'api_secret_key')
        api_default_org = config.get('threatconnect', 'api_default_org')
        api_base_url = config.get('threatconnect', 'api_base_url')
    except ConfigParser.NoOptionError:
        print('Could not read configuration file.')
        sys.exit(1)

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    owners = tc.owners()

    try:
        owners.retrieve()
    except RunTimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for owner in owners:
        print(owner.id)
        print(owner.name)
        print(owner.type)

The example illustrates how to write a program using the Python SDK for
the ThreatConnect API. An Owner's object will be created in order to
pull a collection of all Owners to which the API account being used has
access. Once retrieved, the Owners objects will be printed to the
console.

Code Highlights

+---------------------------------------------+---------------------------------------------------------------------+
| Snippet                                     | Description                                                         |
+=============================================+=====================================================================+
| ``import ConfigParser``                     | Import the ConfigParser module used to read the configuration file. |
+---------------------------------------------+---------------------------------------------------------------------+
| ``from threatconnect import ThreatConnect`` | Import the ThreatConnect Python SDK module.                         |
+---------------------------------------------+---------------------------------------------------------------------+
| ``config = ConfigParser.RawConfigParser()`` | Get an instance of ConfigParser.                                    |
+---------------------------------------------+---------------------------------------------------------------------+
| ``config.read(config_file)``                | Parse the configuration file containing the API settings.           |
+---------------------------------------------+---------------------------------------------------------------------+
| ``api_access_id = config.get('threatco...`` | Get the configuration items from the config instance.               |
+---------------------------------------------+---------------------------------------------------------------------+
| ``tc = ThreatConnect(api_access_id, ap...`` | Instantiate an instance of the ThreatConnect Class.                 |
+---------------------------------------------+---------------------------------------------------------------------+
| ``owners = tc.owners()``                    | Create an Owner's container object.                                 |
+---------------------------------------------+---------------------------------------------------------------------+
| ``owners.retrieve()``                       | Trigger an API request to retrieve Owners.                          |
+---------------------------------------------+---------------------------------------------------------------------+
| ``for owner in owners:``                    | Iterate through Owner's generator.                                  |
+---------------------------------------------+---------------------------------------------------------------------+
| ``print(owner.id)``                         | Display the **'id'** property of the Owner.                         |
+---------------------------------------------+---------------------------------------------------------------------+

Logging
~~~~~~~

Example of Python SDK calling log-file and debug level:

.. code:: python

        tc.set_tcl_file('log/tc.log', 'debug')
        tc.set_tcl_console_level('critical')

The Python SDK allows for the setting of the log-file location and debug
level. The level on the console logging can be set as well. The default
logging level for each is *critical*.

Code Highlights

+--------------------------------------------+-------------------------------------------------+
| Snippet                                    | Description                                     |
+============================================+=================================================+
| ``tc.set_tcl_file('log/tc.log', 'debug')`` | Set the destination log path and logging level. |
+--------------------------------------------+-------------------------------------------------+
| ``tc.set_tcl_console_level('info')``       | Set the console logging level.                  |
+--------------------------------------------+-------------------------------------------------+

Summary

This section explained how to:

-  Connect to the ThreatConnect API by passing reading the configuration
   file
-  Get a list of Owners
-  Iterate through an object container

Developing a Python App
-----------------------

This section provides an overview of the Python app development process
and how to package an app for deployment to the ThreatConnect platform.

Supported Version

The current supported version for Cloud deployment Python apps is 2.7.
This Python version is typically pre-installed on Linux®/Mac® OS/Unix
systems. On-Premise clients do not have this restriction. They simply
need to ensure that the Python runtime is available in their PATH
environment variable.

Third-Party Libraries

Third-party libraries are restricted to the list below at this point in
time. Cloud deployments will need to contact support@threatconnect.com
to request installation of additional third-party libraries not on this
list.

+-----------------+-----------+--------------------------------------------------------------------------------------------------+
| Name            | Version   | Link                                                                                             |
+=================+===========+==================================================================================================+
| threatconnect   | 2.0.0     | `ThreatConnect python libraries <https://github.com/ThreatConnect-Inc/threatconnect-python>`__   |
+-----------------+-----------+--------------------------------------------------------------------------------------------------+
| requests        | 2.6.0     | `Python Requests <http://docs.python-requests.org/en/latest/>`__                                 |
+-----------------+-----------+--------------------------------------------------------------------------------------------------+
| enum34          | 1.0.4     | `Python Enum34 <https://pypi.python.org/pypi/enum34>`__                                          |
+-----------------+-----------+--------------------------------------------------------------------------------------------------+

Deployment Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

`Apps use a deployment configuration file to define variables and
execution environment <#deployment-configuration-file>`__

Command-Line Parameters
-----------------------

Suppose ``opendns.py`` uses the following syntax:

.. code:: python

    python opendns.py \
        --tc_log_path log \
        --tc_temp_path tmp \
        --tc_out_path out \
        --tc_api_path https://api.threatconnect.com \
        --api_access_id 1234567890 \
        --api_default_org Test & Org \
        --api_max_results 300 \
        --api_secret_key qwertyuiopasdfghjklzxcvbnm \
        --confidences >=,75 \
        --delete \
        --logging debug \
        --opendns_key x000000x-x0x0-0x00-x000-xx000x00000x \
        --owners Subscriber Community \
        --owners Test & Org \
        --queue_sleep 30 \
        --ratings >=,3.0 

These command line options can be implemented using ``argparse``:

.. code:: python

    import argparse

    #
    # Parse Args
    #
    parser = argparse.ArgumentParser()

    # Api Args
    parser.add_argument('--api_access_id', help='API Access ID', required=True)
    parser.add_argument('--api_secret_key', help='API Secret Key', required=True)
    parser.add_argument('--api_default_org', help='API Default Org', required=True)
    parser.add_argument('--api_max_results', help='API Max Results', type=int)
    parser.add_argument('--opendns_key', help='OpenDNS API Key')

    # Custom Args
    parser.add_argument('--logging', help='Logging Level', default='critical', choices=list(log_level.keys()))
    parser.add_argument('--queue_sleep', help='Seconds to Sleep', default=60, type=int)
    parser.add_argument('--delete', help='Delete deprecated entries from OpenDNS', action='store_true', default=False)

    # API Filter Args
    parser.add_argument('--modified_since', help='Modified Since Filter')
    parser.add_argument('--owners', help='Owner Names', action='append')
    parser.add_argument('--tags', help='Tag Filter', action='append')

    # Post Filters
    parser.add_argument('--date_added', help='Date Added Filter', action='append')
    parser.add_argument('--last_modified', help='Last Modified Filter', action='append')
    parser.add_argument('--ratings', help='Rating Filter', action='append')
    parser.add_argument('--confidences', help='Confidence Filter', action='append')

    # Standard Args
    parser.add_argument('--tc_log_path', help='ThreatConnect log path', default='/tmp')
    parser.add_argument('--tc_temp_path', help='ThreatConnect temp path', default='/tmp')
    parser.add_argument('--tc_api_path', help='ThreatConnect api path', default='https://api.threatconnect.com')

    # Parse
    args, unknown = parser.parse_known_args()

The developer is strongly advised to use a standard library like
`argparse <https://docs.python.org/3/library/argparse.html>`__ to
simplify command line parsing.

Optional Properties
-------------------

There are some optional flags that may be used by the app to:

-  Restrict intervals for repeating jobs
-  Handle list parsing for parameter arrays
-  Handle Boolean flags to turn features on/off
-  Encrypt parameters like API Keys

Repeating Job Intervals

This optional property controls which interval (in minutes) the
job-creation dialogue can use when creating a repeating job.

A repeating job is a job that runs every day on an interval (e.g., every
30 minutes).

The following property ``repeating.minutes = 5,10,15,30,60,120,240,360``
will display the stated intervals within the repeating scheudle
picklist.

Multiple values should be separated by a comma. All minutes greater than
60 will be discarded unless they are divisible by 60. If this property
is not provided, the following repeating intervals are defaulted during
job creation: ``60, 120, 240, 360, 720``.

Parsing Argument Lists

There is logic in place for parsing a list of values configured by the
job-creation dialogue. In order to allow list parsing for a Python app,
the configuration file must include the ``list.delimiter`` property.

Delimiters may be a single character or a multi-character String:

``list.delimiter = |``

A parameter that accepts lists must have ``<param-name>.list`` property
set. This enables the job executor to pass this parameter in list form
by tokenizing the String using the designated list delimiter.

No equal sign or property value is required for this flag:

``param.<param-name>.list``

Once these two properties are in place, the Python code must include the
option below when the argument is added to the parser.

This option allows argparse to convert duplicate parameters into a
single list:

``action='append'``

Parsing Argument Flags

Apps can also use Boolean flags to designate whether to turn on a
specific feature. In the parsing code noted earlier, there is an example
of an argument flag (``--delete``) configurable by the job-creation
dialogue within ThreatConnect.

The configuration file must have the following flag present for a
Boolean parameter:

``param.<param-name>.flag``

This property will direct the ThreatConnect application to show a
checkbox to the job-creation dialogue. Once the job is created, the flag
will be passed to each job execution without a parameter value. If the
flag is left unchecked during job creation, then no flag is passed on
each job execution.

Encrypted Parameters

This property should be used to encrypt private passwords used by the
app (e.g., API keys). This added level of security will allow the
application to persist the password in encrypted form when at rest. The
input field during job creation will be "password" text, and the key
will not be visible when typed.

Use encrypted parameters by setting the following flag:

``param.<param-name>.encrypt``

At runtime, the application runtime environment will call the app with
the decrypted key. At no point in time is the password persisted in
decrypted form.

The encrypt flag won't encrypt ``.encrypted`` parameters until the
Keychain feature is enabled on the server.

ThreatConnect Parameters
------------------------

ThreatConnect passes standard parameters to all jobs within its standard
sandbox container. There should be no assumptions made on the naming or
existence of paths passed in these variables outside of the lifetime of
the job execution.

Since all job executions are run in a sandboxed environment, app
developers should never hard-code ThreatConnect Parameters:

+-------------------------+------------------------------------------------------------------------+
| ThreatConnect Parameter | Description                                                            |
+=========================+========================================================================+
| ``tc_log_path``         | Log path for the specific instance of the job execution.               |
+-------------------------+------------------------------------------------------------------------+
| ``tc_tmp_path``         | Temporary storage path for the specific instance of the job execution. |
+-------------------------+------------------------------------------------------------------------+
| ``tc_out_path``         | Output path for the specific instance of the job execution.            |
+-------------------------+------------------------------------------------------------------------+
| ``tc_api_path``         | Path to the ThreatConnect API server.                                  |
+-------------------------+------------------------------------------------------------------------+

Results ThreatConnect File
--------------------------

Job executions can use a special file called ``results.tc`` to write
results as a mechanism for updating parameters for subsequent runs. A
use case for this feature is an app that needs to know the last time it
completed successfully in order to process data since that completion.
The parameter definitions are quite flexible, with the only restriction
that the parameters written to the ``results.tc`` file must exist in the
``configuration`` file in order to be persisted.

Example ``results.tc`` file:

``param.last_completed_time = 1430619556``

Assuming there is a property with the same name in ``configuration``,
the job executor will update the new property value in the system for
the next run. The property will only be stored if the job execution is
successful.

This file should be written to the ``tc_out_path`` passed as one of the
standard TC parameters.

Exit Codes
----------

There are standard exit codes that ThreatConnect uses to report if a
program completed successfully. The Python app is responsible for
calling ``sys.exit(N)``, where 'N' is the appropriate exit code
highlighted below.

When ``sys.exit()`` is not called by an app, an exit code of zero is
returned by default during normal code execution. System-critical errors
(e.g., file not found) return non-zero exit codes. The developer is
responsible for catching and handling program errors accordingly.

At times a program may want to report a partial failure (e.g., batch
process where X out of Y updates completed). In cases of partial
failure, the system administrator can retrieve the log file for that job
execution and view more detailed output from the program run.

+-------------------+------------------------------------------------------------------+
| Status            | Description                                                      |
+===================+==================================================================+
| Success           | Exit code 0 - Process completed successfully.                    |
+-------------------+------------------------------------------------------------------+
| Partial Failure   | Exit code 3 - Process had a partial failure.                     |
+-------------------+------------------------------------------------------------------+
| Failure           | Any value not 0 or 3 (typically Exit code 1) - Process failed.   |
+-------------------+------------------------------------------------------------------+

Wrapper-Testing Utility
-----------------------

Command line argument script example:

.. code:: python

    # Config file for tc-wrapper.py to call any ThreatConnect integration script
    # with these properties as command line arguments:
    #
    #   Example:
    #
    #       python tc-wrapper.py <my-script.py>
    [threatconnect]
    tc_log_path = /tmp
    tc_out_path = /tmp
    tc_temp_path = /tmp
    tc_api_path = https://api.threatconnect.com

Calling the wrapper:

.. code:: python


        python tc-wrapper.py <my-script.py>

The wrapper calls the developer's program with the parameters as
ThreatConnect would:

.. code:: python

    python <my-script.py> \
        --tc_log_path /tmp \
        --tc_temp_path /tmp \
        --tc_out_path /tmp \
        --tc_api_path https://api.threatconnect.com \

The command line parameters can be extensive. To facilitate app
development, there is a Python wrapper utility that takes a ``tc.conf``
file and calls a Python script with the properties from the
configuration file as command-line parameters. This simulates the way
ThreatConnect would call the app in a production environment.

The configuration file should be in the same location as the developer's
main Python script, then call the wrapper.

Python Examples
~~~~~~~~~~~~~~~

-  `SDK Examples
   Directory <https://github.com/ThreatConnect-Inc/threatconnect-python/tree/master/examples>`__

Python Retrieve
---------------

Adversaries Retrieve

This section explains how to work with ThreatConnect Adversary
Resources.

Supported API Filters

API filters use the API filtering feature to limit the result set
returned from the API.

+----------------------------+---------------+-------------------------------------------------+
| Filter                     | Value Type    | Description                                     |
+============================+===============+=================================================+
| ``add_id()``               | int           | Filter Adversary by ID                          |
+----------------------------+---------------+-------------------------------------------------+
| ``add_document_id()``      | int           | Filter Adversary on associated Document ID      |
+----------------------------+---------------+-------------------------------------------------+
| ``add_email_id()``         | int           | Filter Adversary on associated Email ID         |
+----------------------------+---------------+-------------------------------------------------+
| ``add_incident_id()``      | int           | Filter Adversary on associated Incident ID      |
+----------------------------+---------------+-------------------------------------------------+
| ``add_indicator()``        | str           | Filter Adversary on associated Indicator        |
+----------------------------+---------------+-------------------------------------------------+
| ``add_owner()``            | list or str   | Filter Adversary on associated Owner            |
+----------------------------+---------------+-------------------------------------------------+
| ``add_security_label()``   | str           | Filter Adversary on associated Security Label   |
+----------------------------+---------------+-------------------------------------------------+
| ``add_signature_id()``     | int           | Filter Adversary on associated Signature ID     |
+----------------------------+---------------+-------------------------------------------------+
| ``add_tag()``              | str           | Filter Adversary on applied Tag                 |
+----------------------------+---------------+-------------------------------------------------+
| ``add_threat_id()``        | int           | Filter Adversary on associated Threat ID        |
+----------------------------+---------------+-------------------------------------------------+
| ``add_victim_id()``        | int           | Filter Adversary on associated Victim ID        |
+----------------------------+---------------+-------------------------------------------------+

Supported Post Filters

Post filters are applied on the results returned by the API request.

+---------------------------+--------------+----------------------------------+
| Filter                    | Value Type   | Description                      |
+===========================+==============+==================================+
| ``add_pf_name()``         | str          | Filter Adversary on name         |
+---------------------------+--------------+----------------------------------+
| ``add_pf_date_added()``   | str          | Filter Adversary on date added   |
+---------------------------+--------------+----------------------------------+

Filter Example
~~~~~~~~~~~~~~

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    adversaries = tc.adversaries()

    try:
        owner = 'Example Community'
        filter1 = adversaries.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        adversaries.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for adversary in adversaries:
        print(adversary.id)
        print(adversary.name)
        print(adversary.date_added)
        print(adversary.weblink)

This example will demonstrate how to retrieve Adversaries while applying
filters. Two filters will be added: one for the Owner and another for a
Tag. The result set returned from this example will contain any
Adversaries in the "Example Community" Owner that has a Tag of
***EXAMPLE***.

Note: The ``filter1`` object contains a ``filters`` property that
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more on using filters, see the `Advanced Filter
Tutorial <#filtering>`__.

Code Highlights

+----------------------------------------------+--------------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                                |
+==============================================+============================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                      |
+----------------------------------------------+--------------------------------------------------------------------------------------------+
| ``adversaries = tc.adversaries()``           | Instantiate an Adversaries container object.                                               |
+----------------------------------------------+--------------------------------------------------------------------------------------------+
| ``filter1 = adversaries.add_filter()``       | Add a filter object to the Adversaries container object (support multiple filter objects). |
+----------------------------------------------+--------------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``               | Add API filter to retrieve Adversaries with the 'Example' tag.                             |
+----------------------------------------------+--------------------------------------------------------------------------------------------+
| ``adversaries.retrieve()``                   | Trigger the API request and retrieve the Adversaries intelligence data.                    |
+----------------------------------------------+--------------------------------------------------------------------------------------------+
| ``for adversary in adversaries:``            | Iterate over the Adversaries container object generator.                                   |
+----------------------------------------------+--------------------------------------------------------------------------------------------+
| ``print(adversary.id)``                      | Display the **'id'** property of the Adversary object.                                     |
+----------------------------------------------+--------------------------------------------------------------------------------------------+

Resource Metadata

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations

Groups

See the `Group Associations Documentation <#associations>`__.

Indicators

See the `Indicator Associations
Documentation <#retrieving-indicator-associations>`__.

Victims

See the `Victim Associations
Documentation <#victim-associations-retrieve>`__.

Outputs

CSV

See the `CSV Output Documentation <#csv>`__.

JSON

See the `JSON Output Documentation <#json>`__.

Key Value

See the `Key Value Output Documentation <#key-value>`__.

Bulk Indicator Download
-----------------------

This section explains how to work with ThreatConnect Bulk Indicators.

Supported API Filters

The Bulk Download feature of the ThreatConnect API does not support any
API filters.

Supported Post Filters

Post filters are applied on the results returned by the API request.

+---------------------------------------+------------+------------------------------------------------+
| Filter                                | Value Type | Description                                    |
+=======================================+============+================================================+
| ``add_pf_attribute()``                | str        | Filter Indicators on Attribute type.           |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_confidence()``               | int        | Filter Indicators on Confidence value.         |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_date_added()``               | str        | Filter Indicators on date added.               |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_last_modified()``            | str        | Filter Indicators on last modified date.       |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_rating()``                   | str        | Filter Indicators on Rating.                   |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_tag()``                      | str        | Filter Indicators on Tag.                      |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_threat_assess_confidence()`` | int        | Filter Indicators on Threat Assess Confidence. |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_threat_assess_rating()``     | str        | Filter Indicators on Threat Assess Rating.     |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_type()``                     | str        | Filter Indicators on Indicator type.           |
+---------------------------------------+------------+------------------------------------------------+

Bulk Download Example
~~~~~~~~~~~~~~~~~~~~~

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python

    from threatconnect.Config.FilterOperator import FilterOperator

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # indicator object
    indicators = tc.bulk_indicators()
    owner = 'Example Community'
     
    # Add Post Filters
    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        filter1.add_pf_confidence(75, FilterOperator.GE)
        filter1.add_pf_rating('2.5', FilterOperator.GT)
    except AttributeError as e:
        print(e)
        sys.exit(1)

    # Retrieve Indicators and Apply Filters
    try:
        indicators.retrieve()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    # Iterate Through Results
    for indicator in indicators:
        if isinstance(indicator.indicator, dict):
            for indicator_type, indicator_value in indicator.indicator.items():
                print('{0}: {1}'.format(indicator_type, indicator_value))
        else:
            print(indicator.indicator)
        print(indicator.id)
        print(indicator.owner_name)
        print(indicator.date_added)
        print(indicator.last_modified)
        print(indicator.rating)
        print(indicator.threat_assess_rating)
        print(indicator.confidence)
        print(indicator.threat_assess_confidence)
        print(indicator.type)
        print(indicator.weblink)
        

This example will demonstrate how to retrieve Indicators while applying
filters. In this example, three filters will be added, one for the
Owner, one for the Confidence, and one for the Rating. The result set
returned from this example will contain any Indicators in the **"Example
Community"** Owner that has a Confidence greater than or equal to 75 and
a Rating greater than 2.5.

Note: The ``filter1`` object contains a ``filters`` property which
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more on using filters, see the `Advanced Filter
Tutorial <#filtering>`__.

Code Highlights

+------------------------------------------+-------------------------------------------------------------------------------------------+
| Snippet                                  | Description                                                                               |
+==========================================+===========================================================================================+
| ``tc = ThreatConnect(api_access_id,...`` | Instantiate the ThreatConnect object.                                                     |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``indicators = tc.indicators()``         | Instantiate an Indicators container object.                                               |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``filter1 = indicator.add_filter()``     | Add a filter object to the Indicators container object (support multiple filter objects). |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``           | Add API filter to retrieve Indicators with the 'Example' tag.                             |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``indicator.retrieve()``                 | Trigger the API request and retrieve the Indicators intelligence data.                    |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``for indicator in indicators:``         | Iterate over the Indicators container object generator.                                   |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``print(indicator.indicator)``           | Display the **'indicator'** property of the Indicator object.                             |
+------------------------------------------+-------------------------------------------------------------------------------------------+

Loading Attributes Example
~~~~~~~~~~~~~~~~~~~~~~~~~~

Example of Python SDK iterating through a container of indicator
objects:

.. code:: python

     
        for attribute in indicator.attributes:
            print(attribute.type)
            print(attribute.value)
            print(attribute.date_added)
            print(attribute.last_modified)
            print(attribute.displayed)

The example continues from the previous `Bulk Download
Example <#bulk-download-example>`__. Iterating through the
**'indicators'** container provides ``indicator`` objects. The
``load_attribute()`` method does not need to be called for Bulk
Indicator downloads, since the Attribute data is packaged with the
Indicator data.

Code Highlights

+--------------------------------------------+----------------------------------------------------------+
| Snippet                                    | Description                                              |
+============================================+==========================================================+
| ``for attribute in indicator.attributes:`` | Iterate over the Attribute property object generator.    |
+--------------------------------------------+----------------------------------------------------------+
| ``print(attribute.type)``                  | Display the **'type'** property of the Attribute object. |
+--------------------------------------------+----------------------------------------------------------+

Loading Security Label Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example of Python SDK loading the Indicator Security Label:

.. code:: python

        indicator.load_security_label()
        if indicator.security_label is not None:
            print(indicator.security_label.name)
            print(indicator.security_label.description)
            print(indicator.security_label.date_added)

The example continues from the previous `Loading Attributes
Example <#loading-attributes-example>`__. While still in the indicator's
loop, the Indicator Security Label can be loaded by calling the
``load_security_label()`` method of the Indicator object. By calling
this method, another API request will be triggered, and the resulting
data will be stored as a Security Label object in the Indicator object.
This object can then be directly accessed from the ``security_label``
property.

Code Highlights

+--------------------------------------------+------------------------------------------------------------------------+
| Snippet                                    | Description                                                            |
+============================================+========================================================================+
| ``indicator.load_security_label()``        | Trigger API call to load the Security Label into the Indicator object. |
+--------------------------------------------+------------------------------------------------------------------------+
| ``if indicator.security_label is not ...`` | Ensure the object has been loaded before displaying properties.        |
+--------------------------------------------+------------------------------------------------------------------------+
| ``print(indicator.security_label.name)``   | Display the **'name'** property of the Security Label object.          |
+--------------------------------------------+------------------------------------------------------------------------+

Loading Tags Example
~~~~~~~~~~~~~~~~~~~~

Example of Python SDK:

.. code:: python

        for tag in indicator.tags:
            print(tag.name)
            print(tag.weblink)

The example continues from the previous `Loading Security Label
Example <#loading-security-label-example>`__. The ``load_tags()`` method
of the Indicator object does not need to be called for Bulk Indicator
downloads, since the Tag is packaged with the Indicator data. By calling
this method, another API request will be triggered, and the resulting
data will be stored as a Tag objects in the Indicator object. This
object can then be directly accessed from the ``tags`` property.

Code Highlights

+--------------------------------+----------------------------------------------------------+
| Snippet                        | Description                                              |
+================================+==========================================================+
| ``for tag in indicator.tags:`` | Iterate over the Tag property object generator.    |
+--------------------------------+----------------------------------------------------------+
| ``print(tag.name)``            | Display the **'name'** property of the Tag object. |
+--------------------------------+----------------------------------------------------------+

Group Associations
------------------

Example of Python SDK pulling Groups from the API:

.. code:: python

        for g_association in indicator.group_associations:
            print(g_association.id)
            print(g_association.name)
            if hasattr(g_association, 'type'):
                print(g_association.type)
            print(g_association.owner_name)
            print(g_association.date_added)
            print(g_association.weblink)

Iterate through all Groups associated with this Indicator. These Groups
are pulled directly from the API and are not stored in the Indicator
object.

Code Highlights

+---------------------------------------------+-------------------------------------------------------------------------+
| Snippet                                     | Description                                                             |
+=============================================+=========================================================================+
| ``for g_associations in indicator.grou...`` | Trigger API call to retrieve all Groups associated with this Indicator. |
+---------------------------------------------+-------------------------------------------------------------------------+
| ``print(g_association.id)``                 | Display the **'id'** property of the associated Group object.           |
+---------------------------------------------+-------------------------------------------------------------------------+

Indicator Associations
~~~~~~~~~~~~~~~~~~~~~~

Example Python SDK iterating through all Indicators associated with an
Indicator:

.. code:: python

        for i_association in indicator.indicator_associations:
            print(i_association.id)
            print(i_association.indicator)
            print(i_association.type)
            print(i_association.description)
            print(i_association.owner_name)
            print(i_association.rating)
            print(i_association.confidence)
            print(i_association.date_added)
            print(i_association.last_modified)
            print(i_association.weblink)

Iterate through all Indicators associated with this Indicator. These
Indicators are pulled directly from the API and are not stored in the
Indicator object.

Code Highlights

+--------------------------------------------+-----------------------------------------------------------------------------+
| Snippet                                    | Description                                                                 |
+============================================+=============================================================================+
| ``for i_association in indicator.ind_...`` | Trigger API call to retrieve all Indicators associated with this Indicator. |
+--------------------------------------------+-----------------------------------------------------------------------------+
| ``print(i_association.id)``                | Display the **'id'** property of the associated Indicator object.           |
+--------------------------------------------+-----------------------------------------------------------------------------+

Victim Associations
~~~~~~~~~~~~~~~~~~~

Python SDK example of iterating through all Victims associated with this
Indicator:

.. code:: python

        for v_associations in indicator.victim_associations:
            print(v_associations.id)
            print(v_associations.name)
            print(v_associations.description)
            print(v_associations.owner_name)
            print(v_associations.nationality)
            print(v_associations.org)
            print(v_associations.suborg)
            print(v_associations.work_location)
            print(v_associations.weblink)

Iterate through all Victims associated with this Indicator. These
Victims are pulled directly from the API and are not stored in the
Indicator object.

Code Highlights

+---------------------------------------------+--------------------------------------------------------------------------+
| Snippet                                     | Description                                                              |
+=============================================+==========================================================================+
| ``for v_associations in indicator.vic_...`` | Trigger API call to retrieve all Victims associated with this Indicator. |
+---------------------------------------------+--------------------------------------------------------------------------+
| ``print(v_association.id)``                 | Display the **'id'** property of the associated Victim object.           |
+---------------------------------------------+--------------------------------------------------------------------------+

Outputs

CSV

See the `CSV Output Documentation <#csv>`__.

JSON

See the `JSON Output Documentation <#json>`__.

Key Value

See the `Key Value Output Documentation <#key-value>`__.

Documents Retrieve
------------------

This document explains how to work with ThreatConnect Document
Resources.

Supported API Filters

API filters use the API filtering feature to limit the result set
returned from the API.

+----------------------------+---------------+-------------------------------------------------+
| Filter                     | Value Type    | Description                                     |
+============================+===============+=================================================+
| ``add_id()``               | int           | Filter Document by ID.                          |
+----------------------------+---------------+-------------------------------------------------+
| ``add_document_id()``      | int           | Filter Document on associated Document ID.      |
+----------------------------+---------------+-------------------------------------------------+
| ``add_email_id()``         | int           | Filter Document on associated Email ID.         |
+----------------------------+---------------+-------------------------------------------------+
| ``add_incident_id()``      | int           | Filter Document on associated Incident ID.      |
+----------------------------+---------------+-------------------------------------------------+
| ``add_indicator()``        | str           | Filter Document on associated Indicator.        |
+----------------------------+---------------+-------------------------------------------------+
| ``add_owner()``            | list or str   | Filter Document on associated Owner.            |
+----------------------------+---------------+-------------------------------------------------+
| ``add_security_label()``   | str           | Filter Document on associated Security Label.   |
+----------------------------+---------------+-------------------------------------------------+
| ``add_signature_id()``     | int           | Filter Document on associated Signature ID.     |
+----------------------------+---------------+-------------------------------------------------+
| ``add_tag()``              | str           | Filter Document on applied Tag.                 |
+----------------------------+---------------+-------------------------------------------------+
| ``add_threat_id()``        | int           | Filter Document on associated Threat ID.        |
+----------------------------+---------------+-------------------------------------------------+
| ``add_victim_id()``        | int           | Filter Document on associated Victim ID.        |
+----------------------------+---------------+-------------------------------------------------+

Supported Post Filters

Post filters are applied on the results returned by the API request.

+---------------------------+--------------+----------------------------------+
| Filter                    | Value Type   | Description                      |
+===========================+==============+==================================+
| ``add_pf_name()``         | str          | Filter Document on name.         |
+---------------------------+--------------+----------------------------------+
| ``add_pf_date_added()``   | str          | Filter Document on date added.   |
+---------------------------+--------------+----------------------------------+

Documents Retrieve Filter Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    documents = tc.documents()
    owner = 'Example Community'

    try:
        filter1 = documents.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        documents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for document in documents:
        print(document.id)
        print(document.name)
        print(document.date_added)
        print(document.owner_name)
        print(document.weblink)
        
        # document specific property
        print(document.file_name)

This example will demonstrate how to retrieve documents while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any documents in the **Example Community** Owner that has a Tag
of **EXAMPLE**.

Note: The ``filter1`` object contains a ``filters`` property that
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more on using filters see the `Advanced Filter
Tutorial </python/advanced/filtering/>`__.

Code Highlights

+--------------------------------------------+------------------------------------------------------------------------------------------+
| Snippet                                    | Description                                                                              |
+============================================+==========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                    |
+--------------------------------------------+------------------------------------------------------------------------------------------+
| ``documents = tc.documents()``               | Instantiate a Documents container object.                                                |
+--------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1 = documents.add_filter()``         | Add a filter object to the Documents container object (support multiple filter objects). |
+--------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``               | Add API filter to retrieve Documents with the 'Example' tag                              |
+--------------------------------------------+------------------------------------------------------------------------------------------+
| ``documents.retrieve()``                     | Trigger the API request and retrieve the Documents intelligence data.                    |
+--------------------------------------------+------------------------------------------------------------------------------------------+
| ``for document in documents:``               | Iterate over the Documents container object generator.                                   |
+--------------------------------------------+------------------------------------------------------------------------------------------+
| ``print(document.id)``                       | Display the **'id'** property of the Document object.                                    |
+--------------------------------------------+------------------------------------------------------------------------------------------+


Download Document Contents Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python SDK example of downloading the contents of the document stored
with the Document Resource:

.. code:: python

        document.download()
        if document.contents is not None:
            print(document.contents)

Continuing from the `Filter Example <#filter-example>`__, the example
will download the contents of the document stored with the Document
Resource.

Code Highlights

+-------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                             | Description                                                                          |
+=====================================+======================================================================================+
| ``document.download()``               | Trigger API request to download the Document contents.                               |
+-------------------------------------+--------------------------------------------------------------------------------------+
| ``if document.contents is not None:`` | Validate the Document has downloaded before displaying.                              |
+-------------------------------------+--------------------------------------------------------------------------------------+
| ``print(document.contents)``          | Display the contents of the Document. (This should only be done for ASCII contents.) |
+-------------------------------------+--------------------------------------------------------------------------------------+

Resource Metadata

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations

Groups

See the `Group Associations Documentation <#associations>`__.

Indicators

See the `Indicator Associations
Documentation <#retrieving-indicator-associations>`__.

Victims

See the `Victim Associations
Documentation <#victim-associations-retrieve>`__.

Outputs

CSV

See the `CSV Output Documentation <#csv>`__.

JSON

See the `JSON Output Documentation <#json>`__.

Key Value

See the `Key Value Output Documentation <#key-value>`__.

Emails Retrieve
---------------

This section explains how to work with ThreatConnect Email Resources.

Supported API Filters

API filters use the API filtering feature to limit the result set
returned from the API.

+----------------------------+---------------+----------------------------------------------+
| Filter                     | Value Type    | Description                                  |
+============================+===============+==============================================+
| ``add_id()``               | int           | Filter Email by ID.                          |
+----------------------------+---------------+----------------------------------------------+
| ``add_document_id()``      | int           | Filter Email on associated Document ID.      |
+----------------------------+---------------+----------------------------------------------+
| ``add_email_id()``         | int           | Filter Email on associated Email ID.         |
+----------------------------+---------------+----------------------------------------------+
| ``add_incident_id()``      | int           | Filter Email on associated Incident ID.      |
+----------------------------+---------------+----------------------------------------------+
| ``add_indicator()``        | str           | Filter Email on associated Indicator.        |
+----------------------------+---------------+----------------------------------------------+
| ``add_owner()``            | list or str   | Filter Email on associated Owner.            |
+----------------------------+---------------+----------------------------------------------+
| ``add_security_label()``   | str           | Filter Email on associated Security Label.   |
+----------------------------+---------------+----------------------------------------------+
| ``add_signature_id()``     | int           | Filter Email on associated Signature ID.     |
+----------------------------+---------------+----------------------------------------------+
| ``add_tag()``              | str           | Filter Email on applied Tag.                 |
+----------------------------+---------------+----------------------------------------------+
| ``add_threat_id()``        | int           | Filter Email on associated Threat ID.        |
+----------------------------+---------------+----------------------------------------------+
| ``add_victim_id()``        | int           | Filter Email on associated Victim ID.        |
+----------------------------+---------------+----------------------------------------------+

Supported Post Filters

Post filters are applied on the results returned by the API request.

+---------------------------+--------------+-------------------------------+
| Filter                    | Value Type   | Description                   |
+===========================+==============+===============================+
| ``add_pf_name()``         | str          | Filter Email on name.         |
+---------------------------+--------------+-------------------------------+
| ``add_pf_date_added()``   | str          | Filter Email on date added.   |
+---------------------------+--------------+-------------------------------+

Emails Retrieve Filter Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    emails = tc.emails()
    owner = 'Example Community'

    try:
        filter1 = emails.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        emails.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for email in emails:
        print(email.id)
        print(email.name)
        print(email.date_added)
        print(email.weblink)
        
        # email specific properties
        print(email.header)
        print(email.subject)
        print(email.from_address)
        print(email.to)
        print(email.body)
        print(email.score)

This example will demonstrate how to retrieve emails while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any emails in the **Example Community** Owner that has a Tag of
***EXAMPLE***.

To retrieve the headers and body for a single email, include a filter
for its ID. (Make an individual query for each email.)

``filter1.add_id($email_id)``

Note: The ``filter1`` object contains a ``filters`` property which
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more on using filters, see the `Advanced Filter
Tutorial <#filtering>`__.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                           |
+==============================================+=======================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                 |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``emails = tc.emails()``                     | Instantiate an Emails container object.                                               |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``filter1 = emails.add_filter()``            | Add a Filter object to the Emails container object (support multiple filter objects). |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``               | Add API Filter to be applied to the API request.                                      |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``emails.retrieve()``                        | Trigger the API request and retrieve the Emails intelligence data.                    |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``for email in emails:``                     | Iterate over the Emails container object generator.                                   |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``print(email.id)``                          | Display the **'id'** property of the Email object.                                    |
+----------------------------------------------+---------------------------------------------------------------------------------------+

Resource Metadata

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations

Groups

See the `Group Associations Documentation <#associations>`__.

Indicators

See the `Indicator Associations
Documentation <#retrieving-indicator-associations>`__.

Victims

See the `Victim Associations
Documentation <#victim-associations-retrieve>`__.

Outputs

CSV

See the `CSV Output Documentation <#csv>`__.

JSON

See the `JSON Output Documentation <#json>`__.

Key Value

See the `Key Value Output Documentation <#key-value>`__.

Groups Retrieve
---------------

This section explains how to work with the ThreatConnect Group
Resources.

Supported API Filters

API filters use the API filtering feature to limit the result set
returned from the API.

+----------------------------+---------------+----------------------------------------------+
| Filter                     | Value Type    | Description                                  |
+============================+===============+==============================================+
| ``add_document_id()``      | int           | Filter Group on associated Document ID.      |
+----------------------------+---------------+----------------------------------------------+
| ``add_email_id()``         | int           | Filter Group on associated Email ID.         |
+----------------------------+---------------+----------------------------------------------+
| ``add_incident_id()``      | int           | Filter Group on associated Incident ID.      |
+----------------------------+---------------+----------------------------------------------+
| ``add_indicator()``        | str           | Filter Group on associated Indicator.        |
+----------------------------+---------------+----------------------------------------------+
| ``add_owner()``            | list or str   | Filter Group on associated Owner.            |
+----------------------------+---------------+----------------------------------------------+
| ``add_security_label()``   | str           | Filter Group on associated Security Label.   |
+----------------------------+---------------+----------------------------------------------+
| ``add_signature_id()``     | int           | Filter Group on associated Signature ID.     |
+----------------------------+---------------+----------------------------------------------+
| ``add_tag()``              | str           | Filter Group on applied Tag.                 |
+----------------------------+---------------+----------------------------------------------+
| ``add_threat_id()``        | int           | Filter Group on associated Threat ID.        |
+----------------------------+---------------+----------------------------------------------+
| ``add_victim_id()``        | int           | Filter Group on associated Victim ID.        |
+----------------------------+---------------+----------------------------------------------+

Supported Post Filters

Post filters are applied on the results returned by the API request.

+---------------------------+--------------+-------------------------------+
| Filter                    | Value Type   | Description                   |
+===========================+==============+===============================+
| ``add_pf_name()``         | str          | Filter Group on name.         |
+---------------------------+--------------+-------------------------------+
| ``add_pf_date_added()``   | str          | Filter Group on date added.   |
+---------------------------+--------------+-------------------------------+

Groups Retrieve Filter Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    groups = tc.groups()
    owner = 'Example Community'

    try:
        filter1 = groups.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        groups.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for group in groups:
        print(group.id)
        print(group.name)
        print(group.date_added)
        print(group.weblink)
        
        # group specific property
        print(group.type)

This example will demonstrate how to retrieve Groups while applying
filters. In this example two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Groups in the **Example Community** Owner that has a Tag of
***EXAMPLE***.

Note: The ``filter1`` object contains a ``filters`` property that
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more on using filters see the `Advanced Filter
Tutorial <#filtering>`__.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                           |
+==============================================+=======================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                 |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``groups = tc.groups()``                     | Instantiate a Groups container object.                                                |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``filter1 = groups.add_filter()``            | Add a filter object to the Groups container object (support multiple filter objects). |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``               | Add API filter to retrieve Groups with the 'Example' tag.                             |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``groups.retrieve()``                        | Trigger the API request and retrieve the Groups intelligence data.                    |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``for group in groups:``                     | Iterate over the Groups container object generator.                                   |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``print(group.id)``                          | Display the **'id'** property of the Group object.                                    |
+----------------------------------------------+---------------------------------------------------------------------------------------+

Resource Metadata

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations

Groups

See the `Group Associations Documentation <#associations>`__.

Indicators

See the `Indicator Associations
Documentation <#retrieving-indicator-associations>`__.

Victims

See the `Victim Associations
Documentation <#victim-associations-retrieve>`__.

Outputs

CSV

See the `CSV Output Documentation <#csv>`__.

JSON

See the `JSON Output Documentation <#json>`__.

Key Value

See the `Key Value Output Documentation <#key-value>`__.

Incidents Retrieve
------------------

This section explains how to work with ThreatConnect Incident Resources.

Supported API Filters

API filters use the API filtering feature to limit the result set
returned from the API.

+----------------------------+---------------+-------------------------------------------------+
| Filter                     | Value Type    | Description                                     |
+============================+===============+=================================================+
| ``add_id()``               | int           | Filter Incident by ID.                          |
+----------------------------+---------------+-------------------------------------------------+
| ``add_document_id()``      | int           | Filter Incident on associated Document ID.      |
+----------------------------+---------------+-------------------------------------------------+
| ``add_email_id()``         | int           | Filter Incident on associated Email ID.         |
+----------------------------+---------------+-------------------------------------------------+
| ``add_incident_id()``      | int           | Filter Incident on associated Incident ID.      |
+----------------------------+---------------+-------------------------------------------------+
| ``add_indicator()``        | str           | Filter Incident on associated Indicator.        |
+----------------------------+---------------+-------------------------------------------------+
| ``add_owner()``            | list or str   | Filter Incident on associated Owner.            |
+----------------------------+---------------+-------------------------------------------------+
| ``add_security_label()``   | str           | Filter Incident on associated Security Label.   |
+----------------------------+---------------+-------------------------------------------------+
| ``add_signature_id()``     | int           | Filter Incident on associated Signature ID.     |
+----------------------------+---------------+-------------------------------------------------+
| ``add_tag()``              | str           | Filter Incident on applied Tag.                 |
+----------------------------+---------------+-------------------------------------------------+
| ``add_threat_id()``        | int           | Filter Incident on associated Threat ID.        |
+----------------------------+---------------+-------------------------------------------------+
| ``add_victim_id()``        | int           | Filter Incident on associated Victim ID.        |
+----------------------------+---------------+-------------------------------------------------+

Supported Post Filters

Post filters are applied on the results returned by the API request.

+---------------------------+--------------+----------------------------------+
| Filter                    | Value Type   | Description                      |
+===========================+==============+==================================+
| ``add_pf_name()``         | str          | Filter Incident on name.         |
+---------------------------+--------------+----------------------------------+
| ``add_pf_date_added()``   | str          | Filter Incident on date added.   |
+---------------------------+--------------+----------------------------------+

Incidents Retrieve Filter Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    incidents = tc.incidents()
    owner = 'Example Community'

    try:
        filter1 = incidents.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        incidents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for incident in incidents:
        print(incident.id)
        print(incident.name)
        print(incident.date_added)
        print(incident.weblink)
        print(incident.event_date)
            

This example will demonstrate how to retrieve Incidents while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Incidents in the **Example Community** Owner that has a Tag
of ***EXAMPLE***.

Note: The ``filter1`` object contains a ``filters`` property that
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more on using filters see the `Advanced Filter
Tutorial </python/advanced/filtering/>`__.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                              |
+==============================================+==========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``incidents = tc.incidents()``               | Instantiate an Incidents container object.                                               |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1 = incidents.add_filter()``         | Add a filter object to the Incidents container object (support multiple filter objects). |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``               | Add API filter to retrieve Incidents with the 'Example' tag.                             |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``incidents.retrieve()``                     | Trigger the API request and retrieve the Incidents intelligence data.                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``for incident in incidents:``               | Iterate over the Incidents container object generator.                                   |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``print(incident.id)``                       | Display the **'id'** property of the Incidents object.                                   |
+----------------------------------------------+------------------------------------------------------------------------------------------+

Resource Metadata

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations

Groups

See the `Group Associations Documentation <#associations>`__.

Indicators

See the `Indicator Associations
Documentation <#retrieving-indicator-associations>`__.

Victims

See the `Victim Associations
Documentation <#victim-associations-retrieve>`__.

Outputs

CSV

See the `CSV Output Documentation <#csv>`__.

JSON

See the `JSON Output Documentation <#json>`__.

Key Value

See the `Key Value Output Documentation <#key-value>`__.

Indicators Retrieve
-------------------

This section explains how to work with ThreatConnect Indicator
Resources.

Supported API Filters

API filters use the API filtering feature to limit the result set
returned from the API.

+----------------------------+---------------+--------------------------------------------------+
| Filter                     | Value Type    | Description                                      |
+============================+===============+==================================================+
| ``add_adversary_id()``     | int           | Filter Indicator on associated Adversary ID.     |
+----------------------------+---------------+--------------------------------------------------+
| ``add_document_id()``      | int           | Filter Indicator on associated Document ID.      |
+----------------------------+---------------+--------------------------------------------------+
| ``add_email_id()``         | int           | Filter Indicator on associated Email ID.         |
+----------------------------+---------------+--------------------------------------------------+
| ``add_incident_id()``      | int           | Filter Indicator on associated Incident ID.      |
+----------------------------+---------------+--------------------------------------------------+
| ``add_indicator()``        | str           | Filter Indicator by Indicator value.             |
+----------------------------+---------------+--------------------------------------------------+
| ``add_owner()``            | list or str   | Filter Indicator on associated Owner.            |
+----------------------------+---------------+--------------------------------------------------+
| ``add_security_label()``   | str           | Filter Indicator on associated Security Label.   |
+----------------------------+---------------+--------------------------------------------------+
| ``add_signature_id()``     | int           | Filter Indicator on associated Signature ID.     |
+----------------------------+---------------+--------------------------------------------------+
| ``add_tag()``              | str           | Filter Indicator on applied Tag.                 |
+----------------------------+---------------+--------------------------------------------------+
| ``add_threat_id()``        | int           | Filter Indicator on associated Threat ID.        |
+----------------------------+---------------+--------------------------------------------------+
| ``add_victim_id()``        | int           | Filter Indicator on associated Victim ID.        |
+----------------------------+---------------+--------------------------------------------------+

Supported Post Filters

Post filters are applied on the results returned by the API request.

+---------------------------------------+------------+------------------------------------------------+
| Filter                                | Value Type | Description                                    |
+=======================================+============+================================================+
| ``add_pf_attribute()``                | str        | Filter Indicators on Attribute type.           |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_confidence()``               | int        | Filter Indicators on Confidence value.         |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_date_added()``               | str        | Filter Indicators on date added.               |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_last_modified()``            | str        | Filter Indicators on last modified date.       |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_rating()``                   | str        | Filter Indicators on Rating.                   |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_tag()``                      | str        | Filter Indicators on Tag.                      |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_threat_assess_confidence()`` | int        | Filter Indicators on Threat Assess Confidence. |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_threat_assess_rating()``     | str        | Filter Indicators on Threat Assess Rating.     |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_type()``                     | str        | Filter Indicators on Indicator type.           |
+---------------------------------------+------------+------------------------------------------------+

Indicators Retrieve Filter Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # indicator object
    indicators = tc.indicators()
    owner = 'Example Community'
     
    # Add API/Post Filters
    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print(e)
        sys.exit(1)

    # Retrieve Indicators and Apply Filters
    try:
        indicators.retrieve()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    # Iterate Through Results
    for indicator in indicators:
        if isinstance(indicator.indicator, dict):
            for indicator_type, indicator_value in indicator.indicator.items():
                print('{0}: {1}'.format(indicator_type, indicator_value))
        else:
            print(indicator.indicator)
        print(indicator.id)
        print(indicator.owner_name)
        print(indicator.date_added)
        print(indicator.last_modified)
        print(indicator.rating)
        print(indicator.confidence)
        print(indicator.threat_assess_rating)
        print(indicator.threat_assess_confidence)
        print(indicator.source)
        print(indicator.description)
        print(indicator.dns_active)
        print(indicator.weblink)

This example will demonstrate how to retrieve Indicators while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Indicators in the **Example Community** Owner that has a Tag
of ***EXAMPLE***.

Note: The ``filter1`` object contains a ``filters`` property that
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more on using filters see the `Advanced Filter
Tutorial <#filtering>`__.

Code Highlights

+----------------------------------------+-------------------------------------------------------------------------------------------+
| Snippet                                | Description                                                                               |
+========================================+===========================================================================================+
| ``tc = ThreatConnect(api_access_id,...`` | Instantiate the ThreatConnect object.                                                     |
+----------------------------------------+-------------------------------------------------------------------------------------------+
| ``indicators = tc.indicators()``         | Instantiate an Indicators container object.                                               |
+----------------------------------------+-------------------------------------------------------------------------------------------+
| ``filter1 = indicator.add_filter()``     | Add a filter object to the Indicators container object (support multiple filter objects). |
+----------------------------------------+-------------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``           | Add API filter to retrieve Indicators with the 'Example' tag.                             |
+----------------------------------------+-------------------------------------------------------------------------------------------+
| ``indicator.retrieve()``                 | Trigger the API request and retrieve the Indicators intelligence data.                    |
+----------------------------------------+-------------------------------------------------------------------------------------------+
| ``for indicator in indicators:``         | Iterate over the Indicators container object generator.                                   |
+----------------------------------------+-------------------------------------------------------------------------------------------+
| ``print(indicator.indicator)``           | Display the **'indicator'** property of the Indicator object.                             |
+----------------------------------------+-------------------------------------------------------------------------------------------+

Loading Attributes Example
~~~~~~~~~~~~~~~~~~~~~~~~~~

Example Python SDK iterating through the ``indicators`` container
provides ``indicator`` objects

.. code:: python

     
        indicator.load_attributes()
        for attribute in indicator.attributes:
            print(attribute.type)
            print(attribute.value)
            print(attribute.date_added)
            print(attribute.last_modified)
            print(attribute.displayed)

The example continues from the previous `Filter
Example <#filter-example>`__. Iterating through the ``indicators``
container provides ``indicator`` objects. By calling the
``load_attribute()`` method of the Indicator object, an API request is
triggered and the resulting data is stored as Attribute objects in the
parent Indicator object. These Attribute objects can be retrieved by
iterating over the ``attributes`` property generator, which will return
the individual Attribute objects.

Code Highlights

+--------------------------------------------+----------------------------------------------------------------+
| Snippet                                    | Description                                                    |
+============================================+================================================================+
| ``indicator.load_attributes()``            | Trigger API call to load Attributes into the Indicator object. |
+--------------------------------------------+----------------------------------------------------------------+
| ``for attribute in indicator.attributes:`` | Iterate over the Attribute property object generator.          |
+--------------------------------------------+----------------------------------------------------------------+
| ``print(attribute.type)``                  | Display the **'type'** property of the Attribute object.       |
+--------------------------------------------+----------------------------------------------------------------+

Loading Security Label Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example Python SDK loading the Indicator Security Label by calling the
``load_security_label()`` method of the Indicator object:

.. code:: python


        indicator.load_security_label()
        if indicator.security_label is not None:
            print(indicator.security_label.name)
            print(indicator.security_label.description)
            print(indicator.security_label.date_added)

The example continues from the previous `Loading Attributes
Example <#loading-attributes-example>`__. While still in the
``indicators`` loop, the Indicator Security Label can be loaded by
calling the ``load_security_label()`` method of the Indicator object. By
calling this method, another API request will be triggered and the
resulting data will be stored as a Security Label object in the
Indicator object. This object can then be directly accessed from the
``security_label`` property.

Code Highlights

+--------------------------------------------+------------------------------------------------------------------------+
| Snippet                                    | Description                                                            |
+============================================+========================================================================+
| ``indicator.load_security_label()``        | Trigger API call to load the Security Label into the Indicator object. |
+--------------------------------------------+------------------------------------------------------------------------+
| ``if indicator.security_label is not ...`` | Ensure the object has been loaded before displaying properties.        |
+--------------------------------------------+------------------------------------------------------------------------+
| ``print(indicator.security_label.name)``   | Display the **'name'** property of the Security Label object.          |
+--------------------------------------------+------------------------------------------------------------------------+

Loading Tags Example
~~~~~~~~~~~~~~~~~~~~

Example of Python SDK loading the Indicator Tags by calling the
``load_tags()`` method of the Indicator object:

.. code:: python

        indicator.load_tags()
        for tag in indicator.tags:
            print(tag.name)
            print(tag.weblink)

The example continues from the previous `Loading Security Label
Example <#loading-security-label-example>`__. While still in the
``indicators`` loop, the Indicator Tags can be loaded by calling the
``load_tags()`` method of the Indicator object. By calling this method,
another API request will be triggered and the resulting data will be
stored as a Tag object in the Indicator object. This object can then be
directly accessed from the ``tags`` property.

Code Highlights

+--------------------------------+----------------------------------------------------------+
| Snippet                        | Description                                              |
+================================+==========================================================+
| ``indicator.load_tags()``      | Trigger API call to load Tags into the Indicator object. |
+--------------------------------+----------------------------------------------------------+
| ``for tag in indicator.tags:`` | Iterate over the Attribute property object generator.    |
+--------------------------------+----------------------------------------------------------+
| ``print(tag.name)``            | Display the **'name'** property of the Attribute object. |
+--------------------------------+----------------------------------------------------------+

Group Associations
~~~~~~~~~~~~~~~~~~

Example of Python SDK iterating through all Groups associated with this
Indicator:

.. code:: python

        for g_association in indicator.group_associations:
            print(g_association.id)
            print(g_association.name)
            if hasattr(g_association, 'type'):
                print(g_association.type)
            print(g_association.owner_name)
            print(g_association.date_added)
            print(g_association.weblink)

Iterate through all Groups associated with this Indicator. These Groups
are pulled directly from the API and are not stored in the Indicator
object.

Code Highlights

+---------------------------------------------+-------------------------------------------------------------------------+
| Snippet                                     | Description                                                             |
+=============================================+=========================================================================+
| ``for g_associations in indicator.grou...`` | Trigger API call to retrieve all Groups associated with this Indicator. |
+---------------------------------------------+-------------------------------------------------------------------------+
| ``print(g_association.id)``                 | Display the **'id'** property of the associated Group object.           |
+---------------------------------------------+-------------------------------------------------------------------------+


Indicator Associations
~~~~~~~~~~~~~~~~~~~~~~

Example Python SDK iterating through all Indicators associated with an
Indicator:

.. code:: python

        for i_association in indicator.indicator_associations:
            print(i_association.id)
            print(i_association.indicator)
            print(i_association.type)
            print(i_association.description)
            print(i_association.owner_name)
            print(i_association.rating)
            print(i_association.confidence)
            print(i_association.date_added)
            print(i_association.last_modified)
            print(i_association.weblink)

Iterate through all Indicators associated with this Indicator. These
Indicators are pulled directly from the API and are not stored in the
Indicator object.

Code Highlights

+--------------------------------------------+-----------------------------------------------------------------------------+
| Snippet                                    | Description                                                                 |
+============================================+=============================================================================+
| ``for i_association in indicator.ind_...`` | Trigger API call to retrieve all Indicators associated with this Indicator. |
+--------------------------------------------+-----------------------------------------------------------------------------+
| ``print(i_association.id)``                | Display the **'id'** property of the associated Indicator object.           |
+--------------------------------------------+-----------------------------------------------------------------------------+

Victim Associations
~~~~~~~~~~~~~~~~~~~

Example Python SDK iterating through all Victims associated with this
Indicator:

.. code:: python


        for v_associations in indicator.victim_associations:
            print(v_associations.id)
            print(v_associations.name)
            print(v_associations.description)
            print(v_associations.owner_name)
            print(v_associations.nationality)
            print(v_associations.org)
            print(v_associations.suborg)
            print(v_associations.work_location)
            print(v_associations.weblink)

Iterate through all Victims associated with this Indicator. These Groups
are pulled directly from the API and are not stored in the Indicator
object.

Code Highlights

+--------------------------------------------+--------------------------------------------------------------------------+
| Snippet                                    | Description                                                              |
+============================================+==========================================================================+
| ``for v_associations in indicator.vic_..`` | Trigger API call to retrieve all Victims associated with this Indicator. |
+--------------------------------------------+--------------------------------------------------------------------------+
| ``print(v_association.id)``                | Display the **'id'** property of the associated Victim object.           |
+--------------------------------------------+--------------------------------------------------------------------------+

DNS Resolution
~~~~~~~~~~~~~~

Example Python SDK DNS Resolution:

.. code:: python


    indicator.load_dns_resolutions()
    for dns in indicator.dns_resolutions:
        print(dns.ip)
        print(dns.owner_name)
        print(dns.resolution_date)
        print(dns.weblink)

DNS Resolution is only supported for the Host Indicator Type.

Code Highlights

+-------------------------------------------+---------------------------------------------------------------------+
| Snippet                                   | Description                                                         |
+===========================================+=====================================================================+
| ``indicator.load_dns_resolutions()``      | Trigger API call to load DNS Resolutions into the Indicator object. |
+-------------------------------------------+---------------------------------------------------------------------+
| ``for dns in indicator.dns_resolutions:`` | Iterate over the DNS Resolutions property object generator.         |
+-------------------------------------------+---------------------------------------------------------------------+
| ``print(dns.ip)``                         | Display the **'ip'** property of the Attribute object.              |
+-------------------------------------------+---------------------------------------------------------------------+

Output Formats

CSV

See the `CSV Output Documentation <#csv>`__.

JSON

See the `JSON Output Documentation <#json>`__.

Key Value

See the `Key Value Output Documentation <#key-value>`__.

Signatures Retrieve
-------------------

This section explains how to work with ThreatConnect Signature
Resources.

Supported API Filters

API filters use the API filtering feature to limit the result set
returned from the API.

+----------------------------+---------------+--------------------------------------------------+
| Filter                     | Value Type    | Description                                      |
+============================+===============+==================================================+
| ``add_id()``               | int           | Filter Signature by ID.                          |
+----------------------------+---------------+--------------------------------------------------+
| ``add_document_id()``      | int           | Filter Signature on associated Document ID.      |
+----------------------------+---------------+--------------------------------------------------+
| ``add_email_id()``         | int           | Filter Signature on associated Email ID.         |
+----------------------------+---------------+--------------------------------------------------+
| ``add_incident_id()``      | int           | Filter Signature on associated Incident ID.      |
+----------------------------+---------------+--------------------------------------------------+
| ``add_indicator()``        | str           | Filter Signature on associated Indicator.        |
+----------------------------+---------------+--------------------------------------------------+
| ``add_owner()``            | list or str   | Filter Signature on associated Owner.            |
+----------------------------+---------------+--------------------------------------------------+
| ``add_security_label()``   | str           | Filter Signature on associated Security Label.   |
+----------------------------+---------------+--------------------------------------------------+
| ``add_signature_id()``     | int           | Filter Signature on associated Signature ID.     |
+----------------------------+---------------+--------------------------------------------------+
| ``add_tag()``              | str           | Filter Signature on applied Tag.                 |
+----------------------------+---------------+--------------------------------------------------+
| ``add_threat_id()``        | int           | Filter Signature on associated Threat ID.        |
+----------------------------+---------------+--------------------------------------------------+
| ``add_victim_id()``        | int           | Filter Signature on associated Victim ID.        |
+----------------------------+---------------+--------------------------------------------------+

Supported Post Filters

Post filters are applied on the results returned by the API request.

+---------------------------+--------------+-----------------------------------+
| Filter                    | Value Type   | Description                       |
+===========================+==============+===================================+
| ``add_pf_name()``         | str          | Filter Signature on name.         |
+---------------------------+--------------+-----------------------------------+
| ``add_pf_date_added()``   | str          | Filter Signature on date added.   |
+---------------------------+--------------+-----------------------------------+

Signatures Retrieve Filter Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    signatures = tc.signatures()
    owner = 'Example Community'

    try:
        filter1 = signatures.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        signatures.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for signature in signatures:
        print(signature.id)
        print(signature.name)
        print(signature.date_added)
        print(signature.weblink)

This example will demonstrate how to retrieve Signatures while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Signatures in the **Example Community** Owner that has a Tag
of ***EXAMPLE***.

Note: The ``filter1`` object contains a ``filters`` property which
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more on using filters, see the `Advanced Filter
Tutorial <#filtering>`__.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                               |
+==============================================+===========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                     |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``signatures = tc.signatures()``             | Instantiate an Signatures container object.                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``filter1 = signatures.add_filter()``        | Add a filter object to the Signatures container object (support multiple filter objects). |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``               | Add API filter to retrieve Signatures with the 'Example' tag.                             |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``signatures.retrieve()``                    | Trigger the API request and retrieve the Signatures intelligence data.                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``for signature in signatures:``             | Iterate over the Signatures container object generator.                                   |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``print(signature.id)``                      | Display the **'id'** property of the Signature object.                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------+

Signature Download
~~~~~~~~~~~~~~~~~~

Example Python SDK downloading the Signature contents for the Signature
Resource:

.. code:: python


        signature.download()
        if signature.contents is not None:
            print(signature.contents)

Download the Signature contents for the Signature Resource.

Code Highlights

+----------------------------------------+---------------------------------------------------------------+
| Snippet                                | Description                                                   |
+========================================+===============================================================+
| ``signature.download()``               | Trigger API request to download the Signature contents.       |
+----------------------------------------+---------------------------------------------------------------+
| ``if signature.contents is not None:`` | Validate that the Signature has downloaded before displaying. |
+----------------------------------------+---------------------------------------------------------------+
| ``print(signature.contents)``          | Display the contents of the Signature.                        |
+----------------------------------------+---------------------------------------------------------------+

Resource Metadata

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations

Groups

See the `Group Associations Documentation <#associations>`__.

Indicators

See the `Indicator Associations
Documentation <#retrieving-indicator-associations>`__.

Victims

See the `Victim Associations
Documentation <#victim-associations-retrieve>`__.

Outputs

CSV

See the `CSV Output Documentation <#csv>`__.

JSON

See the `JSON Output Documentation <#json>`__.

Key Value

See the `Key Value Output Documentation <#key-value>`__.

Tasks Retrieve
--------------

This section explains how to work with ThreatConnect Task Resources.

Supported API Filters
---------------------

API filters use the API filtering feature to limit the result set
returned from the API.

+--------------------------+---------------+---------------------------------------------+
| Filter                   | Value Type    | Description                                 |
+==========================+===============+=============================================+
| add\_id()                | int           | Filter Task by ID.                          |
+--------------------------+---------------+---------------------------------------------+
| add\_document\_id()      | int           | Filter Task on associated Document ID.      |
+--------------------------+---------------+---------------------------------------------+
| add\_email\_id()         | int           | Filter Task on associated Email ID.         |
+--------------------------+---------------+---------------------------------------------+
| add\_incident\_id()      | int           | Filter Task on associated Incident ID.      |
+--------------------------+---------------+---------------------------------------------+
| add\_indicator()         | int           | Filter Task on associated Indicator.        |
+--------------------------+---------------+---------------------------------------------+
| add\_owner()             | list or str   | Filter Task on associated Owner.            |
+--------------------------+---------------+---------------------------------------------+
| add\_security\_label()   | str           | Filter Task on associated Security Label.   |
+--------------------------+---------------+---------------------------------------------+
| add\_signature\_id()     | int           | Filter Task on associated Signature ID.     |
+--------------------------+---------------+---------------------------------------------+
| add\_tag()               | str           | Filter Task on applied Tag.                 |
+--------------------------+---------------+---------------------------------------------+
| add\_threat\_id()        | int           | Filter Task on associated Task ID.          |
+--------------------------+---------------+---------------------------------------------+
| add\_victim\_id()        | int           | Filter Task on associated Victim ID.        |
+--------------------------+---------------+---------------------------------------------+

Supported Post Filters
----------------------

Post filters are applied on the results returned by the API request.

+--------------------------+--------------+------------------------------+
| Filter                   | Value Type   | Description                  |
+==========================+==============+==============================+
| add\_pf\_name()          | str          | Filter Task on name.         |
+--------------------------+--------------+------------------------------+
| add\_pf\_date\_added()   | str          | Filter Task on date added.   |
+--------------------------+--------------+------------------------------+

Filter Example
--------------

This example will demonstrate how to retrieve Tasks while applying
filters. In this example, one filters will be added for a Tag. The
result set returned from this example will contain any Tasks that has a
Tag of ***EXAMPLE***.

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    tasks = tc.tasks()

    try:
        filter1 = tasks.add_filter()
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        tasks.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for task in tasks:
        print(task.id)
        print(task.name)
        print(task.date_added)
        print(task.weblink)

Note: The ``filter1`` object contains a ``filters`` property that
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more information on using filters, see the `Advanced Filter
Tutorial </python/advanced/filtering/>`__.

-  Code Highlights\*

+----------------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                          |
+==============================================+======================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``Tasks = tc.Tasks()``                       | Instantiate a Tasks container object.                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``filter1 = Tasks.add_filter()``             | Add a filter object to the Tasks container object (support multiple filter objects). |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``               | Add an API filter to be applied to the API request.                                  |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``Tasks.retrieve()``                         | Trigger the API request and retrieve the Tasks-intelligence data.                    |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``for task in Tasks:``                       | Iterate over the Tasks container object generator.                                   |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``print(task.id)``                           | Display the **id** property of the Task object.                                      |
+----------------------------------------------+--------------------------------------------------------------------------------------+

Resource Metadata

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations

Groups

See the `Group Associations Documentation <#associations>`__.

Indicators

See the `Indicator Associations
Documentation <#retrieving-indicator-associations>`__.

Victims

See the `Victim Associations
Documentation <#victim-associations-retrieve>`__.

Outputs

CSV

See the `CSV Output Documentation <#csv>`__.

JSON

See the `JSON Output Documentation <#json>`__.

Key Value

See the `Key Value Output Documentation <#key-value>`__.

Threats Retrieve
----------------

This section explains how to work with ThreatConnect Threat Resources.

Supported API Filters

API filters use the API filtering feature to limit the result set
returned from the API.

+----------------------------+---------------+-----------------------------------------------+
| Filter                     | Value Type    | Description                                   |
+============================+===============+===============================================+
| ``add_id()``               | int           | Filter Threat by ID.                          |
+----------------------------+---------------+-----------------------------------------------+
| ``add_document_id()``      | int           | Filter Threat on associated Document ID.      |
+----------------------------+---------------+-----------------------------------------------+
| ``add_email_id()``         | int           | Filter Threat on associated Email ID.         |
+----------------------------+---------------+-----------------------------------------------+
| ``add_incident_id()``      | int           | Filter Threat on associated Incident ID.      |
+----------------------------+---------------+-----------------------------------------------+
| ``add_indicator()``        | str           | Filter Threat on associated Indicator.        |
+----------------------------+---------------+-----------------------------------------------+
| ``add_owner()``            | list or str   | Filter Threat on associated Owner.            |
+----------------------------+---------------+-----------------------------------------------+
| ``add_security_label()``   | str           | Filter Threat on associated Security Label.   |
+----------------------------+---------------+-----------------------------------------------+
| ``add_signature_id()``     | int           | Filter Threat on associated Signature ID.     |
+----------------------------+---------------+-----------------------------------------------+
| ``add_tag()``              | str           | Filter Threat on applied Tag.                 |
+----------------------------+---------------+-----------------------------------------------+
| ``add_threat_id()``        | int           | Filter Threat on associated Threat ID.        |
+----------------------------+---------------+-----------------------------------------------+
| ``add_victim_id()``        | int           | Filter Threat on associated Victim ID.        |
+----------------------------+---------------+-----------------------------------------------+

Supported Post Filters

Post filters are applied on the results returned by the API request.

+---------------------------+--------------+--------------------------------+
| Filter                    | Value Type   | Description                    |
+===========================+==============+================================+
| ``add_pf_name()``         | str          | Filter Threat on name.         |
+---------------------------+--------------+--------------------------------+
| ``add_pf_date_added()``   | str          | Filter Threat on date added.   |
+---------------------------+--------------+--------------------------------+

Threats Retrieve Filter Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    threats = tc.threats()
    owner = 'Example Community'

    try:
        filter1 = threats.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        threats.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for threat in threats:
        print(threat.id)
        print(threat.name)
        print(threat.date_added)
        print(threat.weblink)

This example will demonstrate how to retrieve Threats while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Threats in the **Example Community** Owner that has a Tag of
***EXAMPLE***.

Note: The ``filter1`` object contains a ``filters`` property that
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more on using filters, see the `Advanced Filter
Tutorial </python/advanced/filtering/>`__.

Code Highlights

+----------------------------------------------+----------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                            |
+==============================================+========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                  |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``threats = tc.threats()``                   | Instantiate a Threats container object.                                                |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``filter1 = threats.add_filter()``           | Add a filter object to the Threats container object (support multiple filter objects). |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``               | Add API filter to retrieve Threats with the 'Example' tag.                             |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``threats.retrieve()``                       | Trigger the API request and retrieve the Threats intelligence data.                    |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``for threat in threats:``                   | Iterate over the Threats container object generator.                                   |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``print(threat.id)``                         | Display the **id** property of the Threat object.                                      |
+----------------------------------------------+----------------------------------------------------------------------------------------+

Victims Retrieve
----------------

This section explains how to work with ThreatConnect Victims Resources.

Supported API Filters

API filters use the API filtering feature to limit the result set
returned from the API.

+--------------------------+---------------+---------------------------------------------+
| Filter                   | Value Type    | Description                                 |
+==========================+===============+=============================================+
| ``add_id()``             | int           | Filter Victim by ID.                        |
+--------------------------+---------------+---------------------------------------------+
| ``add_adversary_id()``   | int           | Filter Victim on associated Adversary ID.   |
+--------------------------+---------------+---------------------------------------------+
| ``add_document_id()``    | int           | Filter Victim on associated Document ID.    |
+--------------------------+---------------+---------------------------------------------+
| ``add_email_id()``       | int           | Filter Victim on associated Email ID.       |
+--------------------------+---------------+---------------------------------------------+
| ``add_incident_id()``    | int           | Filter Victim on associated Incident ID.    |
+--------------------------+---------------+---------------------------------------------+
| ``add_indicator()``      | str           | Filter Victim on associated Indicator.      |
+--------------------------+---------------+---------------------------------------------+
| ``add_owner()``          | list or str   | Filter Victim on associated Owner.          |
+--------------------------+---------------+---------------------------------------------+
| ``add_signature_id()``   | int           | Filter Victim on associated Signature ID.   |
+--------------------------+---------------+---------------------------------------------+
| ``add_threat_id()``      | int           | Filter Victim on associated Threat ID.      |
+--------------------------+---------------+---------------------------------------------+

Supported Post Filters

Post filters are applied on the results returned by the API request.

+---------------------------+--------------+--------------------------------+
| Filter                    | Value Type   | Description                    |
+===========================+==============+================================+
| ``add_pf_name()``         | str          | Filter Victim on name.         |
+---------------------------+--------------+--------------------------------+
| ``add_pf_date_added()``   | str          | Filter Victim on date added.   |
+---------------------------+--------------+--------------------------------+

Victims Retrieve Filter Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    victims = tc.victims()
    owner = 'Example Community'

    try:
        filter1 = victims.add_filter()
        filter1.add_owner(owner)
        filter1.add_adversary_id(531)
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        victims.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)
        
    for victim in victims:
        print(obj.id)
        print(obj.name)
        print(obj.nationality)
        print(obj.org)
        print(obj.suborg)
        print(obj.work_location)
        print(obj.weblink)

This example will demonstrate how to retrieve Victims while applying
filters. In this example two filters will be added, one for the Owner
and another for an Adversary ID. The result set returned from this
example would contain any Victim in the "Example Community" Owner that
has associations with the Adversary having the supplied ID.

Note: The ``filter1`` object contains a ``filters`` property that
provides a list of supported filters for the resource type being
retrieved. To display this list, ``print(filter1.filters)`` can be used.
For more on using filters, see the `Advanced Filter
Tutorial <#filtering>`__.

Code Highlights

+----------------------------------------------+----------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                            |
+==============================================+========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                  |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``victims = tc.victims()``                   | Instantiate a Victims container object.                                                |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``filter1 = victims.add_filter()``           | Add a filter object to the Victims container object (support multiple filter objects). |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``filter1.add_adversary_id(531)``            | Add API filter to retrieve Victims associated with the given Adversary.                |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``victims.retrieve()``                       | Trigger the API request and retrieve the Victims intelligence data.                    |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``for victim in victims:``                   | Iterate over the Victims container object generator.                                   |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``print(victim.id)``                         | Display the **id** property of the Victim object.                                      |
+----------------------------------------------+----------------------------------------------------------------------------------------+

Load Victim Assets
~~~~~~~~~~~~~~~~~~

This Python SDK example will pull all Assets for the current Victim
Resource:

.. code:: python

        victim.load_assets()
        for asset in victim.assets:
            print(asset.id)
            print(asset.name)
            print(asset.type)
            print(asset.weblink)

Continuing from the `Filter Example <#filter-example>`__, the following
example will pull all Assets for the current Victim Resource.

Code Highlights

+---------------------------------+-----------------------------------------------------------+
| Snippet                         | Description                                               |
+=================================+===========================================================+
| ``victim.load_assets()``        | Trigger API call to load Assets into the Resource object. |
+---------------------------------+-----------------------------------------------------------+
| ``for asset in victim.assets:`` | Iterate over the Assets object generator.                 |
+---------------------------------+-----------------------------------------------------------+
| ``print(asset.id)``             | Display the **id** property of the Asset object.          |
+---------------------------------+-----------------------------------------------------------+

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations
------------

Python SDK example demonstrating how to use the ``Group_Associations``
method on an Adversary Resource:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()

    try:
        resources.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for resource in resources:
        print(resource.id)
        print(resource.name)
        print(resource.date_added)
        print(resource.weblink)

        for g_associations in resource.group_associations:
            print(g_associations.id)
            print(g_associations.name)
            print(g_associations.type)
            print(g_associations.owner_name)
            print(g_associations.date_added)
            print(g_associations.weblink)

Group Associations

The Python SDK provides the ``group_associations`` method to retrieve
Group Associations for a Resource. Group Associations are supported on
Indicators as well as `Group <#groups-commit>`__ Resources (e.g.,
`Adversaries <#resources-commit>`__, `Documents <#documents-commit>`__,
`Emails <#emails-commit>`__, `Incidents <#incidents-commit>`__,
`Signatures <#signatures-commit>`__, and `Threats <#threats-commit>`__)
and `Indicators <#indicators-commit>`__. An example of the `Retrieving
Group Associations <#associations>`__ method, as well as an explanation
of the code, is provided in the following section.

Resource Groups of the same type cannot be directly associated (e.g.,
Adversaries cannot be associated with other Adversaries).

Retrieving Group Associations

The following example demonstrates how to use the ``Group_Associations``
method on an Adversary Resource. For other Resource Groups and
Indicators, the same method should be used. These Associations are
pulled directly from the API and are not stored in the Resource object.

Group Associations Properties

+-----------------+--------+
| Property Name   | Type   |
+=================+========+
| id              | int    |
+-----------------+--------+
| name            | str    |
+-----------------+--------+
| type            | str    |
+-----------------+--------+
| owner\_name     | str    |
+-----------------+--------+
| date\_added     | str    |
+-----------------+--------+
| weblink         | str    |
+-----------------+--------+

For more information on the properties of an Attribute, read the
ThreatConnect API documentation.

When the ``Group_Associations`` method is called, an API request is
invoked immediately.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------------+
| Snippet                                      | Description                                                               |
+==============================================+===========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                     |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate an Resources container object.                                |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``resources.retrieve()``                     | Trigger API calls to retrieve the Resources.                              |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``for resource in resources:``               | Iterate over the Resources container object generator.                    |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``print(resource.id)``                       | Display the **id** property of the Resource object.                       |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``for g_associations in resource.group_...`` | Trigger an API call to retrieve all Groups associated with this Resource. |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``print(g_association.id)``                  | Display the **id** property of the associated Group object.               |
+----------------------------------------------+---------------------------------------------------------------------------+

Indicator Associations
----------------------

Python SDK example demonstrating how to use the
``indicator_associations`` method on an Adversary Resource:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()

    try:
        resources.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for resource in resources:
        print(resource.id)
        print(resource.name)
        print(resource.date_added)
        print(resource.weblink)

        for associations in resource.indicator_associations:
            print(associations.id)
            print(associations.indicator)
            print(associations.type)
            print(associations.description)
            print(associations.owner_name)
            print(associations.rating)
            print(associations.confidence)
            print(associations.date_added)
            print(associations.last_modified)
            print(associations.weblink)

The Python SDK provides the ``indicator_associations`` method to
retrieve Indicators Associations for a resource. Indicator Associations
are supported on Indicators as well as `Group <#groups-commit>`__
Resources (e.g., `Adversaries <#resources-commit>`__,
`Documents <#documents-commit>`__, `Emails <#emails-commit>`__,
`Incidents <#incidents-commit>`__, `Signatures <#signatures-commit>`__,
and `Threats <#threats-commit>`__) and
`Indicators <#indicators-commit>`__. An example of the `Retrieving
Indicator Associations <#retrieving-indicator-associations>`__ method,
as well as explanations of the code, is provided in the following
section.

Retrieving Indicator Associations

The following example demonstrates how to use the
``indicator_associations`` method on an Adversary Resource. For other
Resource Groups and Indicators, the same method should be used. These
Associations are pulled directly from the API and are not stored in the
Resource object.

Indicator Associations Properties

+------------------+--------+
| Property Name    | Type   |
+==================+========+
| id               | int    |
+------------------+--------+
| indicator        | str    |
+------------------+--------+
| type             | str    |
+------------------+--------+
| description      | str    |
+------------------+--------+
| owner\_name      | str    |
+------------------+--------+
| rating           | str    |
+------------------+--------+
| confidence       | str    |
+------------------+--------+
| date\_added      | str    |
+------------------+--------+
| last\_modified   | str    |
+------------------+--------+
| weblink          | str    |
+------------------+--------+

For more information on the properties of an Attribute, read the
ThreatConnect API documentation.

When the ``indicator_associations`` method is called, an API request is
invoked immediately.

Code Highlights

+----------------------------------------------+----------------------------------------------------------------------------+
| Snippet                                      | Description                                                                |
+==============================================+============================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                      |
+----------------------------------------------+----------------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate an Resources container object.                                 |
+----------------------------------------------+----------------------------------------------------------------------------+
| ``resources.retrieve()``                     | Trigger API calls to retrieve the Resources.                               |
+----------------------------------------------+----------------------------------------------------------------------------+
| ``for resource in resources:``               | Iterate over the Resources container object generator.                     |
+----------------------------------------------+----------------------------------------------------------------------------+
| ``print(resource.id)``                       | Display the **id** property of the Resource object.                        |
+----------------------------------------------+----------------------------------------------------------------------------+
| ``for associations in resource.indicat_...`` | Trigger API call to retrieve all Indicators associated with this Resource. |
+----------------------------------------------+----------------------------------------------------------------------------+
| ``print(association.id)``                    | Display the **'id'** property of the associated Indicator object.          |
+----------------------------------------------+----------------------------------------------------------------------------+

Victim Associations Retrieve
----------------------------

Python SDK example demonstrating how to use the ``victim_associations``
method on an Adversary Resource:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()

    try:
        resources.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for resource in resources:
        print(resource.id)
        print(resource.name)
        print(resource.date_added)
        print(resource.weblink)

        for associations in resource.victim_associations:
            print(associations.id)
            print(associations.name)
            print(associations.description)
            print(associations.owner_name)
            print(associations.nationality)
            print(associations.org)
            print(associations.suborg)
            print(associations.work_location)
            print(associations.weblink)

The Python SDK provides the ``victim_associations`` method to retrieve
Victim Associations for a resource. Victim Associations are supported on
all `Group <#groups_commit>`__ Resources (e.g.,
`Adversaries <#resources-commit>`__, `Documents <#documents-commit>`__,
`Emails <#emails-commit>`__, `Incidents <#incidents-commit>`__,
`Signatures <#signatures-commit>`__, and `Threats <#threats-commit>`__)
and `Indicators <#indicators-commit>`__. An example of the `Retrieving
Victim Associations <#victim-associations-retrieve>`__ method, as well
as explanations of the code, is provided in the following section.

The following example demonstrates how to use the
``victim_associations`` method on an Adversary Resource. For other
Resource Groups and Indicators, the same method should be used. These
associations are pulled directly from the API and are not stored in the
Resource object.

Victim Associations Properties

+-----------------+--------+
| Property Name   | Type   |
+=================+========+
| id              | int    |
+-----------------+--------+
| name            | str    |
+-----------------+--------+
| date\_added     | str    |
+-----------------+--------+
| weblink         | str    |
+-----------------+--------+

For more information on the properties of an Attribute, read the
ThreatConnect API documentation.

When the ``victim_associations`` method is called, an API request is
invoked immediately.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------------+
| Snippet                                      | Description                                                             |
+==============================================+=========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                   |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate an Resources container object.                              |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``resources.retrieve()``                     | Trigger API calls to retrieve the Resources.                            |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``for resource in resources:``               | Iterate over the Resources container object generator.                  |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``print(resource.id)``                       | Display the **id** property of the Resource object.                     |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``for associations in resource.victim_...``  | Trigger API call to retrieve all Victims associated with this Resource. |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``print(v_association.id)``                  | Display the **id** property of the associated Victim object.            |
+----------------------------------------------+-------------------------------------------------------------------------+

Loading Attributes
------------------

Python SDK example on how to Load Attributes on an Adversary Resource:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()

    try:
        resources.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for resource in resources:
        print(resource.id)
        print(resource.name)
        print(resource.date_added)
        print(resource.weblink)

        resource.load_attributes()
        for attribute in resource.attributes:
            print(attribute.type)
            print(attribute.value)
            print(attribute.date_added)
            print(attribute.last_modified)
            print(attribute.displayed)

The Python SDK provides the ``load_attributes()`` method to load a
Resources Attribute. Attributes are supported on all
`Group <#groups-commit>`__ Resources (e.g.,
`Adversaries <#resources-commit>`__, `Documents <#documents-commit>`__,
`Emails <#emails-commit>`__, `Incidents <#incidents-commit>`__,
`Signatures <#signatures-commit>`__, and `Threats <#threats-commit>`__)
and `Indicators <#indicators-commit>`__.

The following example demonstrates how to `Load
Attributes <#loading-attributes>`__ on an Adversary Resource. For other
Resource Groups and Indicators, the same method should be used.

Attribute Properties

+------------------+--------+
| Property Name    | Type   |
+==================+========+
| type             | str    |
+------------------+--------+
| value            | str    |
+------------------+--------+
| date\_added      | str    |
+------------------+--------+
| last\_modified   | str    |
+------------------+--------+
| displayed        | bool   |
+------------------+--------+

For more information on the properties of an Attribute read, the
ThreatConnect API documentation.

Code Highlights

+----------------------------------------------+-----------------------------------------------------------------------+
| Snippet                                      | Description                                                           |
+==============================================+=======================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate a Resources container object.                             |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resources.retrieve()``                     | Trigger the API request and retrieve the Resources intelligence data. |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``for resource in resources:``               | Iterate over the Resources container object generator.                |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``print(resource.id)``                       | Display the **id** property of the Resource object.                   |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resource.load_attributes()``               | Trigger API call to load Attributes into the Resource object.         |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``for attribute in resource.attributes:``    | Iterate over the Attribute property object generator.                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``print(attribute.type)``                    | Display the **'type'** property of the Attribute object.              |
+----------------------------------------------+-----------------------------------------------------------------------+

Loading a Security Label
------------------------

Python SDK example demonstrating how to **Load a Security Label** on an
Adversary Resource:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()

    try:
        resources.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for resource in resources:
        print(resource.id)
        print(resource.name)
        print(resource.date_added)
        print(resource.weblink)

        resource.load_security_label()
        if resource.security_label is not None:
            print(resource.security_label.name)
            print(resource.security_label.description)
            print(resource.security_label.date_added)

The Python SDK provides the ``load_security_label()`` method to load the
Security Label for a resource. Attributes are supported on all
`Group <#groups-commit>`__ Resources (e.g.,
`Adversaries <#resources-commit>`__, `Documents <#documents-commit>`__,
`Emails <#emails-commit>`__, `Incidents <#incidents-commit>`__,
`Signatures <#signatures-commit>`__, and `Threats <#threats-commit>`__)
and `Indicators <#indicators-commit>`__. An example of the `Loading
Security Label <#loading-security-label>`__ method, as well as
explanations of the code, is provided in the following section.

The following example demonstrates how to **Load a Security Label** on
an Adversary Resource. For other Resource Groups and Indicator,s the
same method should be used.

Attribute Properties

+-----------------+--------+
| Property Name   | Type   |
+=================+========+
| name            | str    |
+-----------------+--------+
| description     | str    |
+-----------------+--------+
| date\_added     | str    |
+-----------------+--------+

For more information on the properties of a Security Label, read the
ThreatConnect API documentation.

Code Highlights

+----------------------------------------------+-----------------------------------------------------------------------+
| Snippet                                      | Description                                                           |
+==============================================+=======================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate an Resources container object.                            |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resources.retrieve()``                     | Trigger the API request and retrieve the Resources intelligence data. |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``for resource in resources:``               | Iterate over the Resources container object generator.                |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``print(resource.id)``                       | Display the **id** property of the Resource object.                   |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resource.load_security_label()``           | Trigger API call to load the Security Label into the Resource object. |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``if resource.security_label is not None:``  | Ensure the object has been loaded before displaying properties.       |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``print(resource.security_label.name)``      | Display the **'name'** property of the Security Label object.         |
+----------------------------------------------+-----------------------------------------------------------------------+

Loading Tags
------------

Python SDK example demonstrating how to use the ``load_tags()`` method
on an Adversary Resource:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()

    try:
        resources.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for resource in resources:
        print(resource.id)
        print(resource.name)
        print(resource.date_added)
        print(resource.weblink)

        resource.load_tags()
        for tag in resource.tags:
            print(tag.name)
            print(tag.weblink)

The Python SDK provides the ``load_tags()`` method to load a Resources
Tag. Tags are supported on Indicators as well as Group Resources (e.g.,
Adversaries, Documents, Emails, Incidents, Signatures and Threats). An
example of the `Loading Tags <#loading-tags>`__ method, as well as
explanations of the code, is provided in the following section.

The following example demonstrates how to use the ``load_tags()`` method
on an Adversary Resource. For other Resource Groups and Indicators, the
same method should be used.

Tag Properties

+-----------------+--------+
| Property Name   | Type   |
+=================+========+
| name            | str    |
+-----------------+--------+
| weblink         | str    |
+-----------------+--------+

For more information on the properties of an Attribute, read the
ThreatConnect API documentation.

Code Highlights

+----------------------------------------------+---------------------------------------------------------+
| Snippet                                      | Description                                             |
+==============================================+=========================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                   |
+----------------------------------------------+---------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate an Resources container object.              |
+----------------------------------------------+---------------------------------------------------------+
| ``resources.retrieve()``                     | Trigger API calls to retrieve the Resources.            |
+----------------------------------------------+---------------------------------------------------------+
| ``for resource in resources:``               | Iterate over the Resources container object generator.  |
+----------------------------------------------+---------------------------------------------------------+
| ``print(resource.id)``                       | Display the **id** property of the Resource object.     |
+----------------------------------------------+---------------------------------------------------------+
| ``resource.load_tags()``                     | Trigger API call to load Tags into the Resource object. |
+----------------------------------------------+---------------------------------------------------------+
| ``for tag in resource.tags:``                | Iterate over the Tag property object generator.         |
+----------------------------------------------+---------------------------------------------------------+
| ``print(tag.name)``                          | Display the **'name'** property of the Tag object.      |
+----------------------------------------------+---------------------------------------------------------+

Python Commit
-------------

Example Python SDK creating an adversary resource in the ThreatConnect
platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    adversaries = tc.adversaries()
        
    owner = 'Example Community'
    adversary = adversaries.add('New Adversary', owner)
    adversary.add_attribute('Description', 'Description Example')
    adversary.add_tag('EXAMPLE')
    adversary.set_security_label('TLP Green')
    try:
        adversary.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

Adversaries Commit

The ThreatConnect platform supports
`adding <#add-an-adversary-resource>`__,
`deleting <#delete-an-adversary-resource>`__, and
`updating <#update-an-adversary-resource>`__ of threat-intelligence data
programmatically using the API. The Python SDK features an easy-to-use
interface to assist in rapid development of software to manage this
data.

Adding Adversary Resources

The example demonstrates how to create an Adversary Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``adversaries = tc.adversaries()``           | Instantiate an Adversaries container object.                     |
+----------------------------------------------+------------------------------------------------------------------+
| ``adversary = adversaries.add('New Adve...`` | Add a resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``adversary.add_attribute('Description'...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``adversary.add_tag('EXAMPLE')``             | Add a Tag to the Adversary.                                      |
+----------------------------------------------+------------------------------------------------------------------+
| ``adversary.set_security_label('TLP Gre...`` | Add a Security Label to the Adversary.                           |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Updating Adversary Resources
----------------------------

The example below demonstrates how to update an Adversary Resource in
the ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    adversaries = tc.adversaries()

    owner = 'Example Community'
    adversary = adversaries.add('Updated Adversary', owner)
    adversary.set_id(20)

    adversary.load_attributes()
    for attribute in adversary.attributes:
        if attribute.type == 'Description':
            adversary.delete_attribute(attribute.id)

    adversary.add_attribute('Description', 'Updated Description')

    adversary.load_tags()
    for tag in adversary.tags:
        adversary.delete_tag(tag.name)

    adversary.add_tag('EXAMPLE')

    try:
        adversary.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to update an Adversary Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------------+
| Snippet                                      | Description                                                               |
+==============================================+===========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                     |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversaries = tc.adversaries()``           | Instantiate an Adversaries container object.                              |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary = adversaries.add('Updated ...`` | Add a resource object setting the name and Owner.                         |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.set_id(20)``                     | Set the ID of the Adversary to the ***EXISTING*** Adversary ID to update. |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.load_attributes()``              | Load existing Attributes into the Adversary object.                       |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.delete_attribute(attribute.id)`` | Add a delete flag on the Attribute with type **Description**.             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.add_attribute('Description'...`` | Add an Attribute of type **Description** to the Resource.                 |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.load_tags()``                    | Load existing Tags into the Adversary object.                             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.delete_tag(tag.name)``           | Add a delete flag to all Tags.                                            |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.add_tag('EXAMPLE')``             | Add a Tag to the Resource.                                                |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.commit()``                       | Trigger API calls to write all added, deleted, or modified data.          |
+----------------------------------------------+---------------------------------------------------------------------------+

Deleting Adversary Resources
----------------------------

The example below demonstrates how to delete an Adversary Resource in
the ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    adversaries = tc.adversaries()

    adversary = adversaries.add('', owner)
    adversary.set_id(20)

    try:
        adversary.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

The example demonstrates how to delete an Adversary Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``delete()``
method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------------+
| Snippet                                      | Description                                                             |
+==============================================+=========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                   |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``adversaries = tc.adversaries()``           | Instantiate an Adversaries container object.                            |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``adversary = adversaries.add('', owner)``   | Add a resource object setting the name and Owner.                       |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``adversary.set_id(20)``                     | Set the ID of the Adversary to the **EXISTING** Adversary ID to delete. |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``adversary.delete()``                       | Trigger API calls to write all added, deleted, or modified data.        |
+----------------------------------------------+-------------------------------------------------------------------------+

Batch Commit
------------

Python SDK Batch Commit Code Sample:

.. code:: python


    dst_tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    #
    # ... populate 'indicators' list of dictionaries...
    #

    batch_job_ids = []
    batch_jobs = dst_tc.batch_jobs()
    batch_job = batch_jobs.add()

    batch_job.set_halt_on_error(False)             # If True, abort processing after first error
    batch_job.set_attribute_write_type('Replace')  # Replace attributes (can also be Append)
    batch_job.set_action('Create')                 # Create indicators (can also be Delete) 
    batch_job.set_owner(dst_owner)                 # Owner to write indicators to

    batch_job.upload(json.dumps(indicators))

    try:
        batch_job.commit()
        print("Created batchjob %s" % batch_job.id)
        batch_job_ids.append(batch_job.id)
    except RuntimeError as re:
        print("Encountered problem creating batchJob")
        traceback.print_exc(file=sys.stderr)

    finished_batches = []
    total_time = 0 
    while len(batch_job_ids) > 0:
        time.sleep(args.poll_time)
        total_time += args.poll_time
        print("polling (total wait time {0} minutes)...".format(int(total_time / 60)))
                     
        batch_jobs = dst_tc.batch_jobs()
        for batchId in batch_job_ids:
            filter = batch_jobs.add_filter()
            filter.add_id(batchId)
            batch_jobs.retrieve()

            for batch_job in batch_jobs:
                if batch_job.status == 'Completed':
                    finished_batches.append(batch_job)
                    batch_job_ids.remove(batchId)
                    print("Finished batch job {0}: succeeded: {1}, "
                          "failed: {2}, unprocessed: {3}".format(batchId, batch_job.success_count, batch_job.error_count, batch_job.unprocess_count))

    success_total = 0
    error_total = 0
    unprocess_total = 0
    for batch_job in finished_batches:
        if batch_job.unprocess_count:
            success_total += batch_job.success_count
        if batch_job.unprocess_count:
            unprocess_total += batch_job.unprocess_count
        if batch_job.unprocess_count:
            error_total += batch_job.error_count
            batch_job.download_errors()
            for error in batch_job.errors:
                print("Batch Job {0} errors: {1}".format(batch_job.id, batch_job.errors))
    print("All batch jobs completed, totals:  "
          "succeeded: {0}, failed: {1}, unprocessed: {2}".format(success_total, error_total, unprocess_total))
          

The ThreatConnect platform supports adding indicators in bulk using the
API. The Python SDK features an easy-to-use interface to assist in rapid
development of software to manage this data.

These API calls assume that indicator data is `formatted in JSON,
specifically a list of
dictionaries <#batch-indicator-input-file-format>`__

Adding Batch Resources
~~~~~~~~~~~~~~~~~~~~~~

The example below demonstrates how to use a Batch Resource in the
ThreatConnect platform. The Batch Resource has a few methods to support
batch configuration before uploading a batch Indicator file to the
platform. For more information on the purpose of each line of code, see
the **Code Highlights** section below.

Supported Functions and Properties

+--------------------------+-------------------------------+------------+-------------------------+
| Property Name            | Method                        | Required   | Allowable Values        |
+==========================+===============================+============+=========================+
| halt\_on\_error          | set\_halt\_on\_error          | True       | True, False             |
+--------------------------+-------------------------------+------------+-------------------------+
| attribute\_write\_type   | set\_attribute\_write\_type   | True       | Replace, Append         |
+--------------------------+-------------------------------+------------+-------------------------+
| action                   | set\_action                   | True       | Create, Delete          |
+--------------------------+-------------------------------+------------+-------------------------+
| owner                    | set\_owner                    | True       | Any Owner               |
+--------------------------+-------------------------------+------------+-------------------------+
| --                       | upload                        | True       | Indicator JSON String   |
+--------------------------+-------------------------------+------------+-------------------------+

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                     |
+==============================================+=================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                           |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``batch_jobs = dst_tc.batch_jobs()``         | Instantiate a Batch Job container object.                                       |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``for batch in indicators:``                 | Iterator through an array of arrays of indicator objects.                       |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``batch_job.set_...``                        | Configure batch job to process as many indicators as possible without aborting. |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``batch_job.upload(json.dumps(batch))``      | Upload job with indicator chunk as JSON data.                                   |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``batch_job.commit()``                       | Start batch job with configuration and data defined.                            |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``while len(batch_ids) > 0:``                | Begin polling for batch status until all pending batches are complete.          |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``filter.add_id(batchId)``                   | Add current batchId to filter.                                                  |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``for batch_job in batch_jobs:``             | Get job for filtered batch ID.                                                  |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``if batch_job.status == 'Completed':``      | Check job status completion.                                                    |
+----------------------------------------------+---------------------------------------------------------------------------------+
| ``for batch_job in finished_batches:``       | Iterate through the finished batches for status print.                          |
+----------------------------------------------+---------------------------------------------------------------------------------+

Documents Commit
----------------

The example below demonstrates how to a Document Resource in the
ThreatConnect platform.

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    documents = tc.documents()
        
    owner = 'Example Community'
    document = documents.add('New Document', owner)
    document.set_file_name('New File.txt')

    fh = open('./sample1.zip', 'rb')
    contents = fh.read()
    document.upload(contents)

    document.add_attribute('Description', 'Description Example')
    document.add_tag('EXAMPLE')
    document.set_security_label('TLP Green')
    try:
        document.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The ThreatConnect platform supports
`adding <#add-an-document-resource>`__,
`deleting <#delete-an-document-resource>`__, and
`updating <#update-an-document-resource>`__ of threat-intelligence data
programmatically using the API. The Python SDK features an easy-to-use
interface to assist in rapid development of software to manage this
data.

Adding Document Resources

The example demonstrates how to a Document Resource in the ThreatConnect
platform. The Document Resource has a special method ``upload()`` that
allows for uploading files to the platform. For more information on the
purpose of each line of code, see the **Code Highlights** section below.

Supported Properties

+-----------------+-------------------+------------+
| Property Name   | Method            | Required   |
+=================+===================+============+
| file\_name      | set\_file\_name   | True       |
+-----------------+-------------------+------------+

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``documents = tc.documents()``               | Instantiate a Documents container object.                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``document = documents.add('New Documen...`` | Add a resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.set_file_name('New File.txt')``   | **(REQUIRED)** Set the Document file name.                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``fh = open('./sample1.zip', 'rb')``         | Open the file handle.                                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``contents = fh.read()``                     | Read contents of file from file handle.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.upload(contents)``                | **Upload** file contents.                                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.add_attribute('Description',...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.add_tag('EXAMPLE')``              | Add a Tag to the Document.                                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.set_security_label('TLP Green')`` | Add a Security Label to the Document.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Updating Document Resources
---------------------------

The example below demonstrates how to update a Document Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    documents = tc.documents()

    owner = 'Example Community'
    document = documents.add('Updated Document', owner)
    document.set_id(20)

    document.load_attributes()
    for attribute in document.attributes:
        if attribute.type == 'Description':
            document.delete_attribute(attribute.id)

    document.add_attribute('Description', 'Updated Description')

    document.load_tags()
    for tag in document.tags:
        document.delete_tag(tag.name)

    document.add_tag('EXAMPLE')

    try:
        document.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to update a Document Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------------+
| Snippet                                      | Description                                                             |
+==============================================+=========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                   |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``documents = tc.documents()``               | Instantiate a Documents container object.                               |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document = documents.add('Updated Doc...`` | Add a Resource object setting the name and Owner.                       |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.set_id(20)``                      | Set the ID of the Document to the ***EXISTING*** Document ID to update. |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.load_attributes()``               | Load existing Attributes into the Document object.                      |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.delete_attribute(attribute.id)``  | Add a delete flag on the Attribute with type **Description**.           |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.add_attribute('Description',...`` | Add an Attribute of type **Description** to the Resource.               |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.load_tags()``                     | Load existing Tags into the Document object.                            |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.delete_tag(tag.name)``            | Add a delete flag to all Tags.                                          |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.add_tag('EXAMPLE')``              | Add a Tag to the Resource.                                              |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.commit()``                        | Trigger API calls to write all added, deleted, or modified data.        |
+----------------------------------------------+-------------------------------------------------------------------------+

Deleting Document Resources
---------------------------

The example below demonstrates how to delete a Document Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    documents = tc.documents()

    document = documents.add('', owner)
    document.set_id(20)

    try:
        document.delete()
    except RuntimeError as e:
        print(e)

The example demonstrates how to delete a Document Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Code Highlights

+----------------------------------------------+-----------------------------------------------------------------------+
| Snippet                                      | Description                                                           |
+==============================================+=======================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``documents = tc.documents()``               | Instantiate a Documents container object.                             |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``document = documents.add('', owner)``      | Add a Resource object setting the name and Owner.                     |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``document.set_id(20)``                      | Set the ID of the Document to the **EXISTING** Document ID to delete. |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``document.delete()``                        | Trigger API calls to write all added, deleted, or modified data.      |
+----------------------------------------------+-----------------------------------------------------------------------+

Emails Commit
-------------

The example below demonstrates how to create an Email Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    emails = tc.emails()
        
    owner = 'Example Community'
    email = emails.add('New Email', owner)

    email.set_body('This is an email body.')
    email.set_from_address('bad_guy@badguys.com')
    email.set_header('This is an improper email header.')
    email.set_subject('This is an email subject.')
    email.set_to('victim@goodguys.com')

    email.add_attribute('Description', 'Description Example')
    email.add_tag('EXAMPLE')
    email.set_security_label('TLP Green')
    try:
        email.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The ThreatConnect platform supports `adding <#add-an-email-resource>`__,
`deleting <#delete-an-email-resource>`__, and
`updating <#update-an-email-resource>`__ of threat-intelligence data
programmatically using the API. The Python SDK features an easy-to-use
interface to assist in rapid development of software to manage this
data.

Adding Email Resources

The example demonstrates how to create an Email Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Supported Properties

+-----------------+----------------------+------------+
| Property Name   | Method               | Required   |
+=================+======================+============+
| body            | set\_body            | True       |
+-----------------+----------------------+------------+
| from\_address   | set\_from\_address   | False      |
+-----------------+----------------------+------------+
| header          | set\_header          | True       |
+-----------------+----------------------+------------+
| score           | set\_score           | False      |
+-----------------+----------------------+------------+
| subject         | set\_subject         | True       |
+-----------------+----------------------+------------+
| to              | set\_to              | False      |
+-----------------+----------------------+------------+

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``emails = tc.emails()``                     | Instantiate an Emails container object.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``email = emails.add('New Email', ...``      | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_body('This is an email body...`` | **(REQUIRED)** Set the Email body.                               |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_from_address('bad_guy@badgu...`` | **(OPTIONAL)** Set the Email from address.                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_header('This is an improper...`` | **(REQUIRED)** Set the Email header.                             |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_subject('This is an email s...`` | **(REQUIRED)** Set the Email subject.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_to('victim@goodguys.com')``      | **(OPTIONAL)** Set the Email to address.                         |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.add_attribute('Description', 'D...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.add_tag('EXAMPLE')``                 | Add a Tag to the Email.                                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_security_label('TLP Green')``    | Add a Security Label to the Email.                               |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.commit()``                           | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Updating Email Resources
------------------------

The example below demonstrates how to update an Email Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    emails = tc.emails()

    owner = 'Example Community'
    email = emails.add('Updated Email', owner)
    email.set_id(20)

    email.load_attributes()
    for attribute in email.attributes:
        if attribute.type == 'Description':
            email.delete_attribute(attribute.id)

    email.add_attribute('Description', 'Updated Description')

    email.load_tags()
    for tag in email.tags:
        email.delete_tag(tag.name)

    email.add_tag('EXAMPLE')

    try:
        email.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to update an Email Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------+
| Snippet                                      | Description                                                       |
+==============================================+===================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                             |
+----------------------------------------------+-------------------------------------------------------------------+
| ``emails = tc.emails()``                     | Instantiate an Emails container object.                           |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email = emails.add('Updated Email', o...`` | Add a Resource object setting the name and Owner.                 |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.set_id(20)``                         | Set the ID of the Email to the ***EXISTING*** Email ID to update. |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.load_attributes()``                  | Load existing Attributes into the Email object.                   |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.delete_attribute(attribute.id)``     | Add a delete flag on the Attribute with type **Description**.     |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.add_attribute('Description', 'U...`` | Add an Attribute of type **Description** to the Resource.         |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.load_tags()``                        | Load existing Tags into the Email object.                         |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.delete_tag(tag.name)``               | Add a delete flag to all Tags.                                    |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.add_tag('EXAMPLE')``                 | Add a Tag to the Resource.                                        |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.commit()``                           | Trigger API calls to write all added, deleted, or modified data.  |
+----------------------------------------------+-------------------------------------------------------------------+

Deleting Email Resources
------------------------

The example below demonstrates how to delete an Email Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    emails = tc.emails()

    email = emails.add('', owner)
    email.set_id(20)

    try:
        email.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

The example demonstrates how to delete an Email Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``delete()``
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``emails = tc.emails()``                     | Instantiate an Emails container object.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``email = emails.add('', owner)``            | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_id(20)``                         | Set the ID of the Email to the **EXISTING** Email ID to delete.  |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.delete()``                           | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Incidents Commit
----------------

The example below demonstrates how to create an Incident Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    incidents = tc.incidents()
        
    owner = 'Example Community'
    incident = incidents.add('New Incident', owner)

    incident.set_event_date('2015-03-21T00:00:00Z')
        
    incident.add_attribute('Description', 'Description Example')
    incident.add_tag('EXAMPLE')
    incident.set_security_label('TLP Green')
    try:
        incident.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The ThreatConnect platform supports
`adding <#add-an-incident-resource>`__,
`deleting <#delete-an-incident-resource>`__, and
`updating <#update-an-incident-resource>`__ of threat-intelligence data
programmatically using the API. The Python SDK features an easy-to-use
interface to assist in rapid development of software to manage this
data.

Adding Incident Resources

The example demonstrates how to create an Incident Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Supported Properties

+-----------------+--------------------+------------+
| Property Name   | Method             | Required   |
+=================+====================+============+
| event\_date     | set\_event\_date   | True       |
+-----------------+--------------------+------------+

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``incidents = tc.incidents()``               | Instantiate an Incidents container object.                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident = incidents.add('New Incident')`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident.set_event_date('2015-03-21T0...`` | **(REQUIRED)** Set event date of Incident.                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident.add_attribute('Description' ...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident.add_tag('EXAMPLE')``              | Add a Tag to the Incident.                                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident.set_security_label('TLP Green')`` | Add a Security Label to the Incident.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``incident.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Updating Incident Resources
---------------------------

The example below demonstrates how to update an Incident Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    incidents = tc.incidents()

    owner = 'Example Community'
    incident = incidents.add('Updated Incident', owner)
    incident.set_id(20)

    incident.load_attributes()
    for attribute in incident.attributes:
        if attribute.type == 'Description':
            incident.delete_attribute(attribute.id)

    incident.add_attribute('Description', 'Updated Description')

    incident.load_tags()
    for tag in incident.tags:
        incident.delete_tag(tag.name)

    incident.add_tag('EXAMPLE')

    try:
        incident.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to update an Incident Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example ,no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------------+
| Snippet                                      | Description                                                             |
+==============================================+=========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                   |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incidents = tc.incidents()``               | Instantiate an Incidents container object.                              |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident = incidents.add('Updated Inc...`` | Add a Resource object setting the name and Owner.                       |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.set_id(20)``                      | Set the ID of the Incident to the ***EXISTING*** Incident ID to update. |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.load_attributes()``               | Load existing Attributes into the Incident object.                      |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.delete_attribute(attribute.id)``  | Add a delete flag to the Attribute with type **Description**.           |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.add_attribute('Description' ...`` | Add an Attribute of type **Description** to the Resource.               |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.load_tags()``                     | Load existing Tags into the Incident object.                            |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.delete_tag(tag.name)``            | Add a delete flag to all Tags.                                          |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.add_tag('EXAMPLE')``              | Add a Tag to the Resource.                                              |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.commit()``                        | Trigger API calls to write all added, deleted, or modified data.        |
+----------------------------------------------+-------------------------------------------------------------------------+

Deleting Incident Resources
---------------------------

The example below demonstrates how to delete an Incident Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    incidents = tc.incidents()

    incident = incidents.add('', owner)
    incident.set_id(20)

    try:
        incident.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

The example demonstrates how to delete an Incident Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``delete()``
method is invoked.

Code Highlights

+----------------------------------------------+-----------------------------------------------------------------------+
| Snippet                                      | Description                                                           |
+==============================================+=======================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``incidents = tc.incidents()``               | Instantiate an Incidents container object.                            |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``incident = incidents.add('', owner)``      | Add a Resource object setting the name and Owner.                     |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``incident.set_id(20)``                      | Set the ID of the Incident to the **EXISTING** Incident ID to delete. |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``incident.delete()``                        | Trigger API calls to write all added, deleted, or modified data.      |
+----------------------------------------------+-----------------------------------------------------------------------+

Indicators Commit
-----------------

The example below demonstrates how to create an Address Indicator
resource in the ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
        
    owner = 'Example Community'
    indicator = indicators.add('4.3.254.1', owner)
    indicator.set_confidence(75)
    indicator.set_rating(2.5)

    indicator.add_attribute('Description', 'Example Attribute')
    indicator.add_tag('EXAMPLE')
    indicator.set_security_label('TLP Green')

    try:
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The ThreatConnect platform supports the committing of Indicators of
Compromise programmatically using the API. The Python SDK features an
easy-to-use interface to assist in rapid development of software to
manage this data.

Indicator Type Override

The ``add()`` method on the ``indicators()`` object allows the user to
bypass the automatic Indicator identification and validation check by
specifying the IndicatorType (e.g.
``indicator = indicators.add('<indicator>', owner, IndicatorType.ADDRESSES)``).

Adding Address Indicators

The example demonstrates how to create an Address Indicator resource in
the ThreatConnect platform. For more information on the purpose of each
line of code, see the **Code Highlights** section below.

Code Highlights

+---------------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                                     | Description                                                                          |
+=============================================+======================================================================================+
| ``tc = ThreatConnect(api_access_id,...``    | Instantiate the ThreatConnect object.                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicators = tc.indicators()``            | Instantiate an Indicator container object.                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator = indicators.add('4.3.254....`` | Add a Resource object setting the value and Owner.                                   |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_confidence(75)``            | Set the Confidence value for this Indicator.                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_rating(2.5)``               | Set the Rating value for this Indicator.                                             |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_attribute('Description...`` | Add an Attribute of type **Description** to the Resource.                            |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_tag('EXAMPLE')``            | Add a Tag to the Resource.                                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_security_label('TLP Gre..`` | Add a Security Label to the Resource.                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.commit()``                      | Trigger multiple API calls to write Resource, Attributes, Security Labels, and Tags. |
+---------------------------------------------+--------------------------------------------------------------------------------------+

Adding Email Address Indicators
-------------------------------

The example below demonstrates how to create an Email Address Indicator
Resource in the ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
        
    owner = 'Example Community'
    indicator = indicators.add('badguy@badguysareus.com', owner)
    indicator.set_confidence(75)
    indicator.set_rating(2.5)

    indicator.add_attribute('Description', 'Example Attribute')
    indicator.add_tag('EXAMPLE')
    indicator.set_security_label('TLP Green')

    try:
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to create an Email Address Indicator
Resource in the ThreatConnect platform. For more information on the
purpose of each line of code, see the **Code Highlights** section below.

Code Highlights

+---------------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                                     | Description                                                                          |
+=============================================+======================================================================================+
| ``tc = ThreatConnect(api_access_id,...``    | Instantiate the ThreatConnect object.                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicators = tc.indicators()``            | Instantiate an Indicator container object.                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator = indicators.add('badguy@....`` | Add a Resource object setting the value and Owner.                                   |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_confidence(75)``            | Set the Confidence value for this Indicator.                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_rating(2.5)``               | Set the Rating value for this Indicator.                                             |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_attribute('Description...`` | Add an Attribute of type **Description** to the Resource.                            |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_tag('EXAMPLE')``            | Add a Tag to the Resource.                                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_security_label('TLP Gre..`` | Add a Security Label to the Resource.                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.commit()``                      | Trigger multiple API calls to write Resource, Attributes, Security Labels, and Tags. |
+---------------------------------------------+--------------------------------------------------------------------------------------+

Adding File Hash Indicators
---------------------------

The example below demonstrates how to create a File Hash Indicator
Resource in the ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
        
    owner = 'Example Community'
    indicator = indicators.add('8743b52063cd84097a65d1633f5c74f5', owner) # MD5 hash of string `hashcat`
    indicator.set_indicator('b89eaac7e61417341b710b727768294d0e6a277b') #SHA1 hash of same string
    indicator.set_indicator('127e6fbfe24a750e72930c220a8e138275656b8e5d8f48a98c3c92df2caba935') # SHA256 hash of same string
    indicator.set_confidence(75)
    indicator.set_rating(2.5)
    indicator.set_size(112)

    indicator.add_attribute('Description', 'Example Attribute')
    indicator.add_tag('EXAMPLE')
    indicator.set_security_label('TLP Green')

    try:
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to create a File Hash Indicator Resource in
the ThreatConnect platform. File Indicators support MD5, SHA1, and
SHA256 hashes, added in the above order to the same Indicator with the
``set_indicator()`` method. For more information on the purpose of each
line of code, see the **Code Highlights** section below.

Code Highlights

+---------------------------------------------+---------------------------------------------------------------------------------------+
| Snippet                                     | Description                                                                           |
+=============================================+=======================================================================================+
| ``tc = ThreatConnect(api_access_id,...``    | Instantiate the ThreatConnect object.                                                 |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator = indicators.add('8743b520...`` | Add an Indicator object setting the value and Owner.                                  |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_indicator('b89eaac7e61...`` | Add File addition File Hashes for this Indicator.                                     |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_indicator('127e6fbfe24...`` | Add File addition File Hashes for this Indicator.                                     |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_confidence(75)``            | Set the Confidence value for this Indicator.                                          |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_rating(2.5)``               | Set the Rating value for this Indicator.                                              |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_size(112)``                 | Set the File size property of the Indicator.                                          |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.add_attribute('Description...`` | Add an Attribute of type **Description** to the Resource.                             |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.add_tag('EXAMPLE')``            | Add a Tag to the Indicator.                                                           |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_security_label('TLP Gre..`` | Add a Security Label to the Indicator.                                                |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.commit()``                      | Trigger multiple API calls to write Indicator, Attributes, Security Labels, and Tags. |
+---------------------------------------------+---------------------------------------------------------------------------------------+

Adding File Occurrences
-----------------------

A File occurrence can be added to File Indicators by inserting the
example code before the ``indicator.commit()`` method is called:

.. code:: python


    fo_date = (datetime.isoformat(datetime(2015, 3, 29))) + 'Z'
    indicator.add_file_occurrence('badfile.exe', 'C:\windows', fo_date)

A File occurrence can be added to File Indicators by inserting the
example code before the ``indicator.commit()`` method is called.

Adding Host Indicators
----------------------

The example below demonstrates how to create a Host Indicator Resource
in the ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
        
    owner = 'Example Community'
    indicator = indicators.add('badguy.com', owner)
    indicator.set_confidence(75)
    indicator.set_rating(2.5)

    indicator.add_attribute('Description', 'Example Attribute')
    indicator.add_tag('EXAMPLE')
    indicator.set_security_label('TLP Green')

    try:
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

Automatically enrich indicator with DNS resolution or ownership
information from a third-party service

.. code:: python

    # Query PTR record for a given domain, or {A, AAAA} record for a given IP
    indicator.set_dns_active(True)

    # Look up IP or domain ownership information 
    indicator.set_whois_active(True) 

The example demonstrates how to create a Host Indicator Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Code Highlights

+---------------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                                     | Description                                                                          |
+=============================================+======================================================================================+
| ``tc = ThreatConnect(api_access_id,...``    | Instantiate the ThreatConnect object.                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicators = tc.indicators()``            | Instantiate an Indicator container object.                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator = indicators.add('badguy.....`` | Add a Resource object setting the value and Owner.                                   |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_confidence(75)``            | Set the Confidence value for this Indicator.                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_rating(2.5)``               | Set the Rating value for this Indicator.                                             |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_attribute('Description...`` | Add an Attribute of type **Description** to the Resource.                            |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_tag('EXAMPLE')``            | Add a Tag to the Resource.                                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_security_label('TLP Gre..`` | Add a Security Label to the Resource.                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.commit()``                      | Trigger multiple API calls to write Resource, Attributes, Security Labels, and Tags. |
+---------------------------------------------+--------------------------------------------------------------------------------------+

Adding URL Indicators
---------------------

The example below demonstrates how to create a URL Indicator Resource in
the ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
        
    owner = 'Example Community'
    indicator = indicators.add('badguy.com/clickme.html', owner)
    indicator.set_confidence(75)
    indicator.set_rating(2.5)

    indicator.add_attribute('Description', 'Example Attribute')
    indicator.add_tag('EXAMPLE')
    indicator.set_security_label('TLP Green')

    try:
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to create a URL Indicator Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Code Highlights

+---------------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                                     | Description                                                                          |
+=============================================+======================================================================================+
| ``tc = ThreatConnect(api_access_id,...``    | Instantiate the ThreatConnect object.                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicators = tc.indicators()``            | Instantiate an Indicator container object.                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator = indicators.add('badguy.....`` | Add a Resource object setting the value and Owner.                                   |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_confidence(75)``            | Set the Confidence value for this Indicator.                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_rating(2.5)``               | Set the Rating value for this Indicator.                                             |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_attribute('Description...`` | Add an Attribute of type **Description** to the Resource.                            |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.add_tag('EXAMPLE')``            | Add a Tag to the Resource.                                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.set_security_label('TLP Gre..`` | Add a Security Label to the Resource.                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------+
| ``indicator.commit()``                      | Trigger multiple API calls to write Resource, Attributes, Security Labels, and Tags. |
+---------------------------------------------+--------------------------------------------------------------------------------------+

Deleting Indicator Resources
----------------------------

Python SDK deleting Indicator Resources:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()

    indicator = indicators.add('4.3.2.1', owner)

    try:
        indicator.delete()
    except RuntimeError as e:
        print(e)

Code Highlights

+--------------------------------------------+----------------------------------------------------+
| Snippet                                    | Description                                        |
+============================================+====================================================+
| ``tc = ThreatConnect(api_access_id,...``   | Instantiate the ThreatConnect object.              |
+--------------------------------------------+----------------------------------------------------+
| ``indicators = tc.indicators()``           | Instantiate an Indicator container object.         |
+--------------------------------------------+----------------------------------------------------+
| ``indicator = indicators.add('4.3.2.1...`` | Add a Resource object setting the value and Owner. |
+--------------------------------------------+----------------------------------------------------+
| ``indicator.delete()``                     | Trigger API calls to delete the Resource.          |
+--------------------------------------------+----------------------------------------------------+

Signatures Commit
-----------------

The example below demonstrates how to create a Signature Resource in the
ThreatConnect platform.

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    signatures = tc.signatures()
        
    owner = 'Example Community'
    signature = signatures.add('New Signature', owner)

    file_text = '"rule example_sig : example\n{\n'
    file_text += 'meta:\n        description = "This '
    file_text += 'is just an example"\n\n '
    file_text += 'strings:\n        $a = {6A 40 68 00 '
    file_text += '30 00 00 6A 14 8D 91}\n        $b = '
    file_text += '{8D 4D B0 2B C1 83 C0 27 99 6A 4E '
    file_text += '59 F7 F9}\n    condition:\n '
    file_text += '$a or $b or $c\n}"'

    signature.set_file_name('bad_file.txt')
    signature.set_file_type('YARA')
    signature.set_file_text(file_text)
        
    signature.add_attribute('Description', 'Description Example')
    signature.add_tag('EXAMPLE')
    signature.set_security_label('TLP Green')
    try:
        signature.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The ThreatConnect platform supports
`adding <#add-an-signature-resource>`__,
`deleting <#delete-an-signature-resource>`__, and
`updating <#update-an-signature-resource>`__ of threat-intelligence data
programmatically using the API. The Python SDK features an easy-to-use
interface to assist in rapid development of software to manage this
data.

Adding Signature Resources

The example demonstrates how to create a Signature Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Supported Properties

+-----------------+-------------------+------------+
| Property Name   | Method            | Required   |
+=================+===================+============+
| file\_name      | set\_file\_name   | True       |
+-----------------+-------------------+------------+
| file\_text      | set\_file\_text   | False      |
+-----------------+-------------------+------------+
| file\_type      | set\_file\_type   | True       |
+-----------------+-------------------+------------+

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``signatures = tc.signatures()``             | Instantiate a Signatures container object.                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``signature = signatures.add('New Signa...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``signature.set_file_name('bad_file.txt')``  | **(REQUIRED)** Set file name for Signature.                      |
+----------------------------------------------+------------------------------------------------------------------+
| ``signature.set_file_type('YARA')``          | **(REQUIRED)** Set file type for Signature.                      |
+----------------------------------------------+------------------------------------------------------------------+
| ``signature.set_file_text(file_text)``       | **(OPTIONAL)** Set file contents for Signature.                  |
+----------------------------------------------+------------------------------------------------------------------+
| ``signature.add_attribute('Description'...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``signature.add_tag('EXAMPLE')``             | Add a Tag to the Signature.                                      |
+----------------------------------------------+------------------------------------------------------------------+
| ``signature.set_security_label('TLP Gre...`` | Add a Security Label to the Signature.                           |
+----------------------------------------------+------------------------------------------------------------------+
| ``signature.commit()``                       | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Updating Signature Resources
----------------------------

The example below demonstrates how to update a Signature Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    signatures = tc.signatures()

    owner = 'Example Community'
    signature = signatures.add('Updated Signature', owner)
    signature.set_id(20)

    signature.load_attributes()
    for attribute in signature.attributes:
        if attribute.type == 'Description':
            signature.delete_attribute(attribute.id)

    signature.add_attribute('Description', 'Updated Description')

    signature.load_tags()
    for tag in signature.tags:
        signature.delete_tag(tag.name)

    signature.add_tag('EXAMPLE')

    try:
        signature.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to update a Signature Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------------+
| Snippet                                      | Description                                                               |
+==============================================+===========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                     |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signatures = tc.signatures()``             | Instantiate a Signatures container object.                                |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature = signatures.add('Updated D...`` | Add a Resource object setting the name and Owner.                         |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.set_id(20)``                     | Set the ID of the Signature to the ***EXISTING*** Signature ID to update. |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.load_attributes()``              | Load existing Attributes into the Signature object.                       |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.delete_attribute(attribute.id)`` | Add a delete flag to the Attribute with type **Description**.             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.add_attribute('Description'...`` | Add an Attribute of type **Description** to the Resource.                 |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.load_tags()``                    | Load existing Tags into the Signature object.                             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.delete_tag(tag.name)``           | Add a delete flag to all Tags.                                            |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.add_tag('EXAMPLE')``             | Add a Tag to the Resource.                                                |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.commit()``                       | Trigger API calls to write all added, deleted, or modified data.          |
+----------------------------------------------+---------------------------------------------------------------------------+

Deleting Signature Resources
----------------------------

The example below demonstrates how to delete a Signature Resource in the
ThreatConnect platform.

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    signatures = tc.signatures()

    signature = signatures.add('', owner)
    signature.set_id(20)

    try:
        signature.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

The example demonstrates how to delete a Signature Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``delete()``
method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------------+
| Snippet                                      | Description                                                             |
+==============================================+=========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                   |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``signatures = tc.signatures()``             | Instantiate a Signatures container object.                              |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``signature = signatures.add('', owner)``    | Add a Resource object setting the name and Owner.                       |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``signature.set_id(20)``                     | Set the ID of the Signature to the **EXISTING** Signature ID to delete. |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``signature.delete()``                       | Trigger API calls to write all added, deleted, or modified data.        |
+----------------------------------------------+-------------------------------------------------------------------------+

Tasks Commit
------------

The ThreatConnect platform supports `adding <#adding-task-resources>`__,
`deleting <#deleting-task-resources>`__, and
`updating <#updating-task-resources>`__ of task-intelligence data
programmatically using the API. The Python SDK features an easy-to-use
interface to assist in rapid development of software to manage this
data.

Other task-specific data such as ``Assignee`` or ``Escalation Date`` can
be `modified using built-in library
functions <https://github.com/ThreatConnect-Inc/threatconnect-python/blob/master/examples/commit/tasks_commit.py#L175>`__

Adding Task Resources
---------------------

The example below demonstrates how to create a Task Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Code Sample
~~~~~~~~~~~

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    tasks = tc.tasks()

    task = tasks.add('New Task')
    task.add_attribute('Description', 'Description Example')
    task.add_tag('EXAMPLE')
    task.add_security_label('TLP Green')

    try:
        task.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights
~~~~~~~~~~~~~~~

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``tasks = tc.tasks()``                       | Instantiate a Tasks container object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``task = tasks.add('New task' own...``       | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.add_attribute('Description' 'D...``   | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.add_tag('EXAMPLE')``                  | Add a Tag to the Task.                                           |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.add_security_label('TLP Green')``     | Add a Security Label to the task.                                |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.commit()``                            | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Updating Task Resources
-----------------------

The example below demonstrates how to update a Task Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Code Sample
~~~~~~~~~~~

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    tasks = tc.tasks()

    task = tasks.add('Updated Task')
    task.set_id(20)

    task.load_attributes()
    for attribute in task.attributes:
        if attribute.type == 'Description':
            task.delete_attribute(attribute.id)

    task.add_attribute('Description', 'Updated Description')

    task.load_tags()
    for tag in task.tags:
        task.delete_tag(tag.name)

    task.add_tag('EXAMPLE')

    try:
        task.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

*Code Highlights*

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``tasks = tc.tasks()``                       | Instantiate a Tasks container object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``task = Tasks.add('Updated task'...``       | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.set_id(20)``                          | Set the ID of the task to the ***EXISTING*** task ID to update.  |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.load_attributes()``                   | Load existing Attributes into the task object.                   |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.delete_attribute(attribute.id)``      | Add a delete flag to the Attribute with type **Description**.    |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.add_attribute('Description', '...``   | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.load_tags()``                         | Load existing Tags into the task object.                         |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.delete_tag(tag.name)``                | Add a delete flag to all Tags.                                   |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.add_tag('EXAMPLE')``                  | Add a Tag to the Resource.                                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.commit()``                            | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Deleting Task Resources
-----------------------

The example below demonstrates how to delete a Task Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Code Sample
~~~~~~~~~~~

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    tasks = tc.tasks()

    task = tasks.add('', owner)
    task.set_id(20)

    try:
        task.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

Note: In the prior example, no API calls are made until the ``delete()``
method is invoked.

*Code Highlights*

+----------------------------------------------+---------------------------------------------------------------+
| Snippet                                      | Description                                                   |
+==============================================+===============================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                         |
+----------------------------------------------+---------------------------------------------------------------+
| ``tasks = tc.tasks()``                       | Instantiate a Tasks container object.                         |
+----------------------------------------------+---------------------------------------------------------------+
| ``task = tasks.add('', owner)``              | Add a Task Resource setting the name and Owner.               |
+----------------------------------------------+---------------------------------------------------------------+
| ``task.set_id(20)``                          | Set the ID of the task to the **EXISTING** task ID to delete. |
+----------------------------------------------+---------------------------------------------------------------+
| ``task.delete()``                            | Trigger API calls to delete the task.                         |
+----------------------------------------------+---------------------------------------------------------------+

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations

Groups

See the `Group Associations Documentation <#associations>`__.

Indicators

See the `Indicator Associations
Documentation <#retrieving-indicator-associations>`__.

Victims

See the `Victim Associations
Documentation <#victim-associations-retrieve>`__.

Threats Commit
--------------

The example below demonstrates how to create a Threat Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    threats = tc.threats()
        
    owner = 'Example Community'
    threat = threats.add('New Threat', owner)
    threat.add_attribute('Description', 'Description Example')
    threat.add_tag('EXAMPLE')
    threat.set_security_label('TLP Green')
    try:
        threat.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The ThreatConnect platform supports
`adding <#add-an-threat-resource>`__,
`deleting <#delete-an-threat-resource>`__, and
`updating <#update-an-threat-resource>`__ of threat-intelligence data
programmatically using the API. The Python SDK features an easy-to-use
interface to assist in rapid development of software to manage this
data.

Adding Threat Resources

The example demonstrates how to create a Threat Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``threats = tc.threats()``                   | Instantiate a Threats container object.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``threat = threats.add('New Threat' own...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``threat.add_attribute('Description' 'D...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``threat.add_tag('EXAMPLE')``                | Add a Tag to the Threat.                                         |
+----------------------------------------------+------------------------------------------------------------------+
| ``threat.set_security_label('TLP Green')``   | Add a Security Label to the Threat.                              |
+----------------------------------------------+------------------------------------------------------------------+
| ``threat.commit()``                          | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Updating Threat Resources
-------------------------

The example below demonstrates how to update a Threat Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    threats = tc.threats()

    owner = 'Example Community'
    threat = threats.add('Updated Threat', owner)
    threat.set_id(20)

    threat.load_attributes()
    for attribute in threat.attributes:
        if attribute.type == 'Description':
            threat.delete_attribute(attribute.id)

    threat.add_attribute('Description', 'Updated Description')

    threat.load_tags()
    for tag in threat.tags:
        threat.delete_tag(tag.name)

    threat.add_tag('EXAMPLE')

    try:
        threat.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to update a Threat Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------+
| Snippet                                      | Description                                                         |
+==============================================+=====================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                               |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threats = tc.threats()``                   | Instantiate a Threats container object.                             |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat = threats.add('Updated Threat'...`` | Add a Resource object setting the name and Owner.                   |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.set_id(20)``                        | Set the ID of the Threat to the ***EXISTING*** Threat ID to update. |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.load_attributes()``                 | Load existing Attributes into the Threat object.                    |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.delete_attribute(attribute.id)``    | Add a delete flag to the Attribute with type **Description**.       |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.add_attribute('Description', '...`` | Add an Attribute of type **Description** to the Resource.           |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.load_tags()``                       | Load existing Tags into the Threat object.                          |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.delete_tag(tag.name)``              | Add a delete flag to all Tags.                                      |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.add_tag('EXAMPLE')``                | Add a Tag to the Resource.                                          |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.commit()``                          | Trigger API calls to write all added, deleted, or modified data.    |
+----------------------------------------------+---------------------------------------------------------------------+

Deleting Threat Resources
-------------------------

The example below demonstrates how to delete an Threat Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    threats = tc.threats()

    threat = threats.add('', owner)
    threat.set_id(20)

    try:
        threat.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

The example demonstrates how to delete an Threat Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``delete()``
method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------+
| Snippet                                      | Description                                                       |
+==============================================+===================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                             |
+----------------------------------------------+-------------------------------------------------------------------+
| ``threats = tc.threats()``                   | Instantiate a Threats container object.                           |
+----------------------------------------------+-------------------------------------------------------------------+
| ``threat = threats.add('', owner)``          | Add a Resource object setting the name and Owner.                 |
+----------------------------------------------+-------------------------------------------------------------------+
| ``threat.set_id(20)``                        | Set the ID of the Threat to the **EXISTING** Threat ID to delete. |
+----------------------------------------------+-------------------------------------------------------------------+
| ``threat.delete()``                          | Trigger API calls to write all added, deleted, or modified data.  |
+----------------------------------------------+-------------------------------------------------------------------+

Victims Commit
--------------

The example below demonstrates hoe to create a Victim Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    victims = tc.victims()
        
    owner = 'Example Community'
    victim = victims.add('Robin Scherbatsky', owner)

    victim.set_nationality('Canadian')
    victim.set_org('Royal Canadian Mounted Police')
    victim.set_suborg('Quebec Office')
    victim.set_work_location('Quebec')

    # email address assets can be added to new victim
    asset = VictimAssetObject(ResourceType.VICTIM_EMAIL_ADDRESSES)
    asset.set_address('victim@victimsareus.com')
    asset.set_address_type('Personal')
    victim.add_asset(asset)

    # network account assets can be added to new victim
    asset = VictimAssetObject(ResourceType.VICTIM_NETWORK_ACCOUNTS)
    asset.set_account('victim')
    asset.set_network('victimsareus Active Directory')
    victim.add_asset(asset)

    # phone assets can be added to new victim
    asset = VictimAssetObject(ResourceType.VICTIM_PHONES)
    asset.set_phone_type('555-555-5555')
    victim.add_asset(asset)

    # social network assets can be added to new victim
    asset = VictimAssetObject(ResourceType.VICTIM_SOCIAL_NETWORKS)
    asset.set_account('@victim')
    asset.set_network('Twitter')
    victim.add_asset(asset)

    # website assets can be added to new victim
    asset = VictimAssetObject(ResourceType.VICTIM_WEBSITES)
    asset.set_website('www.victimsareus.com')
    victim.add_asset(asset)
        
    try:
        victim.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The ThreatConnect platform supports
`adding <#add-an-victim-resource>`__,
`deleting <#delete-an-victim-resource>`__, and
`updating <#update-an-victim-resource>`__ of threat-intelligence data
programmatically using the API. The Python SDK features an easy-to-use
interface to assist in rapid development of software to manage this
data.

Adding Victim Resources

The example demonstrates hoe to create a Victim Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code see, the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``victims = tc.victims()``                   | Instantiate a Victims container object.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim = victims.add('Robin Scherbats...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim.set_nationality('Canadian')``       | **(OPTIONAL)** Set Victim nationality.                           |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim.set_org('Royal Canadian Mounte...`` | **(OPTIONAL)** Set Victim Organization.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim.set_suborg('Quebec Office')``       | **(OPTIONAL)** Set Victim Sub-Organization.                      |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim.set_work_location('Quebec')``       | **(OPTIONAL)** Set Victim location.                              |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim.commit()``                          | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Updating Victim Resources
-------------------------

The example below demonstrates how to update a Victim Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    victims = tc.victims()

    owner = 'Example Community'
    victim = victims.add('Updated Victim', owner)
    victim.set_id(20)

    try:
        victim.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to update a Victim Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------+
| Snippet                                      | Description                                                         |
+==============================================+=====================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                               |
+----------------------------------------------+---------------------------------------------------------------------+
| ``victims = tc.victims()``                   | Instantiate a Victims container object.                             |
+----------------------------------------------+---------------------------------------------------------------------+
| ``victim = victims.add('Updated Victim'...`` | Add a Resource object setting the name and Owner.                   |
+----------------------------------------------+---------------------------------------------------------------------+
| ``victim.set_id(20)``                        | Set the ID of the Victim to the ***EXISTING*** Victim ID to update. |
+----------------------------------------------+---------------------------------------------------------------------+
| ``victim.commit()``                          | Trigger API calls to write all added, deleted, or modified data.    |
+----------------------------------------------+---------------------------------------------------------------------+

Deleting Victim Resources
-------------------------

The example below demonstrates how to delete a Victim Resource in the
ThreatConnect platform:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    victims = tc.victims()

    victim = victims.add('', owner)
    victim.set_id(20)

    try:
        victim.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

The example demonstrates how to delete a Victim Resource in the
ThreatConnect platform. For more information on the purpose of each line
of code, see the **Code Highlights** section below.

Note: In the prior example, no API calls are made until the ``delete()``
method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------+
| Snippet                                      | Description                                                       |
+==============================================+===================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                             |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victims = tc.victims()``                   | Instantiate a Victims container object.                           |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victim = victims.add('', owner)``          | Add a Resource object setting the name and Owner.                 |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victim.set_id(20)``                        | Set the ID of the Victim to the **EXISTING** Victim ID to delete. |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victim.delete()``                          | Trigger API calls to write all added, deleted, or modified data.  |
+----------------------------------------------+-------------------------------------------------------------------+

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations

Groups

See the `Group Associations Documentation <#associations>`__.

Associations
------------

The following example demonstrates how to **Associate** an Adversary
Resource with an Incident and Signature Resource. For other Resource
Groups, Indicators, and Victims, the same method should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('New Resource', owner)
    resource.associate_group(ResourceType.INCIDENTS, 555)
    resource.associate_group(ResourceType.SIGNATURE, 123)

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The Python SDK provides easy methods to manage all Group, Indicator, and
Victim Associations. Associations are supported on Indicators as well as
Group Resources (e.g., Adversaries, Documents, Emails, Incidents,
Signatures and Threats)

An example of the `Associate Group <#associate-group>`__, `Associate
Indicator <#associate-indicator>`__, `Associate
Victim <#associate-victim>`__, `Disassociate
Group <#disassociate-group>`__, `Disassociate
Indicator <#disassociate-indicator>`__, and `Disassociate
Victim <#disassociate-victim>`__ methods, as well as explanations of the
code, are provided in the following section .

Associate Group
---------------

An Association to a Resource Group, Indicator, or Victim can be created
to another Resource Group by using the ``associate_group()`` method and
passing the Resource Type and Resource ID. The Associated Resource must
exist in the ThreatConnect platform prior to the Association attempt.

Note: In the prior example, no API calls are made until the commit()
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate a Resources container object.                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('New Resourc...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.associate_group(ResourceType...`` | Add an Association to another Resource.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.associate_group(ResourceType...`` | Add an Association to another Resource.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Associate Indicator
-------------------

The following example demonstrates how to **Associate** an Indicator to
an Adversary Resource. For other Resource Groups, Indicators, and
Victims, the same method should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('New Resource', owner)
    resource.associate_indicator(ResourceType.EMAIL_ADDRESSES, 'badguy@badguys.com')
    resource.associate_indicator(ResourceType.ADDRESSES, '4.3.2.1')
    resource.associate_indicator(ResourceType.HOSTS, 'badguys.com')

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

An Association to a Resource Group, Indicator, or Victim can be created
to a Indicator by using the ``associate_indicator()`` method and passing
the Resource Type and Indicator Value. The Associated Indicator must
exist in the ThreatConnect platform prior to the Association attempt.

Note: In the prior example, no API calls are made until the commit()
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate a Resources container object.                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('New Resourc...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.associate_indicator(Resource...`` | Add an Association to an Indicator.                              |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.associate_indicator(Resource...`` | Add an Association to an Indicator.                              |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.associate_indicator(Resource...`` | Add an Association to an Indicator.                              |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Associate Victim
----------------

The following example demonstrates how to **Associate** a Victim to an
Adversary Resource. For other Resource Groups and Indicators, the same
method should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('New Adversary', owner)
    resource.associate_victim(325)

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

An Association to a Resource Group or Indicator can be created to a
Victim by using the ``associate_victim()`` method and passing the Victim
ID. The Associated Victim must exist in the ThreatConnect platform prior
to the Association attempt.

Note: In the prior example, no API calls are made until the commit()
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate a Resources container object.                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('New Adversa...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.associate_victim(325)``           | Add an Association to a Victim.                                  |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Disassociate Group
------------------

The following example demonstrates how to **Disassociate** a Group from
an Adversary Resource. For other Resource Groups, Indicators, and
Victims, the same method should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('Existing Resource', owner)

    for association in resource.group_associations:
        if association.type == 'Incident':
            resource.disassociate_group(association.resource_type, association.id)

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

An existing Group Association to another Resource Group, Indicator, or
Victim can be removed by using the ``disassociate_group()`` method and
passing the Resource Type and Resource ID. If the Resource ID of the
Group is not known, all Associated Groups can be retrieved from the API
iterating over the
`group\_associations </python/retrieve/group_associations_retrieve/#associations>`__
property.

Note: In the prior example, no API calls are made until the commit()
method is invoked.

Code Highlights

+---------------------------------------------------+------------------------------------------------------------------+
| Snippet                                           | Description                                                      |
+===================================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...``      | Instantiate the ThreatConnect object.                            |
+---------------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``                  | Instantiate a Resources container object.                        |
+---------------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('Existing Re...``      | Add a Resource object setting the name and Owner.                |
+---------------------------------------------------+------------------------------------------------------------------+
| ``for association in resource.group_associat...`` | Iterate through all Associated Groups.                           |
+---------------------------------------------------+------------------------------------------------------------------+
| ``if association.type == 'Incident':``            | Match any Association of type Incidents.                         |
+---------------------------------------------------+------------------------------------------------------------------+
| ``res.disassociate_group(association.re...``      | Disassociate the Group Resource.                                 |
+---------------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                             | Trigger API calls to write all added, deleted, or modified data. |
+---------------------------------------------------+------------------------------------------------------------------+

Disassociate Indicator
----------------------

The following example demonstrates how to **Disassociate** an Indicator
from an Adversary Resource. For other Resource Groups and Victim,s the
same method should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('Existing Resource', owner)

    for association in resource.indicator_associations:
        if association.type == 'EmailAddress':
            resource.disassociate_indicator(association.resource_type, association.indicator)

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

An existing Indicator Association to a Resource Group or Victim can be
removed by using the ``disassociate_indicator()`` method and passing the
Resource Type and Indicator Value. If the Indicator Value of the
Indicator is not known, all Associated Indicators can be retrieved from
the API iterating over the
`indicator\_associations </python/retrieve/indicator_associations_retrieve/#retrieving-indicator-associations>`__
property.

Note: In the prior example, no API calls are made until the commit()
method is invoked.

Code Highlights

+---------------------------------------------------+------------------------------------------------------------------+
| Snippet                                           | Description                                                      |
+===================================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...``      | Instantiate the ThreatConnect object.                            |
+---------------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``                  | Instantiate a Resources container object.                        |
+---------------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('Existing Re...``      | Add a Resource object setting the name and Owner.                |
+---------------------------------------------------+------------------------------------------------------------------+
| ``for association in resource.indicator_asso...`` | Iterate through all Associated Groups.                           |
+---------------------------------------------------+------------------------------------------------------------------+
| ``if association.type == 'EmailAdd':``            | Match any Association of type Incidents.                         |
+---------------------------------------------------+------------------------------------------------------------------+
| ``resource.disassociate_indicator(associatio...`` | Disassociate the Incident.                                       |
+---------------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                             | Trigger API calls to write all added, deleted, or modified data. |
+---------------------------------------------------+------------------------------------------------------------------+

Disassociate Victim
-------------------

The following example demonstrates how to **Disassociate** a Victim from
an Adversary Resource. For other Resource Groups and Indicators, the
same method should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('Existing Resource', owner)

    for association in resource.victim_associations:
        if association.name == 'Drew Brees':
            resource.disassociate_victim(association.id)

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

An existing Victim Association to a Resource Group or Indicator can be
removed by using the ``disassociate_victim()`` method and passing the
Victim ID. If the ID of the Victim is not known, all Associated Victims
can be retrieved from the API iterating over the
`victim\_associations </python/retrieve/victim_associations_retrieve/#victim-associations-retrieve>`__
property.

Note: In the prior example, no API calls are made until the commit()
method is invoked.

Code Highlights

+---------------------------------------------------+------------------------------------------------------------------+
| Snippet                                           | Description                                                      |
+===================================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...``      | Instantiate the ThreatConnect object.                            |
+---------------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``                  | Instantiate a Resources container object.                        |
+---------------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('Existing Re...``      | Add a Resource object setting the name and Owner.                |
+---------------------------------------------------+------------------------------------------------------------------+
| ``for association in resource.victim_associa...`` | Iterate through all Associated Groups.                           |
+---------------------------------------------------+------------------------------------------------------------------+
| ``if association.name == 'Drew Brees':``          | Match any Association of type Incidents.                         |
+---------------------------------------------------+------------------------------------------------------------------+
| ``res.disassociate_victim(association.i...``      | Disassociate the Incident.                                       |
+---------------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                             | Trigger API calls to write all added, deleted, or modified data. |
+---------------------------------------------------+------------------------------------------------------------------+

Resource Metadata

Attributes See the `Loading Attributes
Example <#loading-attributes-example>`__.

Security Label See the `Loading Security Label
Documentation <#loading-security-label>`__.

Tags See the `Loading Tags Documentation <#loading-tags>`__.

Associations

Groups

See the `Group Associations Documentation <#associations>`__.

Indicators

See the `Indicator Associations
Documentation <#retrieving-indicator-associations>`__.

Victims

See the `Victim Associations
Documentation <#victim-associations-retrieve>`__.

Outputs

CSV

See the `CSV Output Documentation <#csv>`__.

JSON

See the `JSON Output Documentation <#json>`__.

Key Value

See the `Key Value Output Documentation <#key-value>`__.

Attributes
----------

The following example demonstrates how to **add** an Attribute to an
Adversary Resource. For other Resource Groups and Indicators, the same
method should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('New Adversary', owner)

    resource.add_attribute('Description', 'Description Example')
    resource.add_attribute('Source', 'SIEM')

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The Python SDK provides easy methods to manage Attributes. Attributes
are supported on Indicators as well as Group Resources (e.g.,
Adversaries, Documents, Emails, Incidents, Signatures and Threats)

An example of the `add <#add-attribute>`__,
`delete <#delete-attribute>`__, and `update <#update-attribute>`__
methods, as well as explanations of the code, are provided in the
following section.

Adding Attributes
-----------------

An Attribute can be added to a Resource Group or Indicator using the
``add_attribute()`` method and passing the Attribute Type and Attribute
Value. Attributes can be added while creating a new Resource or during a
Resource update. The Attribute Type (e.g., description) must be created
in the Organization prior to it being added via the API. Some Attributes
come packaged with the ThreatConnect platform, but custom Attributes
must have been previously created in the User Interface by the
ThreatConnect administrator.

Note: In the prior example, no API calls are made until the commit()
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate a Resources container object.                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('New Adversa...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.add_attribute('Description',...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.add_attribute('Source, 'SIEM')``  | Add an Attribute of type **Source** to the Resource.             |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Deleting Attributes
-------------------

The following example demonstrates how to **delete** an Attribute for an
Adversary Resource. For other Resource Groups and Indicators, the same
method should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('Existing Resource', owner)
    resource.add_id(34)

    resource.load_attributes()
    for attribute in resource.attributes:
        if attribute.type == 'Description':
            resource.delete_attribute(attribute.id)

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

An Attribute can be deleted from an existing Resource Group or Indicator
using the ``delete_attribute()`` method and passing the Attribute ID. If
the Attribute ID is not known, all Attributes for this Resource or
Indicator can be retrieved from the API using the
`load\_attributes() </python/retrieve/loading_attributes_retrieve/#loading-attributes>`__
method.

Note: In the prior example, no API calls are made until the commit()
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate a Resources container object.                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('Existing Re...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.load_attributes()``               | Load existing Attributes.                                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``for attribute in resource.attributes:``    | Iterate through Attribute objects.                               |
+----------------------------------------------+------------------------------------------------------------------+
| ``if attribute.type == 'Description':``      | Look for a **Description** Attribute.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.delete_attribute(attribute.id)``  | Delete the Attribute from the Resource.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Update Attribute
----------------

Python SDK Updating Attribute using the load attributes method:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('Existing Resource', owner)
    resource.set_id(123)

    try:
        resource.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    resource.load_attributes()
    for attribute in resource.attributes:
        if attribute.type == 'Description':
            resource.update_attribute(attribute.id, 'Updated Description')

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

An Attribute can be updated on an existing Resource Group or Indicator
using the ``update_attribute()`` method and passing the Attribute ID and
the updated Attribute Value. If the Attribute ID is not known all
Attributes for this Resource or Indicator can be retrieved from the API
using the
`load\_attributes() </python/retrieve/loading_attributes_retrieve/#loading-attributes>`__
method.

Code Highlights

+----------------------------------------------+-----------------------------------------------------------------------+
| Snippet                                      | Description                                                           |
+==============================================+=======================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate a Resources container object.                             |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resource = resources.add('Existing Re...`` | Add a Resource object setting the name and Owner.                     |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resource.retrieve()``                      | Trigger the API request and retrieve the Adversary intelligence data. |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resource.load_attributes()``               | Load existing Attributes.                                             |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``for attribute in resource.attributes:``    | Iterate through Attribute objects.                                    |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``if attribute.type == 'Description':``      | Look for a **Description** Attribute.                                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resource.update_attribute(attribute.i...`` | Update the **Description** Attribute.                                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger API calls to write all added, deleted, or modified data.      |
+----------------------------------------------+-----------------------------------------------------------------------+

Security Label
--------------

The following example demonstrates how to **set** a Security Label for
an Adversary Resource. For other Resource Groups and Indicators, the
same method should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('New Resource', owner)
    resource.set_security_label('TLP Green')

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The Python SDK provides easy methods to manage Security Labels, which
are supported on Indicators as well as Group Resources (e.g.,
Adversaries, Documents, Emails, Incidents, Signatures and Threats)

An example of the `set <#set-security-label>`__ and
`delete <#delete-security-label>`__ methods, as well as explanations of
the code, are provided in the following section.

Setting Security Labels

A Security Label can be set on a Resource Group or Indicator using the
``set_security_label()`` method and passing the Security Label Value.
Security Labels can be set while creating a new Resource or during a
Resource update. The Security Label (e.g., TLP Green) must be created in
the Organization prior to being added via the API. The ThreatConnect
administrator can add Security Labels via the User Interface.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate an Adversaries container object.                     |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('New Resourc...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.set_security_label('TLP Green')`` | Set the Security Label on the Resource.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Deleting Security Labels
------------------------

The following example demonstrates how to **delete** a Security Label
for an Adversary Resource. For other Resource Groups and Indicators, the
same method should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('New Resource', owner)
    resource.delete_security_label('TLP Green')

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

A Security Label can be deleted on a Resource Group or Indicator using
the ``delete_security_label()`` method and passing the Security Label
value.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate an Adversaries container object.                     |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('New Resourc...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.delete_security_label('TLP G...`` | Set the Security Label on the Resource.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

Tags
----

The following example demonstrates how to add a Tag on an Adversary
Resource. For other Resource Groups and Indicators, the same method
should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('New Adversary', owner)
    resource.add_tag('EXAMPLE')
    resource.add_tag('APT')

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The Python SDK provides easy methods to manage Tags, which are supported
on Indicators as well as Group Resources (e.g., Adversaries, Documents,
Emails, Incidents, Signatures and Threats)

An example of the `add <#adding-tag>`__ and `delete <#deleting-tags>`__
methods are provided in the following section as well as explanations of
the code.

Adding Tags
-----------

A Tag can be added to a Group Resource or Indicator using the
``add_tag()`` method and passing the Tag value. Tags can be added while
creating a new Resource or during a Resource update.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+------------------------------------------+------------------------------------------------------------------+
| Snippet                                  | Description                                                      |
+==========================================+==================================================================+
| ``tc = ThreatConnect(api_access_id,...`` | Instantiate the ThreatConnect object.                            |
+------------------------------------------+------------------------------------------------------------------+
| ``resources = tc.adversaries()``         | Instantiate a Resources container object.                        |
+------------------------------------------+------------------------------------------------------------------+
| ``resource = resources.add('New Ads...`` | Add a Resource object setting the name and Owner.                |
+------------------------------------------+------------------------------------------------------------------+
| ``resource.add_tag('EXAMPLE')``          | Add a Tag to the Resource.                                       |
+------------------------------------------+------------------------------------------------------------------+
| ``resource.add_tag('APT')``              | Add a Tag to the Resource.                                       |
+------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                    | Trigger API calls to write all added, deleted, or modified data. |
+------------------------------------------+------------------------------------------------------------------+

Deleting Tags
-------------

The following example demonstrates how to delete a Tag on an Adversary
Resource. For other Resource Groups and Indicators, the same method
should be used:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    resources = tc.adversaries()
        
    owner = 'Example Community'
    resource = resources.add('Existing Resource', owner)
    resource.set_id(123)
    resource.delete_tag('EXAMPLE')
    resource.delete_tag('APT')

    try:
        resource.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

A Tag can be deleted from a Resource using the ``delete_tag()`` method
and passing the Tag value.

Note: In the prior example, no API calls are made until the ``commit()``
method is invoked.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------------+
| Snippet                                      | Description                                                               |
+==============================================+===========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                     |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``resources = tc.adversaries()``             | Instantiate a Resources container object.                                 |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``resource = resources.add('Existing Re...`` | Add a Resource object setting the name and Owner.                         |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``resource.set_id(123)``                     | Set the Resource ID to an existing Adversary.                             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``resource.delete_tag('EXAMPLE')``           | Delete a Tag to the Resource.                                             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``resource.delete_tag('APT')``               | Delete a Tag to the Resource.                                             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger multiple API calls to write all added, deleted, or modified data. |
+----------------------------------------------+---------------------------------------------------------------------------+

Python Advanced
---------------

API Settings

The Python SDK provides a few methods that affect interactions with the
ThreatConnect API. The default settings should work in most cases.

Activity Log
~~~~~~~~~~~~

    Enabling the Activity Log:

.. code:: python

    tc.set_activity_log(True)

    Disabling the Activity Log:

.. code:: python

    tc.set_activity_log(False)

The ThreatConnect platform tracks all activity by users, including API
accounts. When using the API to create thousands of Indicators, the
Activity Log could generate excessive data. Activity tracing is
**disabled by default** in the Python SDK. This feature can be turned on
by calling the ``tc.set_activity_log()`` method, passing ``True`` as the
argument. To disable tracking again during the same execution period,
call the ``tc.set_activity_log()`` method once more, passing ``False``.

API Request Timeout
~~~~~~~~~~~~~~~~~~~

    This timeout value can be changed by passing the new timeout value,
    in seconds, to the ``tc.set_api_request_timeout()`` method.

.. code:: python

    tc.set_api_request_timeout(15)

The Python SDK uses the Request module for communicating to the API. To
prevent script from hanging on a bad socket, there is a timeout value
set to **30 seconds by default**.

API Retries/Sleep Period
~~~~~~~~~~~~~~~~~~~~~~~~

To change the default sleep period, call the ``set_api_sleep()`` method,
passing an Integer for the number of seconds to sleep.

.. code:: python

    tc.set_api_retries(3)
    tc.set_api_sleep(30)

If the Python SDK loses network connectivity to the API server, it will
automatically retry the connection.

The Python SDK has a **default of 5** retries, with a **default
59-second** sleep between retries before a RunTimeError is raised. To
change the default retry value, call the ``set_api_retries()`` method,
passing an Integer for the number of retries.

Note: There is a maximum window of 5 minutes before the API will reject
the HMAC (hash message authentication code) header due to a time
mismatch.

API Result Limit
~~~~~~~~~~~~~~~~

To change the default value, call the ``set_api_result_limit()`` method,
passing an Integer between 1-500.

.. code:: python

    tc.set_api_result_limit(500)

The ThreatConnect API supports a **maximum of 500** results to be
returned per API call during pagination. The Python SDK is configured
for a **default of 200** results per API request. To change the default
value, call the ``set_api_result_limit()`` method, passing an Integer
between 1-500. The higher the number, the less API calls will be made,
but in some cases, a lower number is required due to network
limitations.

Proxies
~~~~~~~

    Proxy Setting (No Authentication)

.. code:: python

    tc.set_proxies('10.10.10.10', 8443)

    Proxy Setting (Authentication Provided)

.. code:: python

    tc.set_proxies('10.10.10.10', 8443, 'proxy_user', 'password123')

In some environments, the server running the Python SDK does not have
the required Internet access to connect to the ThreatConnect API server.
In these cases, a proxy server can be used to provide the required
connectivity. To configure the Python SDK to use a proxy, call the
``set_proxies()`` method, providing the proxy-server IP address and port
number as parameters. If the proxy server requires authentication, also
provide the proxy user and proxy password as parameters.

Filtering
~~~~~~~~~

    A list of Filters can also be retrieved by using the
    ``filter1.filters`` property:

.. code:: python

    owner = 'Example Community'

    try:
        filter1 = adversary.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

        print(filter1)

The Python SDK provides a powerful filtering system. When possible, it
allows the user to set API Filters that limit the results returned from
the API. If further filtering is required, there are Post Filters that
allow the user to further refine the result set. The API Filters in a
single Filter object will **OR** the results together, while the Post
Filter will **AND** the results.

Printing Filter Objects

After creating a Filter object, the object can be printed, which will
display the number of Request objects created, as well as the supported
API Filters and Post Filters. A list of Filters can also be retrieved by
using the ``filter1.filters`` property.

filter1.filters Resulting Output

+---------------------+---------------------------+
| Filter Object       |                           |
+=====================+===========================+
| Filter Properties   |                           |
+---------------------+---------------------------+
| Operator            | FilterSetOperator.AND     |
+---------------------+---------------------------+
| Request Objects     | 1                         |
+---------------------+---------------------------+
| Owners              |                           |
+---------------------+---------------------------+
| Owner               | Example Community         |
+---------------------+---------------------------+
| Filters             |                           |
+---------------------+---------------------------+
| Filter              | api filter by tag "APT"   |
+---------------------+---------------------------+
| API Filters         |                           |
+---------------------+---------------------------+
| Filter              | add\_adversary\_id        |
+---------------------+---------------------------+
| Filter              | add\_email\_id            |
+---------------------+---------------------------+
| Filter              | add\_document\_id         |
+---------------------+---------------------------+
| Filter              | add\_id                   |
+---------------------+---------------------------+
| Filter              | add\_incident\_id         |
+---------------------+---------------------------+
| Filter              | add\_indicator            |
+---------------------+---------------------------+
| Filter              | add\_security\_label      |
+---------------------+---------------------------+
| Filter              | add\_signature\_id        |
+---------------------+---------------------------+
| Filter              | add\_threat\_id           |
+---------------------+---------------------------+
| Filter              | add\_tag                  |
+---------------------+---------------------------+
| Filter              | add\_victim\_id           |
+---------------------+---------------------------+
| Post Filters        |                           |
+---------------------+---------------------------+
| Filter              | add\_pf\_name             |
+---------------------+---------------------------+
| Filter              | add\_pf\_date\_added      |
+---------------------+---------------------------+

Filter Object Basics
~~~~~~~~~~~~~~~~~~~~

Python SDK Filter Object Basics example:

.. code:: python

    filter1 = adversary.add_filter()
    filter1 = adversary.indicator('10.20.30.40')
    filter1 = adversary.victim_id(10)
    filter1 = adversary.tag('APT')

Python SDK Post Filter Basics example:

.. code:: python

    from threatconnect.Config.FilterOperator import FilterOperator

    filter1 = adversary.add_filter()
    filter1 = adversary.add_pf_name('Bad Guy')
    filter1 = adversary.add_pf_date_added('2015-06-18T20:21:45-05:00', FilterOperator.GE)

As mentioned above, an API Filter will join the results. In the example,
the API results will contain any Adversary that has an Association with
the Indicator *10.20.30.40*, **OR** an Association with the Victim with
an ID of *10*, **OR** has the Tag of *APT*.

As mentioned above, the Post Filters will intersect the results. In the
example, the API results will only contain Adversaries that have the
name *"Bad Guy"* **AND** have a date added of >=
*2015-06-18T20:21:45-05:00*.

Owner API Filter
~~~~~~~~~~~~~~~~

Python SDK formatted URI example:

::

    /v2/indicators/address/10.20.30.40?owner=Example+Community

::

    /v2/groups/adversaries/5/indicators?owner=Example+Community

The Owner API Filter is a special Filter that is applied to all other
API Filters in the same Filter Object. This is due to the fact that the
API supports adding the Owner as a query String. See the formatted URI
examples below.

Indicator-Type Filter
~~~~~~~~~~~~~~~~~~~~~

Python SDK example Supported Indicator Types:

.. code:: python

    filter1 = indicators.add_filter(IndicatorType.ADDRESSES)
    filter1 = indicators.add_filter(IndicatorType.EMAIL_ADDRESSES)
    filter1 = indicators.add_filter(IndicatorType.FILES)
    filter1 = indicators.add_filter(IndicatorType.HOSTS)
    filter1 = indicators.add_filter(IndicatorType.URLS)

An Indicator Filter object supports passing an optional IndicatorType
enum argument to the ``add_filter`` method. This will filter all results
in the Filter object to the Indicator Type specified.

+-----------------------------+
| Supported Indicator Types   |
+=============================+
| ADDRESSES                   |
+-----------------------------+
| EMAIL\_ADDRESSES            |
+-----------------------------+
| FILES                       |
+-----------------------------+
| HOSTS                       |
+-----------------------------+
| URLS                        |
+-----------------------------+

Modified Since API Filter
~~~~~~~~~~~~~~~~~~~~~~~~~

Python SDK Modified Since API Filter:

.. code:: python


    modified_since = (datetime.isoformat(datetime(2015, 6, 17))) + 'Z'
    indicators.set_modified_since(modified_since)

The **Modified Since** Filter applies to the entire Indicators Container
but can only be used on **base** Indicator searches (e.g.,
``/v2/indicators``). If a Filter on **modified since** is required on a
different Indicator search, there is a Post Filter for **modified
since** that works on all Indicator result sets.

Multiple Filter Objects
~~~~~~~~~~~~~~~~~~~~~~~

Python SDK Multiple Filter Objects example:

.. code:: python

    owner = 'Example Community'

    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        filter1.add_security_label('TLP Red')
    except AttributeError as e:
        print(e)
        sys.exit(1)

    try:
        filter2 = indicators.add_filter()
        filter2.add_owner(owner)
        filter2.add_filter_operator(FilterSetOperator.AND)
        filter2.add_threat_id(38)
    except AttributeError as e:
        print(e)
        sys.exit(1)

    try:
        filter3 = indicators.add_filter(IndicatorType.ADDRESSES)
        filter3.add_owner(owner)
        filter3.add_filter_operator(FilterSetOperator.OR)
        filter3.add_tag('EXAMPLE')
    except AttributeError as e:
        print(e)
        sys.exit(1)

The Python SDK supports adding multiple Filter objects to a Resource
Container. A **filter\_operator** allows a user to configure the results
sets of the separate Filter objects to be **JOINED** or **INTERSECTED**.
No **filter\_operator** is required on the first Filter object added.
Each subsequent Filter object can be joined (FilterSetOperator.OR) or
intersected (FilterSetOperator.AND).

Manual API Calls
----------------

The Python SDK supports a manual way to access the API by allowing the
creation of a ``RequestObject()`` and submitting these objects to the
``api_request()`` method. The returned result will be a **Python
Requests** object containing the HTTP Status Code, Response Headers, and
API Results.

Retrieving Indicators
~~~~~~~~~~~~~~~~~~~~~

The example below displays how to create a ``RequestObject`` that will
retrieve all Indicators from a specified Owner:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    ro = RequestObject()
    ro.set_http_method('GET')
    ro.set_owner('Example Community')
    ro.set_owner_allowed(True)
    ro.set_resource_pagination(True)
    ro.set_request_uri('/v2/indicators')

    results = tc.api_request(ro)
    if results.headers['content-type'] == 'application/json':
        data = results.json()
        print(json.dumps(data, indent=4))

The example displays how to create a ``RequestObject`` that will
retrieve all Indicators from a specified Owner.

Code Highlights

Refer to `ThreatConnect API documentation <#rest-api>`__ for proper
values for the ``RequestObject``.

+------------------------------------------+-------------------------------------------------------------------------------------------+
| Snippet                                  | Description                                                                               |
+==========================================+===========================================================================================+
| ``ro = RequestObject()``                 | Instantiate and Instance of a Request object.                                             |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_http_method('GET')``            | Set the HTTP Method for the Request.                                                      |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_owner('Example Community')``    | Set the Owner for the Request (optional).                                                 |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_owner_allowed(True)``           | Set the Owner-Allowed flag for the Request to indicate if this API call supports Owners.  |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_resource_pagination(True)``     | Set the Pagination flag for the Request to indicate if this API call supports pagination. |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_request_uri('/v2/indicators')`` | Set the URI (uniform resource identifier) for the Request.                                |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``results = tc.api_request(ro)``         | Trigger the API Request and store result as ``results``.                                  |
+------------------------------------------+-------------------------------------------------------------------------------------------+

Downloading Document Contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example below displays how to create a ``RequestObject`` that will
retrieve the contents of a document stored in a Document Resource.

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    ro = RequestObject()
    ro.set_http_method('GET')
    ro.set_owner('Example Community')
    ro.set_owner_allowed(True)
    ro.set_resource_pagination(False)
    ro.set_request_uri('/v2/groups/documents/19/download')

    results = tc.api_request(ro)
    if results.headers['content-type'] == 'application/octet-stream':
        file_contents = results.content
        print(file_contents)

The example displays how to create a ``RequestObject`` that will
retrieve the contents of a document stored in a Document Resource.

Code Highlights

Refer to `ThreatConnect API documentation <#rest-api>`__ for proper
values for the ``RequestObject``.

+------------------------------------------+-------------------------------------------------------------------------------------------+
| Snippet                                  | Description                                                                               |
+==========================================+===========================================================================================+
| ``ro = RequestObject()``                 | Instantiate and Instance of a Request object.                                             |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_http_method('GET')``            | Set the HTTP Method for the Request.                                                      |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_owner('Example Community')``    | Set the Owner for the Request (optional).                                                 |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_owner_allowed(True)``           | Set the Owner-Allowed flag for the Request to indicate if this API call supports Owners.  |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_resource_pagination(True)``     | Set the Pagination flag for the Request to indicate if this API call supports pagination. |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_request_uri('/v2/indicators')`` | Set the URI for the Request.                                                              |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``results = tc.api_request(ro)``         | Trigger the API Request and store result as ``results``.                                  |
+------------------------------------------+-------------------------------------------------------------------------------------------+

Creating and Uploading Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example below displays how to create a ``RequestObject`` that will
create a Document Resource in ThreatConnect and upload a file to this
Resource.

.. code:: python

     
    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    ro = RequestObject()
    ro.set_http_method('POST')
    body = {'name': 'Raw Upload Example', 'fileName': 'raw_example.txt'}
    ro.set_body(json.dumps(body))
    ro.set_content_type('application/json')
    ro.set_owner('Example Community')
    ro.set_owner_allowed(True)
    ro.set_resource_pagination(False)
    ro.set_request_uri('/v2/groups/documents')

    print(ro)

    results = tc.api_request(ro)
    if results.headers['content-type'] == 'application/json':
        data = results.json()
        print(json.dumps(data, indent=4))

        document_id = data['data']['document']['id']

        ro = RequestObject()
        ro.set_http_method('POST')
        body = 'Raw upload example file Contents.'
        ro.set_body(body)
        ro.set_content_type('application/octet-stream')
        ro.set_owner('Example Community')
        ro.set_owner_allowed(True)
        ro.set_resource_pagination(False)
        ro.set_request_uri('/v2/groups/documents/{0}/upload'.format(document_id))

        results = tc.api_request(ro)
        print('Status Code: {0}'.format(results.status_code))

The example displays how to create a ``RequestObject`` that will create
a Document Resource in ThreatConnect and upload a file to this Resource.

Code Highlights

Refer to `ThreatConnect API documentation <#rest-api>`__ for proper
values for the ``RequestObject``.

+-------------------------------------------+-------------------------------------------------------------------------------------------+
| Snippet                                   | Description                                                                               |
+===========================================+===========================================================================================+
| ``ro = RequestObject()``                  | Instantiate and Instance of a Request Object.                                             |
+-------------------------------------------+-------------------------------------------------------------------------------------------+
| ``body = {'name': 'Raw Upload Exam...``   | Create the JSON body for POST.                                                            |
+-------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_http_method('POST')``            | Set the HTTP Method for the Request.                                                      |
+-------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_owner('Example Community')``     | Set the Owner for the Request (optional).                                                 |
+-------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_owner_allowed(True)``            | Set the Owner-Allowed flag for the Request to indicate if this API call supports Owners.  |
+-------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_resource_pagination(False)``     | Set the Pagination flag for the Request to indicate if this API call supports pagination. |
+-------------------------------------------+-------------------------------------------------------------------------------------------+
| ``ro.set_request_uri('/v2/groups/doc...`` | Set the URI for the Request.                                                              |
+-------------------------------------------+-------------------------------------------------------------------------------------------+
| ``print(ro)``                             | Display the Request Object before submitting (optional).                                  |
+-------------------------------------------+-------------------------------------------------------------------------------------------+
| ``results = tc.api_request(ro)``          | Trigger the API Request and store result as ``results``.                                  |
+-------------------------------------------+-------------------------------------------------------------------------------------------+
| ``document_id = data['data']['doc...``    | Get the ID of the created Document to use in the contents upload.                         |
+-------------------------------------------+-------------------------------------------------------------------------------------------+

Advanced Outputs Formats
~~~~~~~~~~~~~~~~~~~~~~~~

The Python SDK allows for a Resource to be returned in multiple standard
formats. The SDK currently supports the following formats: CEF (Common
Event Format), CSV (Comma-Separated Values), JSON (JavaScript® Object
Notation) , KeyVal (Key Value), and LEEF (Log Event Extended Format).

CEF
~~~

Python SDK CEF Code Sample:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
    owner = 'Example Community'

    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print(e)
        sys.exit(1)

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    for indicator in indicators:
        print(indicator.cef)

Python SDK Sample CEF Output:

::

    CEF:0|threatconnect|threatconnect|2|355999|TEST attribute #14|2.0|confidence="14" dateAdded="2015-06-21T10:40:33-05:00" dnsActive="None" hostName="www.badguy_014.com" lastModified="2015-06-21T10:40:33-05:00" ownerName="Example Community" type="None" weblink="https://tc.sumx.us/auth/indicators/details/host.xhtml?host\=www.badguy_014.com&owner\=Example+Community" whoisActive="None"

The Python SDK provides the ``cef`` methods to output data structured in
CEF, whose output is only supported on
`Indicators <#indicators_commit>`__. The CEF-formatted data maps the
ThreatConnect Resource properties to the standard fields, when possible,
and then uses the extension feature to store non-standard properties.

CSV
~~~

Python SDK CSV Code Sample:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
    owner = 'Example Community'

    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print(e)
        sys.exit(1)

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    print(indicator.csv_header)
    for indicator in indicators:
        print(indicator.csv)

Python SDK Sample CSV Output:

.. code:: text

    {
        "confidence": 14, 
        "dateAdded": "2015-06-21T10:40:33-05:00", 
        "description": "TEST attribute #14", 
        "id": 355999,
        "indicator":"www.badguy_014.com"
        "lastModified": "2015-06-21T10:40:33-05:00", 
        "ownerName": "Example Community", 
        "rating": 1.0, 
        "type": null, 
        "weblink": "https://tc.sumx.us/auth/indicators/details/host.xhtml?host=www.badguy_014.com&owner=Example+Community", 
    }

The Python SDK provides the ``csv`` and ``csv_header`` methods for CSV
output, which are supported on Indicators as well as Group Resources
(e.g., Adversaries, Documents, Emails, Incidents, Signatures and
Threats)

The ``csv_header`` method should normally be called once per result set.

JSON
~~~~

Python SDK JSON Code Sample:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
    owner = 'Example Community'

    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print(e)
        sys.exit(1)

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    for indicator in indicators:
        print(indicator.json)

Python SDK Sample JSON Output:

.. code:: json

    {
        "confidence": 14, 
        "dateAdded": "2015-06-21T10:40:33-05:00", 
        "description": "TEST attribute #14", 
        "dnsActive": null, 
        "hostName": "www.badguy_014.com", 
        "id": 355999, 
        "lastModified": "2015-06-21T10:40:33-05:00", 
        "ownerName": "Example Community", 
        "rating": 1.0, 
        "type": null, 
        "weblink": "https://tc.sumx.us/auth/indicators/details/host.xhtml?host=www.badguy_014.com&owner=Example+Community", 
        "whoisActive": null
    }

| The Python SDK provides the ``json`` method for output in JSON, are
  supported on Indicators as well as Group Resources (e.g., Adversaries,
  Documents, Emails, Incidents, Signatures and Threats)
| The fields in the output depend on the type of Resource that has been
  requested.

Key Value
~~~~~~~~~

Python SDK Key Value Code Sample:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
    owner = 'Example Community'

    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print(e)
        sys.exit(1)

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    for indicator in indicators:
        print(indicator.keyval)

Sample Key/Value Output:

.. code:: text

    confidence="14" dateAdded="2015-06-21T10:40:33-05:00" description="TEST attribute #14" dnsActive="None" hostName="www.badguy_014.com" id="355999" lastModified="2015-06-21T10:40:33-05:00" ownerName="Example Community" rating="1.0" type="None" weblink="https://tc.sumx.us/auth/indicators/details/host.xhtml?host=www.badguy_014.com&owner=Example+Community" whoisActive="None" 

The Python SDK provides the ``keyval`` method for output in the Key
Value format, whose output is supported on Indicators as well as Group
Resources (e.g., Adversaries, Documents, Emails, Incidents, Signatures
and Threats)

The fields in the output depend on the type of Resource that has been
requested.

LEEF
~~~~

Python SDK LEEF Code Sample:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
    owner = 'Example Community'

    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print(e)
        sys.exit(1)

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    for indicator in indicators:
        print(indicator.leef)

Python SDK Sample LEEF Output:

.. code:: text

    LEEF:0|threatconnect|threatconnect|2|355999|confidence="14" devTime="2015-06-21T10:40:33-05:00" description="TEST attribute #14" dnsActive="None" hostName="www.badguy_014.com" id="355999" lastModified="2015-06-21T10:40:33-05:00" ownerName="Example Community" severity="1.0" type="None" weblink="https://tc.sumx.us/auth/indicators/details/host.xhtml?host=www.badguy_014.com&owner=Example+Community" whoisActive="None" 

The Python SDK provides the ``leef`` method to output data structured in
LEEF, whose output is only supported on
`Indicators <#indicators_commit>`__. The LEEF-formatted data maps the
ThreatConnect Resource properties to the standard fields, when possible,
and then uses the custom attribute feature to store non-standard
properties.

Regex Overrides
~~~~~~~~~~~~~~~

Python SDK Regex Code Sample

::


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    #
    # override FILES Regex
    #
    md5_re = re.compile(r'^([a-fA-F\d]{32})$')
    sha1_re = re.compile(r'^([a-fA-F\d]{40})$')
    sha256_re = re.compile(r'^([a-fA-F\d]{64})$')
    tc.set_indicator_regex(IndicatorType.FILES, [md5_re, sha1_re, sha256_re])

    #
    # override ADDRESSES Regex
    #
    ipv4_regex = re.compile('(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}' +
                             '(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
    ipv6_regex = re.compile('(S*([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}S*|S*(' +
                             '[0-9a-fA-F]{1,4}:){1,7}:S*|S*([0-9a-fA-F]{1,4}:)' +
                             '{1,6}:[0-9a-fA-F]{1,4}S*|S*([0-9a-fA-F]{1,4}:)' +
                             '{1,5}(:[0-9a-fA-F]{1,4}){1,2}S*|S*([0-9a-fA-F]' +
                             '{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}S*|S*(' +
                             '[0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}S*' +
                             '|S*([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4})' +
                             '{1,5}S*|S*[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4})' +
                             '{1,6})S*|S*:((:[0-9a-fA-F]{1,4}){1,7}|:)S*|::(ffff' +
                             '(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}' +
                             '[0-9]){0,1}[0-9]).){3,3}(25[0-5]|(2[0-4]|1{0,1}[' +
                             '0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[' +
                             '0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]).){3,3}(25[' +
                             '0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))')
    tc.set_indicator_regex(IndicatorType.ADDRESSES, [ipv4_regex, ipv6_regex])

    #
    # override HOSTS Regex
    #
    host_re = re.compile(r'\b((?:(?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+(?i)(?!exe|php|dll|doc' \
        '|docx|txt|rtf|odt|xls|xlsx|ppt|pptx|bin|pcap|ioc|pdf|mdb|asp|html|xml|jpg|gif$|png' \
        '|lnk|log|vbs|lco|bat|shell|quit|pdb|vbp|bdoda|bsspx|save|cpl|wav|tmp|close|ico|ini' \
        '|sleep|run|dat$|scr|jar|jxr|apt|w32|css|js|xpi|class|apk|rar|zip|hlp|tmp|cpp|crl' \
        '|cfg|cer|plg|tmp|lxdns|cgi|xn$)(?:xn--[a-zA-Z0-9]{2,22}|[a-zA-Z]{2,13}))(?:\s|$)')
    tc.set_indicator_regex(IndicatorType.HOSTS, host_re)

    indicator = indicators.add('new.domain.tld', owner)
    indicator.set_confidence(50)
    indicator.set_rating('2.0')

    try:
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0!s}'.format(e))
        sys.exit(1))

The Python SDK provides the ``set_indicator_regex`` method which allows
a user to override the baked-in Regular Expressions (Regexes) in the SDK
with user defined compiled Regexes. The method takes an IndicatorType
enum and either a single compiled Regex or a list of Regexes. If a list
is provided each Regex will be checked for a match for that Indicator
Type.

Reporting
~~~~~~~~~

The ``tc.report.stats`` properties method provides an overview of the
script results:

.. code:: python


    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
    owner = 'Example Community'

    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print(e)
        sys.exit(1)

    try:
        indicators.retrieve()
        


    print(tc.report.stats)

Sample Report-Statistics Output:

.. code:: text

    _Stats_

    API Stats                               
      API Calls                    32                                                
      Unfiltered Results           3                                                 
      Filtered Results             3                                                 

    Filters                                 
      API Filters                  1                                                 
      Post Filters                 0                                                 
      Total Filters                1                                                 

    HTTP Methods                            
      PUT                          2                                                 
      POST                         11                                                
      DELETE                       11                                                
      GET                          8                                                 

    Status Codes                            
      200                          21                                                
      201                          11                                                

    Performance Stats                       
      Request Time           0:00:03.021702                                    
      Processing Time        0:00:00.014082                                    
      Run Time               0:00:03.035795     

The Python SDK includes a reporting feature that provides a number of
methods for reporting on the execution status of a script that uses the
SDK.

Enabling Reporting

The basic data collection of the Reporting feature is always enabled,
but the report-entry collection feature is disabled by default. To
enable the report-entry collection feature, use the
``tc.report_enable()`` method. To disable reporting, use the
``tc.report_disable()`` method.

Statistics

The ``tc.report.stats`` properties method provides an overview of the
script results.

Failed Reports
~~~~~~~~~~~~~~

Python SDK failed reports example:

.. code:: python


    for fail in tc.report.failures:
        print(fail)

Sample Failed-Report Output:

.. code:: text

    _Report Entry_

    Properties                              
    Status Code
    : 404                                               
    Fail Msg
    : {"status":"Failure","message":"The requested resource was not found"}
    Description
    : api filter by incident id 708996                  
    Resource Type
    : ResourceType.ADVERSARIES                          

    HTTP Settings                           
      HTTP Method                 
      GET                                               
      Request URI
      /v2/groups/incidents/708996/groups/adversaries    
      Request URL
      https://tc.sumx.us/api/v2/groups/incidents/708996/groups/adversaries?resultStart=0&resultLimit=500&createActivityLog=false
      Content Type                 None                                              
      Body                         None                                              

    Payload                                 
      Payload
      {'resultStart': 0, 'resultLimit': 500, 'createActivityLog': 'false'}

All API requests and Post Filters are stored as a report entry in the
Reports object. Any request that does not receive a status code of 200,
201 or 202, is stored as a failed-report entry and can be retrieved with
the ``tc.report.failures`` property method. This feature helps debug
issues when receiving failures while communicating with the API.

Other Reporting Features
~~~~~~~~~~~~~~~~~~~~~~~~

API Calls

The number of API calls can be retrieved using the
``tc.report.api_calls`` property method of the Report object.

Runtime

The script execution time can be retrieved using the
``tc.report.runtime`` property method of the Report object. This method
can be called anytime during the script execution to get the current
runtime and at the end of the script to get the total runtime.

Request Time

The time spent on API requests can be retrieved using the
``tc.report.request_time`` property method of the Report object.

Report Entries

All report entries can be accessed via the Report generator. By
iterating over ``tc.report``, each individual report entry will be
returned. These report entries can be printed and the individual
properties can be accessed.