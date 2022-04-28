TAXII 2.1
=========

To retrieve data from the ThreatConnect TAXII 2.1 server via the TAXII REST API, you must use a TAXII user account. If you do not have a TAXII user account, see the “Creating a TAXII User” section of the `Using the ThreatConnect TAXII 2.1 Server <https://training.threatconnect.com/learn/article/using-the-threatconnect-taxii-21-server-kb-article>`_ knowledge base article.

Authentication
--------------

The TAXII REST API uses `basic authentication <https://swagger.io/docs/specification/authentication/basic-authentication/#:~:text=Basic%20authentication%20is%20a%20simple,%2Dencoded%20string%20username%3Apassword%20>`_, which is completed using the username and password of your TAXII user account.

Required Headers
----------------

The **Accept** header must be set to **application/taxii+json;version=2.1**.

Supported Endpoints
-------------------
Refer to the following table descriptions of each available API endpoint on the ThreatConnect TAXII 2.1 server and supported HTTP method(s) for each endpoint.

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Endpoint
     - Method(s)
     - Description
   * - ``/tc_taxii/``
     - GET
     - Retrieve information about the ThreatConnect TAXII 2.1 server
   * - ``/tc_taxii/collections/``
     - GET
     - Retrieve information about all collections available on the ThreatConnect TAXII 2.1 server
   * - ``/tc_taxii/collections/{collection_id or org_name}/``
     - GET
     - Retrieve information about a specific collection available on the ThreatConnect TAXII 2.1 server
   * - ``/tc_taxii/collections/{collection_id or org_name}/manifest/``
     - GET
     - Retrieve manifest information about the contents of a specific collection available on the ThreatConnect TAXII 2.1 server
   * - ``/tc_taxii/collections/{collection_id or org_name}/objects/``
     - GET
     - Retrieve all objects from a specific collection available on the ThreatConnect TAXII 2.1 server
   * - ``/taxii2/``
     - GET
     - Retrieve information about the TAXII 2.1 server and available API Roots

Available Parameters
--------------------

`Parameters <https://docs.oasis-open.org/cti/taxii/v2.1/cs01/taxii-v2.1-cs01.html#_Toc31107517>`_ included in common STIX™ 2.1 frameworks are supported for the API endpoints listed in the preceding.

Example Requests and Responses
------------------------------

