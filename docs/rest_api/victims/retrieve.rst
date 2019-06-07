Retrieve Victims
----------------

.. include:: filters.rst

Retrieve Multiple Victims
^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve multiple Victims, use the following query:

.. code::

    GET /v2/victims/
  
JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "victim": [
          {
            "id": "54321",
            "name": "Burton Guster",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=54321"
          },
          {
            "id": "54322",
            "name": "West Coast HR Department",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=54322"
          }
        ]
      }
    }

Retrieve a Single Victim
^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a single Victim, use a query in the following format:

.. code::

    GET /v2/victims/{victimId}

For example, if you want to retrieve the Victim with ID 12345, you would use the following query:

.. code::

    GET /v2/victims/12345

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "victim": {
          "id": "12345",
          "name": "Burton Guster",
          "description": "He also goes by 'Magic Head', 'Lavender Gooms', 'Ghee Buttersnaps', and 'Control Alt Delete' (among others).",
          "org": "Psych",
          "suborg": "Super Sniffer Department",
          "workLocation": "Santa Barbara, California",
          "nationality": "American",
          "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=12345"
        }
      }
    }

Retrieve Victim Metadata
------------------------

Retrieve Victim Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a Victim's Attributes, use the following format:

.. code::

    GET /v2/victims/{victimId}/attributes

For example, if you want to retrieve the Attributes on the Victim with ID 12345, you would use the following query:

.. code::

    GET /v2/victims/12345/attributes

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

To retrieve the Security Labels that are on an Attribute, use the following format:

.. code::

    GET /v2/victims/{victimId}/attributes/{attributeId}/securityLabels

Here is an example query:

.. code::

    GET /v2/victims/12345/attributes/54321/securityLabels

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "securityLabel": [
          {
            "name": "TLP Amber",
            "description": "TLP Amber information requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the Organizations involved.",
            "dateAdded": "2017-07-13T17:50:17"
          }
        ]
      }
    }

Retrieve Victim Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve the Security Labels for a Victim, use a query in the following format:

.. code::

    GET /v2/victims/{victimId}/securityLabels

For example, the query below will retrieve all Security Labels for the Victim with ID 12345:

.. code::

    GET /v2/victims/12345/securityLabels

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "securityLabel": [
          {
            "name": "TLP Amber",
            "description": "TLP Amber information requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the Organizations involved.",
            "dateAdded": "2017-07-13T17:50:17"
          }
        ]
      }
    }

Retrieve Victim Tags
^^^^^^^^^^^^^^^^^^^^

To retrieve the Tags for a Victim, use a query in the following format:

.. code::

    GET /v2/victims/{victimId}/tags

For example, the query below will retrieve all Tags for the Victim with ID 12345:

.. code::

    GET /v2/victims/12345/tags

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

Retrieve Victim Associations
----------------------------

Group to Victim Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Groups associated with a given Victim, use a query in the following format:

.. code::

    GET /v2/victims/{victimId}/groups

For example, the query below will retrieve all of the Groups associated with the Victim with ID 12345:

.. code::

    GET /v2/victims/12345/groups

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "group": [
          {
            "id": "54321",
            "name": "Associated Incident",
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

    GET /v2/victims/{victimId}/groups/{associatedGroupType}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, you could use the following query to find all Incidents associated with the Victim with ID 12345:

.. code::

    GET /v2/victims/12345/groups/incidents

You can delve further by adding the ID of an associated Victim to the end of the query:

.. code::

    GET /v2/victims/12345/groups/incidents/54321

Where ``54321`` is the ID of an Incident associated with Victim 12345.

Indicator to Victim Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: It is not possible to associate an Indicator directly with a Victim in ThreatConnect. The query described in this section returns Indicators that share a Group association with the given Victim. In the image below, the Victim and Indicator are not directly associated, but are both associated with the same Group. Therefore, the Indicator would be returned when querying for Indicator associations from the Victim.

.. figure:: ../../_static/victim-to-indicator-associations.png
    :alt: Victim to Indicator Associations

To view Indicators sharing a Group association with the given Victim, use a query in the following format:

.. code::

    GET /v2/victims/{victimId}/indicators

For example, the query below will retrieve all of the Indicators associated with the Victim with ID 12345:

.. code::

    GET /v2/victims/12345/indicators

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

    GET /v2/victims/{victimId}/indicators/{associatedIndicatorType}

For example, you could use the following query to find all Address Indicators associated with the Victim with ID 12345:

.. code::

    GET /v2/victims/12345/indicators/addresses

Retrieve a Victim's Assets
^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victim Assets associated with a given Victim, use a query in the following format:

.. code::

    GET /v2/victims/{victimId}/victimAssets

For example, the query below will retrieve all of the Victim Assets associated with the Victim with ID 12345:

.. code::

    GET /v2/victims/12345/victimAssets

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

    GET /v2/victims/{victimId}/victimAssets/{victimAssetType}

The available Victim Asset types are:

.. include:: ../_includes/victim_asset_types.rst

For example, you could use the following query to find all Victim Assets that are Email Addresses which are associated with the Victim with ID 12345:

.. code::

    GET /v2/victims/12345/victimAssets/emailAddresses

You can delve further by adding the ID of an associated Victim Asset to the end of the query:

.. code::

    GET /v2/victims/12345/victimAssets/emailAddresses/54321

Where ``54321`` is the ID of a Victim Asset associated with Victim 12345.

Victim to Victim Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: It is not possible to associate one Victim directly with another in ThreatConnect. The query described in this section returns Victims which are associated with (or 'through') the same Group(s). In the image below, the two Victims are not directly associated, but are both associated with the same Group. Therefore, Victim B would be returned when querying for Victim associations from Victim A.

.. figure:: ../../_static/victim-to-victim-associations.png
    :alt: Victim to Victim Associations

To view Victims sharing a Group association with the given Victim, use a query in the following format:

.. code::

    GET /v2/victims/{victimId}/victims

For example, the query below will retrieve all of the Victims associated with the Victim with ID 12345:

.. code::

    GET /v2/victims/12345/victims

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

    GET /v2/victims/12345/victims/54321

Where ``54321`` is the ID of a Victim associated with Victim 12345.
