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