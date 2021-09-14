Retrieve Groups
---------------

.. include:: filters.rst

Retrieve All Groups
^^^^^^^^^^^^^^^^^^^

To retrieve Groups of all types, use the following query:

.. code::

    GET /v2/groups

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "group": [
          {
            "id": 12345,
            "name": "Likely Nation State Intrusion on Remote Server",
            "type": "Document",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T16:43:19Z",
            "webLink": "https://app.threatconnect.com/auth/document/document.xhtml?document=12345"
          },
          {
            "id": 12346,
            "name": "Investment Status",
            "type": "Email",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T19:28:10Z",
            "webLink": "https://app.threatconnect.com/auth/email/email.xhtml?email=12346"
          }
        ]
      }
    }

Retrieve Multiple Groups
^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve multiple Groups of a certain type, use a query in the following format:

.. code::

    GET /v2/groups/{groupType}

The ``{groupType}`` can be any one of the available Group types:

- ``adversaries``
- ``attackPatterns``
- ``campaigns``
- ``coursesOfAction``
- ``documents``
- ``emails``
- ``events``
- ``incidents``
- ``intrusionSets``
- ``malware``
- ``reports``
- ``signatures``
- ``tactics``
- ``threats``
- ``tools``
- ``vulnerabilities``
  
For example, the query below will retrieve a list of all Incidents in the default owner:

.. code::

    GET /v2/groups/incidents

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "incident": [
          {
            "id": "54321",
            "name": "Test Incident",
            "ownerName": "Wanna Cry Hits Stoic Department",
            "dateAdded": "2017-07-13T17:50:17",
            "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=54321",
            "eventDate": "2017-03-21T00:00:00Z"
          },
          {
            "id": "54322",
            "name": "PoS Malware Detected at Denver Location",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T17:51:17",
            "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=54322",
            "eventDate": "2017-06-27T00:00:00Z"
          }
        ]
      }
    }

Retrieve a Single Group
^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a single Group, use a query in the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}

For example, if you want to retrieve the Threat with the ID 12345, you would use the following query:

.. code::

    GET /v2/groups/threats/12345

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "threat": {
          "id": 12345,
          "name": "Bad Dude",
          "owner": {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-05-13T18:40:22Z",
          "webLink": "https://app.threatconnect.com/auth/threat/threat.xhtml?threat=12345"
        }
      }
    }

Retrieve Document or Signature Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To download the contents of a Document or Signature in ThreatConnect, you can use a query in the following format:

.. code::

    GET /v2/groups/documents/{documentId}/download
    GET /v2/groups/signatures/{signatureId}/download

For example, the query below downloads the contents of a Document with ID 12345:

.. code::

    GET /v2/groups/documents/12345/download

JSON Response:

.. code::

    This is the content of the document!

The contents of a Document will be returned as ``Content-Type: application/octet-stream``. The contents of a Signature will be returned as ``Content-Type: text/plain``.

Retrieve Group Metadata
-----------------------

Retrieve Group Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a Group's Attributes, use the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/attributes

For example, if you want to retrieve the Attributes on the Threat with the ID 12345, you would use the following query:

.. code::

    GET /v2/groups/threats/12345/attributes

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "attribute": [
          {
            "id": "54321",
            "type": "Description",
            "dateAdded": "2016-07-13T17:50:17",
            "lastModified": "2017-05-02T18:40:22Z",
            "displayed": true,
            "value": "Description Example"
          },
          {
            "id": "54322",
            "type": "Source",
            "dateAdded": "2016-07-13T17:51:17",
            "lastModified": "2017-05-02T18:40:22Z",
            "displayed": true,
            "value": "Source Example"
          }
        ]
      }
    }

To retrieve the Security Labels that are on an attribute, use the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/attributes/{attributeId}/securityLabels

Here is an example query:

.. code::

    GET /v2/groups/threats/12345/attributes/54321/securityLabels

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "securityLabel": [
          {
            "name": "TLP Amber",
            "description": "TLP Amber information requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved.",
            "dateAdded": "2017-07-13T17:50:17"
          }
        ]
      }
    }

Retrieve Group Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve the Security Labels for a Group, use a query in the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/securityLabels

For example, the query below will retrieve all Security Labels for the Threat with ID 12345:

.. code::

    GET /v2/groups/threats/12345/securityLabels

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "securityLabel": [
          {
            "name": "TLP Amber",
            "description": "TLP Amber information requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved.",
            "dateAdded": "2017-07-13T17:50:17"
          }
        ]
      }
    }

Retrieve Group Tags
^^^^^^^^^^^^^^^^^^^

To retrieve the Tags for a Group, use a query in the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/tags

For example, the query below will retrieve all Tags for the Threat with ID 12345:

.. code::

    GET /v2/groups/threats/12345/tags

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "tag": [
          {
            "name": "Nation State",
            "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Nation+State&owner=Common+Community"
          }
        ]
      }
    }

Retrieve Adversary Assets
^^^^^^^^^^^^^^^^^^^^^^^^^

Adversary Assets are accounts or web resources that Adversaries leverage in support of their operations. They can be retrieved from a given Adversary using the following query format:

.. code::

    GET /v2/groups/adversaries/{adversaryId}/adversaryAssets

For example, the query below will return the Adversary Assets for the Adversary with ID 12345:

.. code::

    GET /v2/groups/adversaries/12345/adversaryAssets

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "bucketAsset": [
          {
            "id": "54321",
            "name": "Real Bad Guy",
            "type": "Handle",
            "webLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=1157242"
          },
          {
            "id": "54322",
            "name": "http://facebook.com/therealbadguy",
            "type": "URL",
            "webLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=1157242"
          }
        ]
      }
    }

