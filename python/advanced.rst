Advanced Python Functionality
=============================

API Settings

The Python SDK provides a few methods that affect interactions with the
ThreatConnect API. The default settings should work in most cases.

Logging
-------

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

Activity Log
------------

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
-------------------

    This timeout value can be changed by passing the new timeout value,
    in seconds, to the ``tc.set_api_request_timeout()`` method.

.. code:: python

    tc.set_api_request_timeout(15)

The Python SDK uses the Request module for communicating to the API. To
prevent script from hanging on a bad socket, there is a timeout value
set to **30 seconds by default**.

API Retries/Sleep Period
------------------------

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

.. note:: There is a maximum window of 5 minutes before the API will reject the HMAC (hash message authentication code) header due to a time mismatch.

API Result Limit
----------------

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
-------

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
---------

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

+-----------------------+-------------------------+
| Filter Object         |                         |
+=======================+=========================+
| **Filter Properties** |                         |
+-----------------------+-------------------------+
| Operator              | FilterSetOperator.AND   |
+-----------------------+-------------------------+
| Request Objects       | 1                       |
+-----------------------+-------------------------+
| **Owners**            |                         |
+-----------------------+-------------------------+
| Owner                 | Example Community       |
+-----------------------+-------------------------+
| **Filters**           |                         |
+-----------------------+-------------------------+
| Filter                | api filter by tag "APT" |
+-----------------------+-------------------------+
| **API Filters**       |                         |
+-----------------------+-------------------------+
| Filter                | add\_adversary\_id      |
+-----------------------+-------------------------+
| Filter                | add\_email\_id          |
+-----------------------+-------------------------+
| Filter                | add\_document\_id       |
+-----------------------+-------------------------+
| Filter                | add\_id                 |
+-----------------------+-------------------------+
| Filter                | add\_incident\_id       |
+-----------------------+-------------------------+
| Filter                | add\_indicator          |
+-----------------------+-------------------------+
| Filter                | add\_security\_label    |
+-----------------------+-------------------------+
| Filter                | add\_signature\_id      |
+-----------------------+-------------------------+
| Filter                | add\_threat\_id         |
+-----------------------+-------------------------+
| Filter                | add\_tag                |
+-----------------------+-------------------------+
| Filter                | add\_victim\_id         |
+-----------------------+-------------------------+
| **Post Filters**      |                         |
+-----------------------+-------------------------+
| Filter                | add\_pf\_name           |
+-----------------------+-------------------------+
| Filter                | add\_pf\_date\_added    |
+-----------------------+-------------------------+

Filter Object Basics
--------------------

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
----------------

The Owner API Filter is a special Filter that is applied to all other
API Filters in the same Filter Object. This is due to the fact that the
API supports adding the Owner as a query String. See the formatted URI
examples below.

Python SDK formatted URI examples:

::

    /v2/indicators/address/10.20.30.40?owner=Example+Community

::

    /v2/groups/adversaries/5/indicators?owner=Example+Community

Indicator-Type Filter
---------------------

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

Python SDK example filtering on supported Indicator Types:

.. code:: python

    from threatconnect.Config.IndicatorType import IndicatorType

    filter1 = indicators.add_filter(IndicatorType.ADDRESSES)
    filter1 = indicators.add_filter(IndicatorType.EMAIL_ADDRESSES)
    filter1 = indicators.add_filter(IndicatorType.FILES)
    filter1 = indicators.add_filter(IndicatorType.HOSTS)
    filter1 = indicators.add_filter(IndicatorType.URLS)

Modified Since API Filter
-------------------------

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
-----------------------

Python SDK Multiple Filter Objects example:

.. code:: python

    from threatconnect.Config.FilterOperator import FilterSetOperator
    from threatconnect.Config.IndicatorType import IndicatorType

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

    # add code here...

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
^^^^^^^^^^^^^^^^^^^^^

The example below displays how to create a ``RequestObject`` that will
retrieve all Indicators from a specified Owner:

.. code:: python

    ...

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
-----------------------------

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
--------------------------------

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
------------------------

The Python SDK allows for a Resource to be returned in multiple standard formats. The SDK currently supports the following formats:

* CEF (Common Event Format)
* CSV (Comma-Separated Values)
* JSON (JavaScript® Object Notation)
* KeyVal (Key Value)
* LEEF (Log Event Extended Format)

CEF
^^^

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
^^^

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
^^^^

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
^^^^^^^^^

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
^^^^

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

Indicator Type Override
-----------------------

The ``add()`` method on the ``tc.indicators()`` object allows the user to bypass the automatic Indicator identification and validation check by specifying the IndicatorType:

.. code-block:: python

    from threatconnect.Config.IndicatorType import IndicatorType

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
    owner = 'Example Community'

    indicator = indicators.add('<indicator>', owner, IndicatorType.ADDRESSES)

Regex Overrides
---------------

Python SDK Regex Code Sample

.. code-block:: python

    ...

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
---------

Stats Reporting
^^^^^^^^^^^^^^^

The ``tc.report.stats`` properties method provides an overview of the
script results:

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
    owner = 'Example Community'

    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)
    else:
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

**Enabling Reporting**

The basic data collection of the Reporting feature is always enabled,
but the report-entry collection feature is disabled by default. To
enable the report-entry collection feature, use the
``tc.report_enable()`` method. To disable reporting, use the
``tc.report_disable()`` method.

**Statistics**

The ``tc.report.stats`` properties method provides an overview of the
script results.

Failed Reports
^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^

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
