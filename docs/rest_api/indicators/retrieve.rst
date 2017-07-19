Retrieve Indicators
-------------------

.. include:: indicators/filters.rst

Retrieve All Indicator Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve Indicators of all types, use the following query:

.. code::

    GET /v2/indicators

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "indicator": [
          {
            "id": "54321",
            "ownerName": "Example Organization",
            "type": "URL",
            "dateAdded": "2017-07-13T17:50:17",
            "lastModified": "2017-07-19T17:35:31Z",
            "threatAssessRating": 3,
            "threatAssessConfidence": 50,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/url.xhtml?orgid=54321&owner=Research+Labs",
            "summary": "http://example.com/login.php"
          },
          {
            "id": "54322",
            "ownerName": "Example Organization",
            "type": "EmailAddress",
            "dateAdded": "2017-07-13T17:51:17",
            "lastModified": "2017-07-19T17:35:29Z",
            "threatAssessRating": 4,
            "threatAssessConfidence": 75,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=bad%40gmail.com&owner=Research+Labs",
            "summary": "bad@gmail.com"
          }
        ]
      }
    }

Retrieve Multiple Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve multiple indicators of a certain type, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}

The ``{indicatorType}`` can be any one of the available Indicator types below or any of the custom Indicator types available in your instance of threatconnect:

- ``addresses``
- ``emailAddresses``
- ``files``
- ``hosts``
- ``urls``

For example, the query below will retrieve a list of all Email Address Indicators in the default owner:

.. code::

    GET /v2/indicators/emailAddresses

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "emailAddress": [
          {
            "id": "54321",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T17:50:17",
            "lastModified": "2017-07-19T17:53:50Z",
            "threatAssessRating": 3,
            "threatAssessConfidence": 50,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=phish%40example.com&owner=Research+Labs",
            "address": "phish@example.com"
          },
          {
            "id": "54322",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T17:51:17",
            "lastModified": "2017-07-19T17:53:49Z",
            "threatAssessRating": 3,
            "threatAssessConfidence": 50,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=bad%40gmail.com&owner=Research+Labs",
            "address": "bad@gmail.com"
          }
        ]
      }
    }

Retrieve a Single Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a single Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}

For example, if you wanted to retrieve the Email Address ``bad@example.com``, you would use the following query:

.. code::

    GET /v2/indicators/emailAddresses/bad@example.com

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "emailAddress": {
          "id": "54321",
          "owner": {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-03-29T12:53:49Z",
          "threatAssessRating": 1.67,
          "threatAssessConfidence": 18.33,
          "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=bad%40example.com&owner=Example+Organization",
          "address": "bad@example.com"
        }
      }
    }

Retrieve Indicator Metadata
---------------------------

Retrieve Indicator Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve an Indicator's Attributes, use the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/attributes

For example, if you wanted to retrieve the attributes on the Email Address ``bad@example.com``, you would use the following query:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/attributes

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

    GET /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}/securityLabels

Here is an example query:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/attributes/54321/securityLabels

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

Retrieve Indicator Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve the Security Labels for an Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/securityLabels

For example, the query below will retrieve all Security Labels for the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/securityLabels

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

Retrieve Indicator Tags
^^^^^^^^^^^^^^^^^^^^^^^

To retrieve the Tags for an Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/tags

For example, the query below will retrieve all Tags for the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/tags

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

Retrieve Indicator Associations
-------------------------------

Retrieve Associated Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Groups associated with a given Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/groups

For example, the query below will retrieve all of the Groups associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/groups

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

    GET /v2/indicators/{indicatorType}/{indicator}/groups/{associatedGroupType}

For example, we could use the following query to find all Incidents associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/groups/incidents

We can also drill down even further by adding the ID of an associated Group to the end of the query like:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/groups/incidents/54321

Where ``54321`` is the ID of an Incident associated with the Email Address ``bad@example.com``.

Retrieve Associated Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Indicators associated with a given Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/indicators

For example, the query below will retrieve all of the Indicators associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/indicators

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

    GET /v2/indicators/{indicatorType}/{indicator}/indicators/{associatedIndicatorType}

For example, we could use the following query to find all Address Indicators associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/indicators/addresses

We can also drill down even further by adding the ID of an associated Indicator to the end of the query like:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/indicators/addresses/54321

Where ``54321`` is the ID of an Address associated with the Email Address ``bad@example.com``.

Retrieve Associated Victim Assets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victim Assets associated with a given Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/victimAssets

For example, the query below will retrieve all of the Victim Assets associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/victimAssets

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

    GET /v2/indicators/{indicatorType}/{indicator}/victimAssets/{associatedVictimAssetType}

For example, we could use the following query to find all Victim Assets that are Email Addresses which are associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/victimAssets/emailAddresses

We can also drill down even further by adding the ID of an associated Victim Asset to the end of the query like:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/victimAssets/emailAddresses/54321

Where ``54321`` is the ID of a Victim Asset associated with the Email Address ``bad@example.com``.

Retrieve Associated Victims
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victims associated with a given Indicator, use a query in the following format:

.. code::

    GET /v2/indicators/{indicatorType}/{indicator}/victims

For example, the query below will retrieve all of the Victims associated with the Email Address ``bad@example.com``:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/victims

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

We can also drill down even further by adding the ID of an associated Victim to the end of the query like:

.. code::

    GET /v2/indicators/emailAddresses/bad@exaxmple.com/victims/54321

Where ``54321`` is the ID of a Victim associated with the Email Address ``bad@example.com``.
