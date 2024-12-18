TAXII 2.1
=========

Overview
--------

To retrieve data from the ThreatConnect TAXII 2.1 server via the TAXII REST API, you must use a TAXII user account. If you do not have a TAXII user account, see `Creating a TAXII User for the ThreatConnect TAXII 2.1 Server <https://knowledge.threatconnect.com/docs/creating-a-taxii-user-for-the-threatconnect-taxii-21-server>`_ knowledge base article.

Authentication
--------------

The TAXII REST API uses basic authentication, which is completed by combining a TAXII user account's username and password with a colon and then encoding the resulting string in Base64 format.

For example, if your TAXII user account's username and password is ``taxii`` and ``p@55w0rd``, respectively, the combination of ``taxii:p@55w0rd`` will be Base64 encoded and become ``dGF4aWk6cEA1NXcwcmQ=``. In this case, the authentication header for your request would be the following:

.. code::

    Authorization: Basic dGF4aWk6cEA1NXcwcmQ=


Required Headers
----------------

- ``Authorization: Basic {credentials}``
- ``Accept: application/taxii+json;version=2.1``


Available Endpoints
-------------------
Refer to the following table for a description of each available API endpoint on the TAXII REST API and supported HTTP method for each endpoint.

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     - Description
   * - ``/tc_taxii``
     - GET
     - Retrieve information about the ThreatConnect TAXII 2.1 server
   * - ``/tc_taxii/collections``
     - GET
     - Retrieve information about all collections available on the ThreatConnect TAXII 2.1 server
   * - ``/tc_taxii/collections/{collectionId or ownerName}``
     - GET
     - Retrieve information about a specific collection available on the ThreatConnect TAXII 2.1 server
   * - ``/tc_taxii/collections/{collectionId or ownerName}/manifest``
     - GET
     - | Retrieve manifest information about the contents of a specific collection available on the ThreatConnect TAXII 2.1 server
       |  
       | **Note**: This endpoint is available on **version 1.0** of the **ThreatConnect TAXII Server** App only.
   * - ``/tc_taxii/collections/{collectionId or ownerName}/objects``
     - GET
     - Retrieve all objects from a specific collection available on the ThreatConnect TAXII 2.1 server
   * - ``/taxii2``
     - GET
     - Retrieve information about the ThreatConnect TAXII 2.1 server and available API roots

Query Parameters
----------------

The TAXII REST API supports `query parameters <https://docs.oasis-open.org/cti/taxii/v2.1/cs01/taxii-v2.1-cs01.html#_Toc31107517>`_ included in common STIX™ 2.1 frameworks.

Path Parameters
---------------

The examples in the “Example Requests and Responses” section use the following path parameters to represent the different components of the ThreatConnect TAXII 2.1 server URL:

