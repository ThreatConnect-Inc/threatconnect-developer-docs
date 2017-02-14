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

    read configuration file
    config = ConfigParser.RawConfigParser()
    config.read('threatconnect.conf')

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

     1 [threatconnect]
     2 api_access_id = 12345678900987654321
     3 api_default_org = Acme Corp
     4 api_secret_key = aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz!@#$%^&*()-=
     5 api_base_url = https://api.threatconnect.com

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

    import ConfigParser
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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``import ConfigParser``  | Import the ConfigParser module used to read the |
|                          | configuration file.                             |
+--------------------------+-------------------------------------------------+
| ``from threatconnect imp | Import the ThreatConnect Python SDK module.     |
| ort ThreatConnect``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``config = ConfigParser. | Get an instance of ConfigParser.                |
| RawConfigParser()``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``config.read(config_fil | Parse the configuration file containing the API |
| e)``                     | settings.                                       |
+--------------------------+-------------------------------------------------+
| ``api_access_id = config | Get the configuration items from the config     |
| .get('threatco...``      | instance.                                       |
+--------------------------+-------------------------------------------------+
| ``tc = ThreatConnect(api | Instantiate an instance of the ThreatConnect    |
| _access_id, ap...``      | Class.                                          |
+--------------------------+-------------------------------------------------+
| ``owners = tc.owners()`` | Create an Owner's container object.             |
+--------------------------+-------------------------------------------------+
| ``owners.retrieve()``    | Trigger an API request to retrieve Owners.      |
+--------------------------+-------------------------------------------------+
| ``for owner in owners:`` | Iterate through Owner's generator.              |
+--------------------------+-------------------------------------------------+
| ``print(owner.id)``      | Display the **'id'** property of the Owner.     |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc.set_tcl_file('log/t | Set the destination log path and logging level. |
| c.log', 'debug')``       |                                                 |
+--------------------------+-------------------------------------------------+
| ``tc.set_tcl_console_lev | Set the console logging level.                  |
| el('info')``             |                                                 |
+--------------------------+-------------------------------------------------+

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

+--------------+-------------------------------------------------------------+
| ThreatConnec | Description                                                 |
| t            |                                                             |
| Parameter    |                                                             |
+==============+=============================================================+
| ``tc_log_pat | Log path for the specific instance of the job execution.    |
| h``          |                                                             |
+--------------+-------------------------------------------------------------+
| ``tc_tmp_pat | Temporary storage path for the specific instance of the job |
| h``          | execution.                                                  |
+--------------+-------------------------------------------------------------+
| ``tc_out_pat | Output path for the specific instance of the job execution. |
| h``          |                                                             |
+--------------+-------------------------------------------------------------+
| ``tc_api_pat | Path to the ThreatConnect API server.                       |
| h``          |                                                             |
+--------------+-------------------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversaries = tc.adver | Instantiate an Adversaries container object.    |
| saries()``               |                                                 |
+--------------------------+-------------------------------------------------+
| ``filter1 = adversaries. | Add a filter object to the Adversaries          |
| add_filter()``           | container object (support multiple filter       |
|                          | objects).                                       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_tag('EXAMP | Add API filter to retrieve Adversaries with the |
| LE')``                   | 'Example' tag.                                  |
+--------------------------+-------------------------------------------------+
| ``adversaries.retrieve() | Trigger the API request and retrieve the        |
| ``                       | Adversaries intelligence data.                  |
+--------------------------+-------------------------------------------------+
| ``for adversary in adver | Iterate over the Adversaries container object   |
| saries:``                | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(adversary.id)``  | Display the **'id'** property of the Adversary  |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+-------------------------+----------+------------------------------------------+
| Filter                  | Value    | Description                              |
|                         | Type     |                                          |
+=========================+==========+==========================================+
| ``add_pf_attribute()``  | str      | Filter Indicators on Attribute type.     |
+-------------------------+----------+------------------------------------------+
| ``add_pf_confidence()`` | int      | Filter Indicators on Confidence value.   |
+-------------------------+----------+------------------------------------------+
| ``add_pf_date_added()`` | str      | Filter Indicators on date added.         |
+-------------------------+----------+------------------------------------------+
| ``add_pf_last_modified( | str      | Filter Indicators on last modified date. |
| )``                     |          |                                          |
+-------------------------+----------+------------------------------------------+
| ``add_pf_rating()``     | str      | Filter Indicators on Rating.             |
+-------------------------+----------+------------------------------------------+
| ``add_pf_tag()``        | str      | Filter Indicators on Tag.                |
+-------------------------+----------+------------------------------------------+
| ``add_pf_threat_assess_ | int      | Filter Indicators on Threat Assess       |
| confidence()``          |          | Confidence.                              |
+-------------------------+----------+------------------------------------------+
| ``add_pf_threat_assess_ | str      | Filter Indicators on Threat Assess       |
| rating()``              |          | Rating.                                  |
+-------------------------+----------+------------------------------------------+
| ``add_pf_type()``       | str      | Filter Indicators on Indicator type.     |
+-------------------------+----------+------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id,...``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicators = tc.indica | Instantiate an Indicators container object.     |
| tors()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``filter1 = indicator.ad | Add a filter object to the Indicators container |
| d_filter()``             | object (support multiple filter objects).       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_tag('EXAMP | Add API filter to retrieve Indicators with the  |
| LE')``                   | 'Example' tag.                                  |
+--------------------------+-------------------------------------------------+
| ``indicator.retrieve()`` | Trigger the API request and retrieve the        |
|                          | Indicators intelligence data.                   |
+--------------------------+-------------------------------------------------+
| ``for indicator in indic | Iterate over the Indicators container object    |
| ators:``                 | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(indicator.indica | Display the **'indicator'** property of the     |
| tor)``                   | Indicator object.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``for attribute in indic | Iterate over the Attribute property object      |
| ator.attributes:``       | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(attribute.type)` | Display the **'type'** property of the          |
| `                        | Attribute object.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``indicator.load_securit | Trigger API call to load the Security Label     |
| y_label()``              | into the Indicator object.                      |
+--------------------------+-------------------------------------------------+
| ``if indicator.security_ | Ensure the object has been loaded before        |
| label is not ...``       | displaying properties.                          |
+--------------------------+-------------------------------------------------+
| ``print(indicator.securi | Display the **'name'** property of the Security |
| ty_label.name)``         | Label object.                                   |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``for tag in indicator.t | Iterate over the Attribute property object      |
| ags:``                   | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(tag.name)``      | Display the **'name'** property of the          |
|                          | Attribute object.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``for g_associations in  | Trigger API call to retrieve all Groups         |
| indicator.grou...``      | associated with this Indicator.                 |
+--------------------------+-------------------------------------------------+
| ``print(g_association.id | Display the **'id'** property of the associated |
| )``                      | Group object.                                   |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``for i_association in i | Trigger API call to retrieve all Indicators     |
| ndicator.ind_...``       | associated with this Indicator.                 |
+--------------------------+-------------------------------------------------+
| ``print(i_association.id | Display the **'id'** property of the associated |
| )``                      | Indicator object.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``for v_associations in  | Trigger API call to retrieve all Victims        |
| indicator.vic_...``      | associated with this Indicator.                 |
+--------------------------+-------------------------------------------------+
| ``print(v_association.id | Display the **'id'** property of the associated |
| )``                      | Victim object.                                  |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``documents = tc.documen | Instantiate a Documents container object.       |
| ts()``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``filter1 = documents.ad | Add a filter object to the Documents container  |
| d_filter()``             | object (support multiple filter objects).       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_tag('EXAMP | Add API filter to retrieve Documents with the   |
| LE')``                   | 'Example' tag                                   |
+--------------------------+-------------------------------------------------+
| ``documents.retrieve()`` | Trigger the API request and retrieve the        |
|                          | Documents intelligence data.                    |
+--------------------------+-------------------------------------------------+
| ``for document in docume | Iterate over the Documents container object     |
| nts:``                   | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(document.id)``   | Display the **'id'** property of the Document   |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``document.download()``  | Trigger API request to download the Document    |
|                          | contents.                                       |
+--------------------------+-------------------------------------------------+
| ``if document.contents i | Validate the Document has downloaded before     |
| s not None:``            | displaying.                                     |
+--------------------------+-------------------------------------------------+
| ``print(document.content | Display the contents of the Document. (This     |
| s)``                     | should only be done for ASCII contents.)        |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``emails = tc.emails()`` | Instantiate an Emails container object.         |
+--------------------------+-------------------------------------------------+
| ``filter1 = emails.add_f | Add a Filter object to the Emails container     |
| ilter()``                | object (support multiple filter objects).       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_tag('EXAMP | Add API Filter to be applied to the API         |
| LE')``                   | request.                                        |
+--------------------------+-------------------------------------------------+
| ``emails.retrieve()``    | Trigger the API request and retrieve the Emails |
|                          | intelligence data.                              |
+--------------------------+-------------------------------------------------+
| ``for email in emails:`` | Iterate over the Emails container object        |
|                          | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(email.id)``      | Display the **'id'** property of the Email      |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``groups = tc.groups()`` | Instantiate a Groups container object.          |
+--------------------------+-------------------------------------------------+
| ``filter1 = groups.add_f | Add a filter object to the Groups container     |
| ilter()``                | object (support multiple filter objects).       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_tag('EXAMP | Add API filter to retrieve Groups with the      |
| LE')``                   | 'Example' tag.                                  |
+--------------------------+-------------------------------------------------+
| ``groups.retrieve()``    | Trigger the API request and retrieve the Groups |
|                          | intelligence data.                              |
+--------------------------+-------------------------------------------------+
| ``for group in groups:`` | Iterate over the Groups container object        |
|                          | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(group.id)``      | Display the **'id'** property of the Group      |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``incidents = tc.inciden | Instantiate an Incidents container object.      |
| ts()``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``filter1 = incidents.ad | Add a filter object to the Incidents container  |
| d_filter()``             | object (support multiple filter objects).       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_tag('EXAMP | Add API filter to retrieve Incidents with the   |
| LE')``                   | 'Example' tag.                                  |
+--------------------------+-------------------------------------------------+
| ``incidents.retrieve()`` | Trigger the API request and retrieve the        |
|                          | Incidents intelligence data.                    |
+--------------------------+-------------------------------------------------+
| ``for incident in incide | Iterate over the Incidents container object     |
| nts:``                   | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(incident.id)``   | Display the **'id'** property of the Incidents  |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+-------------------------+----------+------------------------------------------+
| Filter                  | Value    | Description                              |
|                         | Type     |                                          |
+=========================+==========+==========================================+
| ``add_pf_attribute()``  | str      | Filter Indicators on Attribute type.     |
+-------------------------+----------+------------------------------------------+
| ``add_pf_confidence()`` | int      | Filter Indicators on Confidence value.   |
+-------------------------+----------+------------------------------------------+
| ``add_pf_date_added()`` | str      | Filter Indicators on date added.         |
+-------------------------+----------+------------------------------------------+
| ``add_pf_last_modified( | str      | Filter Indicators on last modified date. |
| )``                     |          |                                          |
+-------------------------+----------+------------------------------------------+
| ``add_pf_rating()``     | str      | Filter Indicators on Rating.             |
+-------------------------+----------+------------------------------------------+
| ``add_pf_tag()``        | str      | Filter Indicators on Tag.                |
+-------------------------+----------+------------------------------------------+
| ``add_pf_threat_assess_ | int      | Filter Indicators on Threat Assess       |
| confidence()``          |          | Confidence.                              |
+-------------------------+----------+------------------------------------------+
| ``add_pf_threat_assess_ | str      | Filter Indicators on Threat Assess       |
| rating()``              |          | Rating.                                  |
+-------------------------+----------+------------------------------------------+
| ``add_pf_type()``       | str      | Filter Indicators on Indicator type.     |
+-------------------------+----------+------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id,...``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicators = tc.indica | Instantiate an Indicators container object.     |
| tors()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``filter1 = indicator.ad | Add a filter object to the Indicators container |
| d_filter()``             | object (support multiple filter objects).       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_tag('EXAMP | Add API filter to retrieve Indicators with the  |
| LE')``                   | 'Example' tag.                                  |
+--------------------------+-------------------------------------------------+
| ``indicator.retrieve()`` | Trigger the API request and retrieve the        |
|                          | Indicators intelligence data.                   |
+--------------------------+-------------------------------------------------+
| ``for indicator in indic | Iterate over the Indicators container object    |
| ators:``                 | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(indicator.indica | Display the **'indicator'** property of the     |
| tor)``                   | Indicator object.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``indicator.load_attribu | Trigger API call to load Attributes into the    |
| tes()``                  | Indicator object.                               |
+--------------------------+-------------------------------------------------+
| ``for attribute in indic | Iterate over the Attribute property object      |
| ator.attributes:``       | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(attribute.type)` | Display the **'type'** property of the          |
| `                        | Attribute object.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``indicator.load_securit | Trigger API call to load the Security Label     |
| y_label()``              | into the Indicator object.                      |
+--------------------------+-------------------------------------------------+
| ``if indicator.security_ | Ensure the object has been loaded before        |
| label is not ...``       | displaying properties.                          |
+--------------------------+-------------------------------------------------+
| ``print(indicator.securi | Display the **'name'** property of the Security |
| ty_label.name)``         | Label object.                                   |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``indicator.load_tags()` | Trigger API call to load Tags into the          |
| `                        | Indicator object.                               |
+--------------------------+-------------------------------------------------+
| ``for tag in indicator.t | Iterate over the Attribute property object      |
| ags:``                   | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(tag.name)``      | Display the **'name'** property of the          |
|                          | Attribute object.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``for g_associations in  | Trigger API call to retrieve all Groups         |
| indicator.grou...``      | associated with this Indicator.                 |
+--------------------------+-------------------------------------------------+
| ``print(g_association.id | Display the **'id'** property of the associated |
| )``                      | Group object.                                   |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``for i_association in i | Trigger API call to retrieve all Indicators     |
| ndicator.ind_...``       | associated with this Indicator.                 |
+--------------------------+-------------------------------------------------+
| ``print(i_association.id | Display the **'id'** property of the associated |
| )``                      | Indicator object.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``for v_associations in  | Trigger API call to retrieve all Victims        |
| indicator.vic_..``       | associated with this Indicator.                 |
+--------------------------+-------------------------------------------------+
| ``print(v_association.id | Display the **'id'** property of the associated |
| )``                      | Victim object.                                  |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``indicator.load_dns_res | Trigger API call to load DNS Resolutions into   |
| olutions()``             | the Indicator object.                           |
+--------------------------+-------------------------------------------------+
| ``for dns in indicator.d | Iterate over the DNS Resolutions property       |
| ns_resolutions:``        | object generator.                               |
+--------------------------+-------------------------------------------------+
| ``print(dns.ip)``        | Display the **'ip'** property of the Attribute  |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``signatures = tc.signat | Instantiate an Signatures container object.     |
| ures()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``filter1 = signatures.a | Add a filter object to the Signatures container |
| dd_filter()``            | object (support multiple filter objects).       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_tag('EXAMP | Add API filter to retrieve Signatures with the  |
| LE')``                   | 'Example' tag.                                  |
+--------------------------+-------------------------------------------------+
| ``signatures.retrieve()` | Trigger the API request and retrieve the        |
| `                        | Signatures intelligence data.                   |
+--------------------------+-------------------------------------------------+
| ``for signature in signa | Iterate over the Signatures container object    |
| tures:``                 | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(signature.id)``  | Display the **'id'** property of the Signature  |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``signature.download()`` | Trigger API request to download the Signature   |
|                          | contents.                                       |
+--------------------------+-------------------------------------------------+
| ``if signature.contents  | Validate that the Signature has downloaded      |
| is not None:``           | before displaying.                              |
+--------------------------+-------------------------------------------------+
| ``print(signature.conten | Display the contents of the Signature.          |
| ts)``                    |                                                 |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``Tasks = tc.Tasks()``   | Instantiate a Tasks container object.           |
+--------------------------+-------------------------------------------------+
| ``filter1 = Tasks.add_fi | Add a filter object to the Tasks container      |
| lter()``                 | object (support multiple filter objects).       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_tag('EXAMP | Add an API filter to be applied to the API      |
| LE')``                   | request.                                        |
+--------------------------+-------------------------------------------------+
| ``Tasks.retrieve()``     | Trigger the API request and retrieve the        |
|                          | Tasks-intelligence data.                        |
+--------------------------+-------------------------------------------------+
| ``for task in Tasks:``   | Iterate over the Tasks container object         |
|                          | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(task.id)``       | Display the **id** property of the Task object. |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``threats = tc.threats() | Instantiate a Threats container object.         |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``filter1 = threats.add_ | Add a filter object to the Threats container    |
| filter()``               | object (support multiple filter objects).       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_tag('EXAMP | Add API filter to retrieve Threats with the     |
| LE')``                   | 'Example' tag.                                  |
+--------------------------+-------------------------------------------------+
| ``threats.retrieve()``   | Trigger the API request and retrieve the        |
|                          | Threats intelligence data.                      |
+--------------------------+-------------------------------------------------+
| ``for threat in threats: | Iterate over the Threats container object       |
| ``                       | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(threat.id)``     | Display the **id** property of the Threat       |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``victims = tc.victims() | Instantiate a Victims container object.         |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``filter1 = victims.add_ | Add a filter object to the Victims container    |
| filter()``               | object (support multiple filter objects).       |
+--------------------------+-------------------------------------------------+
| ``filter1.add_adversary_ | Add API filter to retrieve Victims associated   |
| id(531)``                | with the given Adversary.                       |
+--------------------------+-------------------------------------------------+
| ``victims.retrieve()``   | Trigger the API request and retrieve the        |
|                          | Victims intelligence data.                      |
+--------------------------+-------------------------------------------------+
| ``for victim in victims: | Iterate over the Victims container object       |
| ``                       | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(victim.id)``     | Display the **id** property of the Victim       |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``victim.load_assets()`` | Trigger API call to load Assets into the        |
|                          | Resource object.                                |
+--------------------------+-------------------------------------------------+
| ``for asset in victim.as | Iterate over the Assets object generator.       |
| sets:``                  |                                                 |
+--------------------------+-------------------------------------------------+
| ``print(asset.id)``      | Display the **id** property of the Asset        |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate an Resources container object.      |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources.retrieve()`` | Trigger API calls to retrieve the Resources.    |
+--------------------------+-------------------------------------------------+
| ``for resource in resour | Iterate over the Resources container object     |
| ces:``                   | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(resource.id)``   | Display the **id** property of the Resource     |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+
| ``for g_associations in  | Trigger an API call to retrieve all Groups      |
| resource.group_...``     | associated with this Resource.                  |
+--------------------------+-------------------------------------------------+
| ``print(g_association.id | Display the **id** property of the associated   |
| )``                      | Group object.                                   |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate an Resources container object.      |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources.retrieve()`` | Trigger API calls to retrieve the Resources.    |
+--------------------------+-------------------------------------------------+
| ``for resource in resour | Iterate over the Resources container object     |
| ces:``                   | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(resource.id)``   | Display the **id** property of the Resource     |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+
| ``for associations in re | Trigger API call to retrieve all Indicators     |
| source.indicat_...``     | associated with this Resource.                  |
+--------------------------+-------------------------------------------------+
| ``print(association.id)` | Display the **'id'** property of the associated |
| `                        | Indicator object.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate an Resources container object.      |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources.retrieve()`` | Trigger API calls to retrieve the Resources.    |
+--------------------------+-------------------------------------------------+
| ``for resource in resour | Iterate over the Resources container object     |
| ces:``                   | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(resource.id)``   | Display the **id** property of the Resource     |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+
| ``for associations in re | Trigger API call to retrieve all Victims        |
| source.victim_...``      | associated with this Resource.                  |
+--------------------------+-------------------------------------------------+
| ``print(v_association.id | Display the **id** property of the associated   |
| )``                      | Victim object.                                  |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources.retrieve()`` | Trigger the API request and retrieve the        |
|                          | Resources intelligence data.                    |
+--------------------------+-------------------------------------------------+
| ``for resource in resour | Iterate over the Resources container object     |
| ces:``                   | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(resource.id)``   | Display the **id** property of the Resource     |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+
| ``resource.load_attribut | Trigger API call to load Attributes into the    |
| es()``                   | Resource object.                                |
+--------------------------+-------------------------------------------------+
| ``for attribute in resou | Iterate over the Attribute property object      |
| rce.attributes:``        | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(attribute.type)` | Display the **'type'** property of the          |
| `                        | Attribute object.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate an Resources container object.      |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources.retrieve()`` | Trigger the API request and retrieve the        |
|                          | Resources intelligence data.                    |
+--------------------------+-------------------------------------------------+
| ``for resource in resour | Iterate over the Resources container object     |
| ces:``                   | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(resource.id)``   | Display the **id** property of the Resource     |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+
| ``resource.load_security | Trigger API call to load the Security Label     |
| _label()``               | into the Resource object.                       |
+--------------------------+-------------------------------------------------+
| ``if resource.security_l | Ensure the object has been loaded before        |
| abel is not None:``      | displaying properties.                          |
+--------------------------+-------------------------------------------------+
| ``print(resource.securit | Display the **'name'** property of the Security |
| y_label.name)``          | Label object.                                   |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate an Resources container object.      |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources.retrieve()`` | Trigger API calls to retrieve the Resources.    |
+--------------------------+-------------------------------------------------+
| ``for resource in resour | Iterate over the Resources container object     |
| ces:``                   | generator.                                      |
+--------------------------+-------------------------------------------------+
| ``print(resource.id)``   | Display the **id** property of the Resource     |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+
| ``resource.load_tags()`` | Trigger API call to load Tags into the Resource |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+
| ``for tag in resource.ta | Iterate over the Tag property object generator. |
| gs:``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``print(tag.name)``      | Display the **'name'** property of the Tag      |
|                          | object.                                         |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversaries = tc.adver | Instantiate an Adversaries container object.    |
| saries()``               |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversary = adversarie | Add a resource object setting the name and      |
| s.add('New Adve...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``adversary.add_attribut | Add an Attribute of type **Description** to the |
| e('Description'...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``adversary.add_tag('EXA | Add a Tag to the Adversary.                     |
| MPLE')``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversary.set_security | Add a Security Label to the Adversary.          |
| _label('TLP Gre...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversaries = tc.adver | Instantiate an Adversaries container object.    |
| saries()``               |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversary = adversarie | Add a resource object setting the name and      |
| s.add('Updated ...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``adversary.set_id(20)`` | Set the ID of the Adversary to the              |
|                          | ***EXISTING*** Adversary ID to update.          |
+--------------------------+-------------------------------------------------+
| ``adversary.load_attribu | Load existing Attributes into the Adversary     |
| tes()``                  | object.                                         |
+--------------------------+-------------------------------------------------+
| ``adversary.delete_attri | Add a delete flag on the Attribute with type    |
| bute(attribute.id)``     | **Description**.                                |
+--------------------------+-------------------------------------------------+
| ``adversary.add_attribut | Add an Attribute of type **Description** to the |
| e('Description'...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``adversary.load_tags()` | Load existing Tags into the Adversary object.   |
| `                        |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversary.delete_tag(t | Add a delete flag to all Tags.                  |
| ag.name)``               |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversary.add_tag('EXA | Add a Tag to the Resource.                      |
| MPLE')``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversary.commit()``   | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversaries = tc.adver | Instantiate an Adversaries container object.    |
| saries()``               |                                                 |
+--------------------------+-------------------------------------------------+
| ``adversary = adversarie | Add a resource object setting the name and      |
| s.add('', owner)``       | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``adversary.set_id(20)`` | Set the ID of the Adversary to the **EXISTING** |
|                          | Adversary ID to delete.                         |
+--------------------------+-------------------------------------------------+
| ``adversary.delete()``   | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``batch_jobs = dst_tc.ba | Instantiate a Batch Job container object.       |
| tch_jobs()``             |                                                 |
+--------------------------+-------------------------------------------------+
| ``for batch in indicator | Iterator through an array of arrays of          |
| s:``                     | indicator objects.                              |
+--------------------------+-------------------------------------------------+
| ``batch_job.set_...``    | Configure batch job to process as many          |
|                          | indicators as possible without aborting.        |
+--------------------------+-------------------------------------------------+
| ``batch_job.upload(json. | Upload job with indicator chunk as JSON data.   |
| dumps(batch))``          |                                                 |
+--------------------------+-------------------------------------------------+
| ``batch_job.commit()``   | Start batch job with configuration and data     |
|                          | defined.                                        |
+--------------------------+-------------------------------------------------+
| ``while len(batch_ids) > | Begin polling for batch status until all        |
|  0:``                    | pending batches are complete.                   |
+--------------------------+-------------------------------------------------+
| ``filter.add_id(batchId) | Add current batchId to filter.                  |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``for batch_job in batch | Get job for filtered batch ID.                  |
| _jobs:``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``if batch_job.status == | Check job status completion.                    |
|  'Completed':``          |                                                 |
+--------------------------+-------------------------------------------------+
| ``for batch_job in finis | Iterate through the finished batches for status |
| hed_batches:``           | print.                                          |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``documents = tc.documen | Instantiate a Documents container object.       |
| ts()``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``document = documents.a | Add a resource object setting the name and      |
| dd('New Documen...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``document.set_file_name | **(REQUIRED)** Set the Document file name.      |
| ('New File.txt')``       |                                                 |
+--------------------------+-------------------------------------------------+
| ``fh = open('./sample1.z | Open the file handle.                           |
| ip', 'rb')``             |                                                 |
+--------------------------+-------------------------------------------------+
| ``contents = fh.read()`` | Read contents of file from file handle.         |
+--------------------------+-------------------------------------------------+
| ``document.upload(conten | **Upload** file contents.                       |
| ts)``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``document.add_attribute | Add an Attribute of type **Description** to the |
| ('Description',...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``document.add_tag('EXAM | Add a Tag to the Document.                      |
| PLE')``                  |                                                 |
+--------------------------+-------------------------------------------------+
| ``document.set_security_ | Add a Security Label to the Document.           |
| label('TLP Green')``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``document.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``documents = tc.documen | Instantiate a Documents container object.       |
| ts()``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``document = documents.a | Add a Resource object setting the name and      |
| dd('Updated Doc...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``document.set_id(20)``  | Set the ID of the Document to the               |
|                          | ***EXISTING*** Document ID to update.           |
+--------------------------+-------------------------------------------------+
| ``document.load_attribut | Load existing Attributes into the Document      |
| es()``                   | object.                                         |
+--------------------------+-------------------------------------------------+
| ``document.delete_attrib | Add a delete flag on the Attribute with type    |
| ute(attribute.id)``      | **Description**.                                |
+--------------------------+-------------------------------------------------+
| ``document.add_attribute | Add an Attribute of type **Description** to the |
| ('Description',...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``document.load_tags()`` | Load existing Tags into the Document object.    |
+--------------------------+-------------------------------------------------+
| ``document.delete_tag(ta | Add a delete flag to all Tags.                  |
| g.name)``                |                                                 |
+--------------------------+-------------------------------------------------+
| ``document.add_tag('EXAM | Add a Tag to the Resource.                      |
| PLE')``                  |                                                 |
+--------------------------+-------------------------------------------------+
| ``document.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``documents = tc.documen | Instantiate a Documents container object.       |
| ts()``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``document = documents.a | Add a Resource object setting the name and      |
| dd('', owner)``          | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``document.set_id(20)``  | Set the ID of the Document to the **EXISTING**  |
|                          | Document ID to delete.                          |
+--------------------------+-------------------------------------------------+
| ``document.delete()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``emails = tc.emails()`` | Instantiate an Emails container object.         |
+--------------------------+-------------------------------------------------+
| ``email = emails.add('Ne | Add a Resource object setting the name and      |
| w Email', ...``          | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``email.set_body('This i | **(REQUIRED)** Set the Email body.              |
| s an email body...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``email.set_from_address | **(OPTIONAL)** Set the Email from address.      |
| ('bad_guy@badgu...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``email.set_header('This | **(REQUIRED)** Set the Email header.            |
|  is an improper...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``email.set_subject('Thi | **(REQUIRED)** Set the Email subject.           |
| s is an email s...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``email.set_to('victim@g | **(OPTIONAL)** Set the Email to address.        |
| oodguys.com')``          |                                                 |
+--------------------------+-------------------------------------------------+
| ``email.add_attribute('D | Add an Attribute of type **Description** to the |
| escription', 'D...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``email.add_tag('EXAMPLE | Add a Tag to the Email.                         |
| ')``                     |                                                 |
+--------------------------+-------------------------------------------------+
| ``email.set_security_lab | Add a Security Label to the Email.              |
| el('TLP Green')``        |                                                 |
+--------------------------+-------------------------------------------------+
| ``email.commit()``       | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``emails = tc.emails()`` | Instantiate an Emails container object.         |
+--------------------------+-------------------------------------------------+
| ``email = emails.add('Up | Add a Resource object setting the name and      |
| dated Email', o...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``email.set_id(20)``     | Set the ID of the Email to the ***EXISTING***   |
|                          | Email ID to update.                             |
+--------------------------+-------------------------------------------------+
| ``email.load_attributes( | Load existing Attributes into the Email object. |
| )``                      |                                                 |
+--------------------------+-------------------------------------------------+
| ``email.delete_attribute | Add a delete flag on the Attribute with type    |
| (attribute.id)``         | **Description**.                                |
+--------------------------+-------------------------------------------------+
| ``email.add_attribute('D | Add an Attribute of type **Description** to the |
| escription', 'U...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``email.load_tags()``    | Load existing Tags into the Email object.       |
+--------------------------+-------------------------------------------------+
| ``email.delete_tag(tag.n | Add a delete flag to all Tags.                  |
| ame)``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``email.add_tag('EXAMPLE | Add a Tag to the Resource.                      |
| ')``                     |                                                 |
+--------------------------+-------------------------------------------------+
| ``email.commit()``       | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``emails = tc.emails()`` | Instantiate an Emails container object.         |
+--------------------------+-------------------------------------------------+
| ``email = emails.add('', | Add a Resource object setting the name and      |
|  owner)``                | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``email.set_id(20)``     | Set the ID of the Email to the **EXISTING**     |
|                          | Email ID to delete.                             |
+--------------------------+-------------------------------------------------+
| ``email.delete()``       | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``incidents = tc.inciden | Instantiate an Incidents container object.      |
| ts()``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``incident = incidents.a | Add a Resource object setting the name and      |
| dd('New Incident')``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``incident.set_event_dat | **(REQUIRED)** Set event date of Incident.      |
| e('2015-03-21T0...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``incident.add_attribute | Add an Attribute of type **Description** to the |
| ('Description' ...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``incident.add_tag('EXAM | Add a Tag to the Incident.                      |
| PLE')``                  |                                                 |
+--------------------------+-------------------------------------------------+
| ``incident.set_security_ | Add a Security Label to the Incident.           |
| label('TLP Green')``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``incident.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``incidents = tc.inciden | Instantiate an Incidents container object.      |
| ts()``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``incident = incidents.a | Add a Resource object setting the name and      |
| dd('Updated Inc...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``incident.set_id(20)``  | Set the ID of the Incident to the               |
|                          | ***EXISTING*** Incident ID to update.           |
+--------------------------+-------------------------------------------------+
| ``incident.load_attribut | Load existing Attributes into the Incident      |
| es()``                   | object.                                         |
+--------------------------+-------------------------------------------------+
| ``incident.delete_attrib | Add a delete flag to the Attribute with type    |
| ute(attribute.id)``      | **Description**.                                |
+--------------------------+-------------------------------------------------+
| ``incident.add_attribute | Add an Attribute of type **Description** to the |
| ('Description' ...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``incident.load_tags()`` | Load existing Tags into the Incident object.    |
+--------------------------+-------------------------------------------------+
| ``incident.delete_tag(ta | Add a delete flag to all Tags.                  |
| g.name)``                |                                                 |
+--------------------------+-------------------------------------------------+
| ``incident.add_tag('EXAM | Add a Tag to the Resource.                      |
| PLE')``                  |                                                 |
+--------------------------+-------------------------------------------------+
| ``incident.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``incidents = tc.inciden | Instantiate an Incidents container object.      |
| ts()``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``incident = incidents.a | Add a Resource object setting the name and      |
| dd('', owner)``          | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``incident.set_id(20)``  | Set the ID of the Incident to the **EXISTING**  |
|                          | Incident ID to delete.                          |
+--------------------------+-------------------------------------------------+
| ``incident.delete()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id,...``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicators = tc.indica | Instantiate an Indicator container object.      |
| tors()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator = indicators | Add a Resource object setting the value and     |
| .add('4.3.254....``      | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``indicator.set_confiden | Set the Confidence value for this Indicator.    |
| ce(75)``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_rating(2 | Set the Rating value for this Indicator.        |
| .5)``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.add_attribut | Add an Attribute of type **Description** to the |
| e('Description...``      | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``indicator.add_tag('EXA | Add a Tag to the Resource.                      |
| MPLE')``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_security | Add a Security Label to the Resource.           |
| _label('TLP Gre..``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.commit()``   | Trigger multiple API calls to write Resource,   |
|                          | Attributes, Security Labels, and Tags.          |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id,...``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicators = tc.indica | Instantiate an Indicator container object.      |
| tors()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator = indicators | Add a Resource object setting the value and     |
| .add('badguy@....``      | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``indicator.set_confiden | Set the Confidence value for this Indicator.    |
| ce(75)``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_rating(2 | Set the Rating value for this Indicator.        |
| .5)``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.add_attribut | Add an Attribute of type **Description** to the |
| e('Description...``      | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``indicator.add_tag('EXA | Add a Tag to the Resource.                      |
| MPLE')``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_security | Add a Security Label to the Resource.           |
| _label('TLP Gre..``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.commit()``   | Trigger multiple API calls to write Resource,   |
|                          | Attributes, Security Labels, and Tags.          |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id,...``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator = indicators | Add an Indicator object setting the value and   |
| .add('8743b520...``      | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``indicator.set_indicato | Add File addition File Hashes for this          |
| r('b89eaac7e61...``      | Indicator.                                      |
+--------------------------+-------------------------------------------------+
| ``indicator.set_indicato | Add File addition File Hashes for this          |
| r('127e6fbfe24...``      | Indicator.                                      |
+--------------------------+-------------------------------------------------+
| ``indicator.set_confiden | Set the Confidence value for this Indicator.    |
| ce(75)``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_rating(2 | Set the Rating value for this Indicator.        |
| .5)``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_size(112 | Set the File size property of the Indicator.    |
| )``                      |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.add_attribut | Add an Attribute of type **Description** to the |
| e('Description...``      | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``indicator.add_tag('EXA | Add a Tag to the Indicator.                     |
| MPLE')``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_security | Add a Security Label to the Indicator.          |
| _label('TLP Gre..``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.commit()``   | Trigger multiple API calls to write Indicator,  |
|                          | Attributes, Security Labels, and Tags.          |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id,...``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicators = tc.indica | Instantiate an Indicator container object.      |
| tors()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator = indicators | Add a Resource object setting the value and     |
| .add('badguy.....``      | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``indicator.set_confiden | Set the Confidence value for this Indicator.    |
| ce(75)``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_rating(2 | Set the Rating value for this Indicator.        |
| .5)``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.add_attribut | Add an Attribute of type **Description** to the |
| e('Description...``      | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``indicator.add_tag('EXA | Add a Tag to the Resource.                      |
| MPLE')``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_security | Add a Security Label to the Resource.           |
| _label('TLP Gre..``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.commit()``   | Trigger multiple API calls to write Resource,   |
|                          | Attributes, Security Labels, and Tags.          |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id,...``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicators = tc.indica | Instantiate an Indicator container object.      |
| tors()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator = indicators | Add a Resource object setting the value and     |
| .add('badguy.....``      | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``indicator.set_confiden | Set the Confidence value for this Indicator.    |
| ce(75)``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_rating(2 | Set the Rating value for this Indicator.        |
| .5)``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.add_attribut | Add an Attribute of type **Description** to the |
| e('Description...``      | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``indicator.add_tag('EXA | Add a Tag to the Resource.                      |
| MPLE')``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.set_security | Add a Security Label to the Resource.           |
| _label('TLP Gre..``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator.commit()``   | Trigger multiple API calls to write Resource,   |
|                          | Attributes, Security Labels, and Tags.          |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id,...``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicators = tc.indica | Instantiate an Indicator container object.      |
| tors()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``indicator = indicators | Add a Resource object setting the value and     |
| .add('4.3.2.1...``       | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``indicator.delete()``   | Trigger API calls to delete the Resource.       |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``signatures = tc.signat | Instantiate a Signatures container object.      |
| ures()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature = signatures | Add a Resource object setting the name and      |
| .add('New Signa...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``signature.set_file_nam | **(REQUIRED)** Set file name for Signature.     |
| e('bad_file.txt')``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature.set_file_typ | **(REQUIRED)** Set file type for Signature.     |
| e('YARA')``              |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature.set_file_tex | **(OPTIONAL)** Set file contents for Signature. |
| t(file_text)``           |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature.add_attribut | Add an Attribute of type **Description** to the |
| e('Description'...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``signature.add_tag('EXA | Add a Tag to the Signature.                     |
| MPLE')``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature.set_security | Add a Security Label to the Signature.          |
| _label('TLP Gre...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature.commit()``   | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``signatures = tc.signat | Instantiate a Signatures container object.      |
| ures()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature = signatures | Add a Resource object setting the name and      |
| .add('Updated D...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``signature.set_id(20)`` | Set the ID of the Signature to the              |
|                          | ***EXISTING*** Signature ID to update.          |
+--------------------------+-------------------------------------------------+
| ``signature.load_attribu | Load existing Attributes into the Signature     |
| tes()``                  | object.                                         |
+--------------------------+-------------------------------------------------+
| ``signature.delete_attri | Add a delete flag to the Attribute with type    |
| bute(attribute.id)``     | **Description**.                                |
+--------------------------+-------------------------------------------------+
| ``signature.add_attribut | Add an Attribute of type **Description** to the |
| e('Description'...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``signature.load_tags()` | Load existing Tags into the Signature object.   |
| `                        |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature.delete_tag(t | Add a delete flag to all Tags.                  |
| ag.name)``               |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature.add_tag('EXA | Add a Tag to the Resource.                      |
| MPLE')``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature.commit()``   | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``signatures = tc.signat | Instantiate a Signatures container object.      |
| ures()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``signature = signatures | Add a Resource object setting the name and      |
| .add('', owner)``        | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``signature.set_id(20)`` | Set the ID of the Signature to the **EXISTING** |
|                          | Signature ID to delete.                         |
+--------------------------+-------------------------------------------------+
| ``signature.delete()``   | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``tasks = tc.tasks()``   | Instantiate a Tasks container object.           |
+--------------------------+-------------------------------------------------+
| ``task = tasks.add('New  | Add a Resource object setting the name and      |
| task' own...``           | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``task.add_attribute('De | Add an Attribute of type **Description** to the |
| scription' 'D...``       | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``task.add_tag('EXAMPLE' | Add a Tag to the Task.                          |
| )``                      |                                                 |
+--------------------------+-------------------------------------------------+
| ``task.add_security_labe | Add a Security Label to the task.               |
| l('TLP Green')``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``task.commit()``        | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``tasks = tc.tasks()``   | Instantiate a Tasks container object.           |
+--------------------------+-------------------------------------------------+
| ``task = Tasks.add('Upda | Add a Resource object setting the name and      |
| ted task'...``           | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``task.set_id(20)``      | Set the ID of the task to the ***EXISTING***    |
|                          | task ID to update.                              |
+--------------------------+-------------------------------------------------+
| ``task.load_attributes() | Load existing Attributes into the task object.  |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``task.delete_attribute( | Add a delete flag to the Attribute with type    |
| attribute.id)``          | **Description**.                                |
+--------------------------+-------------------------------------------------+
| ``task.add_attribute('De | Add an Attribute of type **Description** to the |
| scription', '...``       | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``task.load_tags()``     | Load existing Tags into the task object.        |
+--------------------------+-------------------------------------------------+
| ``task.delete_tag(tag.na | Add a delete flag to all Tags.                  |
| me)``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``task.add_tag('EXAMPLE' | Add a Tag to the Resource.                      |
| )``                      |                                                 |
+--------------------------+-------------------------------------------------+
| ``task.commit()``        | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``tasks = tc.tasks()``   | Instantiate a Tasks container object.           |
+--------------------------+-------------------------------------------------+
| ``task = tasks.add('', o | Add a Task Resource setting the name and Owner. |
| wner)``                  |                                                 |
+--------------------------+-------------------------------------------------+
| ``task.set_id(20)``      | Set the ID of the task to the **EXISTING** task |
|                          | ID to delete.                                   |
+--------------------------+-------------------------------------------------+
| ``task.delete()``        | Trigger API calls to delete the task.           |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``threats = tc.threats() | Instantiate a Threats container object.         |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``threat = threats.add(' | Add a Resource object setting the name and      |
| New Threat' own...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``threat.add_attribute(' | Add an Attribute of type **Description** to the |
| Description' 'D...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``threat.add_tag('EXAMPL | Add a Tag to the Threat.                        |
| E')``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``threat.set_security_la | Add a Security Label to the Threat.             |
| bel('TLP Green')``       |                                                 |
+--------------------------+-------------------------------------------------+
| ``threat.commit()``      | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``threats = tc.threats() | Instantiate a Threats container object.         |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``threat = threats.add(' | Add a Resource object setting the name and      |
| Updated Threat'...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``threat.set_id(20)``    | Set the ID of the Threat to the ***EXISTING***  |
|                          | Threat ID to update.                            |
+--------------------------+-------------------------------------------------+
| ``threat.load_attributes | Load existing Attributes into the Threat        |
| ()``                     | object.                                         |
+--------------------------+-------------------------------------------------+
| ``threat.delete_attribut | Add a delete flag to the Attribute with type    |
| e(attribute.id)``        | **Description**.                                |
+--------------------------+-------------------------------------------------+
| ``threat.add_attribute(' | Add an Attribute of type **Description** to the |
| Description', '...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``threat.load_tags()``   | Load existing Tags into the Threat object.      |
+--------------------------+-------------------------------------------------+
| ``threat.delete_tag(tag. | Add a delete flag to all Tags.                  |
| name)``                  |                                                 |
+--------------------------+-------------------------------------------------+
| ``threat.add_tag('EXAMPL | Add a Tag to the Resource.                      |
| E')``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``threat.commit()``      | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``threats = tc.threats() | Instantiate a Threats container object.         |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``threat = threats.add(' | Add a Resource object setting the name and      |
| ', owner)``              | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``threat.set_id(20)``    | Set the ID of the Threat to the **EXISTING**    |
|                          | Threat ID to delete.                            |
+--------------------------+-------------------------------------------------+
| ``threat.delete()``      | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``victims = tc.victims() | Instantiate a Victims container object.         |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``victim = victims.add(' | Add a Resource object setting the name and      |
| Robin Scherbats...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``victim.set_nationality | **(OPTIONAL)** Set Victim nationality.          |
| ('Canadian')``           |                                                 |
+--------------------------+-------------------------------------------------+
| ``victim.set_org('Royal  | **(OPTIONAL)** Set Victim Organization.         |
| Canadian Mounte...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``victim.set_suborg('Que | **(OPTIONAL)** Set Victim Sub-Organization.     |
| bec Office')``           |                                                 |
+--------------------------+-------------------------------------------------+
| ``victim.set_work_locati | **(OPTIONAL)** Set Victim location.             |
| on('Quebec')``           |                                                 |
+--------------------------+-------------------------------------------------+
| ``victim.commit()``      | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``victims = tc.victims() | Instantiate a Victims container object.         |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``victim = victims.add(' | Add a Resource object setting the name and      |
| Updated Victim'...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``victim.set_id(20)``    | Set the ID of the Victim to the ***EXISTING***  |
|                          | Victim ID to update.                            |
+--------------------------+-------------------------------------------------+
| ``victim.commit()``      | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``victims = tc.victims() | Instantiate a Victims container object.         |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``victim = victims.add(' | Add a Resource object setting the name and      |
| ', owner)``              | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``victim.set_id(20)``    | Set the ID of the Victim to the **EXISTING**    |
|                          | Victim ID to delete.                            |
+--------------------------+-------------------------------------------------+
| ``victim.delete()``      | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('New Resourc...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``resource.associate_gro | Add an Association to another Resource.         |
| up(ResourceType...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.associate_gro | Add an Association to another Resource.         |
| up(ResourceType...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('New Resourc...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``resource.associate_ind | Add an Association to an Indicator.             |
| icator(Resource...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.associate_ind | Add an Association to an Indicator.             |
| icator(Resource...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.associate_ind | Add an Association to an Indicator.             |
| icator(Resource...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('New Adversa...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``resource.associate_vic | Add an Association to a Victim.                 |
| tim(325)``               |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('Existing Re...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``for association in res | Iterate through all Associated Groups.          |
| ource.group_associat...` |                                                 |
| `                        |                                                 |
+--------------------------+-------------------------------------------------+
| ``if association.type == | Match any Association of type Incidents.        |
|  'Incident':``           |                                                 |
+--------------------------+-------------------------------------------------+
| ``res.disassociate_group | Disassociate the Group Resource.                |
| (association.re...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('Existing Re...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``for association in res | Iterate through all Associated Groups.          |
| ource.indicator_asso...` |                                                 |
| `                        |                                                 |
+--------------------------+-------------------------------------------------+
| ``if association.type == | Match any Association of type Incidents.        |
|  'EmailAdd':``           |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.disassociate_ | Disassociate the Incident.                      |
| indicator(associatio...` |                                                 |
| `                        |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('Existing Re...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``for association in res | Iterate through all Associated Groups.          |
| ource.victim_associa...` |                                                 |
| `                        |                                                 |
+--------------------------+-------------------------------------------------+
| ``if association.name == | Match any Association of type Incidents.        |
|  'Drew Brees':``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``res.disassociate_victi | Disassociate the Incident.                      |
| m(association.i...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('New Adversa...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``resource.add_attribute | Add an Attribute of type **Description** to the |
| ('Description',...``     | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``resource.add_attribute | Add an Attribute of type **Source** to the      |
| ('Source, 'SIEM')``      | Resource.                                       |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('Existing Re...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``resource.load_attribut | Load existing Attributes.                       |
| es()``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``for attribute in resou | Iterate through Attribute objects.              |
| rce.attributes:``        |                                                 |
+--------------------------+-------------------------------------------------+
| ``if attribute.type == ' | Look for a **Description** Attribute.           |
| Description':``          |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.delete_attrib | Delete the Attribute from the Resource.         |
| ute(attribute.id)``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('Existing Re...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``resource.retrieve()``  | Trigger the API request and retrieve the        |
|                          | Adversary intelligence data.                    |
+--------------------------+-------------------------------------------------+
| ``resource.load_attribut | Load existing Attributes.                       |
| es()``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``for attribute in resou | Iterate through Attribute objects.              |
| rce.attributes:``        |                                                 |
+--------------------------+-------------------------------------------------+
| ``if attribute.type == ' | Look for a **Description** Attribute.           |
| Description':``          |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.update_attrib | Update the **Description** Attribute.           |
| ute(attribute.i...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate an Adversaries container object.    |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('New Resourc...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``resource.set_security_ | Set the Security Label on the Resource.         |
| label('TLP Green')``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate an Adversaries container object.    |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('New Resourc...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``resource.delete_securi | Set the Security Label on the Resource.         |
| ty_label('TLP G...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id,...``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('New Ads...``         | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``resource.add_tag('EXAM | Add a Tag to the Resource.                      |
| PLE')``                  |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.add_tag('APT' | Add a Tag to the Resource.                      |
| )``                      |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger API calls to write all added, deleted,  |
|                          | or modified data.                               |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tc = ThreatConnect(api | Instantiate the ThreatConnect object.           |
| _access_id, api...``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``resources = tc.adversa | Instantiate a Resources container object.       |
| ries()``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource = resources.a | Add a Resource object setting the name and      |
| dd('Existing Re...``     | Owner.                                          |
+--------------------------+-------------------------------------------------+
| ``resource.set_id(123)`` | Set the Resource ID to an existing Adversary.   |
+--------------------------+-------------------------------------------------+
| ``resource.delete_tag('E | Delete a Tag to the Resource.                   |
| XAMPLE')``               |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.delete_tag('A | Delete a Tag to the Resource.                   |
| PT')``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``resource.commit()``    | Trigger multiple API calls to write all added,  |
|                          | deleted, or modified data.                      |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``ro = RequestObject()`` | Instantiate and Instance of a Request object.   |
+--------------------------+-------------------------------------------------+
| ``ro.set_http_method('GE | Set the HTTP Method for the Request.            |
| T')``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``ro.set_owner('Example  | Set the Owner for the Request (optional).       |
| Community')``            |                                                 |
+--------------------------+-------------------------------------------------+
| ``ro.set_owner_allowed(T | Set the Owner-Allowed flag for the Request to   |
| rue)``                   | indicate if this API call supports Owners.      |
+--------------------------+-------------------------------------------------+
| ``ro.set_resource_pagina | Set the Pagination flag for the Request to      |
| tion(True)``             | indicate if this API call supports pagination.  |
+--------------------------+-------------------------------------------------+
| ``ro.set_request_uri('/v | Set the URI (uniform resource identifier) for   |
| 2/indicators')``         | the Request.                                    |
+--------------------------+-------------------------------------------------+
| ``results = tc.api_reque | Trigger the API Request and store result as     |
| st(ro)``                 | ``results``.                                    |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``ro = RequestObject()`` | Instantiate and Instance of a Request object.   |
+--------------------------+-------------------------------------------------+
| ``ro.set_http_method('GE | Set the HTTP Method for the Request.            |
| T')``                    |                                                 |
+--------------------------+-------------------------------------------------+
| ``ro.set_owner('Example  | Set the Owner for the Request (optional).       |
| Community')``            |                                                 |
+--------------------------+-------------------------------------------------+
| ``ro.set_owner_allowed(T | Set the Owner-Allowed flag for the Request to   |
| rue)``                   | indicate if this API call supports Owners.      |
+--------------------------+-------------------------------------------------+
| ``ro.set_resource_pagina | Set the Pagination flag for the Request to      |
| tion(True)``             | indicate if this API call supports pagination.  |
+--------------------------+-------------------------------------------------+
| ``ro.set_request_uri('/v | Set the URI for the Request.                    |
| 2/indicators')``         |                                                 |
+--------------------------+-------------------------------------------------+
| ``results = tc.api_reque | Trigger the API Request and store result as     |
| st(ro)``                 | ``results``.                                    |
+--------------------------+-------------------------------------------------+

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

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``ro = RequestObject()`` | Instantiate and Instance of a Request Object.   |
+--------------------------+-------------------------------------------------+
| ``body = {'name': 'Raw U | Create the JSON body for POST.                  |
| pload Exam...``          |                                                 |
+--------------------------+-------------------------------------------------+
| ``ro.set_http_method('PO | Set the HTTP Method for the Request.            |
| ST')``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``ro.set_owner('Example  | Set the Owner for the Request (optional).       |
| Community')``            |                                                 |
+--------------------------+-------------------------------------------------+
| ``ro.set_owner_allowed(T | Set the Owner-Allowed flag for the Request to   |
| rue)``                   | indicate if this API call supports Owners.      |
+--------------------------+-------------------------------------------------+
| ``ro.set_resource_pagina | Set the Pagination flag for the Request to      |
| tion(False)``            | indicate if this API call supports pagination.  |
+--------------------------+-------------------------------------------------+
| ``ro.set_request_uri('/v | Set the URI for the Request.                    |
| 2/groups/doc...``        |                                                 |
+--------------------------+-------------------------------------------------+
| ``print(ro)``            | Display the Request Object before submitting    |
|                          | (optional).                                     |
+--------------------------+-------------------------------------------------+
| ``results = tc.api_reque | Trigger the API Request and store result as     |
| st(ro)``                 | ``results``.                                    |
+--------------------------+-------------------------------------------------+
| ``document_id = data['da | Get the ID of the created Document to use in    |
| ta']['doc...``           | the contents upload.                            |
+--------------------------+-------------------------------------------------+

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

Java Library
============

The following is a code sample with line numbers syntax highlighting:

.. code:: java

      1     private static void doCreate(Connection conn) {
      2         AbstractGroupWriterAdapter<Adversary> writer WriterAdapterFactory.createAdversaryGroupWriter(conn);
      3         
      4         Adversary adversary = new Adversary();
      5         adversary.setName("Test Adversary");
      6         adversary.setOwnerName("System");
      7         
      8         try {
      9             Adversary savedAdversary = writer.create(adversary);
     10             System.out.println("Saved: " + savedAdversary.toString() );
     11             
     12         } catch (IOException | FailedResponseException ex) {
     13             System.err.println("Error: " + ex.toString()); 
     14         }   
     15         
     16     }   

About This Document

This guide details the process of coding Java applications utilizing the
ThreatConnect API. The Java SDK offers coverage of all features in
version 2.0 of the ThreatConnect API—including the ability to write data
to ThreatConnect. This document will provide an overview of the
reference implementation of the Java SDK for ThreatConnect.

The goal of this Java SDK library is to provide a programmatic
abstraction layer around the ThreatConnect API without losing functional
coverage over the available API resources. This abstraction layer
enables developers to focus on writing enterprise functionality without
worrying about low-level RESTful calls and authentication management.

This document is not a replacement for the official ThreatConnect API
User Guide. This document serves as a companion to the official
documentation for the REST API. Read the official documentation to gain
a further understanding of the functional aspects of using the
ThreatConnect API.

How to Use This Document

This document explains how to create groups, indicators, associations,
tags, security labels, and victims—as well as how to create, update,
delete, and request data from the API using Java; thus, knowledge of the
Java programming Language is a prerequisite.

All code examples will be noted in a separate box with a monospaced font
and line numbers to facilitate explanation of code functionality.

Getting Started with Java SDK
-----------------------------

-  Install `Java JDK
   7+ <http://www.oracle.com/technetwork/java/javase/downloads/index.html>`__
-  Import `Java SDK for
   ThreatConnect <https://github.com/ThreatConnect-Inc/threatconnect-java>`__
-  Create an API User, refer to `REST API documentation <#rest-api>`__

Maven™ Configuration
~~~~~~~~~~~~~~~~~~~~

Add the following entries to your POM (project object model) file. This
is the preferred method to use the SDK:

.. code:: xml

       <properties>
            <threatconnect-sdk.version>2.0.3</threatconnect-sdk.version>
        </properties>


    <!-- repository entry -->
      <repositories>
          <repository>
              <id>threatconnect-java-mvn-repo</id>
             <url>https://raw.github.com/ThreatConnect-Inc/threatconnect-java/mvn-repo-${threatconnect-sdk.version}/</url>
               <snapshots>
                  <enabled>true</enabled>
                  <updatePolicy>always</updatePolicy>
              </snapshots>
          </repository>
      </repositories>


    <!-- sdk dependency -->
        <dependencies>
            <dependency>
                <groupId>com.threatconnect.sdk</groupId>
                <artifactId>threatconnect-sdk</artifactId>
                <version>${threatconnect-sdk.version}</version>
             </dependency>
        </dependencies>

Programmatic Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to the API using the SDK, create a Configuration object with
one of the following constructors:

.. code:: java

       public Configuration(String tcApiUrl, String tcApiAccessID, String tcApiUserSecretKey, String defaultOwner);
       public Configuration(String tcApiUrl, String tcApiAccessID, String tcApiUserSecretKey, String defaultOwner, Integer resultLimit);

Pass the ``Configuration`` object when creating a new ``Connection``.
(See examples in the Reader and Writer sections.)

Configuration using Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This property can be defined in two ways:

In the JVM (Java virtual machine), you can call your program with the
following -D property flag:

``threatconnect.api.config=<YOUR CONFIG FILE LOCATION>``

Or the system property can be directly set at runtime using the
following code:

.. code:: java

    System.getProperties().setProperty("threatconnect.api.config", "<YOUR CONFIG FILE LOCATION>");

Once the configuration has been set up, the examples in this document
should be executable, as long as the Java SDK for ThreatConnect is part
of the classpath. See the following examples for a typical start-up
script.

On Windows:

.. code:: shell

     java -cp ".;threatconnect-sdk-<version>.jar" -Dthreatconnect.api.config=myConfig.properties TestClass

On Linux:

.. code:: shell

    java -cp ".:./threatconnect-sdk-<version>.jar" -Dthreatconnect.api.config=myConfig.properties TestClass

The Java SDK will need to be configured with an Access ID and Secret
Key. When a no-arg ``Configuration`` constructor is called, the SDK
searches system properties for the "threatconnect.api.config" property.

The configuration file should contain the following lines at a minimum:

``connection.tcApiUrl=https://api.threatconnect.com``

``connection.tcApiAccessID=<YOUR API ACCESS ID>``

``connection.tcApiUserSecretKey=<YOUR API SECRET KEY>``

Third-Party Dependencies

The SDK utilizes these open-source libraries primarily for RESTful
communication and JSON (JavaScript Object Notation) parsing.

+----------------------+-----------+--------------------+
| Library              | Version   | Used by            |
+======================+===========+====================+
| HTTP Core            | 4.4.1     | SDK                |
+----------------------+-----------+--------------------+
| HTTP Client          | 4.4.1     | SDK                |
+----------------------+-----------+--------------------+
| Commons Logging      | 1.2       | HTTP Client        |
+----------------------+-----------+--------------------+
| Commons Codec        | 1.9       | HTTP Client        |
+----------------------+-----------+--------------------+
| Jackson Core         | 2.5.3     | SDK                |
+----------------------+-----------+--------------------+
| Jackson Databind     | 2.5.3     | SDK                |
+----------------------+-----------+--------------------+
| Jackson Annotation   | 2.5.0     | Jackson Databind   |
+----------------------+-----------+--------------------+

Technical Design

The Java SDK for ThreatConnect was designed with a focus on abstracting
the API REST calls while enabling the developer to use an
enterprise-level programming language. The abstraction layer is
relatively "thin" because it coincides directly with all of the REST API
calls. In fact, the entities themselves were ported directly from the
ThreatConnect API to enable consistent communication between the Java
SDK and the REST API.

.. figure:: images/sdk-design.png
   :alt: SDK Technical Design

   SDK Design

The Java library was designed with common programming design patterns.
You’ll notice the "Adapter" pattern used to manage the interaction with
the API connection and REST calls. The Java SDK depends on the Apache
HTTP components open-source library to handle these calls. Because
instantiating an Adapter requires a low-level RequestExecutor, a
"Factory" design pattern was utilized to expose reading/writing
functionality in a simplified way.

Java generics are used to type many of the Adapters in an effort to
reuse code, as most readers share functional resources. Below is a
diagram that will help illustrate common interactions between different
classes (Note: Names are conceptual to illustrate interaction. Actual
class names and methods will be discussed later in this document) . All
interactions with the Java SDK will follow this programmatic idiom.

.. figure:: images/sdk-arch.png
   :alt: SDK Architecture

   SDK Architecture

To facilitate interaction with the full set of Java SDK readers and
writers, the use of ReaderAdapterFactory and WriterAdapterFactory,
respectively, is highly recommended.

Example Java App
----------------

Once retrieved, the adversary objects will be printed to the console.

.. code:: java

      1 import com.cyber2.api.lib.client.reader.AbstractGroupReaderAdapter;
      2 import com.cyber2.api.lib.client.reader.ReaderAdapterFactory;
      3 import com.cyber2.api.lib.conn.Connection;
      4 import com.cyber2.api.lib.exception.FailedResponseException;
      5 import com.cyber2.api.lib.server.entity.Adversary;
      6 import java.io.IOException;
      7 import java.util.List;
      8 
      9 public class GroupExample {
     10 
     11     public static void main(String[] args) {
     12     
     13         Connection conn = null;
     14         
     15         try {
     16             
     17             System.getProperties().setProperty("threatconnect.api.config", "/config.properties");
     18             conn = new Connection();
     19             
     20             AbstractGroupReaderAdapter<Adversary> reader = ReaderAdapterFactory.createAdversaryGroupReader(conn);
     21             List<Adversary> data = reader.getAll("System");
     22             for (Adversary g : data ) {
     23                 System.out.println( "Adversary: " + g.toString() );
     24             }   
     25             
     26         } catch (IOException | FailedResponseException ex) {
     27             System.err.println("Error: " + ex);
     28         } finally {
     29             if ( conn != null )     conn.disconnect();
     30         }   
     31         
     32     }   
     33     
     34 }   

To write the first program using the Java SDK for the ThreatConnect API,
an Adversary reader that pulls all adversaries belonging to the "System"
Organization must be created.

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 1-7          | Notable imports include: The                                |
|              | ``com.cyber2.api.lib.client.reader`` package holds all      |
|              | Adapter classes that read data from the API. The            |
|              | ``com.cyber2.api.lib.server.entity`` package holds all      |
|              | entities returned by the Java SDK.                          |
+--------------+-------------------------------------------------------------+
| 17-18        | The platform programmatically define the system property to |
|              | load the configuration file. This allows the developer to   |
|              | instantiate Connection objects (line 18) with a no-arg      |
|              | constructor. If the ``threatconnect.api.config`` property   |
|              | is not defined, the developer has the option of passing the |
|              | configuration file name string in the single-arg Connection |
|              | constructor.                                                |
+--------------+-------------------------------------------------------------+
| 20           | To create an AbstractGroupReaderAdapter object: Use the     |
|              | ReaderAdapterFactory pattern and generics to enforce        |
|              | compile-time type constraints on this abstract class. Then  |
|              | pass the connection object used by the Adapter to interact  |
|              | with the ThreatConnect API.                                 |
+--------------+-------------------------------------------------------------+
| 21           | Using the reader object, call ``getAll()`` method and pass  |
|              | it the Organization string name to return all Adversaries   |
|              | for the "System" Organization.                              |
+--------------+-------------------------------------------------------------+
| 22-24        | Iterate through the data collection to print the contents   |
|              | to the console.                                             |
+--------------+-------------------------------------------------------------+
| 26           | The IOException is potentially thrown if the Connection     |
|              | object cannot find the properties file. The                 |
|              | FailedResponseException is thrown if the API request is     |
|              | invalid.                                                    |
+--------------+-------------------------------------------------------------+
| 29           | In all cases when processing is complete, call              |
|              | ``disconnect()`` on the connection object to release        |
|              | resources.                                                  |
+--------------+-------------------------------------------------------------+

Summary

This section explained:

-  How to connect to the ThreatConnect API by passing the configuration
   file in system properties
-  How to get a list of adversaries for the "System" Organization
-  What types of exceptions a connection and read operation can
   potentially throw
-  How to close a ThreatConnect API connection

Deploying a Java App
--------------------

Apps must be packaged and deployed into ThreatConnect's application
runtime environment.

`Example
Applications <https://github.com/ThreatConnect-Inc/threatconnect-java/tree/master/threatconnect-sdk-core/src/main/java/com/threatconnect/sdk/examples>`__

Supported Version

ThreatConnect Java integrations require Oracle JRE 7 or later. OpenJRE
is not supported.

Third-Party Libraries

These libraries are automatically included in the classpath of every
Java app. There is no need to include these libraries in the
installation zip file. There is also no need to include these libraries
in the ``configuration`` variable named ``java.classpath``.

+-----------------------------------------------------------------------------------+-----------+
| Library                                                                           | Version   |
+===================================================================================+===========+
| `ThreatConnect SDK <https://github.com/ThreatConnect-Inc/threatconnect-java>`__   | 2.0.0     |
+-----------------------------------------------------------------------------------+-----------+
| `HTTP Core <https://hc.apache.org/httpcomponents-core-ga/>`__                     | 4.4.1     |
+-----------------------------------------------------------------------------------+-----------+
| `HTTP Client <https://hc.apache.org/httpcomponents-client-ga/>`__                 | 4.4.1     |
+-----------------------------------------------------------------------------------+-----------+
| `Commons Logging <http://commons.apache.org/proper/commons-logging/>`__           | 1.2       |
+-----------------------------------------------------------------------------------+-----------+
| `Commons Codec <https://commons.apache.org/proper/commons-codec/>`__              | 1.9       |
+-----------------------------------------------------------------------------------+-----------+
| `Jackson Core <https://github.com/FasterXML/jackson-core>`__                      | 2.5.3     |
+-----------------------------------------------------------------------------------+-----------+
| `Jackson Databind <https://github.com/FasterXML/jackson-databind/>`__             | 2.5.3     |
+-----------------------------------------------------------------------------------+-----------+
| `Jackson Annotation <https://github.com/FasterXML/jackson-annotations>`__         | 2.5.0     |
+-----------------------------------------------------------------------------------+-----------+

Deployment Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

`Apps use a deployment configuration file to define variables and
execution environment <#deployment-configuration-file>`__

Command-Line Parameters
-----------------------

The application runtime environment passes standard parameters to all
jobs as part of its standard sandbox container. There should be no
assumptions made on the naming or existence of paths passed in these
variables outside of the lifetime of the job execution. Because all job
executions are run in a sandboxed environment, app developers should
never hard-code ThreatConnect Parameters.

+--------------+-------------------------------------------------------------+
| ThreatConnec | Description                                                 |
| t            |                                                             |
| Parameter    |                                                             |
+==============+=============================================================+
| ``tc_log_pat | Log path for the specific instance of the job execution.    |
| h``          |                                                             |
+--------------+-------------------------------------------------------------+
| ``tc_tmp_pat | Temporary storage path for the specific instance of thejob  |
| h``          | execution.                                                  |
+--------------+-------------------------------------------------------------+
| ``tc_out_pat | Output path for the specific instance of the job execution. |
| h``          |                                                             |
+--------------+-------------------------------------------------------------+
| ``tc_api_pat | Path to the ThreatConnect API server.                       |
| h``          |                                                             |
+--------------+-------------------------------------------------------------+

Job Results
~~~~~~~~~~~

Job executions can use a special file called ``results.tc`` to write
results as a mechanism for updating parameters for subsequent runs. A
use case for this feature is an app that needs to know the last time it
completed successfully in order to process data since that completion.
The parameter definitions are quite flexible, with the only restriction
being that the parameters written to the ``results.tc`` file must exist
in the ``configuration`` file in order to be persisted.

Example ``results.tc`` file:

``param.last_completed_time = 1430619556``

Assuming there is a property with the same name in ``configuration``,
the job executor will update the new property value in the system for
the next run. The property will only be stored if the job execution is
successful. This file should be written to the ``tc_out_path`` passed as
one of the standard ThreatConnect parameters.

Exit Codes
~~~~~~~~~~

There are standard exit codes that the application runtime environment
uses to report whether a program completed successfully. The Java app is
responsible for calling ``System.exit(N)``, where 'N' is the appropriate
exit code highlighted below:

When ``System.exit()`` is not called by the app, an exit code of zero is
returned by default during normal code execution. System-critical errors
(e.g., file not found) return non-zero exit codes. The developer is
responsible for catching and handling program errors accordingly.

At times a program may want to report a partial failure (e.g., batch
process where X out of Y updates completed). In cases of partial
failure, the system administrator can retrieve the log file for that job
execution and view more detailed output from the program run.

The contents of message.tc are typically written any time the program
exits normally or through an error:

+-------------------+------------------------------------------------------------------+
| Status            | Description                                                      |
+===================+==================================================================+
| Success           | Exit code 0 - Process completed successfully.                    |
+-------------------+------------------------------------------------------------------+
| Partial Failure   | Exit code 3 - Process had a partial failure.                     |
+-------------------+------------------------------------------------------------------+
| Failure           | Any value not 0 or 3 (typically Exit code 1) - Process failed.   |
+-------------------+------------------------------------------------------------------+

Exit Message File
~~~~~~~~~~~~~~~~~

Exit codes provide a mechanism to report status at a high level. For
more granular control of the exit message displayed to the user, the app
can write a message to the ``tc_out_path`` directory under the file
named ``message.tc``. All content in this file should be limited to 255
characters or less. The job executor reads this file after execution
completes on each job and displays the contents in the Job table detail
tip.

.. figure:: images/exit-message-tip.png
   :alt: Exit Message

   Exit Message

The Reader Package
------------------

The Reader package is the primary package to retrieve data from the
ThreatConnect API. It covers all available resources exposed through the
ThreatConnect API. The primary classes in the Reader Package, which
encompass all read functionality from the API, are listed below.

+-----------------------------------------------------------+
| Class                                                     |
+===========================================================+
| ``ReaderAdapterFactory``                                  |
+-----------------------------------------------------------+
| ``AbstractGroupReaderAdapter<T extends Group>``           |
+-----------------------------------------------------------+
| ``AbstractIndicatorReaderAdapter<T extends Indicator>``   |
+-----------------------------------------------------------+
| ``AbstractReaderAdapter``                                 |
+-----------------------------------------------------------+
| ``OwnerReaderAdapter``                                    |
+-----------------------------------------------------------+
| ``SecurityLabelReaderAdapter``                            |
+-----------------------------------------------------------+
| ``TagReaderAdapter``                                      |
+-----------------------------------------------------------+
| ``TaskReaderAdapter``                                     |
+-----------------------------------------------------------+
| ``VictimReaderAdapter``                                   |
+-----------------------------------------------------------+

Reader Factory
~~~~~~~~~~~~~~

The ReaderAdapterFactory class is, effectively, the "hub" for reader
Adapters. It provides convenience objects for all the Adapters in the
Reader Package. Below is a list of the static methods and return types
of the ReaderAdapterFactory:

+-----------------------------------------------------------+
| Type                                                      |
+===========================================================+
| ``static AbstractGroupReaderAdapter<Adversary>``          |
+-----------------------------------------------------------+
| ``static AbstractGroupReaderAdapter<Email>``              |
+-----------------------------------------------------------+
| ``static AbstractGroupReaderAdapter<Incident>``           |
+-----------------------------------------------------------+
| ``static AbstractGroupReaderAdapter<Signature>``          |
+-----------------------------------------------------------+
| ``static AbstractGroupReaderAdapter<Threat>``             |
+-----------------------------------------------------------+
| ``static AbstractIndicatorReaderAdapter<Address>``        |
+-----------------------------------------------------------+
| ``static AbstractIndicatorReaderAdapter<EmailAddress>``   |
+-----------------------------------------------------------+
| ``static AbstractIndicatorReaderAdapter<File>``           |
+-----------------------------------------------------------+
| ``static AbstractIndicatorReaderAdapter<Host>``           |
+-----------------------------------------------------------+
| ``static AbstractIndicatorReaderAdapter<Url>``            |
+-----------------------------------------------------------+
| ``static BatchReaderAdapter<Indicator>``                  |
+-----------------------------------------------------------+
| ``static DocumentReaderAdapter``                          |
+-----------------------------------------------------------+
| ``static OwnerReaderAdapter``                             |
+-----------------------------------------------------------+
| ``static SecurityLabelReaderAdapter``                     |
+-----------------------------------------------------------+
| ``static TagReaderAdapter``                               |
+-----------------------------------------------------------+
| ``static TaskReaderAdapter``                              |
+-----------------------------------------------------------+
| ``static VictimReaderAdapter``                            |
+-----------------------------------------------------------+

Reader Factory Example
~~~~~~~~~~~~~~~~~~~~~~

.. code:: java

      1 import com.threatconnect.sdk.client.reader.AbstractGroupReaderAdapter;
      2 import com.threatconnect.sdk.client.reader.ReaderAdapterFactory;
      3 import com.threatconnect.sdk.conn.Connection;
      4 import com.threatconnect.sdk.exception.FailedResponseException;
      5 import com.threatconnect.sdk.server.entity.Adversary;
      6 import com.threatconnect.sdk.server.entity.Email;
      7 import com.threatconnect.sdk.server.entity.Group;
      8 import com.threatconnect.sdk.server.entity.Incident;
      9 import com.threatconnect.sdk.server.entity.Signature;
     10 import com.threatconnect.sdk.server.entity.Threat;
     11 import java.io.IOException;
     13 
      
     53     private static void doGetById(Connection conn) throws IOException, FailedResponseException {
     54 
     55         AbstractGroupReaderAdapter reader = ReaderAdapterFactory.createAdversaryGroupReader(conn);
     56         IterableResponse<Group> data = reader.getAllGroups();
     57         for (Group group : data) {
     58             System.err.println("Checking group.class=" + group.getClass() + ", type=" + group.getType());
     59             Group result = null;
     60             switch( Group.Type.valueOf(group.getType()) ) {
     61                 case Adversary:
     62                     AbstractGroupReaderAdapter<Adversary> adversaryReader 
     63                         = ReaderAdapterFactory.createAdversaryGroupReader(conn);
     64                     // "result" is assigned an Adversary object
     65                     result = adversaryReader.getById(group.getId(),group.getOwnerName());
     66                     break;
     67                 case Email:
     68                     AbstractGroupReaderAdapter<Email> emailReader 
     69                         = ReaderAdapterFactory.createEmailGroupReader(conn);
     70                     // "result" is assigned an Email object
     71                     result = emailReader.getById(group.getId(), group.getOwnerName());  
     72                     break;
     73                 case Incident:
     74                     AbstractGroupReaderAdapter<Incident> incidentReader 
     75                         = ReaderAdapterFactory.createIncidentGroupReader(conn);
     76                     // "result" is assigned an Incident object
     77                     result = incidentReader.getById(group.getId(), group.getOwnerName()); 
     78                     break;
     79                 case Signature:
     80                     AbstractGroupReaderAdapter<Signature> sigReader 
     81                         = ReaderAdapterFactory.createSignatureGroupReader(conn);
     82                     // "result" is assigned a Signature object
     83                     result = sigReader.getById(group.getId(), group.getOwnerName() ); 
     84                     break;
     85                 case Threat:
     86                     AbstractGroupReaderAdapter<Threat> threatReader 
     87                         = ReaderAdapterFactory.createThreatGroupReader(conn);
     88                     // "result" is assigned a Threat object
     89                     result = threatReader.getById(group.getId(), group.getOwnerName() ); 
     90                     break;
     91                 default: 
     92                     System.err.println("Unknown Group Type: " + group.getType() );
     93                     break;
     94             }
     95 
     96             assert result.getId().equals(group.getId());
     97         }
     98 
     99     }

This example continues building from the first one and uses more
Adapters available in the Reader Package. The following example reads
all Groups available to the "System" Organization. It then proceeds to
iterate through each Group, printing and performing "getById()" lookups
to get the full Group object from the ThreatConnect API. (Note: An
ellipsis (...) has been substituted for code sections removed for
brevity.)

There are more concise ways of handling reading data and purely checking
its ID. This code is written in a more verbose form strictly to
illustrate the usage of different methods in the ReaderFactory.

+--------+-------------------------------------------------------------------+
| Line   | Description                                                       |
+========+===================================================================+
| 5-10   | Notice how all Group-level entities in the imports are added.     |
|        | Results from reader Adapters will return an entity or a           |
|        | collection of entities from the                                   |
|        | ``com.threatconnect.sdk.server.entity`` package.                  |
+--------+-------------------------------------------------------------------+
| 52-53  | Groups to which the current API user has access under the         |
|        | "System" Organization should be retrieved. All                    |
|        | AbstractGroupReaderAdapter’s have access to the                   |
|        | ``getAllGroups()`` method—it returns a collection of Group        |
|        | objects for the "System" Organization from the ThreatConnect API. |
+--------+-------------------------------------------------------------------+
| 60     | To illustrate the different instantiations, a switch statement on |
|        | the generic Group object is used.                                 |
+--------+-------------------------------------------------------------------+
| 61-63  | Based on the Group.Type enum value (in this section,              |
|        | "Adversary"), an AdversaryGroupReader object is created from the  |
|        | ReaderAdapterFactory. The assignment to the adversaryReader       |
|        | variable is typed using generics to enforce compile time checks   |
|        | on the data returned from this reader.                            |
+--------+-------------------------------------------------------------------+
| 65     | The ``getById()`` method to retrieve the proper Adversary Group   |
|        | data, based on the ID and Organization name, from the             |
|        | ThreatConnect API, is used here. The ``result`` variable is       |
|        | assigned an Adversary-type object.                                |
+--------+-------------------------------------------------------------------+
| 67-90  | The remaining case statement blocks will check for different      |
|        | Group types, but, effectively, does the same operation. Take some |
|        | time to review these blocks to understand how the ReaderFactory   |
|        | facilitates the creation of proper readers.                       |
+--------+-------------------------------------------------------------------+
| 96     | Here the Group ID is compared against the result ID returned by   |
|        | the ``getById`` method to assert that they are, in fact, the same |
|        | entity.                                                           |
+--------+-------------------------------------------------------------------+

IterableResponse Class
~~~~~~~~~~~~~~~~~~~~~~

    Using this iterable, the developer can utilize traditional
    ``iterator()`` methods to iterate through the results, or, more
    concisely, the Java for each loop is as follows:

.. code:: java

        IterableResponse<Address> data = reader.getAll();
        for(Address a : data) {
           System.out.println("Address: " + a); 
        }

In the previous example, the ``IterableResponse`` class retrieves all
Groups for the default owner. The ``IterableResponse`` class is the
primary type returned by all collection-based reader operations.
Typically, a collection, like a ``List``, would be expected in this
scenario, but to resolve the paging limits of the ThreatConnect API, the
``IterableResponse`` was created.

All paging is performed behind the scenes, allowing the developer to
rely on an Iterable to fulfill its contract and return a ``hasNext()``
of false when there are no more results. The Iterable will make use of
the ``resultLimit`` value defined during the creation of the
``Configuration`` object.

Reader Class Overview
---------------------

While the main entry point to the Reader Package is the ReaderFactory,
getting familiar with the main Adapters helps developers understand how
to interact with the data returning from the ThreatConnect API. Although
there is extensive use of Java Generics, the method-naming conventions
will be familiar and self-explanatory. Parameter naming conventions have
been kept abstract to more accurately reflect the identifiers being
passed.

Parameter Naming Convention
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------+------------------------------------+
| Type                 | Description                        |
+======================+====================================+
| ``uniqueId``         | Identifier for the reader/writer   |
|                      | Group or Incident Adapter type.    |
|                      | For Groups, this is an Integer     |
|                      | that requires an Adversary ID,     |
|                      | Email ID, Incident ID, Signature   |
|                      | ID, or Threat ID. This identifier  |
|                      | is system generated when the group |
|                      | is created in ThreatConnect. For   |
|                      | Indicators, this is a String that  |
|                      | requires an IP Address, Email      |
|                      | Address, File Hash, Host Name, or  |
|                      | URL text. This identifier is user  |
|                      | generated when the Indicator is    |
|                      | created in ThreatConnect.          |
+----------------------+------------------------------------+
| ``victimId``         | Identifier for the Victim Adapter  |
|                      | type. This identifier is an        |
|                      | Integer created by the system when |
|                      | the Victim entry is created in     |
|                      | ThreatConnect.                     |
+----------------------+------------------------------------+
| ``assetId``          | Identifier for the VictimAsset     |
|                      | Adapter type. This identifier is   |
|                      | an Integer created by the system   |
|                      | when the VictimAsset is created in |
|                      | ThreatConnect. This identifier     |
|                      | represents a VictimEmailAddress    |
|                      | ID, VictimNetworkAccount ID,       |
|                      | VictimPhone ID,                    |
|                      | VictimSocialNetwork ID, or         |
|                      | VictimWebsite ID.                  |
+----------------------+------------------------------------+
| ``securityLabel``    | Identifier for SecurityLabel       |
|                      | Adapter type. This is a            |
|                      | user-provided String that          |
|                      | represents the Security Label.     |
+----------------------+------------------------------------+
| ``tagName``          | Identifier for Iag Adapter type.   |
|                      | This is a user-provided String     |
|                      | that represents the Tag.           |
+----------------------+------------------------------------+

The AbstractGroupReaderAdapter is the object returned when GroupReader
is called from the ReaderFactory. These GroupReader instantiations were
reviewed in the last example.

The Java SDK library for ThreatConnect comes with JavaDocs in the
"apidocs" directory, which is an additional reference to the Java SDK.

Filtering
~~~~~~~~~

Example filter usage:

.. code:: java

    IterableResponse<Url> urls 
      = urlReader.getForFilters("System", // owners
                                 true,                              // OR filters 
                                 ApiFilterType.filterConfidence()   // filter:
                                              .greaterThan(50),     // confidence > 50
                                 ApiFilterType.filterRating()       // filter:
                                              .greaterThan(2.5));   // rating > 2.5

| ``ApiFilterType``\ exposes a builder pattern that can be used to build
  filters for indicators, groups, documents, tags, and victims.
| Filters can be passed to the ``getForFilters(...)`` method in the
  ``AbstractBaseReader`` class.

AbstractGroupReaderAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below get data for the Group type (T) linked to this
Adapter. The uniqueId (P) for Groups is an Integer.

+---------------------------+
| Type                      |
+===========================+
| ``T``                     |
+---------------------------+
| ``T``                     |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+

The methods below get generic Group objects associated to this Group
type (T).

+-------------------------------+
| Type                          |
+===============================+
| ``IterableResponse<Group>``   |
+-------------------------------+
| ``IterableResponse<Group>``   |
+-------------------------------+
| ``String``                    |
+-------------------------------+

Associated Groups
~~~~~~~~~~~~~~~~~

The methods below get associated Group elements by distinct type.

+-----------------------------------+
| Type                              |
+===================================+
| ``IterableResponse<Group>``       |
+-----------------------------------+
| ``IterableResponse<Group>``       |
+-----------------------------------+
| ``IterableResponse<Adversary>``   |
+-----------------------------------+
| ``IterableResponse<Adversary>``   |
+-----------------------------------+
| ``Adversary``                     |
+-----------------------------------+
| ``Adversary``                     |
+-----------------------------------+
| ``IterableResponse<Email>``       |
+-----------------------------------+
| ``IterableResponse<Email>``       |
+-----------------------------------+
| ``Email``                         |
+-----------------------------------+
| ``Email``                         |
+-----------------------------------+
| ``IterableResponse<Incident>``    |
+-----------------------------------+
| ``IterableResponse<Incident>``    |
+-----------------------------------+
| ``Incident``                      |
+-----------------------------------+
| ``Incident``                      |
+-----------------------------------+
| ``IterableResponse<Signature>``   |
+-----------------------------------+
| ``IterableResponse<Signature>``   |
+-----------------------------------+
| ``Signature``                     |
+-----------------------------------+
| ``Signature``                     |
+-----------------------------------+
| ``IterableResponse<Threat>``      |
+-----------------------------------+
| ``IterableResponse<Threat>``      |
+-----------------------------------+
| ``Threat``                        |
+-----------------------------------+
| ``Threat``                        |
+-----------------------------------+

Associated Indicators
~~~~~~~~~~~~~~~~~~~~~

The methods below get associated Indicator elements by distinct types.

+-----------------------------------+
| Type                              |
+===================================+
| ``IterableResponse<Indicator>``   |
+-----------------------------------+
| ``IterableResponse<Indicator>``   |
+-----------------------------------+
| ``IterableResponse<Address>``     |
+-----------------------------------+
| ``IterableResponse<Address>``     |
+-----------------------------------+
| ``Address``                       |
+-----------------------------------+
| ``Address``                       |
+-----------------------------------+
| ``IterableResponse<Email>``       |
+-----------------------------------+
| ``IterableResponse<Email>``       |
+-----------------------------------+
| ``Email``                         |
+-----------------------------------+
| ``Email``                         |
+-----------------------------------+
| ``IterableResponse<File>``        |
+-----------------------------------+
| ``IterableResponse<File>``        |
+-----------------------------------+
| ``File``                          |
+-----------------------------------+
| ``IterableResponse<Host>``        |
+-----------------------------------+
| ``IterableResponse<Host>``        |
+-----------------------------------+
| ``Host``                          |
+-----------------------------------+
| ``Host``                          |
+-----------------------------------+
| ``IterableResponse<Url>``         |
+-----------------------------------+
| ``IterableResponse<Url>``         |
+-----------------------------------+
| ``Url``                           |
+-----------------------------------+
| ``Url``                           |
+-----------------------------------+

Associated Security Labels
~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below get associated SecurityLabel data elements.

+---------------------------------------+
| Type                                  |
+=======================================+
| ``IterableResponse<SecurityLabel>``   |
+---------------------------------------+
| ``IterableResponse<SecurityLabel>``   |
+---------------------------------------+
| ``SecurityLabel``                     |
+---------------------------------------+
| ``SecurityLabel``                     |
+---------------------------------------+

Associated Tags
~~~~~~~~~~~~~~~

The methods below get associated Tag data elements.

+-----------------------------+
| Type                        |
+=============================+
| ``IterableResponse<Tag>``   |
+-----------------------------+
| ``IterableResponse<Tag>``   |
+-----------------------------+
| ``Tag``                     |
+-----------------------------+
| ``Tag``                     |
+-----------------------------+

Associated VictimAssets
~~~~~~~~~~~~~~~~~~~~~~~

The methods below get associated VictimAsset data elements.

+----------------------------------------------+
| Type                                         |
+==============================================+
| ``IterableResponse<VictimAsset>``            |
+----------------------------------------------+
| ``IterableResponse<VictimAsset>``            |
+----------------------------------------------+
| ``IterableResponse<VictimEmailAddress>``     |
+----------------------------------------------+
| ``IterableResponse<VictimEmailAddress>``     |
+----------------------------------------------+
| ``VictimEmailAddress``                       |
+----------------------------------------------+
| ``VictimEmailAddress``                       |
+----------------------------------------------+
| ``IterableResponse<VictimNetworkAccount>``   |
+----------------------------------------------+
| ``IterableResponse<VictimNetworkAccount>``   |
+----------------------------------------------+
| ``VictimNetworkAccount``                     |
+----------------------------------------------+
| ``VictimNetworkAccount``                     |
+----------------------------------------------+
| ``IterableResponse<VictimPhone>``            |
+----------------------------------------------+
| ``IterableResponse<VictimPhone>``            |
+----------------------------------------------+
| ``VictimPhone``                              |
+----------------------------------------------+
| ``VictimPhone``                              |
+----------------------------------------------+
| ``IterableResponse<VictimSocialNetwork>``    |
+----------------------------------------------+
| ``IterableResponse<VictimSocialNetwork>``    |
+----------------------------------------------+
| ``VictimSocialNetwork``                      |
+----------------------------------------------+
| ``VictimSocialNetwork``                      |
+----------------------------------------------+
| ``IterableResponse<VictimWebSite>``          |
+----------------------------------------------+
| ``IterableResponse<VictimWebSite>``          |
+----------------------------------------------+
| ``VictimWebSite``                            |
+----------------------------------------------+
| ``VictimWebSite``                            |
+----------------------------------------------+

Associated Attributes
~~~~~~~~~~~~~~~~~~~~~

The methods below get Attributes and Attribute SecurityLabels for this
Group type.

+---------------------------------------+
| Type                                  |
+=======================================+
| ``IterableResponse<Attribute>``       |
+---------------------------------------+
| ``IterableResponse<Attribute>``       |
+---------------------------------------+
| ``Attribute``                         |
+---------------------------------------+
| ``Attribute``                         |
+---------------------------------------+
| ``IterableResponse<SecurityLabel>``   |
+---------------------------------------+
| ``IterableResponse<SecurityLabel>``   |
+---------------------------------------+
| ``SecurityLabel``                     |
+---------------------------------------+
| ``SecurityLabel``                     |
+---------------------------------------+

AbstractIndicatorReaderAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AbstractIndicatorReaderAdapter and AbstractGroupReaderAdapter share many
of the association actions. Indicators share the ability to associate
Groups, Indicators, SecurityLabels, Tags, VictimAssets, and Attributes.
The listings below are some distinctions or subtle differences.

All Indicators in the ThreatConnect API have a uniqueId data type of
"String". This identifier is provided by each Organization in the form
of an Email Address, IP Address, File Hash, Host Name, or URL text. To
understand this distinction, read the Indicator section in the
ThreatConnect API documentation.

The methods below get data for the Indicator type (T) linked to this
Adapter. The uniqueId (P) for Indicators is a String.

+---------------------------+
| Type                      |
+===========================+
| ``T``                     |
+---------------------------+
| ``T``                     |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+

The method below returns all the generic Indicators to which the current
API user has access.

+-----------------------------------+
| Type                              |
+===================================+
| ``IterableResponse<Indicator>``   |
+-----------------------------------+

The methods below return owners who have created the Indicator under the
uniqueId.

+-------------------------------+
| Type                          |
+===============================+
| ``IterableResponse<Owner>``   |
+-------------------------------+
| ``IterableResponse<Owner>``   |
+-------------------------------+

The methods below return False Positive counts for the Indicator under
the uniqueId.

\|Type\|\ *Method* \|
-------------------------------------------------------- \|
``FalsePositive``\ \|getFalsePositive(String uniqueId) \|
``FalsePositive``\ \|getFalsePositive(String uniqueId, String ownerName)
\|

The methods below return Observations and Observation counts for the
Indicator under the uniqueId.

+-------------------------------------+
| Type                                |
+=====================================+
| ``IterableResponse<Observation>``   |
+-------------------------------------+
| ``IterableResponse<Observation>``   |
+-------------------------------------+
| ``ObservationCount``                |
+-------------------------------------+
| ``ObservationCount``                |
+-------------------------------------+

The AbstractIndicatorReaderAdapter class has a concrete subclass
**FileIndicatorReaderAdapter** that exposes the methods below.

+----------------------+
| Type                 |
+======================+
| ``FileOccurrence``   |
+----------------------+
| ``FileOccurrence``   |
+----------------------+

BatchReaderAdapter
~~~~~~~~~~~~~~~~~~

The BatchReaderAdapter class allows the developer to poll for the status
of a batch upload file using a batch id. Once a batch is complete
(either successfully or with errors), the developer can download errors
(if any).

+---------------------------------------------------------------------+
| Type                                                                |
+=====================================================================+
| ``ApiEntitySingleResponse<BatchStatus, BatchStatusResponseData>``   |
+---------------------------------------------------------------------+
| ``ApiEntitySingleResponse<BatchStatus, BatchStatusResponseData>``   |
+---------------------------------------------------------------------+
| ``void``                                                            |
+---------------------------------------------------------------------+
| ``void``                                                            |
+---------------------------------------------------------------------+

DocumentReaderAdapter
~~~~~~~~~~~~~~~~~~~~~

The DocumentReaderAdapter class is a subclass of the AbstractGroupReader
class. In addition to all GroupReader functionality, the document reader
has access to the following method.

+------------+
| Type       |
+============+
| ``void``   |
+------------+

OwnerReaderAdapter
~~~~~~~~~~~~~~~~~~

The OwnerReaderAdapter is a simple Adapter that returns a list of
Organizations to which the API user has access. There is a second method
called "getOwnerMine()" that returns the default Organization for the
API user.

+-------------------------------+
| Type                          |
+===============================+
| ``Owner``                     |
+-------------------------------+
| ``IterableResponse<Owner>``   |
+-------------------------------+

SecurityLabelReaderAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

The SecurityLabelReaderAdapter class is a concrete class (available
through the ReaderFactory) that returns SecurityLabels to which the
developer's API user has access, as well as by uniqueId (P). The
uniqueId data type for SecurityLabels is a String.

+---------------------------+
| Type                      |
+===========================+
| ``T``                     |
+---------------------------+
| ``T``                     |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+

In addition to retrieving basic SecurityLabel data, associated
`Groups <#associate-groups>`__ and
`Indicators <#associate-indicators>`__ can be retrieved. For more
details on these methods, see the
`AbstractGroupReaderAdapter <#abstractgroupreaderadapter>`__ class.

TagReaderAdapter Class
~~~~~~~~~~~~~~~~~~~~~~

The TagReaderAdapter class is a concrete class (available through the
ReaderFactory) that returns Tags to which the developer's API user has
access, as well as by uniqueId (P). The uniqueId data type for Tags is a
String.

+---------------------------+
| Type                      |
+===========================+
| ``T``                     |
+---------------------------+
| ``T``                     |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+

In addition to retrieving basic Tag data, associated
`Groups <#associate-groups>`__ and
`Indicators <#associate-indicators>`__ can be retrieved. For more
details on these methods, review the
`AbstractGroupReaderAdapter <#abstractgroupreaderadapter>`__ class.

TaskReaderAdapter Class
~~~~~~~~~~~~~~~~~~~~~~~

The TaskReaderAdapter class is a concrete class (available through the
ReaderFactory) that returns Tasks to which the API user has access, as
well as by uniqueId (P). The uniqueId data type for a Task is an
Integer.

+---------------------------+
| Type                      |
+===========================+
| ``T``                     |
+---------------------------+
| ``T``                     |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+

In addition to retrieving basic Task data, associated Assignees and
Escalatees can be retrieved.

The methods below return all Assignees or Escalatees associated with a
given Task's id

+------------------------------+
| Type                         |
+==============================+
| ``IterableResponse<User>``   |
+------------------------------+
| ``IterableResponse<User>``   |
+------------------------------+

The methods below return an individual Assignee or Escalatees'
information

+------------------------------+
| Type                         |
+==============================+
| ``IterableResponse<User>``   |
+------------------------------+
| ``IterableResponse<User>``   |
+------------------------------+

VictimReaderAdapter Class
~~~~~~~~~~~~~~~~~~~~~~~~~

The VictimReaderAdapter class is a concrete class (available through the
ReaderFactory) that returns Victims to which the API user has access, as
well as by uniqueId (P). The uniqueId data type for a Victim is an
Integer.

+---------------------------+
| Type                      |
+===========================+
| ``T``                     |
+---------------------------+
| ``T``                     |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+
| ``IterableResponse<T>``   |
+---------------------------+

In addition to retrieving basic Victim data, associated
`Groups <#associate-groups>`__, `Indicators <#associate-indicators>`__,
and `VictimAssets <#associated-victimassets>`__ can be retrieved. For
more details on these methods, review the
`AbstractGroupReaderAdapter <#abstractgroupreaderadapter>`__ class.

Reader IP Address and Tag Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example uses the Reader Package to retrieve associated
Tags from our IP address Indicators:

.. code:: java

      1 
      2     private static void doGetAssociatedTags(Connection conn) throws IOException, FailedResponseException {
      3         AbstractIndicatorReaderAdapter reader = ReaderAdapterFactory.createAddressIndicatorReader(conn);
      4         IterableResponse<Address> data = reader.getAll();
      5         for (Address address : data) {
      6             System.out.printf("IP Address: %20s", address.getIp() );
      7 
      8             IterableResponse<Tag> associatedTags = reader.getAssociatedTags( address.getIp() );
      9             System.out.printf("\tAssociated Tag:");
     10             for(Tag tag : associatedTags) {
     11                 System.out.printf("%20s", tag.getName() );
     12             }
     13             System.out.println();
     14         }
     15     }
     16 

+--------+-------------------------------------------------------------------+
| Line   | Description                                                       |
+========+===================================================================+
| 3-4    | An IndicatorReaderAdapter is created to read all the addresses to |
|        | which the API user has access. The ``getAll()`` method returns a  |
|        | collection of addresses from the ThreatConnect API.               |
+--------+-------------------------------------------------------------------+
| 5-6    | Each address is iterated through and its uniqueId is printed. As  |
|        | mentioned in the AbstractIndicatorReaderAdapter section, all      |
|        | uniqueIds for Indicators are Strings. In the case of address      |
|        | objects, it is the IP address or the ``getIp()`` getter method.   |
+--------+-------------------------------------------------------------------+
| 8      | To get a collection of associated Tags for the IP Address, the    |
|        | ``getAssociatedTags()`` method is called.                         |
+--------+-------------------------------------------------------------------+
| 10-11  | Each Tag returned from the ThreatConnect API for that specific IP |
|        | address is iterated through and printed to the console.           |
+--------+-------------------------------------------------------------------+

Summary

This example explained how to:

-  Get a collection of Indicators to which the API user has access
-  Retrieve associated data (in this case Tags) based on the uniqueId of
   the Indicator

The Writer Package
------------------

The Writer Package shares many of the concepts of the Reader Package
with the distinction of introducing the new functionality of version 2.0
of the ThreatConnect API. Note that the WriterAdapterFactory class is
effectively the "hub" for writer Adapters. It provides convenience
objects for all the Adapters in the Writer Package. Below is a list of
the static methods and return types of the WriterAdapterFactory.

+-----------+----------------------------------------------------------------+
| Class     | *Description*                                                  |
+===========+================================================================+
| ``WriterA | Primary entry point to instantiate all writers in the Writer   |
| dapterFac | Package.                                                       |
| tory``    |                                                                |
+-----------+----------------------------------------------------------------+
| ``Abstrac | Generic Group writer abstract class. Concrete object available |
| tGroupWri | in WriterAdapterFactory.                                       |
| terAdapte |                                                                |
| r<T exten |                                                                |
| ds Group> |                                                                |
| ``        |                                                                |
+-----------+----------------------------------------------------------------+
| ``Abstrac | Generic Indicator writer abstract class. Concrete object       |
| tIndicato | available in WriterAdapterFactory.                             |
| rWriterAd |                                                                |
| apter<T e |                                                                |
| xtends In |                                                                |
| dicator>` |                                                                |
| `         |                                                                |
+-----------+----------------------------------------------------------------+
| ``Abstrac | Base abstract writer for all reader Adapters in the Reader     |
| tWriterAd | Package.                                                       |
| apter``   |                                                                |
+-----------+----------------------------------------------------------------+
| ``Securit | Concrete writer for SecurityLabel data. Convenience object     |
| yLabelWri | available in WriterAdapterFactory.                             |
| terAdapte |                                                                |
| r``       |                                                                |
+-----------+----------------------------------------------------------------+
| ``TagWrit | Concrete writer for Tag data. Convenience object available in  |
| erAdapter | WriterAdapterFactory.                                          |
| ``        |                                                                |
+-----------+----------------------------------------------------------------+
| ``TaskWri | Concrete writer for Task data. Convenience object available in |
| terAdapte | WriterAdapterFactory.                                          |
| r``       |                                                                |
+-----------+----------------------------------------------------------------+
| ``VictimW | Concrete writer for Victim data. Convenience object available  |
| riterAdap | in WriterAdapterFactory.                                       |
| ter``     |                                                                |
+-----------+----------------------------------------------------------------+
| ``Abstrac | Writer for batch indicator uploads. Concrete object available  |
| tBatchWri | in WriterAdapterFactory.                                       |
| terAdapte |                                                                |
| r<T>``    |                                                                |
+-----------+----------------------------------------------------------------+

Writer Factory
~~~~~~~~~~~~~~

The primary methods for the WriterFactory are listed below. They
encompass all write functionality for the ThreatConnect API.

+--------------------------+-------------------------------------------------+
| Class                    | *Method*                                        |
+==========================+=================================================+
| ``static AbstractGroupWr | createAdversaryGroupWriter(Connection conn)     |
| iterAdapter<Adversary>`` |                                                 |
+--------------------------+-------------------------------------------------+
| ``static AbstractGroupWr | createEmailGroupWriter(Connection conn)         |
| iterAdapter<Email>``     |                                                 |
+--------------------------+-------------------------------------------------+
| ``static AbstractGroupWr | createIncidentGroupWriter(Connection conn)      |
| iterAdapter<Incident>``  |                                                 |
+--------------------------+-------------------------------------------------+
| ``static AbstractGroupWr | createSignatureGroupWriter(Connection conn)     |
| iterAdapter<Signature>`` |                                                 |
+--------------------------+-------------------------------------------------+
| ``static AbstractGroupWr | createThreatGroupWriter(Connection conn)        |
| iterAdapter<Threat>``    |                                                 |
+--------------------------+-------------------------------------------------+
| ``static AbstractIndicat | createAddressIndicatorWriter(Connection conn)   |
| orWriterAdapter<Address> |                                                 |
| ``                       |                                                 |
+--------------------------+-------------------------------------------------+
| ``static AbstractIndicat | createEmailAddressIndicatorWriter(Connection    |
| orWriterAdapter<EmailAdd | conn)                                           |
| ress>``                  |                                                 |
+--------------------------+-------------------------------------------------+
| ``static AbstractIndicat | createFileIndicatorWriter(Connection conn)      |
| orWriterAdapter<File>``  |                                                 |
+--------------------------+-------------------------------------------------+
| ``static AbstractIndicat | createHostIndicatorWriter(Connection conn)      |
| orWriterAdapter<Host>``  |                                                 |
+--------------------------+-------------------------------------------------+
| ``static AbstractIndicat | createUrlIndicatorWriter(Connection conn)       |
| orWriterAdapter<Url>``   |                                                 |
+--------------------------+-------------------------------------------------+
| ``static AbstractBatchWr | createBatchIndicatorWriter(Connection conn)     |
| iterAdapter<Indicator>`` |                                                 |
+--------------------------+-------------------------------------------------+
| ``static DocumentWriterA | createDocumentWriter(Connection conn)           |
| dapter``                 |                                                 |
+--------------------------+-------------------------------------------------+
| ``static SecurityLabelWr | createSecurityLabelWriter(Connection conn)      |
| iterAdapter``            |                                                 |
+--------------------------+-------------------------------------------------+
| ``static TagWriterAdapte | createTagWriter(Connection conn)                |
| r``                      |                                                 |
+--------------------------+-------------------------------------------------+
| ``static TaskWriterAdapt | createTaskWriter(Connection conn)               |
| er``                     |                                                 |
+--------------------------+-------------------------------------------------+
| ``static VictimWriterAda | createVictimWriter(Connection conn)             |
| pter``                   |                                                 |
+--------------------------+-------------------------------------------------+

Writer Responses
~~~~~~~~~~~~~~~~

This section details some conventions used in the writer API that will
help clarify how deletes, creates, and updates are handled by the Java
SDK, and what the developer should expect when a failure occurs.

When a single item is modified (create/delete/update) using the Java
SDK, the return type is an ApiEntitySingleResponse object. In an effort
to simplify write-operation response handling, the
ApiEntitySingleResponse object provides a single object for the
developer to validate the modify operation.

When a collection of items is modified (create/delete/update) using the
Java SDK, the return type is a WriteListResponse object. Likewise, in an
effort to simplify write-operation response handling, the
WriteListResponse object holds collections of failed/succeeded
ApiEntitySingleResponse objects. The following listing describes how
modify responses should be handled.

+-------------------------------------+--------------------+
| Type                                | *Method*           |
+=====================================+====================+
| ``List<ApiEntitySingleResponse>``   | getFailureList()   |
+-------------------------------------+--------------------+
| ``List<ApiEntitySingleResponse>``   | getSuccessList()   |
+-------------------------------------+--------------------+
| ``boolean``                         | isSuccess()        |
+-------------------------------------+--------------------+
| ``String``                          | getMessage()       |
+-------------------------------------+--------------------+
| ``T``                               | getItem()          |
+-------------------------------------+--------------------+

While the ApiEntitySingleResponse class manages failed write operations
to the ThreatConnect API, the developer is responsible for capturing any
runtime exceptions that may occur because of network, configuration, or
data-related issues.

Fluent Entities
~~~~~~~~~~~~~~~

The following is a simple Fluent Example:

.. code:: java


           Attribute attribute = new AttributeBuilder()
                    .withDisplayed(true)
                    .withType(type)
                    .withDateAdded(new Date())
                    .withLastModified(new Date())
                    .withValue(value)
                    .createAttribute();

There are entity classes available using a fluent style to simplify
object creation. These classes are part of the SDK and can be used in
place of creating a traditional new ThreatConnect entity with all
setters. Using the fluent entities in the
``com.threatconnect.sdk.client.fluent`` package are optional and a
matter of preference.

+-----------------------------------+
| Fluent Types                      |
+===================================+
| ``AddressBuilder``                |
+-----------------------------------+
| ``AdversaryBuilder``              |
+-----------------------------------+
| ``AttributeBuilder``              |
+-----------------------------------+
| ``CommunityBuilder``              |
+-----------------------------------+
| ``DocumentBuilder``               |
+-----------------------------------+
| ``EmailAddressBuilder``           |
+-----------------------------------+
| ``EmailBuilder``                  |
+-----------------------------------+
| ``FileBuilder``                   |
+-----------------------------------+
| ``FileOccurrenceBuilder``         |
+-----------------------------------+
| ``GroupBuilder``                  |
+-----------------------------------+
| ``HostBuilder``                   |
+-----------------------------------+
| ``IncidentBuilder``               |
+-----------------------------------+
| ``IndicatorBuilder``              |
+-----------------------------------+
| ``IndividualBuilder``             |
+-----------------------------------+
| ``SecurityLabelBuilder``          |
+-----------------------------------+
| ``SignatureBuilder``              |
+-----------------------------------+
| ``SourceBuilder``                 |
+-----------------------------------+
| ``TagBuilder``                    |
+-----------------------------------+
| ``TaskBuilder``                   |
+-----------------------------------+
| ``ThreatBuilder``                 |
+-----------------------------------+
| ``UrlBuilder``                    |
+-----------------------------------+
| ``UserBuilder``                   |
+-----------------------------------+
| ``VictimAssetBuilder``            |
+-----------------------------------+
| ``VictimBuilder``                 |
+-----------------------------------+
| ``VictimEmailAddressBuilder``     |
+-----------------------------------+
| ``VictimNetworkAccountBuilder``   |
+-----------------------------------+
| ``VictimPhoneBuilder``            |
+-----------------------------------+
| ``VictimSocialNetworkBuilder``    |
+-----------------------------------+
| ``VictimWebSiteBuilder``          |
+-----------------------------------+

Writer Create Example
~~~~~~~~~~~~~~~~~~~~~

The following is a simple Writer Create Example:

.. code:: java


      3 import com.threatconnect.sdk.client.writer.AbstractGroupWriterAdapter;
      4 import com.threatconnect.sdk.client.writer.WriterAdapterFactory;
      5 import com.threatconnect.sdk.conn.Connection;
      6 import com.threatconnect.sdk.exception.FailedResponseException;
      7 import com.threatconnect.sdk.server.entity.Adversary;
      8 import com.threatconnect.sdk.server.response.entity.ApiEntitySingleResponse;
      9 import java.io.IOException;
     10 import java.util.List;
    103     private static void doCreate(Connection conn) {
    104         AbstractGroupWriterAdapter<Adversary> writer = WriterAdapterFactory.createAdversaryGroupWriter(conn);
    105 
    106         Adversary adversary = new Adversary();
    107         adversary.setName("Test Adversary");
    108         adversary.setOwnerName("System");
    109 
    110         try {
    111             ApiEntitySingleResponse<Adversary,?> response = writer.create(adversary);
    112             if ( response.isSuccess() ) {
    113                 Adversary savedAdversary = response.getItem();
    114                 System.out.println("Saved: " + savedAdversary.toString() );
    115             } else {
    116                 System.err.println("Error: " + response.getMessage() );
    117 
    118             }
    119 
    120         } catch (IOException | FailedResponseException ex) {
    121             System.err.println("Error: " + ex.toString());
    122         }
    123 
    124     }

Code Sample

+--------+-------------------------------------------------------------------+
| Line   | Description                                                       |
+========+===================================================================+
| 104    | An AbstractGroupWriterAdapter for the Adversary Group type is     |
|        | created. With this Adapter, Group data elements, Victim assets,   |
|        | Attributes, and associations can be written/updated/deleted.      |
+--------+-------------------------------------------------------------------+
| 106-10 | A simple Adversary with a name and owner (Organization) is        |
| 8      | created.                                                          |
+--------+-------------------------------------------------------------------+
| 111    | The writer is used to create an Adversary using the ThreatConnect |
|        | API. For single-item writes, an ApiEntitySingleResponse object is |
|        | always returned. This object allows for the appropriate           |
|        | inspection and handling of the response.                          |
+--------+-------------------------------------------------------------------+
| 112-11 | To see if the create was successful, ``isSuccess()`` is called.   |
| 4      | If the check passes, the item associated with the response is     |
|        | delivered using the ``getItem()`` method (Line 113). The          |
|        | successfully saved Adversary object returns from the              |
|        | ThreatConnect API with a valid ID value.                          |
+--------+-------------------------------------------------------------------+
| 116    | If the response is unsuccessful, the response message to the      |
|        | console is printed.                                               |
+--------+-------------------------------------------------------------------+
| 121    | Any potential runtime exceptions are caught and handled           |
|        | appropriately. In the case of this basic example, it is simply    |
|        | dumped to the console.                                            |
+--------+-------------------------------------------------------------------+

Summary

This example explained how to:

-  Create an Adapter using the WriterFactory
-  Create an Adversary, and verify if the save was successful
-  Handle errors from a write operation to the ThreatConnect API

Writer Class Overview
---------------------

Most of the conventions in the Reader Package are mirrored in the Writer
Package. Much like the Reader Package, the method-naming conventions
will be familiar and self-explanatory. `Parameter-naming
conventions <reader/#parameter-naming-convention>`__ have been kept
abstract to allow for a better representation of the identifiers being
passed. Below is a listing of the classes in the Writer Package.

AbstractGroupWriterAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below write data for the Group type (T) linked to this
Adapter.

-  The create methods require a Group type object as a collection or
   single object.
-  The delete methods require the key ID value as a collection or single
   object.
-  The update methods require a Group type object as a collection or
   single object.

+-------------------------------+--------------------------------------------------------+
| Type                          | *Method*                                               |
+===============================+========================================================+
| ``WriteListResponse<T>``      | create(\ ``List<T> itemList``)                         |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | create(\ ``T item``)                                   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | create(\ ``T item``, ``String ownerName``)             |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<P>``      | delete(\ ``List<P> itemIds``)                          |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<P>``      | delete(\ ``List<P> itemIds``, ``String ownerName``)    |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | delete(\ ``P itemId``)                                 |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | delete(\ ``P itemId``, ``String ownerName``)           |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<T>``      | update(\ ``List<T> itemList``)                         |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<T>``      | update(\ ``List<T> itemList``, ``String ownerName``)   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | update(\ ``T item``)                                   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | update(\ ``T item``, ``String ownerName``)             |
+-------------------------------+--------------------------------------------------------+

Associate Groups
~~~~~~~~~~~~~~~~

The methods below associate a Group type to another Group type. Groups
are associated by passing in the uniqueId (Integer) with the Group ID to
which it will be associated.

+----------------------+------------------------------------------------------+
| Type                 | *Method*                                             |
+======================+======================================================+
| ``WriteListResponse< | associateGroupAdversaries(\ ``Integer uniqueId``,    |
| Integer>``           | ``List<Integer> adversaryIds``)                      |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | associateGroupAdversaries(\ ``Integer uniqueId``,    |
| Integer>``           | ``List<Integer> adversaryIds``,                      |
|                      | ``String ownerName``)                                |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | associateGroupAdversary(\ ``Integer uniqueId``,      |
| ponse``              | ``Integer adversaryId``)                             |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | associateGroupAdversary(\ ``Integer uniqueId``,      |
| ponse``              | ``Integer adversaryId``, ``String ownerName``)       |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | associateGroupEmails(\ ``Integer uniqueId``,         |
| Integer>``           | ``List<Integer> emailIds``)                          |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | associateGroupEmails(\ ``Integer uniqueId``,         |
| Integer>``           | ``List<Integer> emailIds``, ``String ownerName``)    |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | associateGroupEmail(\ ``Integer uniqueId``,          |
| ponse``              | ``Integer emailId``)                                 |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | associateGroupEmail(\ ``Integer uniqueId``,          |
| ponse``              | ``Integer emailId``, ``String ownerName``)           |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | associateGroupIncidents(\ ``Integer uniqueId``,      |
| Integer>``           | ``List<Integer> incidentIds``)                       |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | associateGroupIncidents(\ ``Integer uniqueId``,      |
| Integer>``           | ``List<Integer> incidentIds``, ``String ownerName``) |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | associateGroupIncident(\ ``Integer uniqueId``,       |
| ponse``              | ``Integer incidentId``)                              |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | associateGroupIncident(\ ``Integer uniqueId``,       |
| ponse``              | ``Integer incidentId``, ``String ownerName``)        |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | associateGroupSignatures(\ ``Integer uniqueId``,     |
| Integer>``           | ``List<Integer> signatureIds``)                      |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | associateGroupSignatures(\ ``Integer uniqueId``,     |
| Integer>``           | ``List<Integer> signatureIds``,                      |
|                      | ``String ownerName``)                                |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | associateGroupSignature(\ ``Integer uniqueId``,      |
| ponse``              | ``Integer signatureId``)                             |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | associateGroupSignature(\ ``Integer uniqueId``,      |
| ponse``              | ``Integer signatureId``, ``String ownerName``)       |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | associateGroupThreats(\ ``Integer uniqueId``,        |
| Integer>``           | ``List<Integer> threatIds``)                         |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | associateGroupThreats(\ ``Integer uniqueId``,        |
| Integer>``           | ``List<Integer> threatIds``, ``String ownerName``)   |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | associateGroupThreat(\ ``Integer uniqueId``,         |
| ponse``              | ``Integer threatId``)                                |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | associateGroupThreat(\ ``Integer uniqueId``,         |
| ponse``              | ``Integer threatId``, ``String ownerName``)          |
+----------------------+------------------------------------------------------+

Associate Indicators
~~~~~~~~~~~~~~~~~~~~

The methods below associate Indicators to a Group type.

+--------------------+-------------------------------------------------------+
| Type               | *Method*                                              |
+====================+=======================================================+
| ``WriteListRespons | associateIndicatorAddresses(\ ``Integer uniqueId``,   |
| e<String>``        | ``List<String> ipAddresses``)                         |
+--------------------+-------------------------------------------------------+
| ``WriteListRespons | associateIndicatorAddresses(\ ``Integer uniqueId``,   |
| e<String>``        | ``List<String> ipAddresses``, ``String ownerName``)   |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateIndicatorAddress(\ ``Integer uniqueId``,     |
| esponse``          | ``String ipAddress``)                                 |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateIndicatorAddress(\ ``Integer uniqueId``,     |
| esponse``          | ``String ipAddress``, ``String ownerName``)           |
+--------------------+-------------------------------------------------------+
| ``WriteListRespons | associateIndicatorEmailAddresses(\ ``Integer uniqueId |
| e<String>``        | ``,                                                   |
|                    | ``List<String> emailAddresses``)                      |
+--------------------+-------------------------------------------------------+
| ``WriteListRespons | associateIndicatorEmailAddresses(\ ``Integer uniqueId |
| e<String>``        | ``,                                                   |
|                    | ``List<String> emailAddresses``,                      |
|                    | ``String ownerName``)                                 |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateIndicatorEmailAddress(\ ``Integer uniqueId`` |
| esponse``          | ,                                                     |
|                    | ``String emailAddress``)                              |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateIndicatorEmailAddress(\ ``Integer uniqueId`` |
| esponse``          | ,                                                     |
|                    | ``String emailAddress``, ``String ownerName``)        |
+--------------------+-------------------------------------------------------+
| ``WriteListRespons | associateIndicatorFiles(\ ``Integer uniqueId``,       |
| e<String>``        | ``List<String> fileHashes``)                          |
+--------------------+-------------------------------------------------------+
| ``WriteListRespons | associateIndicatorFiles(\ ``Integer uniqueId``,       |
| e<String>``        | ``List<String> fileHashes``, ``String ownerName``)    |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateIndicatorFile(\ ``Integer uniqueId``,        |
| esponse``          | ``String fileHash``)                                  |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateIndicatorFile(\ ``Integer uniqueId``,        |
| esponse``          | ``String fileHash``, ``String ownerName``)            |
+--------------------+-------------------------------------------------------+
| ``WriteListRespons | associateIndicatorHosts(\ ``Integer uniqueId``,       |
| e<String>``        | ``List<String> hostNames``)                           |
+--------------------+-------------------------------------------------------+
| ``WriteListRespons | associateIndicatorHosts(\ ``Integer uniqueId``,       |
| e<String>``        | ``List<String> hostNames``, ``String ownerName``)     |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateIndicatorHost(\ ``Integer uniqueId``,        |
| esponse``          | ``String hostName``)                                  |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateIndicatorHost(\ ``Integer uniqueId``,        |
| esponse``          | ``String hostName``, ``String ownerName``)            |
+--------------------+-------------------------------------------------------+
| ``WriteListRespons | associateIndicatorUrls(\ ``Integer uniqueId``,        |
| e<String>``        | ``List<String> urlTexts``)                            |
+--------------------+-------------------------------------------------------+
| ``WriteListRespons | associateIndicatorUrls(\ ``Integer uniqueId``,        |
| e<String>``        | ``List<String> urlTexts``, ``String ownerName``)      |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateIndicatorUrl(\ ``Integer uniqueId``,         |
| esponse``          | ``String urlText``)                                   |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateIndicatorUrl(\ ``Integer uniqueId``,         |
| esponse``          | ``String urlText``, ``String ownerName``)             |
+--------------------+-------------------------------------------------------+

Associate Security Labels
~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below associate Security Labels to a Group type.

+---------------------+------------------------------------------------------+
| Type                | *Method*                                             |
+=====================+======================================================+
| ``WriteListResponse | associateSecurityLabels(\ ``Integer uniqueId``,      |
| <String>``          | ``List<String> securityLabels``)                     |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateSecurityLabels(\ ``Integer uniqueId``,      |
| <String>``          | ``List<String> securityLabels``,                     |
|                     | ``String ownerName``)                                |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateSecurityLabel(\ ``Integer uniqueId``,       |
| sponse``            | ``String securityLabel``)                            |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateSecurityLabel(\ ``Integer uniqueId``,       |
| sponse``            | ``String securityLabel``, ``String ownerName``)      |
+---------------------+------------------------------------------------------+

Associate Tag
~~~~~~~~~~~~~

The methods below associate Tags to a Group type.

+--------------------+-------------------------------------------------------+
| Type               | *Method*                                              |
+====================+=======================================================+
| ``WriteListRespons | associateTags(\ ``Integer uniqueId``,                 |
| e<String>``        | ``List<String> tagNames``)                            |
+--------------------+-------------------------------------------------------+
| ``WriteListRespons | associateTags(\ ``Integer uniqueId``,                 |
| e<String>``        | ``List<String> tagNames``, ``String ownerName``)      |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateTag(\ ``Integer uniqueId``,                  |
| esponse``          | ``String tagName``)                                   |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | associateTag(\ ``Integer uniqueId``,                  |
| esponse``          | ``String tagName``, ``String ownerName``)             |
+--------------------+-------------------------------------------------------+

Associate Victim
~~~~~~~~~~~~~~~~

The methods below associate Victims to a Group type.

+---------------------+------------------------------------------------------+
| Type                | *Method*                                             |
+=====================+======================================================+
| ``WriteListResponse | associateVictims(\ ``Integer uniqueId``,             |
| <Integer>``         | ``List<Integer> victimIds``)                         |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateVictims(\ ``Integer uniqueId``,             |
| <Integer>``         | ``List<Integer> victimIds``, ``String ownerName``)   |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictim(\ ``Integer uniqueId``,              |
| sponse``            | ``Integer victimId``)                                |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictim(\ ``Integer uniqueId``,              |
| sponse``            | ``Integer victimId``, ``String ownerName``)          |
+---------------------+------------------------------------------------------+

Associate Victim Asset
~~~~~~~~~~~~~~~~~~~~~~

The methods below associate Victim Assets to a Group type.

+---------------------+------------------------------------------------------+
| Type                | *Method*                                             |
+=====================+======================================================+
| ``WriteListResponse | associateVictimAssetEmailAddresses(\ ``Integer uniqu |
| <Integer>``         | eId``,                                               |
|                     | ``List<Integer> assetIds``)                          |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateVictimAssetEmailAddresses(\ ``Integer uniqu |
| <Integer>``         | eId``,                                               |
|                     | ``List<Integer> assetIds``, ``String ownerName``)    |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictimAssetEmailAddress(\ ``Integer uniqueI |
| sponse``            | d``,                                                 |
|                     | ``Integer assetId``)                                 |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictimAssetEmailAddress(\ ``Integer uniqueI |
| sponse``            | d``,                                                 |
|                     | ``Integer assetId``, ``String ownerName``)           |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateVictimAssetNetworkAccounts(\ ``Integer uniq |
| <Integer>``         | ueId``,                                              |
|                     | ``List<Integer> assetIds``)                          |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateVictimAssetNetworkAccounts(\ ``Integer uniq |
| <Integer>``         | ueId``,                                              |
|                     | ``List<Integer> assetIds``, ``String ownerName``)    |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictimAssetNetworkAccount(\ ``Integer uniqu |
| sponse``            | eId``,                                               |
|                     | ``Integer assetId``)                                 |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictimAssetNetworkAccount(\ ``Integer uniqu |
| sponse``            | eId``,                                               |
|                     | ``Integer assetId``, ``String ownerName``)           |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateVictimAssetPhoneNumbers(\ ``Integer uniqueI |
| <Integer>``         | d``,                                                 |
|                     | ``List<Integer> assetIds``)                          |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateVictimAssetPhoneNumbers(\ ``Integer uniqueI |
| <Integer>``         | d``,                                                 |
|                     | ``List<Integer> assetIds``, ``String ownerName``)    |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictimAssetPhoneNumber(\ ``Integer uniqueId |
| sponse``            | ``,                                                  |
|                     | ``Integer assetId``)                                 |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictimAssetPhoneNumber(\ ``Integer uniqueId |
| sponse``            | ``,                                                  |
|                     | ``Integer assetId``, ``String ownerName``)           |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateVictimAssetSocialNetworks(\ ``Integer uniqu |
| <Integer>``         | eId``,                                               |
|                     | ``List<Integer> assetIds``)                          |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateVictimAssetSocialNetworks(\ ``Integer uniqu |
| <Integer>``         | eId``,                                               |
|                     | ``List<Integer> assetIds``, ``String ownerName``)    |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictimAssetSocialNetwork(\ ``Integer unique |
| sponse``            | Id``,                                                |
|                     | ``Integer assetId``)                                 |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictimAssetSocialNetwork(\ ``Integer unique |
| sponse``            | Id``,                                                |
|                     | ``Integer assetId``, ``String ownerName``)           |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateVictimAssetWebsites(\ ``Integer uniqueId``, |
| <Integer>``         | ``List<Integer> assetIds``)                          |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | associateVictimAssetWebsites(\ ``Integer uniqueId``, |
| <Integer>``         | ``List<Integer> assetIds``, ``String ownerName``)    |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictimAssetWebsite(\ ``Integer uniqueId``,  |
| sponse``            | ``Integer assetId``)                                 |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | associateVictimAssetWebsite(\ ``Integer uniqueId``,  |
| sponse``            | ``Integer assetId``, ``String ownerName``)           |
+---------------------+------------------------------------------------------+

Add Attributes
~~~~~~~~~~~~~~

The methods below add Attribute types to a Group.

+----------------------+-----------------------------------------------------+
| Type                 | *Method*                                            |
+======================+=====================================================+
| ``WriteListResponse< | addAttributes(\ ``Integer uniqueId``,               |
| Attribute>``         | ``List<Attribute> attributes``)                     |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | addAttributes(\ ``Integer uniqueId``,               |
| Attribute>``         | ``List<Attribute> attribute``,                      |
|                      | ``String ownerName``)                               |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | addAttribute(\ ``Integer uniqueId``,                |
| ponse``              | ``Attribute attribute``)                            |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | addAttribute(\ ``Integer uniqueId``,                |
| ponse``              | ``Attribute attribute``, ``String ownerName``)      |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | addAttributeSecurityLabels(\ ``Integer uniqueId``,  |
| String>``            | ``Integer attributeId``,                            |
|                      | ``List<String> securityLabels``)                    |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | addAttributeSecurityLabels(\ ``Integer uniqueId``,  |
| String>``            | ``Integer attributeId``,                            |
|                      | ``List<String> securityLabels``,                    |
|                      | ``String ownerName``)                               |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | addAttributeSecurityLabel(\ ``Integer uniqueId``,   |
| ponse``              | ``Integer attributeId``, ``String securityLabel``)  |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | addAttributeSecurityLabel(\ ``Integer uniqueId``,   |
| ponse``              | ``Integer attributeId``, ``String securityLabel``,  |
|                      | ``String ownerName``)                               |
+----------------------+-----------------------------------------------------+

Update Attribute
~~~~~~~~~~~~~~~~

The methods below **update** an Attribute added to a specific Indicator
type.

+-----------------------+----------------------------------------------------+
| Type                  | *Method*                                           |
+=======================+====================================================+
| ``WriteListResponse<A | updateAttributes(\ ``Integer uniqueId``,           |
| ttribute>``           | ``List<Attribute> attributes``)                    |
+-----------------------+----------------------------------------------------+
| ``WriteListResponse<A | updateAttributes(\ ``Integer uniqueId``,           |
| ttribute>``           | ``List<Attribute> attribute``,                     |
|                       | ``String ownerName``)                              |
+-----------------------+----------------------------------------------------+
| ``ApiEntitySingleResp | updateAttribute(\ ``Integer uniqueId``,            |
| onse``                | ``Attribute attribute``)                           |
+-----------------------+----------------------------------------------------+
| ``ApiEntitySingleResp | updateAttribute(\ ``Integer uniqueId``,            |
| onse``                | ``Attribute attribute``, ``String ownerName``)     |
+-----------------------+----------------------------------------------------+

Create Observation
~~~~~~~~~~~~~~~~~~

The methods below **create** an Observation on a specific Indicator
type.

+--------------------+-------------------------------------------------------+
| Type               | *Method*                                              |
+====================+=======================================================+
| ``ApiEntitySingleR | createObservation(\ ``Integer uniqueId``)             |
| esponse``          |                                                       |
+--------------------+-------------------------------------------------------+
| ``ApiEntitySingleR | createObservation(\ ``Integer uniqueId``,             |
| esponse``          | ``String ownerName``)                                 |
+--------------------+-------------------------------------------------------+

Update False Positive
~~~~~~~~~~~~~~~~~~~~~

The methods below **update** the False Positive field on a specific
Indicator type.

+--------------------+--------------------------------------------------------+
| Type               | *Method*                                               |
+====================+========================================================+
| ``ApiEntitySingleR | updateFalsePositive(\ ``Integer uniqueId``)            |
| esponse``          |                                                        |
+--------------------+--------------------------------------------------------+
| ``ApiEntitySingleR | updateFalsePositive(\ ``Integer uniqueId``,            |
| esponse``          | ``String ownerName``)                                  |
+--------------------+--------------------------------------------------------+

Delete Group Association
~~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** Group associations to a specific Group
type.

+----------------------+------------------------------------------------------+
| Type                 | *Method*                                             |
+======================+======================================================+
| ``WriteListResponse< | dissociateGroupAdversaries(\ ``Integer uniqueId``,   |
| Integer>``           | ``List<Integer> adversaryIds``)                      |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateGroupAdversaries(\ ``Integer uniqueId``,   |
| Integer>``           | ``List<Integer> adversaryIds``,                      |
|                      | ``String ownerName``)                                |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateGroupAdversary(\ ``Integer uniqueId``,     |
| ponse``              | ``Integer adversaryId``)                             |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateGroupAdversary(\ ``Integer uniqueId``,     |
| ponse``              | ``Integer adversaryId``, ``String ownerName``)       |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateGroupEmails(\ ``Integer uniqueId``,        |
| Integer>``           | ``List<Integer> emailIds``)                          |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateGroupEmails(\ ``Integer uniqueId``,        |
| Integer>``           | ``List<Integer> emailIds``, ``String ownerName``)    |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateGroupEmail(\ ``Integer uniqueId``,         |
| ponse``              | ``Integer emailId``)                                 |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateGroupEmail(\ ``Integer uniqueId``,         |
| ponse``              | ``Integer emailId``, ``String ownerName``)           |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateGroupIncidents(\ ``Integer uniqueId``,     |
| Integer>``           | ``List<Integer> incidentIds``)                       |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateGroupIncidents(\ ``Integer uniqueId``,     |
| Integer>``           | ``List<Integer> incidentIds``, ``String ownerName``) |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateGroupIncident(\ ``Integer uniqueId``,      |
| ponse``              | ``Integer incidentId``)                              |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateGroupIncident(\ ``Integer uniqueId``,      |
| ponse``              | ``Integer incidentId``, ``String ownerName``)        |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateGroupSignatures(\ ``Integer uniqueId``,    |
| Integer>``           | ``List<Integer> signatureIds``)                      |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateGroupSignatures(\ ``Integer uniqueId``,    |
| Integer>``           | ``List<Integer> signatureIds``,                      |
|                      | ``String ownerName``)                                |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateGroupSignature(\ ``Integer uniqueId``,     |
| ponse``              | ``Integer signatureId``)                             |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateGroupSignature(\ ``Integer uniqueId``,     |
| ponse``              | ``Integer signatureId``, ``String ownerName``)       |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateGroupThreats(\ ``Integer uniqueId``,       |
| Integer>``           | ``List<Integer> threatIds``)                         |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateGroupThreats(\ ``Integer uniqueId``,       |
| Integer>``           | ``List<Integer> threatIds``, ``String ownerName``)   |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateGroupThreat(\ ``Integer uniqueId``,        |
| ponse``              | ``Integer threatId``)                                |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateGroupThreat(\ ``Integer uniqueId``,        |
| ponse``              | ``Integer threatId``, ``String ownerName``)          |
+----------------------+------------------------------------------------------+

Delete Indicator Associations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** Indicator associations to a specific Group
type.

+----------------------+-----------------------------------------------------+
| Type                 | *Method*                                            |
+======================+=====================================================+
| ``WriteListResponse< | dissociateIndicatorAddresses(\ ``Integer uniqueId`` |
| String>``            | ,                                                   |
|                      | ``List<String> ipAddresses``)                       |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | dissociateIndicatorAddresses(\ ``Integer uniqueId`` |
| String>``            | ,                                                   |
|                      | ``List<String> ipAddresses``, ``String ownerName``) |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateIndicatorAddress(\ ``Integer uniqueId``,  |
| ponse``              | ``String ipAddress``)                               |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateIndicatorAddress(\ ``Integer uniqueId``,  |
| ponse``              | ``String ipAddress``, ``String ownerName``)         |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | dissociateIndicatorEmailAddresses(\ ``Integer uniqu |
| String>``            | eId``,                                              |
|                      | ``List<String> emailAddresses``)                    |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | dissociateIndicatorEmailAddresses(\ ``Integer uniqu |
| String>``            | eId``,                                              |
|                      | ``List<String> emailAddresses``,                    |
|                      | ``String ownerName``)                               |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateIndicatorEmailAddress(\ ``Integer uniqueI |
| ponse``              | d``,                                                |
|                      | ``String emailAddress``)                            |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateIndicatorEmailAddress(\ ``Integer uniqueI |
| ponse``              | d``,                                                |
|                      | ``String emailAddress``, ``String ownerName``)      |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | dissociateIndicatorFiles(\ ``Integer uniqueId``,    |
| String>``            | ``List<String> fileHashes``)                        |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | dissociateIndicatorFiles(\ ``Integer uniqueId``,    |
| String>``            | ``List<String> fileHashes``, ``String ownerName``)  |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateIndicatorFile(\ ``Integer uniqueId``,     |
| ponse``              | ``String fileHash``)                                |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateIndicatorFile(\ ``Integer uniqueId``,     |
| ponse``              | ``String fileHash``, ``String ownerName``)          |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | dissociateIndicatorHosts(\ ``Integer uniqueId``,    |
| String>``            | ``List<String> hostNames``)                         |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | dissociateIndicatorHosts(\ ``Integer uniqueId``,    |
| String>``            | ``List<String> hostNames``, ``String ownerName``)   |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateIndicatorHost(\ ``Integer uniqueId``,     |
| ponse``              | ``String hostName``)                                |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateIndicatorHost(\ ``Integer uniqueId``,     |
| ponse``              | ``String hostName``, ``String ownerName``)          |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | dissociateIndicatorUrls(\ ``Integer uniqueId``,     |
| String>``            | ``List<String> urlTexts``)                          |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | dissociateIndicatorUrls(\ ``Integer uniqueId``,     |
| String>``            | ``List<String> urlTexts``, ``String ownerName``)    |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateIndicatorUrl(\ ``Integer uniqueId``,      |
| ponse``              | ``String urlText``)                                 |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateIndicatorUrl(\ ``Integer uniqueId``,      |
| ponse``              | ``String urlText``, ``String ownerName``)           |
+----------------------+-----------------------------------------------------+

Delete Security Label Associations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** SecurityLabel associations to a specific
Group type.

+---------------------+------------------------------------------------------+
| Type                | *Method*                                             |
+=====================+======================================================+
| ``WriteListResponse | dissociateSecurityLabel(\ ``Integer uniqueId``,      |
| <String>``          | ``List<String> securityLabels``)                     |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | dissociateSecurityLabel(\ ``Integer uniqueId``,      |
| <String>``          | ``List<String> securityLabels``,                     |
|                     | ``String ownerName``)                                |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | dissociateSecurityLabel(\ ``Integer uniqueId``,      |
| sponse``            | ``String securityLabel``)                            |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | dissociateSecurityLabel(\ ``Integer uniqueId``,      |
| sponse``            | ``String securityLabel``, ``String ownerName``)      |
+---------------------+------------------------------------------------------+

Delete Tag Associations
~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** Tag associations to a specific Group type.

+---------------------+------------------------------------------------------+
| Type                | *Method*                                             |
+=====================+======================================================+
| ``WriteListResponse | dissociateTags(\ ``Integer uniqueId``,               |
| <String>``          | ``List<String> tagNames``)                           |
+---------------------+------------------------------------------------------+
| ``WriteListResponse | dissociateTags(\ ``Integer uniqueId``,               |
| <String>``          | ``List<String> tagNames``, ``String ownerName``)     |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | dissociateTag(\ ``Integer uniqueId``,                |
| sponse``            | ``String tagName``)                                  |
+---------------------+------------------------------------------------------+
| ``ApiEntitySingleRe | dissociateTag(\ ``Integer uniqueId``,                |
| sponse``            | ``String tagName``, ``String ownerName``)            |
+---------------------+------------------------------------------------------+

Delete Victim Associations
~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** Victim associations to a specific Group
type.

+----------------------+-----------------------------------------------------+
| Type                 | *Method*                                            |
+======================+=====================================================+
| ``WriteListResponse< | dissociateVictims(\ ``Integer uniqueId``,           |
| Integer>``           | ``List<Integer> victimIds``)                        |
+----------------------+-----------------------------------------------------+
| ``WriteListResponse< | dissociateVictims(\ ``Integer uniqueId``,           |
| Integer>``           | ``List<Integer> victimIds``, ``String ownerName``)  |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictim(\ ``Integer uniqueId``,            |
| ponse``              | ``Integer victimId``)                               |
+----------------------+-----------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictim(\ ``Integer uniqueId``,            |
| ponse``              | ``Integer victimId``, ``String ownerName``)         |
+----------------------+-----------------------------------------------------+

Delete VictimAsset Associations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods below **delete** VictimAsset associations to a specific
Group type.

+----------------------+------------------------------------------------------+
| Type                 | *Method*                                             |
+======================+======================================================+
| ``WriteListResponse< | dissociateVictimAssetEmailAddresses(\ ``Integer uniq |
| Integer>``           | ueId``,                                              |
|                      | ``List<Integer> assetIds``)                          |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateVictimAssetEmailAddresses(\ ``Integer uniq |
| Integer>``           | ueId``,                                              |
|                      | ``List<Integer> assetIds``, ``String ownerName``)    |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictimAssetEmailAddress(\ ``Integer unique |
| ponse``              | Id``,                                                |
|                      | ``Integer assetId``)                                 |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictimAssetEmailAddress(\ ``Integer unique |
| ponse``              | Id``,                                                |
|                      | ``Integer assetId``, ``String ownerName``)           |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateVictimAssetNetworkAccounts(\ ``Integer uni |
| Integer>``           | queId``,                                             |
|                      | ``List<Integer> assetIds``)                          |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateVictimAssetNetworkAccounts(\ ``Integer uni |
| Integer>``           | queId``,                                             |
|                      | ``List<Integer> assetIds``, ``String ownerName``)    |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictimAssetNetworkAccount(\ ``Integer uniq |
| ponse``              | ueId``,                                              |
|                      | ``Integer assetId``)                                 |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictimAssetNetworkAccount(\ ``Integer uniq |
| ponse``              | ueId``,                                              |
|                      | ``Integer assetId``, ``String ownerName``)           |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateVictimAssetPhoneNumbers(\ ``Integer unique |
| Integer>``           | Id``,                                                |
|                      | ``List<Integer> assetIds``)                          |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateVictimAssetPhoneNumbers(\ ``Integer unique |
| Integer>``           | Id``,                                                |
|                      | ``List<Integer> assetIds``, ``String ownerName``)    |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictimAssetPhoneNumber(\ ``Integer uniqueI |
| ponse``              | d``,                                                 |
|                      | ``Integer assetId``)                                 |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictimAssetPhoneNumber(\ ``Integer uniqueI |
| ponse``              | d``,                                                 |
|                      | ``Integer assetId``, ``String ownerName``)           |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateVictimAssetSocialNetworks(\ ``Integer uniq |
| Integer>``           | ueId``,                                              |
|                      | ``List<Integer> assetIds``)                          |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateVictimAssetSocialNetworks(\ ``Integer uniq |
| Integer>``           | ueId``,                                              |
|                      | ``List<Integer> assetIds``, ``String ownerName``)    |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictimAssetSocialNetwork(\ ``Integer uniqu |
| ponse``              | eId``,                                               |
|                      | ``Integer assetId``)                                 |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictimAssetSocialNetwork(\ ``Integer uniqu |
| ponse``              | eId``,                                               |
|                      | ``Integer assetId``, ``String ownerName``)           |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateVictimAssetWebsites(\ ``Integer uniqueId`` |
| Integer>``           | ,                                                    |
|                      | ``List<Integer> assetIds``)                          |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | dissociateVictimAssetWebsites(\ ``Integer uniqueId`` |
| Integer>``           | ,                                                    |
|                      | ``List<Integer> assetIds``, ``String ownerName``)    |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictimAssetWebsite(\ ``Integer uniqueId``, |
| ponse``              | ``Integer assetId``)                                 |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | dissociateVictimAssetWebsite(\ ``Integer uniqueId``, |
| ponse``              | ``Integer assetId``, ``String ownerName``)           |
+----------------------+------------------------------------------------------+

Delete Attribute
~~~~~~~~~~~~~~~~

The methods below **delete** Attributes from a specific Group type.

+----------------------+------------------------------------------------------+
| Type                 | *Method*                                             |
+======================+======================================================+
| ``WriteListResponse< | deleteAttributes(\ ``Integer uniqueId``,             |
| Integer>``           | ``List<Integer> attributes``)                        |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | deleteAttributes(\ ``Integer uniqueId``,             |
| Integer>``           | ``List<Integer> attribute``, ``String ownerName``)   |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | deleteAttribute(\ ``Integer uniqueId``,              |
| ponse``              | ``Integer attribute``)                               |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | deleteAttribute(\ ``Integer uniqueId``,              |
| ponse``              | ``Integer attribute``, ``String ownerName``)         |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | deleteAttributeSecurityLabels(\ ``Integer uniqueId`` |
| String>``            | ,                                                    |
|                      | ``Integer attributeId``,                             |
|                      | ``List<String> securityLabels``)                     |
+----------------------+------------------------------------------------------+
| ``WriteListResponse< | deleteAttributeSecurityLabels(\ ``Integer uniqueId`` |
| String>``            | ,                                                    |
|                      | ``Integer attributeId``,                             |
|                      | ``List<String> securityLabels``,                     |
|                      | ``String ownerName``)                                |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | deleteAttributeSecurityLabel(\ ``Integer uniqueId``, |
| ponse``              | ``Integer attributeId``, ``String securityLabel``)   |
+----------------------+------------------------------------------------------+
| ``ApiEntitySingleRes | deleteAttributeSecurityLabel(\ ``Integer uniqueId``, |
| ponse``              | ``Integer attributeId``, ``String securityLabel``,   |
|                      | ``String ownerName``)                                |
+----------------------+------------------------------------------------------+

AbstractIndicatorWriterAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AbstractIndicatorWriterAdapter shares most of the write
functionality with the AbstractGroupWriterAdapter. In fact, they both
implement the following writer interfaces:

Interface \| ----------------------------------------- \|
``AttributeAssociateWritable<T>`` \| ``GroupAssociateWritable<T>`` \|
``IndicatorAssociateWritable<T>`` \|
``SecurityLabelAssociateWritable<T>`` \| ``TagAssociateWritable<T>`` \|
``VictimAssetAssociateWritable<T>`` \|

These interfaces allow the AbstractIndicatorWriterAdapter to run all of
the same methods as the AbstractGroupWriterAdapter.

The key parameter-level distinction between the
AbstractIndicatorWriterAdapter and the AbstractGroupWriterAdapter is the
type (T) for the ``uniqueId`` parameter. As mentioned in previous
sections, Indicator ``uniqueId`` types are all Strings. The
method-naming conventions are the same.

FileIndicatorWriterAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

FileIndicatorWriterAdapter, which all the functionality of the
AbstractIndicatorWriterAdapter with the addition of the following write
methods:

+--------------------------+-------------------------------------------------+
| Type                     | *Method*                                        |
+==========================+=================================================+
| ``WriteListResponse<File | updateFileOccurrences(\ ``String fileHash``,    |
| Occurrence>``            | ``List<FileOccurrence> fileOccurrences``)       |
+--------------------------+-------------------------------------------------+
| ``WriteListResponse<File | updateFileOccurrences(\ ``String fileHash``,    |
| Occurrence>``            | ``List<FileOccurrence> fileOccurrences``,       |
|                          | ``String ownerName``)                           |
+--------------------------+-------------------------------------------------+
| ``FileOccurrence``       | updateFileOccurrence(\ ``String fileHash``,     |
|                          | ``FileOccurrence fileOccurrence``)              |
+--------------------------+-------------------------------------------------+
| ``FileOccurrence``       | updateFileOccurrence(\ ``String fileHash``,     |
|                          | ``FileOccurrence fileOccurrence``,              |
|                          | ``String ownerName``)                           |
+--------------------------+-------------------------------------------------+

DocumentWriterAdapter
~~~~~~~~~~~~~~~~~~~~~

DocumentWriterAdapter has all the functionality of the
AbstractGroupWriterAdapter with the addition of the following write
methods:

+-------------------+--------------------------------------------------------+
| Type              | *Method*                                               |
+===================+========================================================+
| ``ApiEntitySingle | uploadFile(\ ``int uniqueId``, ``File file``)          |
| Response``        |                                                        |
+-------------------+--------------------------------------------------------+
| ``ApiEntitySingle | uploadFile(\ ``int uniqueId``, ``File file``,          |
| Response``        | ``String ownerName``)                                  |
+-------------------+--------------------------------------------------------+

AbstractBatchWriterAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

The AbstractBatchWriterAdapter class allows batch writing of indicators
to the API. The adapter facilitates the initial creation and upload of
the batch file using the following write methods:

+-------------------------------+--------------------------------------------------------+
| Type                          | *Method*                                               |
+===============================+========================================================+
| ``ApiEntitySingleResponse``   | create(\ ``BatchConfig item`` )                        |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | create(\ ``BatchConfig item``, ``String ownerName``)   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | uploadFile(\ ``int batchId``, ``File file``)           |
+-------------------------------+--------------------------------------------------------+

Once a batch configuration is created, the ApiEntitySingleResponse
object returns BatchResponseData with a batchId if successful. This
batchId is used to upload the batch file using the ``uploadFile``
method. At this point, a successfuly response to the upload will trigger
the batch. Use the BatchReaderAdapter to poll for the status of the
batch.

SecurityLabelWriterAdapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

The SecurityLabelWriterAdapter class allows
`Group <#associate-groups>`__ and `Indicator <#associate-indicators>`__
associations. Much like the Indicator Adapters, the ``uniqueId`` is a
user-created Security Label String. In addition to creating
associations, the SecurityLabelWriterAdapter allows deleting
associations from `Group <#dissociate-groups>`__ and
`Indicator <#dissociate-indicators>`__ types.

Below is the standard create methods available to all WriterAdapter’s.
Note that the deletes require the Security Label as the ``uniqueId``
String (P). The create and update requires the full SecurityLabel object
(T).

+-------------------------------+--------------------------------------------------------+
| Type                          | *Method*                                               |
+===============================+========================================================+
| ``WriteListResponse<T>``      | create(\ ``List<T> itemList``)                         |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | create(\ ``T item``)                                   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | create(\ ``T item``, ``String ownerName``)             |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<P>``      | delete(\ ``List<P> itemIds``)                          |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<P>``      | delete(\ ``List<P> itemIds``, ``String ownerName``)    |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | delete(\ ``P itemId``)                                 |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | delete(\ ``P itemId``, ``String ownerName``)           |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<T>``      | update(\ ``List<T> itemList``)                         |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<T>``      | update(\ ``List<T> itemList``, ``String ownerName``)   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | update(\ ``T item``)                                   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | update(\ ``T item``, ``String ownerName``)             |
+-------------------------------+--------------------------------------------------------+

TagWriterAdapter
~~~~~~~~~~~~~~~~

The TagWriterAdapter class allows `Group <#associate-groups>`__ and
`Indicator <#associate-indicators>`__ associations. Much like the
Indicator Adapters, the uniqueId is a user-created Tag name String. In
addition to creating associations, the TagWriterAdapter allows deleting
associations from `Group <#dissociate-groups>`__ and
`Indicator <#dissociate-indicators>`__ types.

Below is the standard create methods available to all WriterAdapters.
Note that the deletes require the Tag Name as the ``uniqueId`` String
(P). The create and update requires the full Tag object (T).

+-------------------------------+--------------------------------------------------------+
| Type                          | *Method*                                               |
+===============================+========================================================+
| ``WriteListResponse<T>``      | create(\ ``List<T> itemList``)                         |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | create(\ ``T item``)                                   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | create(\ ``T item``, ``String ownerName``)             |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<P>``      | delete(\ ``List<P> itemIds``)                          |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<P>``      | delete(\ ``List<P> itemIds``, ``String ownerName``)    |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | delete(\ ``P itemId``)                                 |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | delete(\ ``P itemId``, ``String ownerName``)           |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<T>``      | update(\ ``List<T> itemList``)                         |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<T>``      | update(\ ``List<T> itemList``, ``String ownerName``)   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | update(\ ``T item``)                                   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | update(\ ``T item``, ``String ownerName``)             |
+-------------------------------+--------------------------------------------------------+

TaskWriterAdapter
~~~~~~~~~~~~~~~~~

The TaskWriterAdapter allows

Below is the standard create methods available to all WriterAdapters.

+-------------------------------+
| Type                          |
+===============================+
| ``WriteListResponse<T>``      |
+-------------------------------+
| ``ApiEntitySingleResponse``   |
+-------------------------------+
| ``ApiEntitySingleResponse``   |
+-------------------------------+
| ``WriteListResponse<P>``      |
+-------------------------------+
| ``WriteListResponse<P>``      |
+-------------------------------+
| ``ApiEntitySingleResponse``   |
+-------------------------------+
| ``ApiEntitySingleResponse``   |
+-------------------------------+
| ``WriteListResponse<T>``      |
+-------------------------------+
| ``WriteListResponse<T>``      |
+-------------------------------+
| ``ApiEntitySingleResponse``   |
+-------------------------------+
| ``ApiEntitySingleResponse``   |
+-------------------------------+

In addition to the User-specific methods below. Note the delete methods
require the username while the create methods require the entire User
object.

+--------------------+------------------------------------------------+
| Type               | *Method*                                       |
+====================+================================================+
| ``UserResponse``   | createAssignee(P uniqueId, User assignee)      |
+--------------------+------------------------------------------------+
| ``UserResponse``   | createEscalatee(P uniqueId, User escalatee)    |
+--------------------+------------------------------------------------+
| ``UserResponse``   | deleteAssignee(P uniqueId, String userName)    |
+--------------------+------------------------------------------------+
| ``UserResponse``   | deleteEscalatee(P uniqueId, String userName)   |
+--------------------+------------------------------------------------+

VictimWriterAdapter
~~~~~~~~~~~~~~~~~~~

The TagWriterAdapter class allows `Group <#associate-groups>`__,
`Indicator <#associate-indicators>`__, and VictimAsset associations.
Much like the Group Adapters, the uniqueId is a user-created Security
Label String. In addition to creating associations, the
VictimAssetWriterAdapter can remove associations for
`Group <#dissociate-groups>`__, `Indicator <#dissociate-indicators>`__,
and `VictimAssets <#dissociate-victimasset>`__.

Below is the standard create methods available to all WriterAdapters.
Note that the deletes require the system-generated VictimAsset ID as the
``uniqueId`` Integer (P). The create and update requires the full
VictimAsset object (T).

+-------------------------------+--------------------------------------------------------+
| Type                          | *Method*                                               |
+===============================+========================================================+
| ``WriteListResponse<T>``      | create(\ ``List<T> itemList``)                         |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | create(\ ``T item``)                                   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | create(\ ``T item``, ``String ownerName``)             |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<P>``      | delete(\ ``List<P> itemIds``)                          |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<P>``      | delete(\ ``List<P> itemIds``, ``String ownerName``)    |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | delete(\ ``P itemId``)                                 |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | delete(\ ``P itemId``, ``String ownerName``)           |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<T>``      | update(\ ``List<T> itemList``)                         |
+-------------------------------+--------------------------------------------------------+
| ``WriteListResponse<T>``      | update(\ ``List<T> itemList``, ``String ownerName``)   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | update(\ ``T item``)                                   |
+-------------------------------+--------------------------------------------------------+
| ``ApiEntitySingleResponse``   | update(\ ``T item``, ``String ownerName``)             |
+-------------------------------+--------------------------------------------------------+

Writer Examples
~~~~~~~~~~~~~~~

Writer Delete Example:

.. code:: java


      2 
      3 import com.threatconnect.sdk.client.reader.AbstractGroupReaderAdapter;
      4 import com.threatconnect.sdk.client.reader.ReaderAdapterFactory;
      5 
      6 import com.threatconnect.sdk.client.writer.AbstractGroupWriterAdapter;
      7 import com.threatconnect.sdk.client.writer.WriterAdapterFactory;
      8 import com.threatconnect.sdk.server.response.entity.ApiEntitySingleResponse;
      9 
     10 import com.threatconnect.sdk.server.entity.Adversary;
     11 import com.threatconnect.sdk.conn.Connection;
     12 import java.io.IOException;
     13 
     
    130     private static void doDelete(Connection conn) {
    131         AbstractGroupWriterAdapter<Adversary> writer = WriterAdapterFactory.createAdversaryGroupWriter(conn);
    132 
    133         Adversary adversary = new Adversary();
    134         adversary.setName("Test Adversary");
    135         adversary.setOwnerName("System");
    136 
    137         try {
    138             ApiEntitySingleResponse<Adversary,?> createResponse = writer.create(adversary);
    139             if ( createResponse.isSuccess() ) {
    140                 System.out.println("Saved: " + createResponse.getItem() );
    141                 ApiEntitySingleResponse<Adversary,?> deleteResponse 
    142                    = writer.delete( createResponse.getItem().getId() );
    143                 if ( deleteResponse.isSuccess() ) {
    144                     System.out.println("Deleted: " + createResponse.getItem() );
    145                 } else {
    146                     System.err.println("Delete Failed. Cause: " + deleteResponse.getMessage() );
    147                 }
    148             } else {
    149                 System.err.println("Create Failed. Cause: " + createResponse.getMessage() );
    150             }
    151             
    152         } catch (IOException | FailedResponseException ex) {
    153             System.err.println("Error: " + ex.toString());
    154         }
    155     
    156     }
     

This section offers examples on how to create, delete, and update data
using the Java SDK for ThreatConnect.

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 131          | Since Adversary objects from the ThreatConnect API will be  |
|              | created and deleted, an AbstractGroupWriterAdapter with the |
|              | Adversary parameterized type applied is instantiated.       |
+--------------+-------------------------------------------------------------+
| 138-139      | An Adversary object with the ThreatConnect API is created,  |
|              | the response is captured, and ``isSuccess()`` is called to  |
|              | check if the save was successful.                           |
+--------------+-------------------------------------------------------------+
| 140          | The response Adversary object returned from the             |
|              | ThreatConnect API is printed. The ``getItem()``\ method     |
|              | will return this object with the ID field populated. This   |
|              | method will always hold the saved item on a successful      |
|              | response.                                                   |
+--------------+-------------------------------------------------------------+
| 141-142      | The ID from the successful create is used to delete the     |
|              | same Adversary object. Note that the call to the            |
|              | ``delete()`` method requires the system-generated Adversary |
|              | ID.                                                         |
+--------------+-------------------------------------------------------------+
| 143-144      | The delete response is verified as successful, and the      |
|              | original response is dumped.                                |
+--------------+-------------------------------------------------------------+
| 146          | With a failed delete, the error message is printed by       |
|              | calling the ``getMessage()`` method on the response object. |
+--------------+-------------------------------------------------------------+
| 149          | If the original create failed, the ``getMessage()`` method  |
|              | is also called to find the cause.                           |
+--------------+-------------------------------------------------------------+

Writer Update Example
~~~~~~~~~~~~~~~~~~~~~

Writer Update Example:

.. code:: java


      2 
      3 import com.threatconnect.sdk.client.reader.AbstractGroupReaderAdapter;
      4 import com.threatconnect.sdk.client.reader.ReaderAdapterFactory;
      5 import com.threatconnect.sdk.client.writer.AbstractGroupWriterAdapter;
      6 import com.threatconnect.sdk.client.writer.WriterAdapterFactory;
      7 import com.threatconnect.sdk.conn.Connection;
      8 import com.threatconnect.sdk.exception.FailedResponseException;
      9 import com.threatconnect.sdk.server.entity.Adversary;

     15 import com.threatconnect.sdk.server.response.entity.ApiEntitySingleResponse;
     16 import java.io.IOException;
     17 import java.util.List;
     18 

    153 
    154     private static void doUpdate(Connection conn) {
    155         AbstractGroupWriterAdapter<Adversary> writer = WriterAdapterFactory.createAdversaryGroupWriter(conn);
    156 
    157         Adversary adversary = new Adversary();
    158         adversary.setName("Test Adversary");
    159         adversary.setOwnerName("System");
    160 
    161         try {
    162             ApiEntitySingleResponse<Adversary,?> createResponse = writer.create(adversary);
    163             if ( createResponse.isSuccess() ) {
    164                 System.out.println("Created Adversary: " + createResponse.getItem() );
    165 
    166                 Adversary updatedAdversary = createResponse.getItem();
    167                 updatedAdversary.setName("UPDATED: " + createResponse.getItem().getName());
    168                 System.out.println("Saving Updated Adversary: " + updatedAdversary );
    169 
    170                 ApiEntitySingleResponse<Adversary,?> updateResponse = writer.update( updatedAdversary );
    171                 if ( updateResponse.isSuccess() ) {
    172                     System.out.println("Updated Adversary: " + updateResponse.getItem());
    173                 } else {
    174                     System.err.println("Failed to Update Adversary: " + updateResponse.getMessage() );
    175                 }   
    176             } else {
    177                 System.err.println("Failed to Create Adversary: " + createResponse.getMessage() );
    178             }   
    179             
    180         } catch (IOException | FailedResponseException ex) {
    181             System.err.println("Error: " + ex.toString()); 
    182         }   
    183         
    184     }

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 155-164      | A test Adversary is created and saved to the ThreatConnect  |
|              | API.                                                        |
+--------------+-------------------------------------------------------------+
| 166-168      | The created Adversary is assigned to a variable called      |
|              | "updatedAdversary()" so that the Adversary name can be      |
|              | changed (line 167). Before updating the Adversary in        |
|              | ThreatConnect, it is printed to the console. The output     |
|              | should have an ID value populated and the name should read: |
|              | "UPDATED: Test Adversary".                                  |
+--------------+-------------------------------------------------------------+
| 170-172      | The "update()" method is called to save the changes to      |
|              | ThreatConnect. The argument to this method is the actual    |
|              | Adversary object. Just like the delete, the response        |
|              | success is verified and written to the console.             |
+--------------+-------------------------------------------------------------+

Writer Add Attribute Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Add Attribute Example

.. code:: java

      1 
      2     private static Email createTestEmail() {
      3         Email email = new Email();
      4         email.setName("Test Email");
      5         email.setOwnerName("System");
      6         email.setFrom("admin@test.com");
      7         email.setTo("test@test.com");
      8         email.setSubject("Test Subject");
      9         email.setBody("Test Body");
     10         email.setHeader("Test Header");
     11 
     12         return email;
     13     }
     14 
     15     private static Attribute createTestAttribute() {
     16         Attribute attribute = new Attribute();
     17         attribute.setSource("Test Source");
     18         attribute.setDisplayed(true);
     19         attribute.setType("Description");
     20         attribute.setValue("Test Attribute Description");
     21 
     22         return attribute;
     23     }

     69     private static void doAddAttribute(Connection conn) {
     70         AbstractGroupWriterAdapter<Email> writer = WriterAdapterFactory.createEmailGroupWriter(conn);
     71 
     72         Email email = createTestEmail();
     73         Attribute attribute = createTestAttribute();
     74 
     75         try {
     76             // ------------------------------------------------------------------
     77             // Create Email
     78             // ------------------------------------------------------------------
     79             ApiEntitySingleResponse<Email, ?> createResponse = writer.create(email);
     80             if (createResponse.isSuccess()) {
     81                 System.out.println("Created Email: " + createResponse.getItem());
     82 
     83                 // -------------------------------------------------------------------
     84                 // Add Attribute
     85                 // -------------------------------------------------------------------
     86                 ApiEntitySingleResponse<Attribute, ?> attribResponse
     87                     = writer.addAttribute( createResponse.getItem().getId(), attribute );
     88 
     89                 if ( attribResponse.isSuccess() ) {
     90                     System.out.println("\tAdded Attribute: " + attribResponse.getItem());
     91                 } else {
     92                     System.err.println("Failed to Add Attribute: " + attribResponse.getMessage());
     93                 }
     94 
     95             } else {
     96                 System.err.println("Failed to Create Email: " + createResponse.getMessage());
     97             }
     98 
     99         } catch (IOException | FailedResponseException ex) {
    100             System.err.println("Error: " + ex.toString());
    101         }
    102 
    103     }
    104

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 72-73        | The test email object and the Attribute to be added are     |
|              | created.                                                    |
+--------------+-------------------------------------------------------------+
| 79-81        | The email in ThreatConnect is created and checked that it   |
|              | is successful.                                              |
+--------------+-------------------------------------------------------------+
| 86-87        | The ``addAttribute()`` method takes the Email Group ID and  |
|              | the Attribute object to be added.                           |
+--------------+-------------------------------------------------------------+
| 89-90        | To confirm that the Attribute was added successfully, the   |
|              | response is checked.                                        |
+--------------+-------------------------------------------------------------+

Writer Associate Indicator Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Associate Indicator Example

.. code:: java

      1 
      2     private static Email createTestEmail() {
      3         Email email = new Email();
      4         email.setName("Test Email");
      5         email.setOwnerName("System");
      6         email.setFrom("admin@test.com");
      7         email.setTo("test@test.com");
      8         email.setSubject("Test Subject");
      9         email.setBody("Test Body");
     10         email.setHeader("Test Header");
     11 
     12         return email;
     13     }
     14 

     25     private static Host createTestHost() {
     26         Host host = new Host();
     27         host.setOwnerName("System");
     28         host.setDescription("Test Host");
     29         host.setHostName("www.bad-hostname.com");
     30         host.setRating( 5.0 );
     31         host.setConfidence(98.0);
     32 
     33         return host;
     34     }

    104 
    105     private static void doAssociateIndicator(Connection conn) {
    106         AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
    107         AbstractIndicatorWriterAdapter<Host> hWriter = WriterAdapterFactory.createHostIndicatorWriter(conn);
    108 
    109         Email email = createTestEmail();
    110         Host host = createTestHost();
    111 
    112         try {
    113 
    114             // ----------------------------------------
    115             // Create Email and Host
    116             // ----------------------------------------
    117             ApiEntitySingleResponse<Email,?> createResponseEmail = gWriter.create(email);
    118             ApiEntitySingleResponse<Host,?> createResponseHost = hWriter.create(host);
    119             if (createResponseEmail.isSuccess() && createResponseHost.isSuccess() ) {
    120                 System.out.println("Created Email: " + createResponseEmail.getItem());
    121                 System.out.println("Created Host: " + createResponseHost.getItem());
    122 
    123                 // -----------------------------------------
    124                 // Associate Host
    125                 // -----------------------------------------
    126                 ApiEntitySingleResponse assocResponse
    127                      gWriter.associateIndicatorHost(createResponseEmail.getItem().getId()
    128                                                   , createResponseHost.getItem().getHostName() );
    129 
    130                 if ( assocResponse.isSuccess() ) {
    131                     System.out.println("\tAssociated Host: " + createResponseHost.getItem().getHostName() );
    132                 } else {
    133                     System.err.println("Failed to Add Attribute: " + assocResponse.getMessage());
    134                 }
    135 
    136             } else {
    137                 if ( !createResponseEmail.isSuccess() ) {
    138                     System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
    139                 }
    140                 if ( !createResponseHost.isSuccess() ) {
    141                     System.err.println("Failed to Create Host: " + createResponseHost.getMessage());
    142                 }
    143             }
    144 
    145         } catch (IOException | FailedResponseException ex) {
    146             System.err.println("Error: " + ex.toString());
    147         }
    148 
    149     }

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 106-107      | Two writers are created: one for the new email and the      |
|              | other for the host to be associated.                        |
+--------------+-------------------------------------------------------------+
| 109-110      | The test email object is crated, as well as the host to be  |
|              | associated.                                                 |
+--------------+-------------------------------------------------------------+
| 117-121      | To set up the example, both email and host are created in   |
|              | ThreatConnect. The create is verified as successful and the |
|              | items are printed to the console.                           |
+--------------+-------------------------------------------------------------+
| 126-128      | The host is associated to the Email Group by using the      |
|              | Email ID and the Host Name (the unique ID for the Host      |
|              | Indicator).                                                 |
+--------------+-------------------------------------------------------------+
| 130-133      | The association is verified as successful.                  |
+--------------+-------------------------------------------------------------+

Writer Associate Group Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Associate Group Example

.. code:: java


      2     private static Email createTestEmail() {
      3         Email email = new Email();
      4         email.setName("Test Email");
      5         email.setOwnerName("System");
      6         email.setFrom("admin@test.com");
      7         email.setTo("test@test.com");
      8         email.setSubject("Test Subject");
      9         email.setBody("Test Body");
     10         email.setHeader("Test Header");
     11 
     12         return email;
     13     }
     14 

     36     private static Threat createTestThreat() {
     37         Threat threat = new Threat();
     38         threat.setOwnerName("System");
     39         threat.setName("Test Threat");
     40 
     41         return threat;
     42     }

    151 
    152     private static void doAssociateGroup(Connection conn) {
    153         AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
    154         AbstractGroupWriterAdapter<Threat> tWriter = WriterAdapterFactory.createThreatGroupWriter(conn);
    155 
    156         Email email = createTestEmail();
    157         Threat threat = createTestThreat();
    158 
    159         try {
    160             // ---------------------------------
    161             // Create Email and Threat
    162             // ---------------------------------
    163             ApiEntitySingleResponse<Email,?> createResponseEmail = gWriter.create(email);
    164             ApiEntitySingleResponse<Threat,?> createResponseThreat = tWriter.create(threat);
    165             if (createResponseEmail.isSuccess() && createResponseThreat.isSuccess() ) {
    166                 System.out.println("Created Email: " + createResponseEmail.getItem());
    167                 System.out.println("Created Threat: " + createResponseThreat.getItem());
    168 
    169                 // ----------------------------------
    170                 // Associate Threat
    171                 // ----------------------------------
    172                 ApiEntitySingleResponse assocResponse
    173                     = gWriter.associateGroupThreat(createResponseEmail.getItem().getId(), 
    174                                                 createResponseThreat.getItem().getId());
    175                 
    176                 if ( assocResponse.isSuccess() ) {
    177                     System.out.println("\tAssociated Threat: " + createResponseThreat.getItem().getId() );
    178                 } else {
    179                     System.err.println("Failed to Associate Threat: " + assocResponse.getMessage());
    180                 }
    181             
    182             } else { 
    183                 if ( !createResponseEmail.isSuccess() ) {
    184                     System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
    185                 }
    186                 if ( !createResponseThreat.isSuccess() ) {
    187                     System.err.println("Failed to Create Threat: " + createResponseThreat.getMessage());
    188                 }
    189             }
    190         
    191         } catch (IOException | FailedResponseException ex) {
    192             System.err.println("Error: " + ex.toString());
    193         }
    194 
    195     }
    196 

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 153-154      | Two writers are created: one for the new email and the      |
|              | other for the Threat to be associated.                      |
+--------------+-------------------------------------------------------------+
| 156-157      | The test email object is created, as well as the Threat to  |
|              | be associated.                                              |
+--------------+-------------------------------------------------------------+
| 163-167      | To set up the example, both email and Threat are created in |
|              | ThreatConnect, the create is verified as successful, and    |
|              | the items are printed to the console.                       |
+--------------+-------------------------------------------------------------+
| 172-174      | The Threat is associated to the Email Group by using the    |
|              | Email ID and the Threat ID.                                 |
+--------------+-------------------------------------------------------------+
| 176-179      | The association is verified as successful.                  |
+--------------+-------------------------------------------------------------+

Writer Associate Tag Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Associate Tag Example

.. code:: java


      2     private static Email createTestEmail() {
      3         Email email = new Email();
      4         email.setName("Test Email");
      5         email.setOwnerName("System");
      6         email.setFrom("admin@test.com");
      7         email.setTo("test@test.com");
      8         email.setSubject("Test Subject");
      9         email.setBody("Test Body");
     10         email.setHeader("Test Header");
     11 
     12         return email;
     13     }
     14 

     44     private static Tag createTestTag() {
     45         Tag tag = new Tag();
     46         tag.setName("Test-Tag");
     47         tag.setDescription("Test Tag Description");
     48 
     49         return tag;
     50     }

    196 
    197     private static void doAssociateTag(Connection conn) {
    198         AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
    199         TagWriterAdapter tWriter = WriterAdapterFactory.createTagWriter(conn);
    200 
    201         Email email = createTestEmail();
    202         Tag tag = createTestTag();
    203 
    204         try {
    205             // -------------------------------------------
    206             // Create Email and Tag 
    207             // -------------------------------------------
    208             ApiEntitySingleResponse<Email, ?> createResponseEmail = gWriter.create(email);
    209             tWriter.delete(tag.getName()); // delete if it exists
    210             ApiEntitySingleResponse<Tag, ?> createResponseTag = tWriter.create(tag);
    211 
    212             if (createResponseEmail.isSuccess() && createResponseTag.isSuccess() ) {
    213                 System.out.println("Created Email: " + createResponseEmail.getItem());
    214                 System.out.println("Created Tag: " + createResponseTag.getItem());
    215 
    216                 // ---------------------------------------------
    217                 // Associate Tag
    218                 // ---------------------------------------------
    219                 ApiEntitySingleResponse assocResponse
    220                     = gWriter.associateTag(createResponseEmail.getItem().getId()
    221                                          , createResponseTag.getItem().getName() );
    222 
    223                 if ( assocResponse.isSuccess() ) {
    224                     System.out.println("\tAssociated Tag: " + createResponseTag.getItem().getName() );
    225                 } else {
    226                     System.err.println("Failed to Associate Tag: " + assocResponse.getMessage());
    227                 }
    228 
    229             } else {
    230                 if ( !createResponseEmail.isSuccess() ) {
    231                     System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
    232                 }
    233                 if ( !createResponseTag.isSuccess() ) {
    234                     System.err.println("Failed to Create Tag: " + createResponseTag.getMessage());
    235                 }
    236             }
    237         
    238         } catch (IOException | FailedResponseException ex) {
    239             System.err.println("Error: " + ex.toString());
    240         }
    241     }

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 198-199      | Two writers are created: one for the new email and the      |
|              | other for the Tag to associate.                             |
+--------------+-------------------------------------------------------------+
| 201-202      | The test email object, and the Tag to associate, are        |
|              | created.                                                    |
+--------------+-------------------------------------------------------------+
| 208-214      | To set up the example, both email and Tag are created in    |
|              | ThreatConnect. The create is verified as successful, and    |
|              | the items are printed to the console.                       |
+--------------+-------------------------------------------------------------+
| 219-221      | The Tag is associated to the Email Group by using the Email |
|              | ID and the Tag name (the ``uniqueID`` for the Tag).         |
+--------------+-------------------------------------------------------------+
| 223-226      | The association is verified as successful.                  |
+--------------+-------------------------------------------------------------+

Writer Associate Victim Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Associate Victim Example

.. code:: java

     
     59 
     60     private static Victim createTestVictim() {
     61         Victim victim = new Victim();
     62         victim.setOrg("System");
     63         victim.setName("Test API Victim");
     64         victim.setDescription("Test API Victim Description");
     65 
     66         return victim;
     67     }

    304     private static void doAssociateVictim(Connection conn) {
    305         AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
    306         VictimWriterAdapter vWriter = WriterAdapterFactory.createVictimWriter(conn);
    307         
    308         Email email = createTestEmail();
    309         Victim victim = createTestVictim();
    310         
    311         try {
    312             // --------------------------------
    313             // Create Email and Victim
    314             // --------------------------------
    315             ApiEntitySingleResponse<Email,?> createResponseEmail = gWriter.create(email);
    316             ApiEntitySingleResponse<Victim,?> createResponseVictim = vWriter.create(victim);
    317             if (createResponseEmail.isSuccess() && createResponseVictim.isSuccess() ) {
    318                 System.out.println("Created Email: " + createResponseEmail.getItem());
    319                 System.out.println("Created Victim: " + createResponseVictim.getItem());
    320 
    321                 // --------------------------------
    322                 // Associate Victim
    323                 // --------------------------------
    324                 ApiEntitySingleResponse assocResponse
    325                     = gWriter.associateVictim(createResponseEmail.getItem().getId()
    326                                             , createResponseVictim.getItem().getId());
    327 
    328                 if ( assocResponse.isSuccess() ) {
    329                     System.out.println("\tAssociated Victim: " + createResponseVictim.getItem().getId() );
    330                 } else {
    331                     System.err.println("Failed to Associate Victim: " + assocResponse.getMessage());
    332                 }
    333 
    334             } else {
    335                 if ( !createResponseEmail.isSuccess() ) {
    336                     System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
    337                 }
    338                 if ( !createResponseVictim.isSuccess() ) {
    339                     System.err.println("Failed to Create Victim: " + createResponseVictim.getMessage());
    340                 }
    341             }
    342 
    343         } catch (IOException | FailedResponseException ex) {
    344             System.err.println("Error: " + ex.toString());
    345         }
    346 
    347     }

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 305-306      | Two writers are created: one for the new email and the      |
|              | other for the Victim to associate.                          |
+--------------+-------------------------------------------------------------+
| 308-309      | The test email object, and the Victim to associate, are     |
|              | created.                                                    |
+--------------+-------------------------------------------------------------+
| 315-319      | To set up the example, both email and Victim are created in |
|              | ThreatConnect. The create is verified as successful, and    |
|              | the items are printed to the console.                       |
+--------------+-------------------------------------------------------------+
| 324-326      | The Victim is associated to the Email Group by using the    |
|              | Email ID and the Victim ID.                                 |
+--------------+-------------------------------------------------------------+
| 328-331      | The association is verified as successful.                  |
+--------------+-------------------------------------------------------------+

Writer Remove Association Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writer Remove Association Example

.. code:: java


    243     private static void doRemoveAssociatedTag(Connection conn) {
    244 
    245         AbstractGroupWriterAdapter<Email> gWriter= WriterAdapterFactory.createEmailGroupWriter(conn);
    246         TagWriterAdapter tWriter = WriterAdapterFactory.createTagWriter(conn);
    247 
    248         Email email = createTestEmail();
    249         Tag tag = createTestTag();
    250 
    251         try {
    252             // -----------------------------------------
    253             // Create Email and Tag 
    254             // -----------------------------------------
    255             ApiEntitySingleResponse<Email,?> createResponseEmail = gWriter.create(email);
    256             tWriter.delete(tag.getName()); // delete if it exists
    257             ApiEntitySingleResponse<Tag, ?> createResponseTag = tWriter.create(tag);
    258 
    259             if (createResponseEmail.isSuccess() && createResponseTag.isSuccess() ) {
    260                 System.out.println("Created Email: " + createResponseEmail.getItem());
    261                 System.out.println("Created Tag: " + createResponseTag.getItem());
    262 
    263                 // -----------------------------------------
    264                 // Associate Tag
    265                 // -----------------------------------------
    266                 ApiEntitySingleResponse assocResponse
    267                     = gWriter.associateTag(createResponseEmail.getItem().getId()
    268                                          , createResponseTag.getItem().getName() );
    269 
    270                 if ( assocResponse.isSuccess() ) {
    271                     System.out.println("\tAssociated Tag: " + createResponseTag.getItem().getName() );
    272 
    273                     // -----------------------------------------
    274                     // Delete Association
    275                     // -----------------------------------------
    276                     ApiEntitySingleResponse dissociateResponse
    277                         = gWriter.dissociateTag(createResponseEmail.getItem()
    278                                       .getId(), createResponseTag.getItem().getName() );
    279 
    280                     if ( dissociateResponse.isSuccess() ) {
    281                         System.out.println("\tDeleted Associated Tag: " + createResponseTag.getItem().getName() );
    282                     } else {
    283                         System.err.println("Failed to delete Associated Tag: "+ dissociateResponse.getMessage());
    284                     }
    285 
    286                 } else {
    287                     System.err.println("Failed to Associate Tag: " + assocResponse.getMessage());
    288                 }
    289 
    290             } else {
    291                 if ( !createResponseEmail.isSuccess() ) {
    292                     System.err.println("Failed to Create Email: " + createResponseEmail.getMessage());
    293                 }
    294                 if ( !createResponseTag.isSuccess() ) {
    295                     System.err.println("Failed to Create Tag: " + createResponseTag.getMessage());
    296                 }
    297             }
    298 
    299         } catch (IOException | FailedResponseException ex) {
    300             System.err.println("Error: " + ex.toString());
    301         }
    302     }

Code Sample Description

+--------------+-------------------------------------------------------------+
| Line         | Description                                                 |
+==============+=============================================================+
| 245-271      | The Email Group is created and associated with the Tag      |
|              | item.                                                       |
+--------------+-------------------------------------------------------------+
| 276-278      | The ``dissociateTag()`` method is called using the same     |
|              | parameters as the associate method. The email item ID value |
|              | is used with the Tag name.                                  |
+--------------+-------------------------------------------------------------+
| 280-281      | The deleting is verified as successful, and the message is  |
|              | dumped to the console.                                      |
+--------------+-------------------------------------------------------------+

Summary

The previous two examples explained how to:

-  Delete and update an Adversary and verify that the action was
   successfully applied to ThreatConnect
-  Add an Attribute to a Group item
-  Associate Indicators, Groups, Tags, and Victims
-  Remove Association from a Group item

JavaScript Library
==================

About This Document

This section explains the process of coding JavaScript applications, and
the implementation of the JavaScript SDK, using the ThreatConnect API.
The JavaScript SDK offers coverage of all features in version 4.0 of the
ThreatConnect API—including the ability to write data to ThreatConnect.

The goal of this JavaScript SDK library is to provide a programmatic
abstraction layer around the ThreatConnect API without losing functional
coverage over the available API resources. This abstraction layer
enables developers to focus on writing enterprise functionality without
worrying about low-level RESTful calls and authentication management.

This document is not a replacement for the ThreatConnect API User Guide.
This document serves as a companion to the official documentation for
the REST API. Read the official documentation to gain a further
understanding of the functional aspects of using the ThreatConnect API.

How to Use This Document

This document explains how to create Groups, Indicators, Associations,
Tags, Security Labels, and Victims. Along with creating data elements, a
developer will learn how to create, update, delete, and request data
from the API using JavaScript. This document assumes the reader knows
the JavaScript programming language.

All code examples will be noted in a separate box with a monospaced font
and line numbers to facilitate explanation of code functionality.

Getting Started
---------------

An example of using configuration to read API configuration values is
the following:

.. code:: javascript

    var apiSettings,
        tcSpaceElementId = getParameterByName('tcSpaceElementId');

    if ( tcSpaceElementId ) {
        apiSettings = {
            apiToken: getParameterByName('tcToken'),
            apiUrl: getParameterByName('tcApiPath')
        };
    } else {
        apiSettings = {
            apiId: '12345678900987654321',
            apiSec: 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz!@#$%^&*()-=',
            apiUrl: 'https://api.threatconnect.com'
        };
    }

.. code:: html

    <!-- JQuery -->
    <script src="./libs/jquery-2.1.4.min.js" type="test/javascript"></script>

    <!-- HMAC -->
    <script src="./libs/core.js" type="text/javascript"></script>
    <script src="./libs/sha256.js" type="text/javascript"></script>
    <script src="./libs/hmac.js" type="text/javascript"></script>
    <script src="./libs/enc-base64.js" type="text/javascript"></script>

    <!-- ThreatConnect -->
    <script src="./libs/threatconnect.js" type="text/javascript"></script>

The JavaScript SDK is written to support ECMAScript®-5 and should work
in most modern browsers.

To use the RESTful API for ThreatConnect, an API user must be
provisioned. See the ThreatConnect API User Guide for details on how to
create an API user as it is out of scope for this document.

The JavaScript SDK can be configured to use an Access ID and Secret Key
or a Token. Token support is only available when working with a Spaces
application.

Once the configuration has been set up, the developer should be able to
run the examples in this document as long as the JavaScript SDK has been
installed.

The following example illustrates a typical initialization of the
ThreatConnect Object:

``var tc = new ThreatConnect(apiSettings);``

Third-Party Dependencies

+-------------+-----------+----------------------------------------+
| Name        | Version   | Link                                   |
+=============+===========+========================================+
| jquery      | 2.1.4     | https://jquery.com/                    |
+-------------+-----------+----------------------------------------+
| Crypto-JS   | 3.1       | https://code.google.com/p/crypto-js/   |
+-------------+-----------+----------------------------------------+

Technical Design

The JavaScript SDK for ThreatConnect was designed with a focus on
abstracting the API REST calls while enabling the developer to use an
enterprise-level programming language.

Supported Resource Types

The JavaScript SDK supports the Resource Types listed below. There is
also a mechanism to do manual API requests to cover any API calls that
are not provided with the core functionality.

+-------------------------+------------------------------------+
| Object                  | Description                        |
+=========================+====================================+
| ``groups()``            | Group container object             |
+-------------------------+------------------------------------+
| ``indicators()``        | Indicator container object         |
+-------------------------+------------------------------------+
| ``indicatorsBatch()``   | Batch Indicator container object   |
+-------------------------+------------------------------------+
| ``owners()``            | Owner container object             |
+-------------------------+------------------------------------+
| ``securityLabel()``     | Security Label container object    |
+-------------------------+------------------------------------+
| ``tags()``              | Tag container object               |
+-------------------------+------------------------------------+
| ``tasks()``             | Task container object              |
+-------------------------+------------------------------------+
| ``victims()``           | Victim container object            |
+-------------------------+------------------------------------+

Example JavaScript App
----------------------

The example below illustrates how to write a program using the
JavaScript SDK for the ThreatConnect API:

.. code:: javascript

    var apiSettings,
        tcSpaceElementId = getParameterByName('tcSpaceElementId');

    if ( tcSpaceElementId ) {
        apiSettings = {
            apiToken: getParameterByName('tcToken'),
            apiUrl: getParameterByName('tcApiPath')
        };
    } else {
        apiSettings = {
            apiId: '12345678900987654321',
            apiSec: 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz!@#$%^&*()-=',
            apiUrl: 'https://demo.threatconnect.com/api'
        };
    }

    var tc = new ThreatConnect(apiSettings);

    tc.owners()
        .done(function(response) {
            console.log('owner response', response);
        })
        .error(function(response) {
            console.log('owner response error', response.error);
        })
        .retrieve();

This example illustrates how to write a program using the JavaScript SDK
for the ThreatConnect API. An Owner's object will be created in order to
pull a collection of all Owners to which the API account being used has
access. Once retrieved, the Owners objects will be printed to the
console.

Code Highlights

+--------------------------+-------------------------------------------------+
| Snippet                  | Description                                     |
+==========================+=================================================+
| ``tcSpaceElementId = get | Retrieve Space Element Id (only supported on    |
| ParameterByNam...``      | Spaces application).                            |
+--------------------------+-------------------------------------------------+
| ``apiToken: getParameter | Retrieve Token from Spaces.                     |
| ByName('tcToken')``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``apiUrl: getParameterBy | Retrieve API Path from Spaces.                  |
| Name('tcApiPath')``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``apiId: '12345678900987 | Set API ID when not using Spaces App.           |
| 654321',``               |                                                 |
+--------------------------+-------------------------------------------------+
| ``apiSec: 'aabbccddeeffg | Set API Secret when not using Spaces App.       |
| ghhiijjkkllmmn...``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``apiUrl: 'https://demo. | Set API URL when not using Spaces App.          |
| threatconnect.com/api``  |                                                 |
+--------------------------+-------------------------------------------------+
| ``var tc = new ThreatCon | Get ThreatConnect Object.                       |
| nect(apiSettings)``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``tc.owners()``          | Get Owners object.                              |
+--------------------------+-------------------------------------------------+
| ``.done(function(respons | Set "done" callback.                            |
| e) {``                   |                                                 |
+--------------------------+-------------------------------------------------+
| ``console.log('owner res | Console log response.                           |
| ponse', response)``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``.error(function(respon | Set "error" callback.                           |
| se) {``                  |                                                 |
+--------------------------+-------------------------------------------------+
| ``console.log('owner res | Console log any error.                          |
| ponse error', ...``      |                                                 |
+--------------------------+-------------------------------------------------+
| ``.retrieve();``         | Retrieve Owners.                                |
+--------------------------+-------------------------------------------------+

Summary

This section explained how to:

-  Connect to the ThreatConnect API
-  Get a list of Owners

Developing a JavaScript App
---------------------------

This section provides an overview of the JavaScript app development
process as it pertains to the Spaces feature within ThreatConnect. This
section will also review how to package an app for deployment to the
ThreatConnect platform.

Deployment Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

`Apps use a deployment configuration file to define variables and
execution environment <#deployment-configuration-file>`__

Query Parameters
~~~~~~~~~~~~~~~~

For the sample install configuration example above, here is a sample
query String passed to the app:

::

    tcSpaceElementId=467&tcToken=ABC123&tcApiPath=https://api.threatconnect.com:8443&tcType=Host&tcSelectedItem=greystoneexpress.com&tcSelectedItemOwner=TestOrg&add_tags=OpenDNS Scan&add_confidence=25&add_rating=1&opendns_api_token=abc-123&logging=info

All Spaces apps will have standard 'tc' prefixed parameters passed that
may be used by the app.

The above query string can be parsed with the following JavaScript code:

.. code:: javascript

        $(document).ready(function () {

            var type = getParameterByName("tcType");
            var selectedItem = getParameterByName("tcSelectedItem");

            // startApp(type, selectedItem);
        });
     

All visible parameters defined in the ``configuration`` file will be
passed to the Spaces app via a query String. The Spaces app is
responsible for retrieving parameter values via the SDK's convenience
function ``getParameterByName``.

All Spaces apps will have standard 'tc' prefixed parameters passed that
may be used by the app.

Optional Properties
-------------------

There are some optional flags that may be used by the app to

-  handle Boolean flags that turn features on/off and to
-  encrypt parameters, like API Keys

Parsing Argument Flags

Apps can also use Boolean flags to designate whether to turn on a
specific feature.

The ``configuration`` file must have the following flag present for a
Boolean parameter:

``param.<param-name>.flag``

This property will direct the ThreatConnect application to show a
checkbox to the Spaces configuration. The flag will be passed to the
Spaces app with a ``true`` or ``false`` parameter value.

Encrypted Parameters

This property should be used to encrypt private passwords used by the
app (e.g., API keys). This added level of security will allow the
application to persist the password in encrypted form when at rest. The
input field during job creation will be "password" text, and the key
will not be visible when typed.

The configuration property is defined for the encrypted parameter using
the following flag:

``param.<param-name>.encrypted``

At runtime, ThreatConnect will call the Spaces app with the decrypted
key. At no point in time is the password persisted in decrypted form.

Encrypted apps require that the Keychain feature be turned on, or apps
with ``.encrypted`` parameters will not run properly.

ThreatConnect Parameters
------------------------

ThreatConnect passes standard parameters to all jobs within its standard
sandbox container. There should be no assumptions made on the naming or
existence of paths passed in these variables outside of the lifetime of
the job execution.

Since all Spaces apps are managed within ThreatConnect, app developers
should never hard-code ThreatConnect Parameters

+--------------------+-------------------------------------------------------+
| ThreatConnect      | Description                                           |
| Parameter          |                                                       |
+====================+=======================================================+
| ``tcSpaceElementId | The unique space element instance ID for the user who |
| ``                 | added this app to their Space. This numeric ID can be |
|                    | used by the app to store state for the user.          |
+--------------------+-------------------------------------------------------+
| ``tcToken``        | Session token to be used by the app to access the     |
|                    | API. The JavaScript SDK has configuration options for |
|                    | this parameter.                                       |
+--------------------+-------------------------------------------------------+
| ``tcApiPath``      | The path to the API defined in System Settings for    |
|                    | all apps.                                             |
+--------------------+-------------------------------------------------------+
| ``tcType``         | Only relevant for context-aware apps. This field      |
|                    | corresponds to the runtime.context Attribute defined  |
|                    | in the install configuration file.                    |
+--------------------+-------------------------------------------------------+
| ``tcSelectedItem`` | Only relevant for context-aware apps. This is the     |
|                    | actual context-item identifier used within            |
|                    | ThreatConnect. For instance, a Host identifier might  |
|                    | be: g00gle.com                                        |
+--------------------+-------------------------------------------------------+
| ``tcSelectedItemOw | Only relevant for context-aware apps. This is the     |
| ner``              | Owner of the context item.                            |
+--------------------+-------------------------------------------------------+

JavaScript Examples

-  `SDK Sample
   index.html <https://github.com/ThreatConnect-Inc/threatconnect-javascript/blob/master/index.html>`__

Authentication
--------------

The example below demonstrates how to authenticate and add an Indicator
via the ThreatConnect API, using the JavaScript programming language.

Dependencies

+------------------+-------------------------------------------------+
| File             | URL                                             |
+==================+=================================================+
| enc-base-64.js   | https://code.google.com/p/crypto-js/downloads   |
+------------------+-------------------------------------------------+
| hmac-sha256.js   | https://code.google.com/p/crypto-js/downloads   |
+------------------+-------------------------------------------------+
| sha256.js        | https://code.google.com/p/crypto-js/downloads   |
+------------------+-------------------------------------------------+

Dependencies Installation (Linux)
---------------------------------

Run these commands to install dependencies:

.. code:: shell

    mkdir lib
    unzip CryptoJS\ v3.1.2.zip
    cp CyrptoJS\ v3.1.2/enc-base-64.js lib/
    cp CyrptoJS\ v3.1.2/hmac-sha256.js lib/
    cp CyrptoJS\ v3.1.2/sha256.js lib/

tc.js code sample:

.. code:: javascript

    var CryptoJS = require('./lib/hmac-sha256.js'),
        Base64 = require('./lib/enc-base-64.js'),
        https = require('https'),
        querystring = require('querystring'),
        url = require('url');

    // https.globalAgent.maxSockets = 20;

    var request_time = 0;
    CryptoJS = CryptoJS.CryptoJS;

    var SETTINGS = {
        api_secret_key: '<ENTER API SECRET KEY HERE>',
        api_access_id: '<ENTER API ACCESS ID HERE>',
        api_base_url: '<ENTER API BASE URL HERE>',
        api_port: '443',
        verify_ssl: false
    };

    function getUTC() {
        var date = new Date().getTime();
        return Math.floor(date / 1000);
    }

    function api_request_headers(request_method, api_uri) {
        var timestamp = getUTC(),
            signature = api_uri + ":" + request_method + ":" + timestamp,
            hmac_signature = CryptoJS.HmacSHA256(signature, SETTINGS.api_secret_key),
            authorization = "TC " + SETTINGS.api_access_id + ":" + CryptoJS.enc.Base64.stringify(hmac_signature);

        return { "Timestamp": timestamp, "Authorization": authorization };
    }

    function apiRequest(request_uri, request_payload, http_method, body, activity_log, content_type) {
        /*
         * Default Values
         */
        activity_log = (activity_log === undefined) ? "false" : activity_log;
        // console.log('activity_log: %s', activity_log);
        body = (body === undefined) ? null : body;
        // console.log('body: %s', body);
        content_type = (content_type === undefined) ? "application/json" : content_type;
        // console.log('content_type: %s', content_type);
        http_method = (http_method === undefined) ? "GET" : http_method.toUpperCase();
        // console.log('http_method: %s', http_method);
        request_payload = (request_payload === undefined) ? {} : request_payload;
        request_payload["createActivityLog"] = activity_log;
        // console.log('request_payload: %s', request_payload);

        request_start = getUTC();

        if (SETTINGS.verify_ssl == false) {
            process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";
        }

        /*
         * Prepare Request
         */
        api_url = request_uri + "?" + querystring.stringify(request_payload);
        // console.log('api_url: %s', api_url);
        path_url = url.parse(api_url).path;
        // console.log('path_url: %s', path_url);
        api_headers = api_request_headers(http_method, path_url)


        /*
         * POST
         */
        if (http_method.toUpperCase() == "POST") {
            api_headers["Content-Type"] = content_type;
            api_headers["Content-Length"] = body.length;
        }
        // console.log(JSON.stringify(api_headers, null, 4));

        /*
         * Options
         */
        var options = {
            host: SETTINGS.api_base_url,
            port: SETTINGS.api_port,
            method: http_method,
            path: api_url,
            headers: api_headers,
            keepAlive: 1,
            agent: false
        };
        // console.log(JSON.stringify(options, null, 4));

        /*
         * API call
         */
        // options.agent = new https.Agent(options);
        var api_request = https.request(options, function(res) {
            // console.log('STATUS: ' + res.statusCode);
            // console.log('HEADERS: ' + JSON.stringify(res.headers, null, 4));
            /*
            res.setEncoding('utf8');
            res.on('data', function (chunk) {
                console.log('BODY: ' + chunk);
            });
            */
        });

        api_request.write(body);
        api_request.end();

        request_time += (getUTC() - request_start);
    }

    function quick_add_ip(ip, rating, confidence, owner) {
        rating = (rating === undefined) ? null : rating;
        confidence = (confidence === undefined) ? null : confidence;
        owner = (owner === undefined) ? null : owner;

        request_uri = '/api/v2/indicators/addresses';

        /* body */
        var body = {"ip": ip};
        if (rating != null) {
            body["rating"] = rating;
        }
        if (confidence != null) {
            body["confidence"] = confidence;
        }

        /*
         * owner
         */
        if (owner != null) {
            var request_payload = {"owner":owner};
        } else {
            var request_payload = {}
        }
        // console.log("%s %j %j", request_uri, request_payload, body)
        apiRequest(request_uri, request_payload, 'POST', JSON.stringify(body), "false", "application/json")
    }

    var owner = "Example Community";
    quick_add_ip('4.3.2.1', '2.5', '75', owner);

In the directory in which the script will be installed, run the commands
in the right column. Once completed, place the example contents in
tc.js.

Indicator Retrieve
------------------

This section explains how to work with ThreatConnect Indicator
Resources.

Supported Indicator Types

+------------------+-----------------------+
| Indicator Name   | Indicator Constant    |
+==================+=======================+
| Address          | TYPE.ADDRESS          |
+------------------+-----------------------+
| Email Address    | TYPE.EMAIL\_ADDRESS   |
+------------------+-----------------------+
| File             | TYPE.FILE             |
+------------------+-----------------------+
| Host             | TYPE.HOST             |
+------------------+-----------------------+
| URL              | TYPE.URL              |
+------------------+-----------------------+

Retrieve Indicator
~~~~~~~~~~~~~~~~~~

Example of Retrieving Indicators:

.. code:: javascript

    var indicators = tc.indicators();

    indicators.owner('Example Community')
        // .type(TYPE.ADDRESS)
        .resultLimit(500)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieve(function() {
            if (indicators.hasNext()) {
                indicators.next()
            }
        });

This example will demonstrate how to retrieve Indicators. The result set
returned from this example will contain the first 500 Indicators in the
"Example Community" Owner.

Retrieve Next
~~~~~~~~~~~~~

Example of retrieve.next method:

.. code:: javascript

    if (indicators.hasNext()) {
        indicators.next();
    }

Example Results of the retrieve.next method:

.. code:: json

    {
      "data": [
        {
          "id": 97262,
          "indicators": "badguys.org",
          "dateAdded": "2015-12-14T02:16:38Z",
          "lastModified": "2015-12-14T02:16:38Z",
          "ownerName": "Example Community",
          "type": "Host",
          "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=badguys.org&owner=Example+Community"
        },
        {
          "id": 94977,
          "indicators": "74.121.142.111",
          "dateAdded": "2015-12-12T01:24:28Z",
          "lastModified": "2015-12-13T23:22:28Z",
          "ownerName": "Example Community",
          "rating": 4,
          "confidence": 75,
          "type": "Address",
          "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=74.121.142.111&owner=Example+Community"
        },
        {
          "id": 94980,
          "indicators": "74.121.139.80",
          "dateAdded": "2015-12-12T01:24:28Z",
          "lastModified": "2015-12-12T01:24:28Z",
          "ownerName": "Example Community",
          "rating": 4,
          "confidence": 50,
          "type": "Address",
          "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=74.121.139.80&owner=Example+Community"
        }
      ],
      "remaining": 35,
      "url": "https://app.threatconnect.com/v2/indicators?owner=Example+Community&resultLimit=5",
      "apiCalls": 1,
      "resultCount": 40,
      "status": "Success"
    }

The JavaScript SDK provide the ``hasNext()`` method for checking if more
entries are available. To retrieve the next set of entries the
``next()`` method is available.

Note: Before the ``next()`` method can be called, the first API must
have completed. This should not be an issue if a user click triggers the
next call; however, if the ``next()`` method is being called
programmatically then it should be passed in a function to the
``retrieve()`` method.

Note: The ``next()`` method will return the same number of results
defined in the ``resultsLimit()`` or the number of results remaining.
The same 'done' and 'error' callbacks are also used for the next set of
results.

Single Indicator
~~~~~~~~~~~~~~~~

This example will demonstrate how to retrieve a Single Indicator:

.. code:: javascript

    var indicators = tc.indicators();

    indicators.owner('Example Community')
        .type(TYPE.ADDRESS)
        .indicator('10.20.30.40')
        .includeAdditional(true)     // OPTIONAL: include observationCount and faslePositiveCount
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieve()

Single Indicator retrieve Example Results:

.. code:: json

    {
        "data": [
            {
                "id": 97934,
                "indicators": "10.20.30.40",
                "dateAdded": "2015-12-14T23:23:00Z",
                "lastModified": "2016-01-14T23:47:53Z",
                "ownerName": "Example Community",
                "rating": 3,
                "confidence": 0,
                "observationCount": 1,
                "falsePositiveCount": 0,
                "type": "Address",
                "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=10.20.30.40&owner=Example+Community"
            }
        ],
        "remaining": 0,
        "url": "https://api.threatconnect.com/v2/indicators/addresses/10.20.30.40?owner=Example+Community&includeAdditional=true",
        "apiCalls": 1,
        "resultCount": 0,
        "status": "Success"
    }

Filters
~~~~~~~

Example of how to retrieve Threats:

.. code:: javascript

    var filter = new Filter(FILTER.AND);
    filter.on('summary', FILTER.SW, 'bad');
    filter.on('dateAdded', FILTER.GT, '2015-12-02');

    var indicators = tc.indicators();

    indicators.owner('Example Community')
        .resultLimit(500)
        .filter(filter)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieve();

Starting with ThreatConnect version 4.0 the API supports filtering using
query string parameters. For more information on which parameters
support which operators see the ThreatConnect API Users Guide.

Filter Options

+------------------------------+-------------------+
| Filter                       | Filter Constant   |
+==============================+===================+
| And                          | FILTER.AND        |
+------------------------------+-------------------+
| Or                           | FILTER.OR         |
+------------------------------+-------------------+
| Equal (=)                    | FILTER.OR         |
+------------------------------+-------------------+
| Greater Than (>)             | FILTER.GT         |
+------------------------------+-------------------+
| Greater Than or Equal (>=)   | FILTER.GE         |
+------------------------------+-------------------+
| Less Than (<)                | FILTER.LT         |
+------------------------------+-------------------+
| Less Than or Equal (<=)      | FILTER.LE         |
+------------------------------+-------------------+
| Starts With (^)              | FILTER.SW         |
+------------------------------+-------------------+

Note that multiple filters can be added to one API call.

Batch/Bulk Retrieve
~~~~~~~~~~~~~~~~~~~

Example of Batch/Bulk Retrieve:

.. code:: javascript

    var indicators = tc.indicatorsBatch();

    indicators.owner('Example Community')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieve('json');

Filters are not supported on Batch/Bulk downloads.

Associations
~~~~~~~~~~~~

.. code:: javascript

    var indicators = tc.indicators();

    indicators.owner('Example Community')
        .indicator('74.121.142.111')
        .type(TYPE.ADDRESS)
        .resultLimit(5)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveAssociations({
            type: TYPE.GROUP
        });

The JavaScript SDK provides the ``retrieveAssociations()`` method to
retrieve both Indicator and Indicator Associations. The ``type()``, and
``id()`` methods are required to retrieve the associations. The
``retrieveAssociations()`` method requires that a parameter object
containing the Association ``type`` be provided. Optionally an ``id``
can be provided to pull a specific association.

Attributes
~~~~~~~~~~

Example of retrieveAttributes() method:

.. code:: javascript

    var indicators = tc.indicators();

    indicators.owner('Example Community')
        .indicator('74.121.142.111')
        .type(TYPE.ADDRESS)
        .resultLimit(5)
        .done(function(response) {
            console.log('response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveAttributes();

The JavaScript SDK provides the ``retrieveAttributes()`` method to
retrieve attributes. Both the ``type()`` method and ``id()`` are
required to retrieve the attributes. An ``id`` can be passed to the
``retrieveAttributes()`` method to retrieve a specific attribute.

Retrieve Observations
~~~~~~~~~~~~~~~~~~~~~

.. code:: javascript

    var indicators = tc.indicators();

    indicators.owner('Example Community')
        .indicator('74.121.142.111')
        .type(TYPE.ADDRESS)
        .resultLimit(5)
        .done(function(response) {
            console.log('response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveObservations();

The JavaScript SDK provides the ``retrieveObservations()`` method to
retrieve Observations. Both the ``type()`` method and ``id()`` are
required to retrieve the Observations.

Retrieve Observation Count
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: javascript

    var indicators = tc.indicators();

    indicators.owner('Example Community')
        .indicator('74.121.142.111')
        .type(TYPE.ADDRESS)
        .done(function(response) {
            console.log('response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveObservationCount();

The JavaScript SDK provides the ``retrieveObservationCount()`` method to
retrieve the Observation Count for an Indicator. Both the ``type()``
method and ``id()`` are required to retrieve the Observation Count.

NOTE: The Observation Count can also be retrieved with the "Single
Indicator" method described above using the includeAdditional parameter.

Retrieve Security Labels Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example of retrieveSecurityLabel() method:

.. code:: javascript

    var indicators = tc.indicators();

    indicators.owner('Example Community')
        .indicator('74.121.142.111')
        .type(TYPE.ADDRESS)
        .resultLimit(5)
        .done(function(response) {
            console.log('response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveSecurityLabel();

Retrieve Tags Method
~~~~~~~~~~~~~~~~~~~~

Example of retrieveTags() method:

.. code:: javascript

    var indicators = tc.indicators();

    indicators.owner('Example Community')
        .indicator('74.121.142.111')
        .type(TYPE.ADDRESS)
        .resultLimit(5)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveTags();

The JavaScript SDK provides the ``retrieveTags()`` method to retrieve
tags. Both the ``type()`` method and ``id()`` are required to retrieve
the tags.

Tags Retrieve
-------------

Example of how to retrieve Tags:

.. code:: javascript

    tc.tags()
        .owner('Example Community')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieve();

Example of retrieve Tags results:

.. code:: json

    {
      "data": [
        {
          "name": "APT",
          "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=APT&owner=Example+Community"
        },
        {
          "name": "BadGuy",
          "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=BadGuy&owner=Example+Community"
        },
        {
          "name": "blah",
          "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=blah&owner=Example+Community"
        },
        {
          "name": "threat_tag",
          "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=threat_tag&owner=Example+Community"
        }
      ],
      "remaining": 0,
      "url": "https://api.threatconnect.com/v2/tags",
      "apiCalls": 1,
      "resultCount": 11,
      "status": "Success"
    }

This section explains how to work with ThreatConnect Tags Resources.

This example will demonstrate how to retrieve Tags. The result set
returned from this example will contain all Tags to which the API
credential being used has access. Optionally the ``name()`` method can
be used to pass a specific Tag name.

Owners Retrieve
---------------

Retrieve Owners Example:

.. code:: javascript

    tc.owners()
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieve();

Example Owners Results:

.. code:: json

    {
      "data": [
        {
          "id": 2,
          "name": "SumX",
          "type": "Organization"
        },
        {
          "id": 3,
          "name": "Local Common Community",
          "type": "Source"
        },
        {
          "id": 4,
          "name": "Blocklist.de Source",
          "type": "Source"
        },
        {
          "id": 10,
          "name": "Example Community",
          "type": "Community"
        }
      ],
      "remaining": 0,
      "url": "https://demo.threatconnect.com/api/v2/owners",
      "apiCalls": 1,
      "resultCount": 9,
      "status": "Success"
    }

This section explains how to work with ThreatConnect Owners Resources.

Metrics
~~~~~~~

Retrieving Owner Metrics:

.. code:: javascript

    tc.owners()
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveMetrics();

Starting with ThreatConnect platform version 4.0 retrieving Owner
metrics is supported. Owner metrics provides the summed data for the
last 15 days. Optionally the ``id()`` method can be used to pass a
specific Owner ID.

Group Retrieve
--------------

This section explains how to work with ThreatConnect Group Resources.

Supported Group Types

+--------------+------------------+
| Group Name   | Group Constant   |
+==============+==================+
| Adversary    | TYPE.ADVERSARY   |
+--------------+------------------+
| Document     | TYPE.DOCUMENT    |
+--------------+------------------+
| Email        | TYPE.EMAIL       |
+--------------+------------------+
| Incident     | TYPE.INCIDENT    |
+--------------+------------------+
| Signature    | TYPE.SIGNATURE   |
+--------------+------------------+
| Threat       | TYPE.THREAT      |
+--------------+------------------+

Retrieve Group
~~~~~~~~~~~~~~

Example of how to retrieve Adversaries:

.. code:: javascript

    groups = tc.groups();

    groups.owner('Example Community')
        .type(TYPE.ADVERSARY)
        .resultLimit(500)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieve();

This example will demonstrate how to retrieve Adversaries. The result
set returned from this example will contain the first 500 Adversaries in
the "Example Community" Owner.

Retrieve Next
~~~~~~~~~~~~~

Example of hasNext() method:

.. code:: javascript

    while (groups.hasNext()) {
        groups.next();
    }

Example of Results:

.. code:: json

    {
      "data": [
        {
          "id": 81,
          "name": "adver-000",
          "ownerName": "Example Community",
          "dateAdded": "2015-10-30T05:46:21Z",
          "webLink": "https://api.threatconnect.com/auth/adversary/adversary.xhtml?adversary=81"
        },
        {
          "id": 189,
          "name": "adver-001",
          "ownerName": "Example Community",
          "dateAdded": "2015-11-02T13:55:45Z",
          "webLink": "https://api.threatconnect.com/auth/adversary/adversary.xhtml?adversary=189"
        },
        {
          "id": 1,
          "name": "adver-015",
          "ownerName": "Example Community",
          "dateAdded": "2015-10-23T21:10:14Z",
          "webLink": "https://api.threatconnect.com/auth/adversary/adversary.xhtml?adversary=200"
        }
      ],
      "remaining": 0,
      "url": "https://api.threatconnect.com/v2/groups/adversaries/?createActivityLog=false&resultLimit=500&resultStart=0&owner=Example+Community",
      "apiCalls": 1,
      "resultCount": 15,
      "status": "Success"
    }

The JavaScript SDK provide the ``hasNext()`` method for checking if more
entries are available. To retrieve the next set of entries the
``next()`` method is available.

Note: Before the ``next()`` method can be called the first API must have
completed. This should not be an issue if a user click triggers the next
call, however if the ``next()`` method is being called programmaticly
then it should be passed in a function to the ``retrieve()`` method.

Note: The ``next()`` method will return the same number of results
defined in the ``resultsLimit()`` or the number of results remaining.
The same 'done' and 'error' callbacks are also used for the next set of
results.

Filters
-------

Example of how to retrieve Threats that start-with 'threat' and have a
dateAdded value greater than '2015-12-02' using an API filter:

.. code:: javascript

    filter = new Filter(FILTER.AND);
    filter.on('name', FILTER.SW, 'threat');
    filter.on('dateAdded', FILTER.GT, '2015-12-02');

    groups = tc.groups();

    groups.owner('Example Community')
        .type(TYPE.THREAT)
        .resultLimit(500)
        .filter(filter)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieve();

Starting with ThreatConnect version 4.0 the API supports filtering using
query string parameters. For more information on which parameters
support which operators see the ThreatConnect API Users Guide.

+------------------------------+-------------------+
| Filter Options               | Filter Constant   |
+==============================+===================+
| And                          | FILTER.AND        |
+------------------------------+-------------------+
| Or                           | FILTER.OR         |
+------------------------------+-------------------+
| Equal (=)                    | FILTER.OR         |
+------------------------------+-------------------+
| Greater Than (>)             | FILTER.GT         |
+------------------------------+-------------------+
| Greater Than or Equal (>=)   | FILTER.GE         |
+------------------------------+-------------------+
| Less Than (<)                | FILTER.LT         |
+------------------------------+-------------------+
| Less Than or Equal (<=)      | FILTER.LE         |
+------------------------------+-------------------+
| Starts With (^)              | FILTER.SW         |
+------------------------------+-------------------+

Note that multiple filters can be added to one API call.

Retrieve Associations
---------------------

Example of retrieveAssociations() method:

.. code:: javascript

    tc.groups()
        .owner('Example Community')
        .type(TYPE.INCIDENT)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveAssociations({
            type: TYPE.ADVERSARY,
            id: 253
        });

The JavaScript SDK provides the ``retrieveAssociations()`` method to
retrieve both Indicator and Group Associations. The ``type()``, and
``id()`` methods are required to retrieve the associations. The
``retrieveAssociations()`` method requires that a parameter object
containing the association ``type`` be provided. Optionally an ``id``
can be provided to pull a specific association.

Retrieve Attributes
-------------------

Example of retrieveAttributes() method:

.. code:: javascript

    tc.groups()
        .owner('Example Community')
        .type(TYPE.INCIDENT)
        .id(173)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveAttributes();

The JavaScript SDK provides the ``retrieveAttributes()`` method to
retrieve attributes. Both the ``type()`` method and ``id()`` are
required to retrieve the attributes. An ``id`` can be passed to the
``retrieveAttributes()`` method to retrieve a specific attribute.

Retrieve Tags
-------------

Example of retrieveTags() method:

.. code:: javascript

    tc.groups()
        .owner('Example Community')
        .type(TYPE.INCIDENT)
        .id(173)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveTags();

The JavaScript SDK provides the ``retrieveTags()`` method to retrieve
tags. Both the ``type()`` method and ``id()`` are required to retrieve
the tags.

Retrieve Security Labels
------------------------

Example of retrieveSecurityLabel() method:

.. code:: javascript

    tc.groups()
        .owner('Example Community')
        .type(TYPE.INCIDENT)
        .id(256)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieveSecurityLabel();

The JavaScript SDK provides the ``retrieveSecurityLabel()`` method to
retrieve security labels. Both the ``type()`` method and ``id()`` are
required to retrieve the security label.

Retrieve Tasks
--------------

This example will demonstrate how to retrieve Tasks. The result set
returned from this example will contain all Tasks that the API
credential being used have access. Optionally the ``id()`` method can be
used to pass a specific task id to retrieve.

Example
~~~~~~~

.. code:: javascript

    tc.tasks()
        .owner('Example Community')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieve();

Example Results
~~~~~~~~~~~~~~~

.. code:: json

    {
      "data": [{
        "id": 571,
        "name": "Test Task",
        "ownerName": "Example Community",
        "dateAdded": "2016-03-11T20:15:52Z",
        "webLink": "https://app.threatconnect.com/auth/workflow/task.xhtml?task=571",
        "status": "In Progress",
        "escalated": false,
        "reminded": false,
        "overdue": true,
        "dueDate": "2016-03-11T00:00:00Z",
        "reminderDate": "2016-03-14T20:14:00Z",
        "escalationDate": "2016-03-22T20:14:00Z"
      }],
      "remaining": 0,
      "url": "https://api.threatconnect.com/v2/tasks?resultLimit=500&owner=Example+Community",
      "apiCalls": 1,
      "resultCount": 1,
      "status": "Success"
    }

Retrieve Victims
----------------

This example will demonstrate how to retrieve Victims. The result set
returned from this example will contain all Victims that the API
credential being used have access. Optionally the ``id()`` method can be
used to pass a specific task id to retrieve.

Example
~~~~~~~

.. code:: javascript

    tc.victims()
        .owner('Example Community')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .retrieve();

Example Results
~~~~~~~~~~~~~~~

.. code:: json

    {
        "data": [{
            "id": 20,
            "name": "Robin Scherbatsky",
            "org": "Fox News",
            "suborg": "Anchor",
            "workLocation": "New York City, New York",
            "nationality": "Canadian",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=20"
        }, {
            "id": 4,
            "name": "Bob Steal",
            "org": "Fox News",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=4"
        }, {
            "id": 3,
            "name": "Rodney Pear",
            "org": "Fox News",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=3"
        }],
        "remaining": 0,
        "url": "https://api.threatconnect.com/api/v2/victims?resultLimit=500&owner=Example+Community",
        "apiCalls": 1,
        "resultCount": 3,
        "status": "Success"
    }

Indicator Commit
----------------

This section explains how to work with ThreatConnect Indicator
Resources.

Supported Indicator Types

+------------------+-----------------------+
| Indicator Name   | Indicator Constant    |
+==================+=======================+
| Address          | TYPE.ADDRESS          |
+------------------+-----------------------+
| Email Address    | TYPE.EMAIL\_ADDRESS   |
+------------------+-----------------------+
| File             | TYPE.FILE             |
+------------------+-----------------------+
| Host             | TYPE.HOST             |
+------------------+-----------------------+
| URL              | TYPE.URL              |
+------------------+-----------------------+

Commit Indicator
~~~~~~~~~~~~~~~~

Example of how to add an Address indicator to the "Example Community"
Owner:

.. code:: javascript

    var indicators = tc.indicators();

    indicators.owner('Example Community')
        .indicator('10.20.30.40')
        .type(TYPE.ADDRESS)
        .rating(3)
        .confidence(75)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commit();

Example Results:

.. code:: json

    {
      "data": [
        {
          "id": 97932,
          "indicators": "10.20.30.40",
          "dateAdded": "2015-12-14T22:41:39Z",
          "lastModified": "2015-12-14T22:41:39Z",
          "ownerName": "Example Community",
          "rating": 3,
          "confidence": 55,
          "type": "Address",
          "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=10.20.30.40&owner=Example+Community"
        }
      ],
      "remaining": 0,
      "url": "https://api.threatconnect.com/v2/indicators/addresses?owner=Example+Community",
      "apiCalls": 1,
      "body": "{\"ip\":\"10.20.30.40\",\"rating\":3,\"confidence\":55}",
      "resultCount": 0,
      "status": "Success"
    }

This example will demonstrate how to add an Address indicator to the
"Example Community" Owner. For indicator specific parameters refer to
the ThreatConnect API User Guide.

Batch/Bulk Commit
~~~~~~~~~~~~~~~~~

Example of Batch/Bulk Commit:

.. code:: javascript

    var indicators = tc.indicatorsBatch();

    indicators.owner('Example Community')
        .action('Create')
        .attributeWriteType('Append')
        .haltOnError(false)
        .done(function(response) {
            c.log('response', response);
        })
        .error(function(response) {
            c.log('error response', response);
        });
        

    for (i = 1; i <= 5; i++) {
        indicators.indicator('10.10.10.' + i)
            .type(TYPE.ADDRESS)
            .rating(3)
            .confidence(42)
            .attributes([
                {
                    type: 'Description',
                    value: 'Example Description'
                }
            ])
            .tags([
                'Example',
                'JS_SDK'
            ])
            .add()
    }

    indicators.commit();

Filters are not supported on Batch/Bulk downloads.

Commit Association
~~~~~~~~~~~~~~~~~~

The JavaScript SDK provides the ``commitAssociation()`` method to add
Group Associations. Both ``.type()``, and ``id()`` methods are required
to commit the Associations. The value passed to the
``commitAssociation()`` method must be the specific Group Type (e.g.,
TYPE.ADVERSARY, TYPE.HOST).

Example of commitAssociations() method:

.. code:: javascript

    tc.indicators()
        .owner('Example Community')
        .type(TYPE.ADDRESS)
        .indicator('10.20.30.40')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitAssociation({
            type: TYPE.ADVERSARY,
            id: '253'
        });

Commit Attribute
~~~~~~~~~~~~~~~~

Example of commitAttributes() method:

.. code:: javascript

    tc.indicators()
        .type(TYPE.ADDRESS)
        .indicator('10.20.30.40')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitAttribute({
            type: 'Description',
            value: 'This is a description.'
        });

The JavaScript SDK provides the ``commitAttribute()`` method to add
Attributes. Both ``.type()`` and ``id()`` are required to add
Attributes. The Attribute object should be passed to
``commitAttribute()`` method with a type and value parameter.

Commit Tags
~~~~~~~~~~~

Example of commitTags() method:

.. code:: javascript

    tc.indicators()
        .owner('Example Community')
        .type(TYPE.ADDRESS)
        .indicator('10.20.30.40')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitTags('Example Tag');

The JavaScript SDK provides the ``commitTags()`` method to add Tags.
Both the ``.type()`` and ``id()`` methods are required to add the Tags.
The Tag value should be passed to the ``commitTags()`` method.

Commit Security Labels
~~~~~~~~~~~~~~~~~~~~~~

Example of commitSecurityLabel() method:

.. code:: javascript

    tc.indicators()
        .type(TYPE.ADDRESS)
        .indicator('10.20.30.40')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitSecurityLabel('TLP Red');

The JavaScript SDK provides the ``commitSecurityLabel()`` method to add
Security Labels. Both the ``.type()`` and ``indicator()`` methods are
required to add the Security Labels. The Security Label value should be
passed to the ``commitSecurityLabel()`` method.

Putting it all Together
~~~~~~~~~~~~~~~~~~~~~~~

Example of how to add an Adversary with a name of 'adver-999' to the
"Example Community" owner

.. code:: javascript

    indicators.owner('Example Community')
        .indicator('10.20.30.40')
        .type(TYPE.ADDRESS)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commit(function() {
            indicators.commitAssociation({
                type: TYPE.INCIDENT,
                id: 256
            });
            indicators.commitAttribute({
                type: 'Description',
                value: 'Example Description.'
            });
            indicators.commitObservation({
                count: 1,
                dateObserved: '2008-12-12T14:26:45-06:00'
            });
            indicators.commitTag('Example');
            indicators.commitSecurityLabel('TLP Red');
        });

This example will demonstrate how to add an Adversary with a name of
'adver-999' to the "Example Community" owner. It passes a callback to
the commit() method that will add a group and indicators association,
attribute, tag, and security label. Any number of Associations,
Attributes, or Tags can be added in the callback.

Note: To ensure that commits for the metadata happen after the commit of
the Indicator, pass a callback to the Indicator Commit method.

Group Commit
------------

This section explains how to work with ThreatConnect Group Resources.

Supported Group Types

+--------------+------------------+
| Group Name   | Group Constant   |
+==============+==================+
| Adversary    | TYPE.ADVERSARY   |
+--------------+------------------+
| Document     | TYPE.DOCUMENT    |
+--------------+------------------+
| Email        | TYPE.EMAIL       |
+--------------+------------------+
| Incident     | TYPE.INCIDENT    |
+--------------+------------------+
| Signature    | TYPE.SIGNATURE   |
+--------------+------------------+
| Threat       | TYPE.THREAT      |
+--------------+------------------+

Commit Group
~~~~~~~~~~~~

Example of how to add an Adversaries with a name of 'adver-001' to the
"Example Community" Owner:

.. code:: javascript

    groups = tc.groups();

    groups.owner('Example Community')
        .name('adver-001')
        .type(TYPE.ADVERSARY)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commit();

Example Results:

.. code:: json

    {
      "data": [
        {
          "id": 265,
          "name": "adver-001",
          "dateAdded": "2015-12-13T15:50:08Z",
          "webLink": "https://api.threatconnect.com/auth/adversary/adversary.xhtml?adversary=265",
          "ownerName": "Example Community"
        }
      ],
      "remaining": 0,
      "url": "https://api.threatconnect.com/v2/groups/adversaries/?createActivityLog=false&owner=Example+Community",
      "apiCalls": 1,
      "body": "{\"name\":\"adver-001\"}",
      "resultCount": 0,
      "status": "Success"
    }

This example will demonstrate how to add an Adversary with a name of
'adver-001' to the "Example Community" Owner. For group specific
parameters refer to the ThreatConnect API User Guide.

Commit Associations
~~~~~~~~~~~~~~~~~~~

Example of commitAssociations() method:

.. code:: javascript

    tc.groups()
        .owner('Example Community')
        .type(TYPE.INCIDENT)
        .id(256)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitAssociation({
            type: TYPE.ADDRESS,
            id: '74.121.142.111'
        });

The JavaScript SDK provides the ``commitAssociations()`` method to add
both Indicator and Group Associations. The ``.type()``, ``id()``,
``associationType()``, and ``associationId()`` methods are required to
commit the associations. The value passed to the ``associationType()``
method must be the specific Group or Indicator Type (e.g.,
TYPE.ADVERSARY, TYPE.HOST).

Commit Attributes
~~~~~~~~~~~~~~~~~

Example of commitAttributes() method:

.. code:: javascript

    tc.groups()
        .type(TYPE.INCIDENT)
        .id(256)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitAttribute({
            type: 'Description',
            value: 'This is a description.'
        });

The JavaScript SDK provides the ``commitAttributes()`` method to add
attributes. The ``.type()`` and ``id()`` are required to add attributes.
The attribute object should be passed to the ``commitAttribute()``
method with a type and value parameter.

Commit False Positive
~~~~~~~~~~~~~~~~~~~~~

.. code:: javascript

    tc.indicators
        .owner('Example Community')
        .indicator('10.20.30.40')
        .type(TYPE.ADDRESS)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitFalsePositive();

The JavaScript SDK provides the ``commitFalsePositive()`` method to add
a False Positive mark on an Indicator. Both .type() and id() are
required to add a False Positive mark.

Commit Observation Method
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: javascript

    tc.indicators
        .owner('Example Community')
        .indicator('10.20.30.40')
        .type(TYPE.ADDRESS)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitObservation({
            count: 1,
            dateObserved: '2008-12-12T14:26:45-06:00'
        });

The JavaScript SDK provides the ``commitObservation()`` method to add an
Indicator Observation. Both .type() and id() are required to add an
Observation. The Observation Count and dateObserved values should be
passed to the ``commitObservation() method``.

Commit Tag Method
~~~~~~~~~~~~~~~~~

Example of commitTag() method:

.. code:: javascript

    tc.groups()
        .type(TYPE.INCIDENT)
        .id(256)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitTag('Example Tag');

The JavaScript SDK provides the ``commitTag()`` method to add tags. Both
the ``.type()`` and ``id()`` methods are required to add the tags. The
Tag value should be passed to the ``commitTag()`` method.

Commit Security Label
~~~~~~~~~~~~~~~~~~~~~

Example of commitSecurityLabel() method:

.. code:: javascript

    tc.groups()
        .type(TYPE.ADDRESS)
        .indicator('10.20.30.40')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitSecurityLabel('TLP Red');

Putting it all Together
~~~~~~~~~~~~~~~~~~~~~~~

Example of how to add an Adversary with a name of 'adver-999' to the
"Example Community" owner

.. code:: javascript

    groups = tc.groups();

    groups.owner('Example Community')
        .name('adver-999')
        .type(TYPE.ADVERSARY)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commit(function() {
            groups.commitAssociation({
                type: TYPE.ADDRESS,
                id: '74.121.142.111'
            });
            groups.commitAssociation({
                type: TYPE.INCIDENT,
                id: 256
            });
            groups.commitAttribute({
                type: 'Description',
                value: 'Example Description.'
            });
            groups.commitTag('Example');
            groups.commitSecurityLabel('TLP Red');
        });

This example will demonstrate how to add an Adversary with a name of
'adver-999' to the Example Community Owner. It passes a callback to the
``commit()`` method that will add a Group and Indicators Association,
Attribute, Tag, and Security Label. Any number of Associations,
Attributes, or Tags can be added in the callback.

Note: To ensure that commits for the metadata happen after the commit of
the Group pass a callback to the Group Commit method.

Commit Task
-----------

This example will demonstrate how to add a Task with a name of
'task-001' to the "Example Community" Owner.

Example
~~~~~~~

.. code:: javascript

    tc.tasks()
        .owner('Example Community')
        // required
        .name('Test Task')
        // optional
        .assignee([{'userName': 'joe-user@gmail.com'}])
        .escalatee([{'userName': 'juser'}])
        .dueDate('2017-01-13T03:04:05Z')
        .escalationDate('2017-01-18T03:04:05Z')
        .reminderDate('2017-01-16T03:04:05Z')
        .escalated(false)
        .reminded(false)
        .overdue(false)
        .status('In Progress')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commit();

Example Results
~~~~~~~~~~~~~~~

.. code:: json

    {
        "data": {
            "id": 600,
            "name": "Test Task",
            "owner": {
                "id": 2,
                "name": "SumX",
                "type": "Organization"
            },
            "dateAdded": "2016-03-17T17:13:30Z",
            "webLink": "https://demo.threatconnect.com/auth/workflow/task.xhtml?task=600",
            "status": "In Progress",
            "escalated": false,
            "reminded": false,
            "overdue": false,
            "dueDate": "2017-01-13T03:04:05Z",
            "reminderDate": "2017-01-16T03:04:05Z",
            "escalationDate": "2017-01-18T03:04:05Z",
            "assignee": [{
                "userName": "joe-user@gmail.com",
                "firstName": "Joe",
                "lastName": "User"
            }],
            "escalatee": [{
                "userName": "joe-admin@gmail.com",
                "firstName": "Joe",
                "lastName": "Admin"
            }]
        },
        "remaining": 0,
        "url": "https://demo.threatconnect.com/api/v2/tasks/?resultLimit=500&owner=SumX",
        "apiCalls": 1,
        "body": "{\"name\":\"Test Task\",\"assignee\":[{\"userName\":\"joe-user@gmail.com\"}],\"escalatee\":[{\"userName\":\"juser\"}],\"dueDate\":\"2017-01-13T03:04:05Z\",\"escalationDate\":\"2017-01-18T03:04:05Z\",\"reminderDate\":\"2017-01-16T03:04:05Z\",\"escalated\":false,\"reminded\":false,\"overdue\":false,\"status\":\"In Progress\"}",
        "resultCount": 0,
        "status": "Success"
    }

Commit Victim
-------------

This example will demonstrate how to add a Victim with a name of
'task-001' to the "Example Community" Owner.

Example
~~~~~~~

.. code:: javascript

    victim.owner('Example Community')
        .name('Robin Scherbatsky')
        .org('Fox News')
        .suborg('Anchor')
        .workLocation('New York City, New York')
        .nationality('Canadian')
        .done(function(response) {
            console.log('response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .error(function(response) {
            console.log('error response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .commit();

Example Results
~~~~~~~~~~~~~~~

.. code:: json

    {
        "data": {
            "id": 22,
            "name": "Robin Scherbatsky",
            "org": "Fox News",
            "suborg": "Anchor",
            "workLocation": "New York City, New York",
            "nationality": "Canadian",
            "webLink": "https://demo.threatconnect.com/auth/victim/victim.xhtml?victim=22"
        },
        "remaining": 0,
        "url": "https://demo.threatconnect.com/api/v2/victims?resultLimit=500&owner=Example+Community",
        "apiCalls": 1,
        "body": "{\"name\":\"Robin Scherbatsky\",\"org\":\"Fox News\",\"suborg\":\"Anchor\",\"workLocation\":\"New York City, New York\",\"nationality\":\"Canadian\"}",
        "resultCount": 0,
        "status": "Success"
    }

Associations
------------

The JavaScript SDK provides the ``commitAssociations()`` method to add
both Indicator and Group Associations. The ``.type()``, ``id()``,
``associationType()``, and ``associationId()`` methods are required to
commit the associations. The value passed to the ``associationType()``
method must be the specific Group or Indicator Type (e.g.
TYPE.ADVERSARY, TYPE.HOST).

.. code:: javascript

    tc.tasks()
        .owner('Example Community')
        .id(571)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitAssociation({
            type: TYPE.ADDRESS,
            id: '74.121.142.111'
        });

.. code:: javascript

    tc.tasks()
        .owner('Example Community')
        .id(571)
        .done(function(response) {
            console.log('response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitAssociation({
            type: TYPE.INCIDENT,
            id: 569
        });

Attributes
----------

The JavaScript SDK provides the ``commitAttributes()`` method to add
attributes. The ``id()`` method is required to add attributes. The
attribute object should be passed to ``commitAttribute()`` method with a
type and value parameter.

.. code:: javascript

    tc.tasks()
        .id(571)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitAttribute({
            type: 'Description',
            value: 'This is a description.'
        });

Tags
----

The JavaScript SDK provides the ``commitTags()`` method to add tags. The
``id()`` method is required to retrieve the task. The tag value should
be passed to the ``commitTags()`` method.

.. code:: javascript

    tc.tasks()
        .id(256)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitTags('Example Tag');

Security Labels
---------------

.. code:: javascript

    tc.tasks()
        .id(256)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitSecurityLabel('TLP Red');

Putting it all Together
-----------------------

This example will demonstrate how to add a Task with a name of
'task-999' to the "Example Community" owner. It passes a callback to the
``commit()`` method that will add a group and indicators association,
attribute, tag, and security label. Any number of Associations,
Attributes, or Tags can be added in the callback.

.. code:: javascript

    tasks = tc.tasks();

    tasks.owner('Example Community')
        .name('task-999')
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commit(function() {
            tasks.commitAssociation({
                type: TYPE.ADDRESS,
                id: '74.121.142.111'
            });
            tasks.commitAssociation({
                type: TYPE.INCIDENT,
                id: 256
            });
            tasks.commitAttribute({
                type: 'Description',
                value: 'Example Description.'
            });
            tasks.commitTag('Example');
            tasks.commitSecurityLabel('TLP Red');
        });

Note: To ensure the commits for the metadata happen after the commit of
the task pass a callback to the group commit method.

Associations
------------

The JavaScript SDK provides the ``commitAssociations()`` method to add
both Indicator and Group Associations. The ``.type()``, ``id()``,
``associationType()``, and ``associationId()`` methods are required to
commit the associations. The value passed to the ``associationType()``
method must be the specific Group or Indicator Type (e.g.
TYPE.ADVERSARY, TYPE.HOST).

.. code:: javascript

    tc.victims()
        .owner('Example Community')
        .id(571)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitAssociation({
            type: TYPE.ADDRESS,
            id: '74.121.142.111'
        });

.. code:: javascript

    tc.victims()
        .owner('Example Community')
        .id(571)
        .done(function(response) {
            console.log('response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitAssociation({
            type: TYPE.INCIDENT,
            id: 569
        });

Attributes
----------

The JavaScript SDK provides the ``commitAttributes()`` method to add
attributes. The ``id()`` method is required to add attributes. The
attribute object should be passed to ``commitAttribute()`` method with a
type and value parameter.

.. code:: javascript

    tc.victims()
        .id(571)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitAttribute({
            type: 'Description',
            value: 'This is a description.'
        });

Tags
----

The JavaScript SDK provides the ``commitTags()`` method to add tags. The
``id()`` method is required to retrieve the victim. The tag value should
be passed to the ``commitTags()`` method.

.. code:: javascript

    tc.victims()
        .id(256)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitTags('Example Tag');

Security Labels
---------------

.. code:: javascript

    tc.victims()
        .id(256)
        .done(function(response) {
            console.log('response', response);
        })
        .error(function(response) {
            console.log('error response', response);
        })
        .commitSecurityLabel('TLP Red');

Putting it all Together
-----------------------

This example will demonstrate how to add a Victim with a name of
'task-999' to the "Example Community" owner. It passes a callback to the
``commit()`` method that will add a group and indicators association,
attribute, tag, and security label. Any number of Associations,
Attributes, or Tags can be added in the callback.

.. code:: javascript

    victim = tc.victims();

    victim.owner('Example Community')
        .name('Robin Scherbatsky')
        .org('Fox News')
        .suborg('Anchor')
        .workLocation('New York City, New York')
        .nationality('Canadian')
        .done(function(response) {
            console.log('response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .error(function(response) {
            console.log('error response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .commit(function() {
            // add email address asset
            victim.address('robin.scherbatsky@foxnews.com')
                .addressType('Work')
                .commitAsset(TYPE.VICTIM_ASSET_EMAIL_ADDRESSES);
                
            // add network account asset
            victim.account('robin')
                .network('LDAP')
                .commitAsset(TYPE.VICTIM_ASSET_NETWORK_ACCOUNTS);
                
            // add phone number asset
            victim.phoneType('222-222-2222')
                .commitAsset(TYPE.VICTIM_ASSET_PHONE_NUMBERS);
                
            // add social network asset
            victim.account('RobinSparkles')
                .network('FaceBook')
                .commitAsset(TYPE.VICTIM_ASSET_SOCIAL_NETWORKS);
                
            // add webSite
            victim.webSite('https://www.robinsparkles.com')
                .commitAsset(TYPE.VICTIM_ASSET_WEBSITES);
        
            // add indicator associations
            victim.commitAssociation({
                type: TYPE.ADDRESS,
                id: '74.121.142.111'
            });
        
            // add group association
            victim.commitAssociation({
                type: TYPE.INCIDENT,
                id: 256
            });
            
            // add attribute association
            victim.commitAttribute({
                type: 'Description',
                value: 'Example Description.'
            });
            
            // add tag
            victim.commitTag('Example');
            
            // add securityLabel
            victim.commitSecurityLabel('TLP Red');
        });

Note: To ensure the commits for the metadata happen after the commit of
the task pass a callback to the group commit method.

Manual API Calls
----------------

The example below accesses the API by allowing the creation of a
requestObject():

::

    tc.requestObject()
    ro.apiRequest(ro);

The JavaScript SDK supports a manual way to access the API by allowing
the creation of a ``requestObject()`` and submitting these objects to
the ``apiRequest()`` method. The returned result will contain API
response.

Retrieving Indicators
~~~~~~~~~~~~~~~~~~~~~

The example below displays how to create a ``RequestObject`` that will
retrieve all Indicators from a specified Owner:

.. code:: javascript

    var ro = tc.requestObject();

    ro.owner('Example Community')
        .createActivityLog(false)
        .requestUri('v2/indicators')
        .requestMethod('GET')
        .resultLimit(250)
        .resultStart(0)
        .done(function(response) {
            c.log('response', response);
        })
        .error(function(response) {
            c.log('error response', response);
        })
        .apiRequest('manual');

This example displays how to create a ``RequestObject`` that will
retrieve all Indicators from a specified Owner.

Downloading Document Contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example below displays how to create a ``RequestObject`` that will
retrieve the contents of a document stored in a Document Resource:

.. code:: javascript

    var ro = tc.requestObject();

    ro.owner('Example Community')
        .createActivityLog(false)
        .requestUri('v2/groups/documents/261/download')
        .requestMethod('GET')
        .done(function(response) {
            c.log('response', response);
        })
        .error(function(response) {
            c.log('error response', response);
        })
        .apiRequest('manual');

This example displays how to create a ``RequestObject`` that will
retrieve the contents of a document stored in a Document Resource.

Creating and Uploading Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example below displays how to create a ``RequestObject`` that will
create a Document Resource in ThreatConnect and upload a file to this
Resource.

.. code:: javascript

    var ro = tc.requestObject();

    ro.owner('Example Community')
        .createActivityLog(false)
        .requestUri('v2/groups/documents/263/upload')
        .requestMethod('POST')
        .body('Content of file.')
        .contentType('application/octet-stream')
        .done(function(response) {
            c.log('response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .error(function(response) {
            c.log('error response', response);
            $('#response-content').append(JSON.stringify(response, null, 4));
        })
        .apiRequest('manual');

This example displays how to create a ``RequestObject`` that will create
a Document Resource in ThreatConnect and upload a file to this Resource.

Query String Parameters
~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to add filters to a manual request using the
``payload()`` option.

.. code:: javascript

    var ro = tc.requestObject();

    ro.owner('Example Community')
        .payload('filters', 'summary="1.2.3.4",rating>3')

The JavaScript SDK ``requestObject`` provides the ``payload()`` method
to add any additional query string parameters. This example shows how to
add filters to a manual request using the ``payload()`` option.

+--------------------------+--------------------------+
| Query String Parameter   | Helper Method            |
+==========================+==========================+
| owner                    | owner()                  |
+--------------------------+--------------------------+
| createActivityLog        | createActivityLog()      |
+--------------------------+--------------------------+
| resultLimit              | resultLimit()            |
+--------------------------+--------------------------+
| resultStart              | resultStart()            |
+--------------------------+--------------------------+
| filters                  | manually via payload()   |
+--------------------------+--------------------------+
| orParams                 | manually via payload()   |
+--------------------------+--------------------------+

For a full list of query string parameters supported by the
ThreatConnect API reference the ThreatConnect API User Guide.

Deployment Configuration File
=============================

A configuration file named ``install.json`` is used for ThreatConnect
apps written in:

-  Python
-  Java
-  JavaScript (Spaces)

Standard Section
----------------

Standard section defines required and optional properties to all apps in
ThreatConnect. The required properties are properties that must be
provided for any packaged app installed through the ThreatConnect
platform. The optional properties provide additional information based
on the type of target app.

The table below lists all of the properties of the Standard section.

+------+------+------+------+
| Prop | Requ | Allo | Desc |
| erty | ired | wed  | ript |
|      | ?    | Valu | ion  |
|      |      | es   |      |
+======+======+======+======+
| prog | Yes  | Any  | This |
| ramV |      |      | prop |
| ersi |      |      | erty |
| on   |      |      | is   |
|      |      |      | the  |
|      |      |      | vers |
|      |      |      | ion  |
|      |      |      | for  |
|      |      |      | this |
|      |      |      | app  |
|      |      |      | as   |
|      |      |      | it   |
|      |      |      | shou |
|      |      |      | ld   |
|      |      |      | be   |
|      |      |      | disp |
|      |      |      | laye |
|      |      |      | d    |
|      |      |      | to   |
|      |      |      | the  |
|      |      |      | Syst |
|      |      |      | em   |
|      |      |      | Sett |
|      |      |      | ings |
|      |      |      | Page |
|      |      |      | unde |
|      |      |      | r    |
|      |      |      | Apps |
|      |      |      | .    |
+------+------+------+------+
| prog | Yes  | JAVA | This |
| ramL |      | PYTH | prop |
| angu |      | ONNO | erty |
| age  |      | NE   | is   |
|      |      |      | the  |
|      |      |      | lang |
|      |      |      | uage |
|      |      |      | runt |
|      |      |      | ime  |
|      |      |      | envi |
|      |      |      | ronm |
|      |      |      | ent  |
|      |      |      | used |
|      |      |      | by   |
|      |      |      | the  |
|      |      |      | Thre |
|      |      |      | atCo |
|      |      |      | nnec |
|      |      |      | t    |
|      |      |      | Job  |
|      |      |      | Exec |
|      |      |      | utor |
|      |      |      | .    |
|      |      |      | It   |
|      |      |      | is   |
|      |      |      | rele |
|      |      |      | vant |
|      |      |      | for  |
|      |      |      | apps |
|      |      |      | that |
|      |      |      | run  |
|      |      |      | on   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Exec |
|      |      |      | utio |
|      |      |      | n    |
|      |      |      | Engi |
|      |      |      | ne   |
|      |      |      | and  |
|      |      |      | can  |
|      |      |      | be   |
|      |      |      | set  |
|      |      |      | to   |
|      |      |      | NONE |
|      |      |      | for  |
|      |      |      | Spac |
|      |      |      | es   |
|      |      |      | apps |
|      |      |      | .    |
+------+------+------+------+
| prog | Yes  | Any  | This |
| ramM | for  |      | prop |
| ain  | Pyth |      | erty |
|      | on   |      | is   |
|      | and  |      | the  |
|      | Java |      | entr |
|      | Apps |      | y    |
|      |      |      | poin |
|      |      |      | t    |
|      |      |      | into |
|      |      |      | the  |
|      |      |      | app. |
|      |      |      | For  |
|      |      |      | Pyth |
|      |      |      | on   |
|      |      |      | apps |
|      |      |      | ,    |
|      |      |      | it   |
|      |      |      | is   |
|      |      |      | gene |
|      |      |      | rall |
|      |      |      | y    |
|      |      |      | the  |
|      |      |      | .py  |
|      |      |      | file |
|      |      |      | (or  |
|      |      |      | excl |
|      |      |      | ude  |
|      |      |      | the  |
|      |      |      | exte |
|      |      |      | nsio |
|      |      |      | n    |
|      |      |      | if   |
|      |      |      | runn |
|      |      |      | ing  |
|      |      |      | it   |
|      |      |      | as a |
|      |      |      | modu |
|      |      |      | le). |
|      |      |      | For  |
|      |      |      | Java |
|      |      |      | apps |
|      |      |      | ,    |
|      |      |      | it   |
|      |      |      | is   |
|      |      |      | the  |
|      |      |      | main |
|      |      |      | clas |
|      |      |      | s    |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Exec |
|      |      |      | utio |
|      |      |      | n    |
|      |      |      | Engi |
|      |      |      | ne   |
|      |      |      | shou |
|      |      |      | ld   |
|      |      |      | use  |
|      |      |      | when |
|      |      |      | call |
|      |      |      | ing  |
|      |      |      | the  |
|      |      |      | app  |
|      |      |      | usin |
|      |      |      | g    |
|      |      |      | the  |
|      |      |      | Java |
|      |      |      | Runt |
|      |      |      | ime  |
|      |      |      | Envi |
|      |      |      | ronm |
|      |      |      | ent. |
+------+------+------+------+
| lang | No   | Any  | This |
| uage |      |      | prop |
| Vers |      |      | erty |
| ion  |      |      | is   |
|      |      |      | used |
|      |      |      | pure |
|      |      |      | ly   |
|      |      |      | for  |
|      |      |      | trac |
|      |      |      | king |
|      |      |      | purp |
|      |      |      | oses |
|      |      |      | and  |
|      |      |      | does |
|      |      |      | not  |
|      |      |      | affe |
|      |      |      | ct   |
|      |      |      | the  |
|      |      |      | vers |
|      |      |      | ion  |
|      |      |      | of   |
|      |      |      | Pyth |
|      |      |      | on   |
|      |      |      | or   |
|      |      |      | Java |
|      |      |      | used |
|      |      |      | by   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Exec |
|      |      |      | utio |
|      |      |      | n    |
|      |      |      | Engi |
|      |      |      | ne.  |
+------+------+------+------+
| runt | Yes  | Orga | This |
| imeL |      | niza | prop |
| evel |      | tion | erty |
|      |      | Spac | desc |
|      |      | eOrg | ribe |
|      |      | aniz | s    |
|      |      | atio | the  |
|      |      | nSys | type |
|      |      | tem  | of   |
|      |      |      | app  |
|      |      |      | and  |
|      |      |      | how  |
|      |      |      | it   |
|      |      |      | shou |
|      |      |      | ld   |
|      |      |      | be   |
|      |      |      | used |
|      |      |      | with |
|      |      |      | in   |
|      |      |      | Thre |
|      |      |      | atCo |
|      |      |      | nnec |
|      |      |      | t.   |
|      |      |      | For  |
|      |      |      | furt |
|      |      |      | her  |
|      |      |      | deta |
|      |      |      | ils  |
|      |      |      | on   |
|      |      |      | this |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | ,    |
|      |      |      | see  |
|      |      |      | the  |
|      |      |      | "Run |
|      |      |      | time |
|      |      |      | Leve |
|      |      |      | l"   |
|      |      |      | sect |
|      |      |      | ion. |
+------+------+------+------+
| runt | No   | Arra | This |
| imeC |      | y    | prop |
| onte |      | of   | erty |
| xt   |      | Stri | is   |
|      |      | ngs: | rele |
|      |      | Url, | vant |
|      |      | Host | for  |
|      |      | ,    | Spac |
|      |      | Addr | eOrg |
|      |      | ess, | aniz |
|      |      | Emai | atio |
|      |      | lAdd | n    |
|      |      | ress | apps |
|      |      | ,    | only |
|      |      | File | .    |
|      |      | ,    | This |
|      |      | Thre | arra |
|      |      | at,  | y    |
|      |      | Inci | of   |
|      |      | dent | Stri |
|      |      | ,    | ngs  |
|      |      | Emai | enab |
|      |      | l,   | les  |
|      |      | Docu | Spac |
|      |      | ment | es   |
|      |      | ,    | apps |
|      |      | Sign | to   |
|      |      | atur | be   |
|      |      | e,   | cont |
|      |      | Tag, | ext  |
|      |      | Adve | awar |
|      |      | rsar | e.   |
|      |      | y,   | For  |
|      |      | Vict | furt |
|      |      | im,  | her  |
|      |      | Menu | deta |
|      |      | ,    | ils  |
|      |      | Sear | on   |
|      |      | ch   | this |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | ,    |
|      |      |      | see  |
|      |      |      | the  |
|      |      |      | "Run |
|      |      |      | time |
|      |      |      | Cont |
|      |      |      | ext" |
|      |      |      | sect |
|      |      |      | ion. |
+------+------+------+------+
| repe | No   | Arra | This |
| atin |      | y    | prop |
| gMin |      | of   | erty |
| utes |      | Inte | is a |
|      |      | gers | list |
|      |      | Exam | of   |
|      |      | ple: | minu |
|      |      | [15, | te   |
|      |      | 30,6 | incr |
|      |      | 0,12 | emen |
|      |      | 0,24 | ts   |
|      |      | 0,36 | to   |
|      |      | 0]   | disp |
|      |      |      | lay  |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | "Rep |
|      |      |      | eat  |
|      |      |      | Ever |
|      |      |      | y…"  |
|      |      |      | sect |
|      |      |      | ion  |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | "Sch |
|      |      |      | edul |
|      |      |      | e"   |
|      |      |      | pane |
|      |      |      | l    |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd.  |
|      |      |      | This |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | rele |
|      |      |      | vant |
|      |      |      | only |
|      |      |      | for  |
|      |      |      | Pyth |
|      |      |      | on   |
|      |      |      | and  |
|      |      |      | Java |
|      |      |      | apps |
|      |      |      | for  |
|      |      |      | whic |
|      |      |      | h    |
|      |      |      | the  |
|      |      |      | deve |
|      |      |      | lope |
|      |      |      | r    |
|      |      |      | want |
|      |      |      | s    |
|      |      |      | to   |
|      |      |      | cont |
|      |      |      | rol  |
|      |      |      | how  |
|      |      |      | freq |
|      |      |      | uent |
|      |      |      | ly   |
|      |      |      | an   |
|      |      |      | app  |
|      |      |      | can  |
|      |      |      | be   |
|      |      |      | exec |
|      |      |      | uted |
|      |      |      | .    |
|      |      |      | If   |
|      |      |      | this |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | not  |
|      |      |      | defi |
|      |      |      | ned, |
|      |      |      | the  |
|      |      |      | defa |
|      |      |      | ult  |
|      |      |      | list |
|      |      |      | ing  |
|      |      |      | is   |
|      |      |      | as   |
|      |      |      | foll |
|      |      |      | ows: |
|      |      |      | [    |
|      |      |      | 60,  |
|      |      |      | 120, |
|      |      |      | 240, |
|      |      |      | 360, |
|      |      |      | 720  |
|      |      |      | ]    |
+------+------+------+------+
| allo | Yes  | Bool | This |
| wOnD |      | ean  | prop |
| eman |      |      | erty |
| d    |      |      | allo |
|      |      |      | ws   |
|      |      |      | an   |
|      |      |      | app  |
|      |      |      | to   |
|      |      |      | disp |
|      |      |      | lay  |
|      |      |      | the  |
|      |      |      | "Run |
|      |      |      | Now" |
|      |      |      | butt |
|      |      |      | on   |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Thre |
|      |      |      | atCo |
|      |      |      | nnec |
|      |      |      | t    |
|      |      |      | plat |
|      |      |      | form |
|      |      |      | when |
|      |      |      | conf |
|      |      |      | igur |
|      |      |      | ed   |
|      |      |      | as a |
|      |      |      | Job. |
+------+------+------+------+

Runtime Level
~~~~~~~~~~~~~

The **runtimeLevel** property allows three distinct values that dictate
how the app is used within the ThreatConnect platform, as detailed in
the table below.

+------+------+
| Valu | Desc |
| e    | ript |
|      | ion  |
+======+======+
| Orga | This |
| niza | valu |
| tion | e    |
|      | is a |
|      | Pyth |
|      | on   |
|      | or   |
|      | Java |
|      | app  |
|      | that |
|      | is   |
|      | run  |
|      | by   |
|      | the  |
|      | Job  |
|      | Exec |
|      | utio |
|      | n    |
|      | Engi |
|      | ne.  |
|      | This |
|      | type |
|      | of   |
|      | app  |
|      | must |
|      | be   |
|      | prov |
|      | isio |
|      | ned  |
|      | to   |
|      | spec |
|      | ific |
|      | orga |
|      | niza |
|      | tion |
|      | s    |
|      | (or  |
|      | "All |
|      | ow   |
|      | All  |
|      | Orgs |
|      | "    |
|      | must |
|      | be   |
|      | sele |
|      | cted |
|      | )    |
|      | by   |
|      | the  |
|      | Syst |
|      | em   |
|      | Admi |
|      | n.   |
|      | Once |
|      | prov |
|      | isio |
|      | ned, |
|      | the  |
|      | app  |
|      | can  |
|      | be   |
|      | sche |
|      | dule |
|      | d    |
|      | to   |
|      | run  |
|      | as   |
|      | part |
|      | of a |
|      | Job. |
+------+------+
| Spac | This |
| eOrg | valu |
| aniz | e    |
| atio | is a |
| n    | Spac |
|      | es   |
|      | app  |
|      | that |
|      | is   |
|      | run  |
|      | with |
|      | in   |
|      | Thre |
|      | atCo |
|      | nnec |
|      | t    |
|      | as a |
|      | Spac |
|      | e.   |
|      | This |
|      | type |
|      | of   |
|      | app  |
|      | must |
|      | be   |
|      | prov |
|      | isio |
|      | ned  |
|      | to   |
|      | spec |
|      | ific |
|      | orga |
|      | niza |
|      | tion |
|      | s    |
|      | (or  |
|      | "All |
|      | ow   |
|      | All  |
|      | Orgs |
|      | "    |
|      | must |
|      | be   |
|      | sele |
|      | cted |
|      | )    |
|      | by   |
|      | the  |
|      | Syst |
|      | em   |
|      | Admi |
|      | n.   |
|      | Once |
|      | prov |
|      | isio |
|      | ned, |
|      | the  |
|      | app  |
|      | can  |
|      | be   |
|      | adde |
|      | d    |
|      | as a |
|      | Spac |
|      | es   |
|      | app  |
|      | by   |
|      | any  |
|      | user |
|      | belo |
|      | ngin |
|      | g    |
|      | to   |
|      | the  |
|      | Orga |
|      | niza |
|      | tion |
|      | .    |
+------+------+
| Syst | Alth |
| em   | ough |
|      | not  |
|      | comm |
|      | only |
|      | used |
|      | ,    |
|      | the  |
|      | Syst |
|      | em   |
|      | leve |
|      | l    |
|      | is a |
|      | Pyth |
|      | on   |
|      | or   |
|      | Java |
|      | app  |
|      | that |
|      | is   |
|      | stri |
|      | ctly |
|      | visi |
|      | ble  |
|      | by   |
|      | the  |
|      | Syst |
|      | em   |
|      | Admi |
|      | n.   |
|      | This |
|      | app  |
|      | can  |
|      | be   |
|      | sche |
|      | dule |
|      | d    |
|      | only |
|      | in a |
|      | Syst |
|      | em   |
|      | Job. |
+------+------+

Runtime Context
~~~~~~~~~~~~~~~

The **runtimeContext** property enables Spaces apps to be context aware.
Users are able to add context-aware Spaces apps to their Spaces in the
respective **Details** page of the ThreatConnect platform. Because this
property is an array of Strings, the app can be displayed in multiple
Spaces within the ThreatConnect platform, including the **Menu** and
**Search** pages.

NOTE: Context-aware Spaces apps are passed contextual information via
the URL query string when the app is displayed in the ThreatConnect
platform. The details of those parameters are out of scope for this
document.

Parameter Array Section
-----------------------

The Parameter Array section of the **install.json** file is the
mechanism used by the Job Execution engine and the Spaces framework to
pass configuration data at runtime. For Java and Python apps, the
entries defined in this section dictate the **Parameters** panel in the
Job Wizard in the ThreatConnect platform. Spaces apps have their own
configuration screen as part of the user’s Space for each app.

The table below highlights the Parameter Array properties (the
**params** array).

+------+------+------+------+
| Prop | Requ | Allo | Desc |
| erty | ired | wed  | ript |
|      |      | Valu | ion  |
|      |      | es   |      |
+======+======+======+======+
| name | Yes  | Any  | This |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | the  |
|      |      |      | inte |
|      |      |      | rnal |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r    |
|      |      |      | name |
|      |      |      | take |
|      |      |      | n    |
|      |      |      | from |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd   |
|      |      |      | and  |
|      |      |      | pass |
|      |      |      | ed   |
|      |      |      | to   |
|      |      |      | the  |
|      |      |      | app  |
|      |      |      | at   |
|      |      |      | runt |
|      |      |      | ime. |
|      |      |      | It   |
|      |      |      | is   |
|      |      |      | the  |
|      |      |      | effe |
|      |      |      | ctiv |
|      |      |      | e    |
|      |      |      | comm |
|      |      |      | and- |
|      |      |      | line |
|      |      |      | argu |
|      |      |      | ment |
|      |      |      | name |
|      |      |      | pass |
|      |      |      | ed   |
|      |      |      | to   |
|      |      |      | the  |
|      |      |      | app. |
+------+------+------+------+
| labe | Yes  | Any  | This |
| l    |      |      | prop |
|      |      |      | erty |
|      |      |      | is a |
|      |      |      | desc |
|      |      |      | ript |
|      |      |      | ion  |
|      |      |      | of   |
|      |      |      | the  |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r    |
|      |      |      | disp |
|      |      |      | laye |
|      |      |      | d    |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Thre |
|      |      |      | atCo |
|      |      |      | nnec |
|      |      |      | t    |
|      |      |      | plat |
|      |      |      | form |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd   |
|      |      |      | or   |
|      |      |      | Spac |
|      |      |      | es   |
|      |      |      | Conf |
|      |      |      | ig   |
|      |      |      | dial |
|      |      |      | og   |
|      |      |      | box. |
+------+------+------+------+
| sequ | No   | Inte | This |
| ence |      | ger  | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | the  |
|      |      |      | numb |
|      |      |      | er   |
|      |      |      | used |
|      |      |      | to   |
|      |      |      | cont |
|      |      |      | rol  |
|      |      |      | the  |
|      |      |      | orde |
|      |      |      | ring |
|      |      |      | of   |
|      |      |      | the  |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd   |
|      |      |      | or   |
|      |      |      | Spac |
|      |      |      | es   |
|      |      |      | Conf |
|      |      |      | ig   |
|      |      |      | dial |
|      |      |      | og   |
|      |      |      | box. |
|      |      |      | If   |
|      |      |      | it   |
|      |      |      | is   |
|      |      |      | not  |
|      |      |      | defi |
|      |      |      | ned, |
|      |      |      | the  |
|      |      |      | orde |
|      |      |      | r    |
|      |      |      | of   |
|      |      |      | the  |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | inst |
|      |      |      | all. |
|      |      |      | json |
|      |      |      | file |
|      |      |      | is   |
|      |      |      | used |
|      |      |      | .    |
+------+------+------+------+
| requ | No   | Bool | This |
| ired |      | ean  | prop |
|      |      |      | erty |
|      |      |      | desi |
|      |      |      | gnat |
|      |      |      | es   |
|      |      |      | this |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r    |
|      |      |      | as a |
|      |      |      | requ |
|      |      |      | ired |
|      |      |      | fiel |
|      |      |      | d    |
|      |      |      | that |
|      |      |      | must |
|      |      |      | be   |
|      |      |      | popu |
|      |      |      | late |
|      |      |      | d    |
|      |      |      | to   |
|      |      |      | save |
|      |      |      | the  |
|      |      |      | Job. |
|      |      |      | Requ |
|      |      |      | ired |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | woul |
|      |      |      | d    |
|      |      |      | fail |
|      |      |      | an   |
|      |      |      | app  |
|      |      |      | at   |
|      |      |      | runt |
|      |      |      | ime  |
|      |      |      | or   |
|      |      |      | caus |
|      |      |      | e    |
|      |      |      | unex |
|      |      |      | pect |
|      |      |      | ed   |
|      |      |      | resu |
|      |      |      | lts. |
+------+------+------+------+
| defa | No   | Any  | This |
| ult  |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | the  |
|      |      |      | defa |
|      |      |      | ult  |
|      |      |      | valu |
|      |      |      | e    |
|      |      |      | pre- |
|      |      |      | popu |
|      |      |      | late |
|      |      |      | d    |
|      |      |      | for  |
|      |      |      | new  |
|      |      |      | Jobs |
|      |      |      | or   |
|      |      |      | Spac |
|      |      |      | es.  |
|      |      |      | The  |
|      |      |      | purp |
|      |      |      | ose  |
|      |      |      | of a |
|      |      |      | defa |
|      |      |      | ult  |
|      |      |      | valu |
|      |      |      | e    |
|      |      |      | is   |
|      |      |      | to   |
|      |      |      | prov |
|      |      |      | ide  |
|      |      |      | the  |
|      |      |      | user |
|      |      |      | with |
|      |      |      | a    |
|      |      |      | guid |
|      |      |      | ance |
|      |      |      | whil |
|      |      |      | e    |
|      |      |      | allo |
|      |      |      | wing |
|      |      |      | edit |
|      |      |      | s    |
|      |      |      | base |
|      |      |      | d    |
|      |      |      | on   |
|      |      |      | pref |
|      |      |      | eren |
|      |      |      | ce.  |
+------+------+------+------+
| type | No   | Stri | Data |
|      |      | ng,  | type |
|      |      | Choi | s    |
|      |      | ce,  | enab |
|      |      | Mult | le   |
|      |      | iCho | the  |
|      |      | ice, | UI   |
|      |      | Bool | to   |
|      |      | ean  | disp |
|      |      |      | lay  |
|      |      |      | rele |
|      |      |      | vant |
|      |      |      | comp |
|      |      |      | onen |
|      |      |      | ts   |
|      |      |      | and  |
|      |      |      | allo |
|      |      |      | w    |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Exec |
|      |      |      | utor |
|      |      |      | to   |
|      |      |      | adap |
|      |      |      | t    |
|      |      |      | how  |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | are  |
|      |      |      | pass |
|      |      |      | ed   |
|      |      |      | to   |
|      |      |      | an   |
|      |      |      | app  |
|      |      |      | at   |
|      |      |      | runt |
|      |      |      | ime. |
|      |      |      | For  |
|      |      |      | furt |
|      |      |      | her  |
|      |      |      | deta |
|      |      |      | ils  |
|      |      |      | on   |
|      |      |      | this |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r,   |
|      |      |      | see  |
|      |      |      | the  |
|      |      |      | "Typ |
|      |      |      | e    |
|      |      |      | Para |
|      |      |      | mete |
|      |      |      | r"   |
|      |      |      | sect |
|      |      |      | ion. |
+------+------+------+------+
| encr | No   | Bool | This |
| ypt  |      | ean  | prop |
|      |      |      | erty |
|      |      |      | desi |
|      |      |      | gnat |
|      |      |      | es   |
|      |      |      | this |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r    |
|      |      |      | as   |
|      |      |      | an   |
|      |      |      | encr |
|      |      |      | ypte |
|      |      |      | d    |
|      |      |      | valu |
|      |      |      | e.   |
|      |      |      | Para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | defi |
|      |      |      | ned  |
|      |      |      | as   |
|      |      |      | encr |
|      |      |      | ypte |
|      |      |      | d    |
|      |      |      | will |
|      |      |      | be   |
|      |      |      | mana |
|      |      |      | ged  |
|      |      |      | by   |
|      |      |      | the  |
|      |      |      | Keyc |
|      |      |      | hain |
|      |      |      | feat |
|      |      |      | ure  |
|      |      |      | that |
|      |      |      | encr |
|      |      |      | ypts |
|      |      |      | pass |
|      |      |      | word |
|      |      |      | whil |
|      |      |      | e    |
|      |      |      | at   |
|      |      |      | rest |
|      |      |      | .    |
|      |      |      | This |
|      |      |      | flag |
|      |      |      | shou |
|      |      |      | ld   |
|      |      |      | be   |
|      |      |      | used |
|      |      |      | with |
|      |      |      | the  |
|      |      |      | "Str |
|      |      |      | ing" |
|      |      |      | type |
|      |      |      | and  |
|      |      |      | will |
|      |      |      | rend |
|      |      |      | er   |
|      |      |      | a    |
|      |      |      | pass |
|      |      |      | word |
|      |      |      | inpu |
|      |      |      | t    |
|      |      |      | text |
|      |      |      | box  |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | and  |
|      |      |      | Spac |
|      |      |      | es   |
|      |      |      | conf |
|      |      |      | igur |
|      |      |      | atio |
|      |      |      | n.   |
+------+------+------+------+
| allo | No   | Bool | The  |
| wMul |      | ean  | valu |
| tipl |      |      | e    |
| e    |      |      | of   |
|      |      |      | this |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | auto |
|      |      |      | mati |
|      |      |      | call |
|      |      |      | y    |
|      |      |      | set  |
|      |      |      | to   |
|      |      |      | "tru |
|      |      |      | e"   |
|      |      |      | if   |
|      |      |      | the  |
|      |      |      | "Mul |
|      |      |      | tiCh |
|      |      |      | oice |
|      |      |      | "    |
|      |      |      | type |
|      |      |      | is   |
|      |      |      | used |
|      |      |      | .    |
|      |      |      | If a |
|      |      |      | "Str |
|      |      |      | ing" |
|      |      |      | type |
|      |      |      | is   |
|      |      |      | used |
|      |      |      | ,    |
|      |      |      | this |
|      |      |      | flag |
|      |      |      | allo |
|      |      |      | ws   |
|      |      |      | the  |
|      |      |      | user |
|      |      |      | to   |
|      |      |      | defi |
|      |      |      | ne   |
|      |      |      | mult |
|      |      |      | iple |
|      |      |      | valu |
|      |      |      | es   |
|      |      |      | in a |
|      |      |      | sing |
|      |      |      | le   |
|      |      |      | inpu |
|      |      |      | t    |
|      |      |      | fiel |
|      |      |      | d    |
|      |      |      | deli |
|      |      |      | mite |
|      |      |      | d    |
|      |      |      | by a |
|      |      |      | pipe |
|      |      |      | ("   |
+------+------+------+------+
| vali | No   | Stri | This |
| dVal |      | ng   | prop |
| ues  |      | Arra | erty |
|      |      | y    | is   |
|      |      |      | used |
|      |      |      | with |
|      |      |      | the  |
|      |      |      | "Cho |
|      |      |      | ice" |
|      |      |      | and  |
|      |      |      | "Mul |
|      |      |      | tiCh |
|      |      |      | oice |
|      |      |      | "    |
|      |      |      | type |
|      |      |      | s    |
|      |      |      | to   |
|      |      |      | rest |
|      |      |      | rict |
|      |      |      | the  |
|      |      |      | poss |
|      |      |      | ible |
|      |      |      | valu |
|      |      |      | es   |
|      |      |      | a    |
|      |      |      | user |
|      |      |      | can  |
|      |      |      | sele |
|      |      |      | ct.  |
|      |      |      | For  |
|      |      |      | inst |
|      |      |      | ance |
|      |      |      | ,    |
|      |      |      | to   |
|      |      |      | defi |
|      |      |      | ne   |
|      |      |      | a    |
|      |      |      | "log |
|      |      |      | ging |
|      |      |      | Leve |
|      |      |      | l"   |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r,   |
|      |      |      | this |
|      |      |      | fiel |
|      |      |      | d    |
|      |      |      | coul |
|      |      |      | d    |
|      |      |      | have |
|      |      |      | the  |
|      |      |      | foll |
|      |      |      | owin |
|      |      |      | g    |
|      |      |      | valu |
|      |      |      | es:  |
|      |      |      | ["FA |
|      |      |      | TAL" |
|      |      |      | ,    |
|      |      |      | "ERR |
|      |      |      | OR", |
|      |      |      | "WAR |
|      |      |      | N",  |
|      |      |      | "INF |
|      |      |      | O",  |
|      |      |      | "DEB |
|      |      |      | UG", |
|      |      |      | "TRA |
|      |      |      | CE"] |
|      |      |      | .    |
+------+------+------+------+
| hidd | No   | Bool | If   |
| en   |      | ean  | this |
|      |      |      | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | set  |
|      |      |      | to   |
|      |      |      | "tru |
|      |      |      | e",  |
|      |      |      | this |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r    |
|      |      |      | will |
|      |      |      | be   |
|      |      |      | hidd |
|      |      |      | en   |
|      |      |      | from |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd.  |
|      |      |      | Hidd |
|      |      |      | en   |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | allo |
|      |      |      | w    |
|      |      |      | the  |
|      |      |      | deve |
|      |      |      | lope |
|      |      |      | r    |
|      |      |      | to   |
|      |      |      | pers |
|      |      |      | ist  |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | betw |
|      |      |      | een  |
|      |      |      | job  |
|      |      |      | exec |
|      |      |      | utio |
|      |      |      | ns   |
|      |      |      | with |
|      |      |      | out  |
|      |      |      | the  |
|      |      |      | need |
|      |      |      | to   |
|      |      |      | rend |
|      |      |      | er   |
|      |      |      | the  |
|      |      |      | valu |
|      |      |      | es   |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | Job  |
|      |      |      | Wiza |
|      |      |      | rd.  |
|      |      |      | This |
|      |      |      | opti |
|      |      |      | on   |
|      |      |      | is   |
|      |      |      | vali |
|      |      |      | d    |
|      |      |      | only |
|      |      |      | for  |
|      |      |      | Pyth |
|      |      |      | on   |
|      |      |      | and  |
|      |      |      | Java |
|      |      |      | apps |
|      |      |      | .    |
|      |      |      | Furt |
|      |      |      | her  |
|      |      |      | deta |
|      |      |      | ils  |
|      |      |      | on   |
|      |      |      | pers |
|      |      |      | isti |
|      |      |      | ng   |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | rs   |
|      |      |      | from |
|      |      |      | the  |
|      |      |      | app  |
|      |      |      | dire |
|      |      |      | ctly |
|      |      |      | are  |
|      |      |      | out  |
|      |      |      | of   |
|      |      |      | scop |
|      |      |      | e    |
|      |      |      | for  |
|      |      |      | this |
|      |      |      | docu |
|      |      |      | ment |
|      |      |      | .    |
+------+------+------+------+
| setu | No   | Bool | This |
| p    |      | ean  | prop |
|      |      |      | erty |
|      |      |      | is   |
|      |      |      | rese |
|      |      |      | rved |
|      |      |      | for  |
|      |      |      | the  |
|      |      |      | App  |
|      |      |      | Prof |
|      |      |      | iles |
|      |      |      | feat |
|      |      |      | ure. |
|      |      |      | Furt |
|      |      |      | her  |
|      |      |      | deta |
|      |      |      | ils  |
|      |      |      | on   |
|      |      |      | this |
|      |      |      | feat |
|      |      |      | ure  |
|      |      |      | are  |
|      |      |      | out  |
|      |      |      | of   |
|      |      |      | scop |
|      |      |      | e    |
|      |      |      | for  |
|      |      |      | this |
|      |      |      | docu |
|      |      |      | ment |
|      |      |      | .    |
+------+------+------+------+

NOTE: In Python, parameters are called by using the "--param <value>"
syntax handled by the argparse library. For Java apps, the system
environment arguments are passed by using the "-Dparam=<value>" syntax.
Discussion of app argument parsing is out of scope for this document.

Type Parameter
~~~~~~~~~~~~~~

The **type** parameter serves a dual purpose in the ThreatConnect
platform, depending on the actual type defined. The table below lists
the available types and how they affect elements within the platform.

+------+------+
| Type | Desc |
|      | ript |
|      | ion  |
+======+======+
| Stri | This |
| ng   | type |
|      | rend |
|      | ers  |
|      | an   |
|      | HTML |
|      | Inpu |
|      | t    |
|      | text |
|      | box  |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
|      | This |
|      | allo |
|      | ws   |
|      | the  |
|      | user |
|      | to   |
|      | ente |
|      | r    |
|      | free |
|      | -for |
|      | m    |
|      | text |
|      | as a |
|      | para |
|      | mete |
|      | r.   |
|      | Valu |
|      | es   |
|      | are  |
|      | pass |
|      | ed   |
|      | as a |
|      | Stri |
|      | ng   |
|      | to   |
|      | Pyth |
|      | on   |
|      | and  |
|      | Java |
|      | apps |
|      | .    |
+------+------+
| Choi | This |
| ce   | type |
|      | rend |
|      | ers  |
|      | an   |
|      | HTML |
|      | Sele |
|      | ct   |
|      | opti |
|      | on   |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
|      | This |
|      | allo |
|      | ws   |
|      | the  |
|      | user |
|      | to   |
|      | sele |
|      | ct   |
|      | pred |
|      | efin |
|      | ed   |
|      | text |
|      | valu |
|      | es   |
|      | as a |
|      | para |
|      | mete |
|      | r.   |
|      | (See |
|      | the  |
|      | desc |
|      | ript |
|      | ion  |
|      | of   |
|      | the  |
|      | "val |
|      | idVa |
|      | lues |
|      | "    |
|      | stri |
|      | ng   |
|      | arra |
|      | y    |
|      | prop |
|      | erty |
|      | in   |
|      | 3.)  |
|      | Valu |
|      | es   |
|      | are  |
|      | pass |
|      | ed   |
|      | as a |
|      | Stri |
|      | ng   |
|      | to   |
|      | Pyth |
|      | on   |
|      | and  |
|      | Java |
|      | apps |
|      | .    |
+------+------+
| Mult | This |
| iCho | type |
| ice  | rend |
|      | ers  |
|      | an   |
|      | HTML |
|      | Mult |
|      | i-Ch |
|      | eckb |
|      | ox   |
|      | Sele |
|      | ct   |
|      | opti |
|      | on   |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
|      | This |
|      | allo |
|      | ws   |
|      | the  |
|      | user |
|      | to   |
|      | sele |
|      | ct   |
|      | mult |
|      | iple |
|      | pred |
|      | efin |
|      | ed   |
|      | text |
|      | valu |
|      | es   |
|      | as a |
|      | para |
|      | mete |
|      | r.   |
|      | (See |
|      | the  |
|      | desc |
|      | ript |
|      | ion  |
|      | of   |
|      | the  |
|      | "val |
|      | idVa |
|      | lues |
|      | "    |
|      | stri |
|      | ng   |
|      | arra |
|      | y    |
|      | prop |
|      | erty |
|      | in   |
|      | 3.)  |
|      | The  |
|      | same |
|      | para |
|      | mete |
|      | r    |
|      | is   |
|      | pass |
|      | ed   |
|      | mult |
|      | iple |
|      | time |
|      | s    |
|      | for  |
|      | a    |
|      | Pyth |
|      | on   |
|      | app. |
|      | Pyth |
|      | on   |
|      | apps |
|      | shou |
|      | ld   |
|      | use  |
|      | the  |
|      | argp |
|      | arse |
|      | "act |
|      | ion= |
|      | 'app |
|      | end' |
|      | "    |
|      | opti |
|      | on   |
|      | to   |
|      | rece |
|      | ive  |
|      | the  |
|      | para |
|      | mete |
|      | rs   |
|      | as   |
|      | an   |
|      | arra |
|      | y.   |
|      | Java |
|      | and  |
|      | Spac |
|      | es   |
|      | apps |
|      | will |
|      | rece |
|      | ive  |
|      | the  |
|      | para |
|      | mete |
|      | r    |
|      | as a |
|      | sing |
|      | le   |
|      | valu |
|      | e    |
|      | sepa |
|      | rate |
|      | d    |
|      | by a |
|      | pipe |
|      | char |
|      | acte |
|      | r.   |
|      | Valu |
|      | es   |
|      | are  |
|      | pass |
|      | ed   |
|      | as a |
|      | Stri |
|      | ng   |
|      | to   |
|      | Pyth |
|      | on   |
|      | and  |
|      | Java |
|      | apps |
|      | .    |
|      | This |
|      | sele |
|      | ctio |
|      | n    |
|      | must |
|      | be   |
|      | used |
|      | toge |
|      | ther |
|      | with |
|      | the  |
|      | "all |
|      | owMu |
|      | ltip |
|      | le"  |
|      | flag |
|      | defi |
|      | ned  |
|      | as   |
|      | "tru |
|      | e".  |
+------+------+
| Bool | This |
| ean  | type |
|      | rend |
|      | ers  |
|      | an   |
|      | HTML |
|      | Chec |
|      | kbox |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
|      | This |
|      | allo |
|      | ws   |
|      | the  |
|      | user |
|      | to   |
|      | turn |
|      | on a |
|      | flag |
|      | as a |
|      | para |
|      | mete |
|      | r.   |
|      | Valu |
|      | es   |
|      | are  |
|      | pass |
|      | ed   |
|      | as a |
|      | "--f |
|      | lag" |
|      | styl |
|      | e    |
|      | para |
|      | mete |
|      | r    |
|      | to   |
|      | Pyth |
|      | on   |
|      | apps |
|      | .    |
|      | (See |
|      | the  |
|      | "act |
|      | ion= |
|      | 'sto |
|      | re\_ |
|      | true |
|      | '"   |
|      | opti |
|      | on   |
|      | in   |
|      | the  |
|      | argp |
|      | arse |
|      | modu |
|      | le.) |
|      | Java |
|      | and  |
|      | Spac |
|      | es   |
|      | apps |
|      | rece |
|      | ive  |
|      | the  |
|      | actu |
|      | al   |
|      | Bool |
|      | ean  |
|      | valu |
|      | e    |
|      | "tru |
|      | e"   |
|      | or   |
|      | "fal |
|      | se". |
|      | Thes |
|      | e    |
|      | apps |
|      | shou |
|      | ld   |
|      | pars |
|      | e    |
|      | the  |
|      | stri |
|      | ng   |
|      | to   |
|      | reso |
|      | lve  |
|      | the  |
|      | Bool |
|      | ean  |
|      | flag |
|      | valu |
|      | e.   |
+------+------+

Variable Expression
-------------------

The variable-expression feature enables developers to reference "$"
style variables in the **install.json** file and have the ThreatConnect
platform resolve the values when displayed in the Job Wizard or Spaces
configuration dialog box. The external-variables component can go one
step further by resolving the value at the time a Job executes. Variable
expressions are allowed only in the **params** section of the
**install.json** file.

Internal Variables
~~~~~~~~~~~~~~~~~~

Internal variables are predefined (reserved) variables that can be
explicitly declared in the **install.json** file. Apps declaring these
variables will direct the Job Wizard and Spaces configuration dialog box
to convert the variables into literal values. Internal variables should
be used only with the **Choice** and **MultiChoice** types. They should
be defined in the **validValues** property.

Example of a validValues parameter definition example:

.. code:: json

    {
       "name": "owner",
       "label": "Owner",
       "type": "choice",
       "validValues": ["${OWNERS}"]
    }

The variables listed in the table below are internal variables
understood by the ThreatConnect platform.

+------+------+------+------+
| Vari | Reso | Exam | Desc |
| able | lves | ple  | ript |
|      | As   | of   | ion  |
|      | Type | Usag |      |
|      |      | e    |      |
+======+======+======+======+
| OWNE | Stri | ["${ | The  |
| RS   | ng   | OWNE | OWNE |
|      | Arra | RS}" | RS   |
|      | y    | ]    | vari |
|      |      |      | able |
|      |      |      | reso |
|      |      |      | lves |
|      |      |      | to   |
|      |      |      | the  |
|      |      |      | avai |
|      |      |      | labl |
|      |      |      | e    |
|      |      |      | owne |
|      |      |      | rs   |
|      |      |      | to   |
|      |      |      | whic |
|      |      |      | h    |
|      |      |      | the  |
|      |      |      | curr |
|      |      |      | ent  |
|      |      |      | user |
|      |      |      | has  |
|      |      |      | acce |
|      |      |      | ss.  |
|      |      |      | Sinc |
|      |      |      | e    |
|      |      |      | this |
|      |      |      | dete |
|      |      |      | rmin |
|      |      |      | atio |
|      |      |      | n    |
|      |      |      | is   |
|      |      |      | dyna |
|      |      |      | mica |
|      |      |      | lly  |
|      |      |      | reso |
|      |      |      | lved |
|      |      |      | at   |
|      |      |      | runt |
|      |      |      | ime, |
|      |      |      | the  |
|      |      |      | owne |
|      |      |      | rs   |
|      |      |      | rend |
|      |      |      | ered |
|      |      |      | depe |
|      |      |      | nd   |
|      |      |      | on   |
|      |      |      | the  |
|      |      |      | user |
|      |      |      | .    |
|      |      |      | This |
|      |      |      | vari |
|      |      |      | able |
|      |      |      | is   |
|      |      |      | usef |
|      |      |      | ul   |
|      |      |      | when |
|      |      |      | an   |
|      |      |      | app  |
|      |      |      | need |
|      |      |      | s    |
|      |      |      | to   |
|      |      |      | have |
|      |      |      | a    |
|      |      |      | defi |
|      |      |      | ned  |
|      |      |      | owne |
|      |      |      | r    |
|      |      |      | pass |
|      |      |      | ed   |
|      |      |      | as a |
|      |      |      | para |
|      |      |      | mete |
|      |      |      | r.   |
|      |      |      | The  |
|      |      |      | stri |
|      |      |      | ng   |
|      |      |      | valu |
|      |      |      | e    |
|      |      |      | of   |
|      |      |      | the  |
|      |      |      | owne |
|      |      |      | r(s) |
|      |      |      | is   |
|      |      |      | pass |
|      |      |      | ed   |
|      |      |      | as   |
|      |      |      | an   |
|      |      |      | argu |
|      |      |      | ment |
|      |      |      | to   |
|      |      |      | the  |
|      |      |      | app. |
+------+------+------+------+
| ATTR | Stri | ["${ | The  |
| IBUT | ng   | ATTR | ATTR |
| ES   | Arra | IBUT | IBUT |
|      | y    | ES}" | ES   |
|      |      | ]["$ | vari |
|      |      | {ATT | able |
|      |      | RIBU | reso |
|      |      | TES: | lves |
|      |      | Addr | to   |
|      |      | ess} | attr |
|      |      | "]   | ibut |
|      |      |      | es   |
|      |      |      | the  |
|      |      |      | curr |
|      |      |      | ent  |
|      |      |      | orga |
|      |      |      | niza |
|      |      |      | tion |
|      |      |      | has  |
|      |      |      | avai |
|      |      |      | labl |
|      |      |      | e.   |
|      |      |      | This |
|      |      |      | vari |
|      |      |      | able |
|      |      |      | has  |
|      |      |      | a    |
|      |      |      | seco |
|      |      |      | nd,  |
|      |      |      | opti |
|      |      |      | onal |
|      |      |      | ,    |
|      |      |      | comp |
|      |      |      | onen |
|      |      |      | t,   |
|      |      |      | :,   |
|      |      |      | that |
|      |      |      | furt |
|      |      |      | her  |
|      |      |      | refi |
|      |      |      | nes  |
|      |      |      | the  |
|      |      |      | attr |
|      |      |      | ibut |
|      |      |      | es   |
|      |      |      | reso |
|      |      |      | lved |
|      |      |      | to   |
|      |      |      | the  |
|      |      |      | spec |
|      |      |      | ific |
|      |      |      | Indi |
|      |      |      | cato |
|      |      |      | r    |
|      |      |      | or   |
|      |      |      | grou |
|      |      |      | p    |
|      |      |      | type |
|      |      |      | .    |
|      |      |      | This |
|      |      |      | comp |
|      |      |      | onen |
|      |      |      | t    |
|      |      |      | give |
|      |      |      | s    |
|      |      |      | the  |
|      |      |      | deve |
|      |      |      | lope |
|      |      |      | r    |
|      |      |      | furt |
|      |      |      | her  |
|      |      |      | cont |
|      |      |      | rol  |
|      |      |      | over |
|      |      |      | the  |
|      |      |      | attr |
|      |      |      | ibut |
|      |      |      | e    |
|      |      |      | type |
|      |      |      | valu |
|      |      |      | es   |
|      |      |      | rend |
|      |      |      | ered |
|      |      |      | at   |
|      |      |      | runt |
|      |      |      | ime. |
|      |      |      | The  |
|      |      |      | stri |
|      |      |      | ng   |
|      |      |      | valu |
|      |      |      | e    |
|      |      |      | of   |
|      |      |      | the  |
|      |      |      | attr |
|      |      |      | ibut |
|      |      |      | e(s) |
|      |      |      | is   |
|      |      |      | pass |
|      |      |      | ed   |
|      |      |      | as   |
|      |      |      | an   |
|      |      |      | argu |
|      |      |      | ment |
|      |      |      | to   |
|      |      |      | the  |
|      |      |      | app. |
+------+------+------+------+

When the $ATTRIBUTES internal variable is used with a :<type> suffix,
the types can be any of the Indicator, Group, Task, or Victim types in
the ThreatConnect platform: Address, Adversary, Campaign, Document,
Email, EmailAddress, File, Host, Incident, Signature, Task, Threat, and
URL.

External Variables
~~~~~~~~~~~~~~~~~~

External variables offer the user an additional level of convenience by
directing the Job Wizard and Spaces configuration dialog box to take
advantage of the Variables feature.

NOTE: The Variables feature in the ThreatConnect platform allows any
user to create variable key/value pairs. Once created, these values can
be selected by the user in the Job Wizard or Spaces configuration dialog
box to reduce the need to copy and paste keys and plain-text data.

Since the variable names are not known by the app developer, the generic
form of the variables is referenced instead in a **<level:type>**
format.

For instance, to allow the user to select one of their plain-text
variables from Organization and User levels, the **install.json** file
would reference them as follows:

.. code:: json

    "validValues": ["{USER:TEXT}", "${ORGANIZATION: TEXT}"]

The left-hand component of the variable is the level. The level can be
any of the options listed in the table below.

+------+------+
| Leve | Desc |
| l    | ript |
| Opti | ion  |
| on   |      |
+======+======+
| User | This |
|      | opti |
|      | on   |
|      | disp |
|      | lays |
|      | the  |
|      | list |
|      | of   |
|      | the  |
|      | user |
|      | ’s   |
|      | vari |
|      | able |
|      | s    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
+------+------+
| Orga | This |
| niza | opti |
| tion | on   |
|      | disp |
|      | lays |
|      | the  |
|      | list |
|      | of   |
|      | Orga |
|      | niza |
|      | tion |
|      | vari |
|      | able |
|      | s    |
|      | avai |
|      | labl |
|      | e    |
|      | to   |
|      | the  |
|      | curr |
|      | ent  |
|      | user |
|      | in   |
|      | the  |
|      | Job  |
|      | wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
+------+------+
| Syst | This |
| em   | opti |
|      | on   |
|      | disp |
|      | lays |
|      | the  |
|      | list |
|      | of   |
|      | syst |
|      | em   |
|      | vari |
|      | able |
|      | s    |
|      | avai |
|      | labl |
|      | e    |
|      | to   |
|      | the  |
|      | curr |
|      | ent  |
|      | user |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | or   |
|      | Spac |
|      | es   |
|      | conf |
|      | igur |
|      | atio |
|      | n    |
|      | dial |
|      | og   |
|      | box. |
+------+------+

The right-hand component of the variable is the type. The type can
either of the options listed in the table below.

+------+------+
| Type | Desc |
| Opti | ript |
| on   | ion  |
+======+======+
| Text | This |
|      | opti |
|      | on   |
|      | rest |
|      | rict |
|      | s    |
|      | the  |
|      | valu |
|      | es   |
|      | in   |
|      | the  |
|      | leve |
|      | l    |
|      | to   |
|      | thos |
|      | e    |
|      | vari |
|      | able |
|      | s    |
|      | defi |
|      | ned  |
|      | as   |
|      | plai |
|      | n    |
|      | text |
|      | .    |
+------+------+
| Keyc | This |
| hain | opti |
|      | on   |
|      | rest |
|      | rict |
|      | s    |
|      | the  |
|      | valu |
|      | es   |
|      | in   |
|      | the  |
|      | leve |
|      | l    |
|      | to   |
|      | thos |
|      | e    |
|      | vari |
|      | able |
|      | s    |
|      | defi |
|      | ned  |
|      | as   |
|      | keyc |
|      | hain |
|      | .    |
|      | Thes |
|      | e    |
|      | para |
|      | mete |
|      | rs   |
|      | are  |
|      | typi |
|      | call |
|      | y    |
|      | set  |
|      | to   |
|      | "enc |
|      | rypt |
|      | :    |
|      | true |
|      | "    |
|      | in   |
|      | the  |
|      | conf |
|      | igur |
|      | atio |
|      | n.   |
+------+------+

Multiple external-variable expressions can be included in string array
form.

Example JSON File
-----------------

This section provides an example of an **install.json** file for a
Python app. The key elements are described with line-number references
in 8, below the example.

Example install.json file for a Python app:

.. code:: json

    {
     "programVersion": "1.0.0",
     "programLanguage": "PYTHON",
     "programMain": "auto_enrich",
     "languageVersion": "2.7",
     "runtimeLevel": "Organization",
     "allowOnDemand": true,
     "params": [{
      "name": "api_access_id",
      "label": "Local ThreatConnect API Access ID",
      "sequence": 1,
      "required": true,
      "validValues": ["${USER:TEXT}", "${ORGANIZATION:TEXT}"]
     }, {
      "name": "api_secret_key",
      "label": "Local ThreatConnect API Secret Key",
      "sequence": 2,
      "encrypt": true,
      "required": true,
      "validValues": ["${USER:KEYCHAIN}", "${ORGANIZATION:KEYCHAIN}"]
     }, {
      "name": "owner",
      "label": "Destination Owner",
      "sequence": 3,
      "required": true,
      "type": "choice",
      "validValues": ["${OWNERS}"]
     }, {
      "name": "remote_api_access_id",
      "label": "Remote ThreatConnect API Access ID",
      "sequence": 4,
      "required": true,
      "validValues": ["${USER:TEXT}", "${ORGANIZATION:TEXT}"]
     }, {
      "name": "remote_api_secret_key",
      "label": "Remote ThreatConnect API Secret Key",
      "sequence": 5,
      "encrypt": true,
      "required": true,
      "validValues": ["${USER:KEYCHAIN}", "${ORGANIZATION:KEYCHAIN}"]
     }, {
      "name": "remote_api_path",
      "label": "Remote ThreatConnect API Path",
      "sequence": 6,
      "required": true,
      "default": "https://api.threatconnect.com",
      "validValues": ["${USER:TEXT}", "${ORGANIZATION:TEXT}"]
     }, {
      "name": "remote_owner",
      "label": "Remote Owner",
      "sequence": 7,
      "required": true
     }, {
      "name": "apply_threat_assess_rating",
      "label": "Apply ThreatAssessRating from Remote Owner",
      "type": "Boolean",
      "sequence": 8
     }, {
      "name": "apply_rating",
      "label": "Apply Rating from Remote Owner if ThreatAssesRating
      is not Available ", "
      type " : "
      Boolean ", "
      sequence " : 9
     }, {
      "name": "apply_threat_assess_confidence",
      "label": "Apply ThreatAssessConfidence from Remote Owner",
      "type": "Boolean",
      "sequence": 10
     }, {
      "name": "apply_confidence",
      "label": "Apply Confidence from Remote Owner if
      ThreatAssessConfidence is not Available ", "
      type " : "
      Boolean ",
      "sequence": 11
     }, {
      "name": "apply_tags",
      "label": "Apply Tags from Remote Owner",
      "type": "Boolean",
      "sequence": 12
     }, {
      "name": "apply_auto_enrich_tag",
      "label": "Apply 'AutoEnriched' Tag",
      "type": "Boolean",
      "sequence": 13
     }, {
      "name": "apply_proxy_tc",
      "label": "Apply Proxy to Local API Connection",
      "type": "Boolean",
      "sequence": 14,
      "default": false
     }, {
      "name": "apply_proxy_ext",
      "label": "Apply Proxy to Remote API Connection",
      "type": "Boolean",
      "sequence": 15,
      "default": false
     }, {
      "name": "logging",
      "label": "Logging Level",
      "sequence": 16,
      "default": "info",
      "type": "choice",
      "validValues": ["debug", "info", "warning", "error", "critical"]
     }]
    }

+------+------+
| Line | Desc |
| Numb | ript |
| er   | ion  |
+======+======+
| 2    | The  |
|      | "pro |
|      | gram |
|      | Vers |
|      | ion" |
|      | is   |
|      | 1.0. |
|      | 0.   |
|      | This |
|      | valu |
|      | e    |
|      | is   |
|      | rend |
|      | ered |
|      | in   |
|      | the  |
|      | apps |
|      | list |
|      | ing  |
|      | for  |
|      | Syst |
|      | em   |
|      | Admi |
|      | nist |
|      | rato |
|      | rs.  |
+------+------+
| 4    | The  |
|      | "pro |
|      | gram |
|      | Main |
|      | "    |
|      | will |
|      | dire |
|      | ct   |
|      | the  |
|      | Job  |
|      | Exec |
|      | utor |
|      | to   |
|      | run  |
|      | this |
|      | app  |
|      | as a |
|      | main |
|      | modu |
|      | le.  |
+------+------+
| 6    | The  |
|      | "run |
|      | time |
|      | Leve |
|      | l"   |
|      | for  |
|      | this |
|      | app  |
|      | is   |
|      | "Org |
|      | aniz |
|      | atio |
|      | n".  |
|      | This |
|      | app  |
|      | will |
|      | allo |
|      | w    |
|      | Jobs |
|      | to   |
|      | be   |
|      | conf |
|      | igur |
|      | ed   |
|      | only |
|      | for  |
|      | an   |
|      | Orga |
|      | niza |
|      | tion |
|      | (ass |
|      | umin |
|      | g    |
|      | the  |
|      | Syst |
|      | em   |
|      | Admi |
|      | n    |
|      | has  |
|      | prov |
|      | isio |
|      | ned  |
|      | the  |
|      | Org) |
|      | .    |
+------+------+
| 8    | This |
|      | line |
|      | is   |
|      | the  |
|      | star |
|      | t    |
|      | of   |
|      | the  |
|      | "par |
|      | ams" |
|      | arra |
|      | y.   |
|      | The  |
|      | cont |
|      | ents |
|      | in   |
|      | this |
|      | arra |
|      | y    |
|      | are  |
|      | pure |
|      | ly   |
|      | for  |
|      | para |
|      | mete |
|      | r    |
|      | defi |
|      | niti |
|      | ons. |
+------+------+
| 9–13 | This |
|      | para |
|      | mete |
|      | r    |
|      | desc |
|      | ribe |
|      | s    |
|      | the  |
|      | "api |
|      | \_ac |
|      | cess |
|      | \_id |
|      | "    |
|      | argu |
|      | ment |
|      | for  |
|      | the  |
|      | app. |
|      | The  |
|      | app  |
|      | will |
|      | be   |
|      | pass |
|      | ed   |
|      | an   |
|      | argu |
|      | ment |
|      | call |
|      | ed   |
|      | "--a |
|      | pi\_ |
|      | acce |
|      | ss\_ |
|      | id"  |
|      | at   |
|      | exec |
|      | utio |
|      | n    |
|      | time |
|      | .    |
|      | The  |
|      | labe |
|      | l    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | will |
|      | be   |
|      | "Loc |
|      | al   |
|      | Thre |
|      | atCo |
|      | nnec |
|      | t    |
|      | API  |
|      | Acce |
|      | ss   |
|      | ID". |
|      | Sinc |
|      | e    |
|      | the  |
|      | sequ |
|      | ence |
|      | is   |
|      | defi |
|      | ned  |
|      | as   |
|      | "1", |
|      | this |
|      | para |
|      | mete |
|      | r    |
|      | will |
|      | be   |
|      | the  |
|      | firs |
|      | t    |
|      | para |
|      | mete |
|      | r    |
|      | disp |
|      | laye |
|      | d    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd.  |
|      | This |
|      | para |
|      | mete |
|      | r    |
|      | is   |
|      | requ |
|      | ired |
|      | ,    |
|      | and  |
|      | the  |
|      | user |
|      | can  |
|      | bene |
|      | fit  |
|      | from |
|      | User |
|      | -    |
|      | and  |
|      | Orga |
|      | niza |
|      | tion |
|      | -lev |
|      | el   |
|      | plai |
|      | n-te |
|      | xt   |
|      | vari |
|      | able |
|      | s,   |
|      | if   |
|      | defi |
|      | ned. |
|      | Othe |
|      | rwis |
|      | e,   |
|      | the  |
|      | user |
|      | is   |
|      | allo |
|      | wed  |
|      | to   |
|      | ente |
|      | r    |
|      | free |
|      | -for |
|      | m    |
|      | text |
|      | (the |
|      | defa |
|      | ult  |
|      | type |
|      | if   |
|      | no   |
|      | vari |
|      | able |
|      | s    |
|      | are  |
|      | defi |
|      | ned) |
|      | .    |
+------+------+
| 35–4 | This |
| 0    | para |
|      | mete |
|      | r    |
|      | desc |
|      | ribe |
|      | s    |
|      | the  |
|      | "rem |
|      | ote\ |
|      | _api |
|      | \_se |
|      | cret |
|      | \_ke |
|      | y"   |
|      | argu |
|      | ment |
|      | for  |
|      | the  |
|      | app. |
|      | The  |
|      | app  |
|      | will |
|      | be   |
|      | pass |
|      | ed   |
|      | an   |
|      | argu |
|      | ment |
|      | call |
|      | ed   |
|      | "--r |
|      | emot |
|      | e\_a |
|      | pi\_ |
|      | secr |
|      | et\_ |
|      | key" |
|      | at   |
|      | exec |
|      | utio |
|      | n    |
|      | time |
|      | .    |
|      | The  |
|      | labe |
|      | l    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | will |
|      | be   |
|      | "Rem |
|      | ote  |
|      | Thre |
|      | atCo |
|      | nnec |
|      | t    |
|      | API  |
|      | Secr |
|      | et   |
|      | Key" |
|      | .    |
|      | This |
|      | para |
|      | mete |
|      | r    |
|      | will |
|      | be   |
|      | the  |
|      | 5th  |
|      | para |
|      | mete |
|      | r    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | "Par |
|      | amet |
|      | ers" |
|      | pane |
|      | l.   |
|      | Sinc |
|      | e    |
|      | the  |
|      | para |
|      | mete |
|      | r    |
|      | is   |
|      | set  |
|      | to   |
|      | "enc |
|      | rypt |
|      | ",   |
|      | the  |
|      | inpu |
|      | t    |
|      | fiel |
|      | d    |
|      | will |
|      | be   |
|      | disp |
|      | laye |
|      | d    |
|      | as a |
|      | pass |
|      | word |
|      | with |
|      | a    |
|      | mask |
|      | ed   |
|      | valu |
|      | e.   |
|      | Encr |
|      | ypte |
|      | d    |
|      | para |
|      | mete |
|      | rs   |
|      | will |
|      | also |
|      | be   |
|      | stor |
|      | ed   |
|      | in   |
|      | encr |
|      | ypte |
|      | d    |
|      | form |
|      | in   |
|      | the  |
|      | data |
|      | base |
|      | .    |
|      | At   |
|      | runt |
|      | ime, |
|      | the  |
|      | decr |
|      | ypte |
|      | d    |
|      | pass |
|      | word |
|      | will |
|      | be   |
|      | pass |
|      | ed   |
|      | to   |
|      | the  |
|      | app. |
|      | Fina |
|      | lly, |
|      | the  |
|      | user |
|      | can  |
|      | bene |
|      | fit  |
|      | from |
|      | User |
|      | -    |
|      | and  |
|      | Orga |
|      | niza |
|      | tion |
|      | -lev |
|      | el   |
|      | keyc |
|      | hain |
|      | vari |
|      | able |
|      | s,   |
|      | if   |
|      | defi |
|      | ned. |
|      | Othe |
|      | rwis |
|      | e,   |
|      | the  |
|      | user |
|      | is   |
|      | allo |
|      | wed  |
|      | to   |
|      | ente |
|      | r    |
|      | free |
|      | -for |
|      | m    |
|      | pass |
|      | word |
|      | text |
|      | .    |
+------+------+
| 65–6 | This |
| 8    | para |
|      | mete |
|      | r    |
|      | desc |
|      | ribe |
|      | s    |
|      | the  |
|      | "app |
|      | ly\_ |
|      | thre |
|      | at\_ |
|      | asse |
|      | ss\_ |
|      | conf |
|      | iden |
|      | ce"  |
|      | Bool |
|      | ean  |
|      | argu |
|      | ment |
|      | for  |
|      | the  |
|      | app. |
|      | The  |
|      | app  |
|      | will |
|      | be   |
|      | pass |
|      | ed   |
|      | an   |
|      | argu |
|      | ment |
|      | call |
|      | ed   |
|      | "--a |
|      | pply |
|      | \_th |
|      | reat |
|      | \_as |
|      | sess |
|      | \_co |
|      | nfid |
|      | ence |
|      | "    |
|      | at   |
|      | exec |
|      | utio |
|      | n    |
|      | time |
|      | only |
|      | if   |
|      | the  |
|      | user |
|      | sele |
|      | cts  |
|      | this |
|      | valu |
|      | e    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd.  |
|      | The  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | will |
|      | disp |
|      | lay  |
|      | a    |
|      | labe |
|      | l    |
|      | call |
|      | ed   |
|      | "App |
|      | ly   |
|      | Thre |
|      | atAs |
|      | sess |
|      | Rati |
|      | ng   |
|      | from |
|      | Remo |
|      | te   |
|      | Owne |
|      | r",  |
|      | alon |
|      | g    |
|      | with |
|      | a    |
|      | chec |
|      | kbox |
|      | .    |
|      | The  |
|      | argp |
|      | arse |
|      | styl |
|      | e    |
|      | flag |
|      | (wit |
|      | hout |
|      | an   |
|      | argu |
|      | ment |
|      | )    |
|      | and  |
|      | the  |
|      | chec |
|      | kbox |
|      | disp |
|      | laye |
|      | d    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | are  |
|      | dict |
|      | ated |
|      | by   |
|      | the  |
|      | "Boo |
|      | lean |
|      | "    |
|      | type |
|      | in   |
|      | the  |
|      | para |
|      | mete |
|      | r    |
|      | defi |
|      | niti |
|      | on.  |
|      | This |
|      | para |
|      | mete |
|      | r    |
|      | will |
|      | be   |
|      | the  |
|      | 8th  |
|      | para |
|      | mete |
|      | r    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | "Par |
|      | amet |
|      | ers" |
|      | pane |
|      | l.   |
+------+------+
| 98–1 | This |
| 03   | para |
|      | mete |
|      | r    |
|      | desc |
|      | ribe |
|      | s    |
|      | the  |
|      | "log |
|      | ging |
|      | "    |
|      | argu |
|      | ment |
|      | for  |
|      | the  |
|      | app. |
|      | The  |
|      | app  |
|      | will |
|      | be   |
|      | pass |
|      | ed   |
|      | a    |
|      | para |
|      | mete |
|      | r    |
|      | name |
|      | d    |
|      | "--l |
|      | oggi |
|      | ng"  |
|      | with |
|      | a    |
|      | stri |
|      | ng   |
|      | argu |
|      | ment |
|      | .    |
|      | The  |
|      | "Log |
|      | ging |
|      | Leve |
|      | l"   |
|      | labe |
|      | l    |
|      | will |
|      | be   |
|      | disp |
|      | laye |
|      | d    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd.  |
|      | This |
|      | para |
|      | mete |
|      | r    |
|      | will |
|      | be   |
|      | the  |
|      | 16th |
|      | (and |
|      | last |
|      | )    |
|      | para |
|      | mete |
|      | r    |
|      | in   |
|      | the  |
|      | Job  |
|      | Wiza |
|      | rd   |
|      | para |
|      | mete |
|      | r    |
|      | pane |
|      | l.   |
|      | The  |
|      | type |
|      | for  |
|      | this |
|      | para |
|      | mete |
|      | r    |
|      | is   |
|      | "Cho |
|      | ice" |
|      | ,    |
|      | and  |
|      | the  |
|      | defi |
|      | niti |
|      | on   |
|      | dict |
|      | ates |
|      | that |
|      | a    |
|      | vali |
|      | d    |
|      | valu |
|      | e    |
|      | for  |
|      | this |
|      | para |
|      | mete |
|      | r    |
|      | is   |
|      | one  |
|      | of   |
|      | "deb |
|      | ug", |
|      | "inf |
|      | o",  |
|      | "war |
|      | ning |
|      | ",   |
|      | "err |
|      | or", |
|      | or   |
|      | "cri |
|      | tica |
|      | l".  |
|      | The  |
|      | user |
|      | will |
|      | not  |
|      | be   |
|      | able |
|      | to   |
|      | edit |
|      | this |
|      | drop |
|      | -dow |
|      | n    |
|      | list |
|      | ,    |
|      | and  |
|      | the  |
|      | defa |
|      | ult  |
|      | valu |
|      | e    |
|      | for  |
|      | new  |
|      | Jobs |
|      | will |
|      | be   |
|      | logg |
|      | ing  |
|      | leve |
|      | l    |
|      | "inf |
|      | o".  |
+------+------+

Trademarks
==========

-  ThreatConnect® is a registered trademark of ThreatConnect, Inc.
-  Maven™ is a trademark of the Apache Software Foundation.
-  Mac® is a registered trademark of Apple, Inc.
-  CrowdStrike® is a registered trademark of CrowdStrike, Inc.
-  ECMAScript® is a registered trademark of Ecma International.
-  GitHub® is a registered trademark of GitHub, Inc.
-  Linux® is a registered trademark of Linus Torvalds.
-  Windows® is a registered trademark of the Microsoft Corporation.
-  Java®, JavaScript®, and Oracle® are registered trademarks of the
   Oracle Corporation.
-  Python® is a registered trademark of the Python Software Foundation.
