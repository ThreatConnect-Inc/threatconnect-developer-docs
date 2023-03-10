Filter Results with TQL
-----------------------

Overview
^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to filter results based a query written in `ThreatConnect Query Language (TQL) <https://knowledge.threatconnect.com/docs/threatconnect-query-language-tql>`_. To use the ``tql`` query parameter, append ``?tql={tqlQuery}`` to the end of the request URL.

Retrieve a List of TQL Parameters for an Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to an object's endpoint:

.. code::

    OPTIONS /v3/{objectType}/tql

For example, the following format will retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/tags`` endpoint:

.. code::

    OPTIONS /v3/tags/tql

JSON Response

.. code:: json

    {
        "data": [
            {
                "keyword": "associatedCase",
                "name": "associatedCase",
                "type": "Integer"
            },
            {
                "keyword": "associatedGroup",
                "name": "associatedGroup",
                "type": "Integer"
            },
            {
                "keyword": "associatedIndicator",
                "name": "associatedIndicator",
                "type": "Integer"
            },
            {
                "keyword": "associatedVictim",
                "name": "associatedVictim",
                "type": "Integer"
            },
            {
                "keyword": "caseId",
                "name": "Case ID",
                "type": "Integer",
                "description": "The ID of the case the tag is applied to"
            },
            {
                "keyword": "description",
                "name": "Description",
                "type": "String",
                "description": "The description of the tag"
            },
            {
                "keyword": "hasCase",
                "name": "Associated Case",
                "type": "Integer",
                "description": "A nested query for association to other cases"
            },
            {
                "keyword": "hasGroup",
                "name": "Associated Group",
                "type": "Integer",
                "description": "A nested query for association to other groups"
            },
            {
                "keyword": "hasIndicator",
                "name": "Associated Indicator",
                "type": "Integer",
                "description": "A nested query for association to other indicators"
            },
            {
                "keyword": "hasVictim",
                "name": "Associated Victim",
                "type": "Integer",
                "description": "A nested query for association to other victims"
            },
            {
                "keyword": "id",
                "name": "ID",
                "type": "Integer",
                "description": "The ID of the tag"
            },
            {
                "keyword": "lastUsed",
                "name": "LastUsed",
                "type": "Date",
                "description": "The date this tag was last used"
            },
            {
                "keyword": "name",
                "name": "Name",
                "type": "String",
                "description": "The name of the tag (case sensitive)"
            },
            {
                "keyword": "owner",
                "name": "Owner ID",
                "type": "Integer",
                "description": "The owner ID of the tag"
            },
            {
                "keyword": "ownerName",
                "name": "Owner Name",
                "type": "String",
                "description": "The owner name of the tag"
            },
            {
                "keyword": "summary",
                "name": "Summary",
                "type": "StringLower",
                "description": "The name of the tag (case insensitive)"
            }
        ],
        "count": 16,
        "status": "Success"
    }

Example Requests
^^^^^^^^^^^^^^^^

This section provides example requests demonstrating sample use cases for the ``tql`` query parameter.

.. note::
    Depending on the tool you are using to interact with the ThreatConnect API, it may be necessary to encode the request URL manually if it includes query parameters. For example, some tools may accept ``/v3/indicators?tql=typeName in ("Address", "Host")`` as a valid request URL and encode it automatically, while others may require you to encode the request URL manually. If you send a request with query parameters and a **401 Unauthorized** error is returned, verify whether the request URL is encoded properly for the API tool you are using.

Filter Indicators by Type
=========================

The following request will retrieve data for all Address and Host Indicators:

Request (Decoded URL)

.. code::

    GET /v3/indicators?tql=typeName in ("Address", "Host")

Request (Encoded URL)

.. code::

    GET /v3/indicators?tql=typeName%20in%20(%22Address%22%2C%20%22Host%22)

Filter Groups by Type and Applied Tags
======================================

The following request will retrieve data for all Adversary Groups with the **Hacker** Tag applied to them:

Request (Decoded URL)

.. code::

    GET /v3/groups?tql=typeName in ("Adversary") and tag in ("hacker")

Request (Encoded URL)

.. code::

    GET /v3/groups?tql=typeName%20in%20(%22Adversary%22)%20and%20tag%20in%20(%22hacker%22)

Filter Cases by Case Open Time
==============================

The following request will retrieve data for all Cases with a **Case Open Time** set between February 1 and 28, 2023, inclusive:

Request (Decoded URL)

.. code::

    GET /v3/cases?tql=caseOpenTime GEQ "2023-02-01" and caseOpenTime LEQ "2023-02-28"

Request (Encoded URL)

.. code::

    GET /v3/cases?tql=caseOpenTime%20GEQ%20%222023-02-01%22%20and%20caseOpenTime%20LEQ%20%222023-02-28%22

Combine the "tql" and "fields" Query Parameters
===============================================

You can combine the ``tql`` and ``fields`` query parameters in a single API request, allowing you to filter results using ThreatConnect Query Language (TQL) and `include additional fields in the API response <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

For example, the following request will retrieve data for all Indicators with a Threat Rating greater than or equal to 4 and include data for Tags and Attributes added to each Indicator in the API response.

Request (Decoded URL)

.. code::

    GET /v3/indicators?tql=rating >= 4&fields=tags&fields=attributes

Request (Encoded URL)

.. code::

  GET /v3/indicators?tql=rating%20%3E%3D%204&fields=tags&fields=attributes