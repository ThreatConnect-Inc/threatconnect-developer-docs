Retrieve Tags
-------------

Tag descriptions can be viewed using the following request:

.. code::

   GET /v2/tags?detailed=true


.. include:: filters.rst

Retrieve All Tags
^^^^^^^^^^^^^^^^^

To retrieve all Tags, use the following query:

.. code::

    GET /v2/tags

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "tag": [
          {
            "name": "Nation State",
            "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=12&owner=Example+Organization"
          },
          {
            "name": "Europe",
            "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=17&owner=Example+Organization"
          }
        ]
      }
    }

.. note::
  ATT&CK® Tags are not included in response returned for a ``GET /v2/tags`` request.

Retrieve a Single Tag
^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Tag, use a query in the following format:

.. code::

    GET /v2/tags/{tagName}

For example, the following query will return information about the ``Nation State`` tag:

.. code::

    GET /v2/tags/Nation%20State

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "tag": {
          "name": "Nation State",
          "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=12&owner=Example+Organization"
        }
      }
    }

.. attention::
  When retrieving a specific ATT&CK Tag, do not include the corresponding technique/sub-technique ID in the Tag's name. For example, to retrieve information about the **T1566 - Phishing** ATT&CK Tag, use **Phishing** as the Tag name in the query.

Retrieve Tag Associations
-------------------------

.. attention::
  You cannot retrieve Indicators, Groups, or Victims associated to an ATT&CK Tag via the ``/v2/tags`` endpoint.

Group to Tag Associations
^^^^^^^^^^^^^^^^^^^^^^^^^

To view Groups associated with a given Tag, use a query in the following format:

.. code::

    GET /v2/tags/{tagName}/groups

For example, the query below will retrieve all of the Groups associated with the ``Nation State`` Tag:

.. code::

    GET /v2/tags/Nation%20State/groups

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "group": [
          {
            "id": "54321",
            "name": "IOCs_report_2017.doc",
            "type": "Document",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T17:50:17",
            "lastModified": "2017-07-13T17:51:17",
            "webLink": "https://app.threatconnect.com/#/details/groups/54321/overview"
          }
        ]
      }
    }

You can also retrieve associated Groups of a given type using the following format:

.. code::

    GET /v2/tags/{tagName}/groups/{associatedGroupType}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, the following query will return all Incidents associated with the ``Nation State`` Tag:

.. code::

    GET /v2/tags/Nation%20State/groups/incidents

To retrieve a specific Incident associated with the ``Nation State`` Tag, include the ID of that Incident in the request URL:

.. code::

    GET /v2/tags/Nation%20State/groups/incidents/54321

Indicator to Tag Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Indicators associated with a given Tag, use a query in the following format:

.. code::

    GET /v2/tags/{tagName}/indicators

For example, the query below will retrieve all of the Indicators associated with the ``Nation State`` Tag:

.. code::

    GET /v2/tags/Nation%20State/indicators

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
            "dateAdded": "2017-07-13T17:50:17",
            "lastModified": "2017-07-20T15:43:09Z",
            "rating": 3.00,
            "confidence": 75,
            "threatAssessRating": 3.0,
            "threatAssessConfidence": 75.0,
            "threatAssessScore": 507,
            "calScore": 181,
            "calIndicatorStatus": 2,
            "webLink": "https://app.threatconnect.com/#/details/indicators/54321/overview&owner=Example+Organization",
            "summary": "0.0.0.0"
          }
        ]
      }
    }

You can also retrieve associated Indicators of a given type using the following format:

.. code::

    GET /v2/tags/{tagName}/indicators/{associatedIndicatorType}

For example, the following query will return all Address Indicators associated with the ``Nation State`` Tag:

.. code::

    GET /v2/tags/Nation%20State/indicators/addresses

Victim to Tag Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victims associated with a given Tag, use a query in the following format:

.. code::

    GET /v2/tags/{tagName}/victims

For example, the query below will return all of the Victims associated with the ``Nation State`` Tag:

.. code::

    GET /v2/tags/Nation%20State/victims

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
            "suborg": "",
            "workLocation": "Washington D.C.",
            "nationality": "",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=54321"
          }
        ]
      }
    }

To retrieve a specific Victim associated with the ``Nation State`` Tag, include the ID of that Victim in the request URL:

.. code::

    GET /v2/tags/Nation%20State/victims/54321