- ``{baseUrl}``: The base URL of your ThreatConnect instance (e.g., ``https://companyabc.threatconnect.com``), followed by ``/api``.
- ``{taxiiServicePath}``:
    - If using **version 2.0** of the **ThreatConnect TAXII Server **App, this will be the API path for the Service that corresponds to the **ThreatConnect TAXII Server** App (e.g., ``/services/taxii/v2``), followed by ``/taxii``. The Service's API path may be found on the `Services screen <https://knowledge.threatconnect.com/docs/playbook-services#viewing-a-service>`_ in the ThreatConnect user interface.
    - If using **version 1.0** of the **ThreatConnect TAXII Server** App, this will be the API path for the Service that corresponds to the **ThreatConnect TAXII Server** App (e.g., ``/services/taxii/v1``). The Service's API path may be found on the `Services screen <https://knowledge.threatconnect.com/docs/playbook-services#viewing-a-service>`_ in the ThreatConnect user interface.

The following are examples of how a complete ThreatConnect TAXII 2.1 server URL should look for each version of the **ThreatConnect TAXII Server** App:

**App Version 2.0**

.. code::

    https://companyabc.threatconnect.com/api/services/taxii/v2/taxii

**App Version 1.0**

.. code::

    https://companyabc.threatconnect.com/api/services/taxii/v1

.. hint::

    If you are using **version 2.0** of the **ThreatConnect TAXII Server** App, you can obtain the complete ThreatConnect TAXII 2.1 server URL by opening the **ThreatConnect TAXII Server** user interface, clicking the ⋮ menu at the top right of the screen, and selecting **TAXII Server Base API URL**. Note that this URL will have the ``/tc_taxii`` endpoint appended to it.

Example Requests and Responses
------------------------------

**GET /tc_taxii**

Request

.. code::

    curl --location --request GET '{baseUrl}{taxiiServicePath}/tc_taxii' \
    --header 'Accept: application/taxii+json;version=2.1' \
    --header 'Authorization: Basic {credentials}'

JSON Response (App Version 1.0 and 2.0)

.. code:: json

    {
        "description": "This TAXII 2.1 server contains Indicators of Compromise from the ThreatConnect API Root.",
        "max_content_length": 100,
        "title": "ThreatConnect TAXII 2.1 Server API Root",
        "versions": [
            "application/taxii+json;version=2.1"
        ]
    }

**GET /tc_taxii/collections**

Request

.. code::

    curl --location --request GET '{baseUrl}{taxiiServicePath}/tc_taxii/collections' \
    --header 'Accept: application/taxii+json;version=2.1' \
    --header 'Authorization: Basic {credentials}'


JSON Response (App Version 2.0)

.. code:: json

    {
        "collections": [
            {
                "can_read": true,
                "can_write": false,
                "description": null,
                "id": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
                "media_types": [
                    "application/taxii+json; version=2.1"
                ],
                "title": "Demo Organization",
                "alias": null,
                "type": null,
                "x_custom_mappings": {},
                "x_custom_ttl": {},
                "x_custom": false,
                "x_tql": "(ownerName EQ \"Demo Organization\") AND typeName in (\"Registry Key\", \"Host\", \"File\", \"EmailAddress\", \"Address\", \"Email Subject\", \"CIDR\", \"ASN\", \"URL\")"
            },
            {
                "can_read": true,
                "can_write": false,
                "description": null,
                "id": "b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2",
                "media_types": [
                    "application/taxii+json; version=2.1"
                ],
                "title": "Demo Source",
                "alias": null,
                "type": null,
                "x_custom_mappings": {},
                "x_custom_ttl": {},
                "x_custom": false,
                "x_tql": "(ownerName EQ \"Demo Source\") AND typeName in (\"Registry Key\", \"Host\", \"File\", \"EmailAddress\", \"Address\", \"Email Subject\", \"CIDR\", \"ASN\", \"URL\")"
            }
        ]
    }

JSON Response (App Version 1.0)

.. code:: json

    {
        "collections": [
            {
                "description": "ThreatConnect Organization: Demo Organization",
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
                "description": "ThreatConnect Source: Demo Source",
                "title": "Demo Source",
                "id": "b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2",
                "type": "Source",
                "can_read": true,
                "media_types": [
                    "application/taxii+json; version=2.1"
                ],
                "alias": "Demo Source",
                "can_write": false
            }
        ]
    }

**GET /tc_taxii/collections/{collectionId or ownerName}**

Request

.. code::

    curl --location --request GET '{baseUrl}{taxiiServicePath}/tc_taxii/collections/Demo%20Organization' \
    --header 'Accept: application/taxii+json;version=2.1' \
    --header 'Authorization: Basic {credentials}'

JSON Response (App Version 2.0)

.. code:: json

    {
        "can_read": true,
        "can_write": false,
        "description": null,
        "id": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        "media_types": [
            "application/taxii+json; version=2.1"
        ],
        "title": "Demo Organization",
        "alias": null,
        "type": null,
        "x_custom_mappings": {},
        "x_custom_ttl": {},
        "x_custom": false,
        "x_tql": "(ownerName EQ \"Demo Organization\") AND typeName in (\"Registry Key\", \"Host\", \"File\", \"EmailAddress\", \"Address\", \"Email Subject\", \"CIDR\", \"ASN\", \"URL\")"
    }

JSON Response (App Version 1.0)

.. code:: json

    {
        "title": "Demo Organization",
        "can_read": true,
        "description": "ThreatConnect Organization: Demo Organization",
        "can_write": false,
        "type": "Organization",
        "alias": "Demo Organization",
        "id": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        "media_types": [
            "application/taxii+json; version=2.1"
        ]
    }

**GET /tc_taxii/collections/{collectionId or ownerName}/manifest**

.. note::

    This endpoint is available on **version 1.0** of the **ThreatConnect TAXII Server** App only.

Request

.. code::

    curl --location --request GET '{baseUrl}{taxiiServicePath}/tc_taxii/collections/Demo%20Organization/manifest' \
    --header 'Accept: application/taxii+json;version=2.1' \
    --header 'Authorization: Basic {credentials}'

JSON Response (App Version 1.0)

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

**GET /tc_taxii/collections/{collectionId or ownerName}/objects**

.. note::

    The following request includes the ``limit`` query parameter.

Request

.. code::

    curl --location --request GET '{baseUrl}{taxiiServicePath}/tc_taxii/collections/Demo%20Organization/objects?limit=5' \
    --header 'Accept: application/taxii+json;version=2.1' \
    --header 'Authorization: Basic {credentials}'

JSON Response (App Version 2.0)

.. code:: json

    {
        "more": true,
        "next": "5",
        "objects": [
            {
                "created": "2017-01-20T00:00:00.000Z",
                "definition": {
                    "tlp": "amber"
                },
                "definition_type": "tlp",
                "id": "marking-definition--f88d31f6-486f-44da-b317-01333bde0b82",
                "name": "TLP:AMBER",
                "spec_version": "2.1",
                "type": "marking-definition"
            },
            {
                "created": "2017-01-20T00:00:00.000Z",
                "definition": {
                    "tlp": "white"
                },
                "definition_type": "tlp",
                "id": "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9",
                "name": "TLP:WHITE",
                "spec_version": "2.1",
                "type": "marking-definition"
            },
            {
                "created": "2017-01-20T00:00:00.000Z",
                "definition": {
                    "tlp": "green"
                },
                "definition_type": "tlp",
                "id": "marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da",
                "name": "TLP:GREEN",
                "spec_version": "2.1",
                "type": "marking-definition"
            },
            {
                "created": "2017-01-20T00:00:00.000Z",
                "definition": {
                    "tlp": "red"
                },
                "definition_type": "tlp",
                "id": "marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed",
                "name": "TLP:RED",
                "spec_version": "2.1",
                "type": "marking-definition"
            },
            {
                "created": "2022-11-17T17:22:31+00:00",
                "id": "4f41230e-518a-5b16-a555-abb790f99e3c",
                "indicator_types": [
                    "malicious-activity"
                ],
                "lang": "en",
                "modified": "2024-11-06T13:29:54+00:00",
                "name": "10.10.1.16/32",
                "object_marking_refs": [],
                "pattern": "[ipv4-addr:value = '10.10.1.16/32']",
                "pattern_type": "stix",
                "revoked": false,
                "spec_version": "2.1",
                "type": "indicator",
                "valid_from": "2024-11-06T13:29:54+00:00",
                "valid_until": "2024-11-13T13:29:54+00:00",
                "x_threat_rating": 2,
                "x_threatconnect_id": 173,
                "x_threatconnect_owner": "Demo Organization",
                "x_threatconnect_type": "CIDR"
            }
        ]
    }

JSON Response (App Version 1.0)

.. code:: json

    {
        "next": "5",
        "more": true,
        "objects": [
            {
                "type": "marking-definition",
                "definition_type": "tlp",
                "name": "TLP:AMBER",
                "created": "2017-01-20T00:00:00.000Z",
                "id": "marking-definition--f88d31f6-486f-44da-b317-01333bde0b82",
                "definition": {
                    "tlp": "amber"
                },
                "spec_version": "2.1"
            },
            {
                "type": "marking-definition",
                "definition_type": "tlp",
                "name": "TLP:WHITE",
                "created": "2017-01-20T00:00:00.000Z",
                "id": "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9",
                "definition": {
                    "tlp": "white"
                },
                "spec_version": "2.1"
            },
            {
                "type": "marking-definition",
                "definition_type": "tlp",
                "name": "TLP:GREEN",
                "created": "2017-01-20T00:00:00.000Z",
                "id": "marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da",
                "definition": {
                    "tlp": "green"
                },
                "spec_version": "2.1"
            },
            {
                "type": "marking-definition",
                "definition_type": "tlp",
                "name": "TLP:RED",
                "created": "2017-01-20T00:00:00.000Z",
                "id": "marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed",
                "definition": {
                    "tlp": "red"
                },
                "spec_version": "2.1"
            },
            {
                "labels": [
                    "Malicious",
                    "Malicious Host",
                    "Targeted Attack",
                    "Threat Rating: Very High"
                ],
                "confidence": 85,
                "type": "indicator",
                "valid_from": "2022-11-17T17:22:31.000Z",
                "modified": "2024-12-10T20:48:24.000Z",
                "description": "",
                "name": "verybadguy.com",
                "pattern_type": "stix",
                "created": "2022-11-17T17:22:31.000Z",
                "id": "indicator--4a86b8a3-d764-58ed-a119-ba3c7ad52d2d",
                "x_threat_rating": 5,
                "lang": "en",
                "spec_version": "2.1",
                "indicator_types": [
                    "malicious-activity"
                ],
                "revoked": true,
                "pattern": "[domain-name:value = 'verybadguy.com']"
            },
            {
                "confidence": 0,
                "type": "indicator",
                "valid_from": "2024-02-15T19:48:05.000Z",
                "modified": "2024-11-06T15:32:19.000Z",
                "description": "",
                "name": "telecomcredits.us",
                "pattern_type": "stix",
                "created": "2024-02-15T19:48:05.000Z",
                "id": "indicator--474a2194-788f-5f63-b776-330de8dcc3e1",
                "x_threat_rating": 0,
                "lang": "en",
                "spec_version": "2.1",
                "indicator_types": [
                    "malicious-activity"
                ],
                "revoked": true,
                "pattern": "[domain-name:value = 'telecomcredits.us']"
            },
            {
                "labels": [
                    "Threat Rating: Low"
                ],
                "confidence": 0,
                "type": "indicator",
                "valid_from": "2022-11-17T17:22:31.000Z",
                "modified": "2024-11-06T13:29:54.000Z",
                "description": "",
                "name": "10.10.1.16/32",
                "pattern_type": "stix",
                "created": "2022-11-17T17:22:31.000Z",
                "id": "indicator--2e0a1128-d55c-53cf-85ad-53fe4cfbcd43",
                "x_threat_rating": 2,
                "lang": "en",
                "spec_version": "2.1",
                "indicator_types": [
                    "malicious-activity"
                ],
                "pattern": "[ipv4-addr:value = '10.10.1.16/32']"
            },
            {
                "confidence": 0,
                "type": "indicator",
                "valid_from": "2024-09-06T15:45:27.000Z",
                "modified": "2024-09-29T06:35:28.000Z",
                "description": "",
                "name": "13.248.213.45",
                "pattern_type": "stix",
                "created": "2024-09-06T15:45:27.000Z",
                "id": "indicator--8d41cc1e-8435-5dc3-a5f8-5da2b7608ce4",
                "x_threat_rating": 0,
                "lang": "en",
                "spec_version": "2.1",
                "indicator_types": [
                    "malicious-activity"
                ],
                "pattern": "[ipv4-addr:value = '13.248.213.45']"
            },
            {
                "confidence": 0,
                "type": "indicator",
                "valid_from": "2024-09-06T15:45:28.000Z",
                "modified": "2024-09-29T06:35:28.000Z",
                "description": "",
                "name": "76.223.67.189",
                "pattern_type": "stix",
                "created": "2024-09-06T15:45:28.000Z",
                "id": "indicator--5e0830dd-1d73-5a7a-b173-b1a2f53f69c5",
                "x_threat_rating": 0,
                "lang": "en",
                "spec_version": "2.1",
                "indicator_types": [
                    "malicious-activity"
                ],
                "pattern": "[ipv4-addr:value = '76.223.67.189']"
            }
        ]
    }

**GET /taxii2**

Request

.. code::

    curl --location --request GET '{baseUrl}{taxiiServicePath}/taxii2' \
    --header 'Accept: application/taxii+json;version=2.1' \
    --header 'Authorization: Basic {credentials}'

JSON Response (App Version 1.0 and 2.0)

.. code:: json

    {
        "title": "ThreatConnect TAXII 2.1 Server",
        "contact": "support@threatconnect.com",
        "api_roots": [
            "https://companyabc.threatconnect.com/api/services/taxii/v1/tc_taxii"
        ],
        "description": "This TAXII 2.1 server contains Indicators of Compromise from ThreatConnect.",
        "default": "https://companyabc.threatconnect.com/api/services/taxii/v1/tc_taxii"
    }