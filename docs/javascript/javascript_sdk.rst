JavaScript SDK
==============

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

.. note:: If you are working with the ThreatConnect **sandbox**, the second apiSettings.apiUrl (the one in the ``else`` branch) should be: ``https://sandbox.threatconnect.com/api/``.

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

**Third-Party Dependencies**

+-----------+---------+--------------------------------------+
| Name      | Version | Link                                 |
+===========+=========+======================================+
| jquery    | 2.1.4   | https://jquery.com/                  |
+-----------+---------+--------------------------------------+
| Crypto-JS | 3.1     | https://code.google.com/p/crypto-js/ |
+-----------+---------+--------------------------------------+

**Technical Design**

The JavaScript SDK for ThreatConnect was designed with a focus on
abstracting the API REST calls while enabling the developer to use an
enterprise-level programming language.

**Supported Resource Types**

The JavaScript SDK supports the Resource Types listed below. There is
also a mechanism to do manual API requests to cover any API calls that
are not provided with the core functionality.

+-----------------------+----------------------------------+
| Object                | Description                      |
+=======================+==================================+
| ``db()``              | Data Store container object      |
+-----------------------+----------------------------------+
| ``groups()``          | Group container object           |
+-----------------------+----------------------------------+
| ``indicators()``      | Indicator container object       |
+-----------------------+----------------------------------+
| ``indicatorsBatch()`` | Batch Indicator container object |
+-----------------------+----------------------------------+
| ``owners()``          | Owner container object           |
+-----------------------+----------------------------------+
| ``securityLabel()``   | Security Label container object  |
+-----------------------+----------------------------------+
| ``tasks()``           | Task container object            |
+-----------------------+----------------------------------+
| ``tags()``            | Tag container object             |
+-----------------------+----------------------------------+
| ``victims()``         | Victim container object          |
+-----------------------+----------------------------------+
| ``whoami()``          | WhoAmI container object          |
+-----------------------+----------------------------------+

Example JavaScript App
----------------------

The example below illustrates how to write a program using the
JavaScript SDK for the ThreatConnect API:

.. code:: javascript

    var apiSettings;

    // retrieve Space Element ID (only supported for Spaces applications running in ThreatConnect)
    var tcSpaceElementId = getParameterByName('tcSpaceElementId');

    // if the Space Element ID exists, pull the token and api from the spaces environment
    if ( tcSpaceElementId ) {
        apiSettings = {
            apiToken: getParameterByName('tcToken'),
            apiUrl: getParameterByName('tcApiPath')
        };
    }
    // otherwise, use the API settings defined below
    else {
        apiSettings = {
            apiId: '12345678900987654321',
            apiSec: 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz!@#$%^&*()-=',
            apiUrl: 'https://demo.threatconnect.com/api'
        };
    }

    // create ThreatConnect object
    var tc = new ThreatConnect(apiSettings);

    // create Owners object
    tc.owners()
        // if the call finishes successfully, the "done" callback will be run
        .done(function(response) {
            console.log('owner response', response);
        })
        // if the call does NOT finish successfully, the "error" callback will be run
        .error(function(response) {
            console.error('owner response error', response.error);
        })
        // retrieve Owners
        .retrieve();

This example illustrates how to write a program using the JavaScript SDK
for the ThreatConnect API. An Owner's object will be created in order to
pull a collection of all Owners to which the API account being used has
access. Once retrieved, the Owners objects will be printed to the
console.

**Summary**

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

Apps use a deployment configuration file to define variables and execution environment. You can read more about the deployment configuration file `here <../deployment_config.html>`_.

Query Parameters
~~~~~~~~~~~~~~~~

For the sample install configuration example above, here is a sample
query String passed to the app:

.. code::

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

+-------------------------+-------------------------------------------------------+
| ThreatConnect           | Description                                           |
| Parameter               |                                                       |
+=========================+=======================================================+
| ``tcSpaceElementId``    | The unique space element instance ID for the user who |
|                         | added this app to their Space. This numeric ID can be |
|                         | used by the app to store state for the user.          |
+-------------------------+-------------------------------------------------------+
| ``tcToken``             | Session token to be used by the app to access the     |
|                         | API. The JavaScript SDK has configuration options for |
|                         | this parameter.                                       |
+-------------------------+-------------------------------------------------------+
| ``tcApiPath``           | The path to the API defined in System Settings for    |
|                         | all apps.                                             |
+-------------------------+-------------------------------------------------------+
| ``tcType``              | Only relevant for context-aware apps. This field      |
|                         | corresponds to the runtime.context Attribute defined  |
|                         | in the install configuration file.                    |
+-------------------------+-------------------------------------------------------+
| ``tcSelectedItem``      | Only relevant for context-aware apps. This is the     |
|                         | actual context-item identifier used within            |
|                         | ThreatConnect. For instance, a Host identifier might  |
|                         | be: g00gle.com                                        |
+-------------------------+-------------------------------------------------------+
| ``tcSelectedItemOwner`` | Only relevant for context-aware apps. This is the     |
|                         | Owner of the context item.                            |
+-------------------------+-------------------------------------------------------+

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