To retrieve Adversary Assets of a particular type, use a query in the following format:

.. code::

    GET /v2/groups/adversaries/{adversaryId}/adversaryAssets/{assetType}

``{assetType}`` can be replaced with the following Asset types:

* handles
* phoneNumbers
* urls

To get details about a specific Adversary Asset, use a query in the following format:

.. code::

    GET /v2/groups/adversaries/{adversaryId}/adversaryAssets/{assetType}/{assetId}

Retrieve Incident Status
^^^^^^^^^^^^^^^^^^^^^^^^

Incidents in ThreatConnect have a status that can be set and retrieved via API. Adding the ‘includeAdditional’ parameter when requesting data about an Incident will return data which includes the Incident’s status. Use a query in the following format to find an Incident's status:

.. code::

    GET /v2/groups/incidents/{incidentId}?includeAdditional=true

For example, the query below will return information about the Incident with ID 12345 as well as the Incident’s status.

.. code::

    GET /v2/groups/incidents/12345?includeAdditional=true

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "incident": {
          "id": 12345,
          "name": "Test Incident",
          "owner": {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T18:15:49Z",
          "webLink": "https://app.threatconnect.com/tc/auth/incident/incident.xhtml?incident=12345",
          "eventDate": "2017-06-21T18:15:49Z",
          "status": "Open"
        }
      }
    }

Note that using the 'includes=additional' parameter will also work. Likewise, 'includes=tags', 'includes=attributes', and 'includes=labels' are permitted for Groups.

Retrieve Group Associations
---------------------------

Group to Group Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Groups associated with a given Group, use a query in the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/groups

For example, the query below will retrieve all of the Groups associated with a Threat with the ID 12345:

.. code::

    GET /v2/groups/threats/12345/groups

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "group": [
          {
            "id": "54321",
            "name": "New Incident",
            "type": "Incident",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T17:50:17",
            "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=54321"
          }
        ]
      }
    }

You can also find associated Groups of a given type using the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/groups/{associatedGroupType}

Replace ``{associatedGroupType}`` with one of the following Group types:

- ``adversaries``
- ``attackPatterns``
- ``campaigns``
- ``coursesOfAction``
- ``documents``
- ``emails``
- ``events``
- ``incidents``
- ``intrusionSets``
- ``malware``
- ``reports``
- ``signatures``
- ``tactics``
- ``threats``
- ``tools``
- ``vulnerabilities``

For example, you could use the following query to find all Incidents associated with the Threat with ID 12345:

.. code::

    GET /v2/groups/threats/12345/groups/incidents

You can also delve further by adding the ID of an associated Group to the end of the query:

.. code::

    GET /v2/groups/threats/12345/groups/incidents/54321

Where ``54321`` is the ID of an incident associated with Threat 12345.

Indicator to Group Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Indicators associated with a given Group, use a query in the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/indicators

For example, the query below will retrieve all of the Indicators associated with a Threat with the ID 12345:

.. code::

    GET /v2/groups/threats/12345/indicators

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "indicator": [
          {
            "id": "54321",
            "ownerName": "Example Organization",
            "type": "Address",
            "dateAdded": "2016-07-13T17:50:17",
            "lastModified": "2017-05-01T21:32:54Z",
            "rating": 3.0,
            "confidence": 55,
            "threatAssessRating": 3.0,
            "threatAssessConfidence": 55.0,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=0.0.0.0&owner=Example+Organization",
            "summary": "0.0.0.0"
          }
        ]
      }
    }

You can also find associated Indicators of a given type using the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/indicators/{associatedIndicatorType}

For example, you could use the following query to find all Address Indicators associated with the Threat with ID 12345:

.. code::

    GET /v2/groups/threats/12345/indicators/addresses

Victim Asset to Group Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victim Assets associated with a given Group, use a query in the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/victimAssets

For example, the query below will retrieve all of the Victim Assets associated with a Threat with the ID 12345:

.. code::

    GET /v2/groups/threats/12345/victimAssets

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "victimAsset": [
          {
            "id": "54321",
            "name": "bad@badguys.com",
            "type": "EmailAddress",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=123"
          },
          {
            "id": "54322",
            "name": "nobody@gmail.com",
            "type": "EmailAddress",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=123"
          }
        ]
      }
    }

You can also find associated Victim Assets of a given type using the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/victimAssets/{victimAssetType}

The available Victim Asset types are:

.. include:: ../_includes/victim_asset_types.rst

For example, you could use the following query to find all Victim Assets that are Email Addresses that are associated with the Threat with ID 12345:

.. code::

    GET /v2/groups/threats/12345/victimAssets/emailAddresses

You can delve further by adding the ID of an associated Victim Asset to the end of the query:

.. code::

    GET /v2/groups/threats/12345/victimAssets/emailAddresses/54321

Where ``54321`` is the ID of a Victim Asset associated with Threat 12345.

Victim to Group Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victims associated with a given Group, use a query in the following format:

.. code::

    GET /v2/groups/{groupType}/{groupId}/victims

For example, the query below will retrieve all of the Victims associated with a Threat with the ID 12345:

.. code::

    GET /v2/groups/threats/12345/victims

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "victim": [
          {
            "id": "54321",
            "name": "Bad Guy",
            "org": "Example Organization",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=54321"
          }
        ]
      }
    }

You can delve further by adding the ID of an associated Victim to the end of the query:

.. code::

    GET /v2/groups/threats/12345/victims/54321

Where ``54321`` is the ID of a Victim associated with Threat 12345.
