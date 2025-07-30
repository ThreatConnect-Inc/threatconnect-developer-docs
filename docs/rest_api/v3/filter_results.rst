Filter Results With TQL
-----------------------

Overview
^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to filter results based a query written in `ThreatConnect Query Language (TQL) <https://knowledge.threatconnect.com/docs/threatconnect-query-language-tql>`_. To use the ``tql`` query parameter, append ``?tql={tqlQuery}`` to the end of the request URL.

.. note::
    If you experience issues with TQL queries timing out while using the v3 API, review the **Custom TQL Timeout** setting for your API user account and ask your System Administrator to review the TQL query timeout system setting for your ThreatConnect instance.

Escape Character Sequences
^^^^^^^^^^^^^^^^^^^^^^^^^^

When constructing TQL queries in API requests, certain characters must be escaped with a backslash character (``\``) if they are used within a string. See the following table for a list of these characters and their corresponding escape sequence.

.. list-table::
   :widths: 33 33 34
   :header-rows: 1

   * - Name
     - Character
     - Escape Sequence
   * - Single quote
     - ``'``
     - ``\'``
   * - Double quote
     - ``"``
     - ``\"``
   * - Backtick
     - \`
     - ``\```
   * - Backslash
     - ``\``
     - ``\\``

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
                "keyword": "financialRisk",
                "name": "Financial Risk",
                "type": "String",
                "description": "The RQ-derived financial risk category of an ATT&CK-based tag as it relates to the user's organization"
            },
            {
                "keyword": "financialRiskScore",
                "name": "Financial Risk Score",
                "type": "Integer",
                "description": "The RQ-derived financial risk score of an ATT&CK-based tag as it relates to the user's organization"
            },
            {
                "keyword": "financialRiskValue",
                "name": "Financial Risk Value",
                "type": "Integer",
                "description": "The RQ-derived financial risk currency value of an ATT&CK-based tag as it relates to the user's organization"
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
                "keyword": "securityCoverage",
                "name": "Security Coverage",
                "type": "Enum",
                "description": "The security coverage level of an ATT&CK-based tag as it relates to the user's organization"
            },
            {
                "keyword": "summary",
                "name": "Summary",
                "type": "StringLower",
                "description": "The name of the tag (case insensitive)"
            },
            {
                "keyword": "techniqueId",
                "name": "Technique ID",
                "type": "String",
                "description": "The standard ID for specific MITRE ATT&CK techniques and subtechniques"
            }
        ],
        "count": 21,
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

Filter Enriched Indicators
==========================

You can `enrich Indicators <https://docs.threatconnect.com/en/latest/rest_api/v3/indicator_enrichment/indicator_enrichment.html>`_ with several built-in enrichment services in ThreatConnect. Enriched Indicators may then be filtered by data points available for a given enrichment service.

For example, the following request will retrieve data for all Indicators enriched with the AbuseIPDB enrichment service that have a confidence score of 50 or greater in AbuseIPDB:

Request (Decoded URL)

.. code::

    GET /v3/indicators?tql=abuseIpdbConfidenceScore>=50

Request (Encoded URL)

.. code::

    GET /v3/indicators?tql=abuseIpdbConfidenceScore%3E%3D50

For a complete list of enrichment-related TQL parameters, send an ``OPTIONS`` request to the ``/v3/indicators/tql`` endpoint.

Filter Indicators by ThreatAssess Score
=======================================

The following request will retrieve data for all Indicators whose ThreatAssess score was updated sometime today and is greater than or equal to 500:

Request (Decoded URL)

.. code::

    GET /v3/indicators?tql=threatAssessLastUpdated>"TODAY()" and threatAssessScore>=500

Request (Encoded URL)

.. code::

    GET /v3/indicators?tql=threatAssessLastUpdated%3E%22TODAY()%22%20and%20threatAssessScore%3E%3D500

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

Filter ATT&CK Tags by Technique ID
==================================

The following request will retrieve data for all ATT&CK® Tags whose technique ID starts with **T1001**:

Request (Decoded URL)

.. code::

    GET /v3/tags?tql=techniqueId startswith "T1001"

Request (Encoded URL)

.. code::

    GET /v3/tags?tql=techniqueId%20startswith%20%22T1001%22

Filter ATT&CK Tags by Associated Groups
=======================================

The following request will retrieve data for all ATT&CK Tags applied to the Group whose ID is 11:

Request (Decoded URL)

.. code::

    GET /v3/tags?tql=techniqueId is not null and associatedGroup EQ 11

Request (Encoded URL)

.. code::

    GET /v3/tags?tql=techniqueId%20is%20not%20null%20and%20associatedGroup%20EQ%2011

Filter Objects by Association Method
====================================

As of ThreatConnect version 7.1, you can use the following TQL parameters when working with the ``/v3/groups`` and ``/v3/indicators`` endpoints to filter results based on the method used to create a Group or Indicator association:

- ``associatedGroupSource``: Use this parameter to filter results based on the method used to create an association to a Group.
- ``associatedIndicatorSource``: Use this parameter to filter results based on the method used to create an association to an Indicator.

If you use one of these parameters in a request, you must assign it one of the following values:

- ``UNKNOWN``: The association was created during a structured or unstructured Indicator import.
- ``MANUAL``: The association was created from an object's Details screen, including the Associations tab, Behavior tab (for File Indicators only), and Sharing tab (for all Group types except Task).
- ``API``: The association was created using the v2, v3, or Batch API.
- ``TQL``: The association was created via a TQL query.
- ``DNS``: The association was created via the DNS resolution tracking feature (for Address and Host Indicators only).
- ``EMAIL``: The association was created during the ingestion of an email.

For example, the following request will retrieve data for all Groups with at least one Indicator associated to them via the v2, v3, or Batch API:

Request (Decoded URL)

.. code::
    
    GET v3/groups?tql=associatedIndicatorSource="API"

Request (Encoded URL)

.. code::

    GET /v3/groups?tql=associatedIndicatorSource%3D%22API%22

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

Retrieve Association Attributes Added to a Specific Group
=========================================================

The following request will retrieve data for association Attributes that belong to two Groups: one whose ID is 10 and another whose ID is 15. The response will include the ``groupId`` field to indicate which Attribute(s) belong to which Group.

Request (Decoded URL)

.. code::

    GET /v3/groupAttributes?fields=groupId&tql=hasGroup(id in (10,15)) AND associable=true

Request (Encoded URL)

.. code::

    GET /v3/groupAttributes?fields=groupId&tql=hasGroup(id%20in%20(10%2C15))%20AND%20associable%3Dtrue

----

*MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation.*