**Supported Indicator Types**

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

.. note:: Before the ``next()`` method can be called, the first API must
have completed. This should not be an issue if a user click triggers the
next call; however, if the ``next()`` method is being called
programmatically then it should be passed in a function to the
``retrieve()`` method.

.. note:: The ``next()`` method will return the same number of results
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

Example of how to retrieve Indicators that start with 'bad' and have a
dateAdded value greater than '2015-12-13' using an API filter:

.. code:: javascript

    var filter = new Filter(FILTER.AND);
    filter.on('summary', FILTER.SW, 'bad');
    filter.on('dateAdded', FILTER.GT, '2015-12-13');

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
            type: TYPE.INCIDENT
        });

The JavaScript SDK provides the ``retrieveAssociations()`` method to
retrieve both Indicator and Indicator Associations. The ``type()`` and
``indicator()`` methods are required to retrieve the associations. The
``retrieveAssociations()`` method requires that a parameter object
containing the Association ``type`` be provided. Optionally, an association ``id``
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
retrieve attributes. Both the ``type()`` method and ``indicator()`` are
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
retrieve Observations. Both the ``type()`` and ``indicator()`` methods are
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
retrieve the Observation Count for an Indicator. Both the ``type()`` and ``indicator()`` methods are required to retrieve the Observation Count.

.. note:: The Observation Count can also be retrieved with the "Single
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
tags. Both the ``type()`` and ``indicator()`` methods are required to retrieve
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

**Supported Group Types**

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

.. note:: Before the ``next()`` method can be called the first API must have
completed. This should not be an issue if a user click triggers the next
call, however if the ``next()`` method is being called programmaticly
then it should be passed in a function to the ``retrieve()`` method.

.. note:: The ``next()`` method will return the same number of results
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
        .id(123)
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
retrieve both Indicator and Group Associations. The ``type()`` and
``id()`` methods are required to retrieve the associations. The
``retrieveAssociations()`` method requires that a parameter object
containing the association ``type`` be provided. Optionally, an ``id``
can be provided to pull a specific associated group.

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
required to retrieve the attributes. Optionally, an ``id`` can be passed to the
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

**Supported Indicator Types**

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
Group Associations. Both ``type()``, and ``indicator()`` methods are required
to commit the Associations. The value passed to the
``commitAssociation()`` method must be the specific Group Type (e.g.,
TYPE.ADVERSARY, TYPE.HOST) and ``id``.

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
Attributes. Both ``type()`` and ``indicator()`` are required to add
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
Both the ``.type()`` and either the ``.id()`` or ``.indicator()`` methods are required to add the Tags.
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
Security Labels. Both the ``type()`` and ``indicator()`` methods are
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

.. note:: To ensure that commits for the metadata happen after the commit of
the Indicator, pass a callback to the Indicator Commit method.

Group Commit
------------

This section explains how to work with ThreatConnect Group Resources.

**Supported Group Types**

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
both Indicator and Group Associations. The ``type()``, ``id()``,
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
attributes. The ``type()`` and ``id()`` are required to add attributes.
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
Indicator Observation. Both ``type()`` and ``id()`` are required to add an
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
the ``type()`` and ``id()`` methods are required to add the tags. The
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

.. note:: To ensure that commits for the metadata happen after the commit of
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
both Indicator and Group Associations. The ``type()``, ``id()``,
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

.. note:: To ensure the commits for the metadata happen after the commit of
the task pass a callback to the group commit method.

Associations
------------

The JavaScript SDK provides the ``commitAssociations()`` method to add
both Indicator and Group Associations. The ``type()``, ``id()``,
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

.. note:: To ensure the commits for the metadata happen after the commit of
the task pass a callback to the group commit method.

Manual API Calls
----------------

The example below accesses the API by allowing the creation of a
requestObject():

.. code-block:: javascript

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

+------------------------+------------------------+
| Query String Parameter | Helper Method          |
+========================+========================+
| owner                  | owner()                |
+------------------------+------------------------+
| createActivityLog      | createActivityLog()    |
+------------------------+------------------------+
| resultLimit            | resultLimit()          |
+------------------------+------------------------+
| resultStart            | resultStart()          |
+------------------------+------------------------+
| filters                | manually via payload() |
+------------------------+------------------------+
| orParams               | manually via payload() |
+------------------------+------------------------+

For a full list of query string parameters supported by the
ThreatConnect API reference the ThreatConnect API User Guide.