**GET /tc/taxii/**

.. code::

    curl --location --request GET 'https://app.threatconnect.com/api/services/taxii2/v1/tc_taxii' --header 'Accept: application/taxii+json;version=2.1' --header 'Authorization: Basic {REPLACE THIS WITH BASIC AUTH}'

JSON Response

.. code:: json

    {
        "description": "This TAXII 2.1 server contains Indicators of Compromise from the ThreatConnect API Root.",
        "title": "ThreatConnect TAXII 2.1 Server API Root",
        "versions": [
            "application/taxii+json;version=2.1"
        ],
        "max_content_length": 100
    }

**GET /tc_taxii/collections**

.. code::

    curl --location --request GET 'https://app.threatconnect.com/api/services/taxii2/v1/tc_taxii/collections' --header 'Accept: application/taxii+json;version=2.1' --header 'Authorization: Basic {REPLACE THIS WITH BASIC AUTH}'

JSON Response

.. code:: json

    {
        "collections": [
            {
                "description": "ThreatConnect Organization: Example Organization",
                "title": "Example Organization",
                "id": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
                "type": "Organization",
                "can_read": true,
                "media_types": [
                    "application/taxii+json; version=2.1"
                ],
                "alias": "Example Organization",
                "can_write": false
            },
            {
                "description": "ThreatConnect Community: Example Community",
                "title": "Example Community",
                "id": "b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2",
                "type": "Community",
                "can_read": true,
                "media_types": [
                    "application/taxii+json; version=2.1"
                ],
                "alias": "Example Community",
                "can_write": false
            },
            {...}
        ]
    }

**GET /tc_taxii/collections/{collection_id or org_name}/**

.. code::

    curl --location --request GET 'https://app.threatconnect.com/api/services/taxii2/v1/tc_taxii/collections/Example%20Organization' --header 'Accept: application/taxii+json;version=2.1' --header 'Authorization: Basic {REPLACE THIS WITH BASIC AUTH}'

JSON Response

.. code:: json

    {
        "title": "Example Organization",
        "can_read": true,
        "description": "ThreatConnect Organization: Example Organization",
        "can_write": false,
        "type": "Organization",
        "alias": "Example Organization",
        "id": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        "media_types": [
            "application/taxii+json; version=2.1"
        ]
    }

**GET /tc_taxii/collections/{collection_id or org_name}/manifest/**

.. code::

    curl --location --request GET 'https://app.threatconnect.com/api/services/taxii2/v1/tc_taxii/collections/Example%20Organization/manifest' --header 'Accept: application/taxii+json;version=2.1' --header 'Authorization: Basic {REPLACE THIS WITH BASIC AUTH}'

JSON Response

.. code:: json

    {
        "objects": [
            {
                "version": "2021-12-13T20:37:44.000Z",
                "media_types": "application/taxii+json;version=2.1",
                "id": "indicator--a8029d03-e2dd-5fa2-a083-6668ba20e1a8",
                "date_added": "2021-12-13T20:37:44.000Z"
            },
            {
                "version": "2021-03-09T12:09:52.000Z",
                "media_types": "application/taxii+json;version=2.1",
                "id": "indicator--0f3b5690-fe26-5ee0-a1b0-3657cbae1af0",
                "date_added": "2021-03-09T12:09:52.000Z"
            },
            {...}
        ]
    }

**GET /tc_taxii/collections/{collection_id or org_name}/objects/**

.. code::

    curl --location --request GET 'https://app.threatconnect.com/api/services/taxii2/v1/tc_taxii/collections/Example%20Organization/objects?limit=10' --header 'Accept: application/taxii+json;version=2.1' --header 'Authorization: Basic {REPLACE THIS WITH BASIC AUTH}'

JSON Response

.. code:: json

    {
        "next": "10",
        "objects": [
            {
                "name": "TLP:AMBER",
                "type": "marking-definition",
                "definition_type": "tlp",
                "spec_version": "2.1",
                "created": "2017-01-20T00:00:00.000Z",
                "definition": {
                    "tlp": "amber"
                },
                "id": "marking-definition--f88d31f6-486f-44da-b317-01333bde0b82"
            },
            {
                "name": "badguy.com",
                "type": "indicator",
                "spec_version": "2.1",
                "pattern": "[domain-name:value = 'badguy.com']",
                "valid_from": "2018-09-18T17:46:56.000Z",
                "indicator_types": [
                    "malicious-activity"
                ],
                "labels": [
                    "hacker”,
                    "Threat Rating: High"
                ],
                "x_threat_rating": 4,
                "confidence": 84,
                "lang": "en",
                "created": "2018-09-18T17:46:56.000Z ",
                "description": "Malicious actor with tires to hacker networks.",
                "modified": "2021-12-13T20:37:44.000Z",
                "object_marking_refs": [
                    "marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed"
                ],
                "pattern_type": "stix",
                "id": "indicator--c3c3c3c3-c3c3-c3c3-c3c3-c3c3c3c3c3c3"
            },
            {...}
        ],
        "more": true
    }

.. note::

    The request in this example includes the ``limit`` query parameter.

**GET /taxii2/**

.. code::

    curl --location --request GET 'https://app.threatconnect.com/api/services/taxii2/v1/taxii2' --header 'Accept: application/taxii+json;version=2.1' --header 'Authorization: Basic {REPLACE THIS WITH BASIC AUTH}'

JSON Response

.. code:: json

    {
        "title": "ThreatConnect TAXII 2.1 Server",
        "contact": "support@threatconnect.com",
        "api_roots": [
            "https://app.threatconnect.com/api/services/taxii2/v1/tc_taxii"
        ],
        "description": "This TAXII 2.1 server contains Indicators of Compromise from ThreatConnect.",
        "default": "https://app.threatconnect.com/api/services/taxii2/v1/tc_taxii"
    }
