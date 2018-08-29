Retrieve Tags
-------------

Tag descriptions can be viewed using the following request:

.. code::

   GET /api/v2/tags?detailed=true


.. include:: filters.rst

Retrieve All Tags
^^^^^^^^^^^^^^^^^

To retrieve all tags, use the following query:

.. code::

    GET /v2/tags/

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "tag": [
          {
            "name": "Nation State",
            "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Nation+State&owner=Example+Organization"
          },
          {
            "name": "Europe",
            "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Europe&owner=Example+Organization"
          }
        ]
      }
    }

Retrieve a Single Tag
^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific tag, use a query in the following format:

Introduction here

.. code::

    GET /v2/tags/{tagName}

For example, the following query will return information about the ``Nation State`` tag:

.. code::

    GET /v2/tags/Nation State

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "tag": {
          "name": "Nation State",
          "webLink": "https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Nation+State&owner=Example+Organization"
        }
      }
    }

Retrieve Tag Associations
-------------------------

Group to Tag Associations
^^^^^^^^^^^^^^^^^^^^^^^^^

To view Groups associated with a given Tag, use a query in the following format:

.. code::

    GET /v2/tags/{tagName}/groups

For example, the query below will retrieve all of the Groups associated with the ``Nation State`` tag:

.. code::

    GET /v2/tags/Nation State/groups

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
            "webLink": "https://app.threatconnect.com/auth/document/document.xhtml?document=54321"
          }
        ]
      }
    }

You can also find associated Groups of a given type using the following format:

.. code::

    GET /v2/tags/{tagName}/groups/{associatedGroupType}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, we could use the following query to find all Incidents associated with the ``Nation State`` tag:

.. code::

    GET /v2/tags/Nation State/groups/incidents

We can also drill down even further by adding the ID of an associated Group to the end of the query such as:

.. code::

    GET /v2/tags/Nation State/groups/incidents/54321

Where ``54321`` is the ID of an Incident associated with the ``Nation State`` tag.

Indicator to Tag Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Indicators associated with a given Tag, use a query in the following format:

.. code::

    GET /v2/tags/{tagName}/indicators

For example, the query below will retrieve all of the Indicators associated with the ``Nation State`` tag:

.. code::

    GET /v2/tags/Nation State/indicators

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
            "threatAssessRating": 3,
            "threatAssessConfidence": 50,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=0.0.0.0&owner=Example+Organization",
            "summary": "0.0.0.0"
          }
        ]
      }
    }

You can also find associated Indicators of a given type using the following format:

.. code::

    GET /v2/tags/{tagName}/indicators/{associatedIndicatorType}

For example, we could use the following query to find all Address Indicators associated with the ``Nation State`` tag:

.. code::

    GET /v2/tags/Nation State/indicators/addresses

Victim to Tag Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victims associated with a given Tag, use a query in the following format:

.. code::

    GET /v2/tags/{tagName}/victims

For example, the query below will retrieve all of the Victims associated with the ``Nation State`` tag:

.. code::

    GET /v2/tags/Nation State/victims

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

    GET /v2/tags/Nation State/victims/54321

Where ``54321`` is the ID of a Victim associated with the ``Nation State`` tag.
