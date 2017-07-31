Retrieve Security Labels
------------------------

.. include:: security_labels/filters.rst

Retrieve All Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Security Labels, use the following query:

.. code::

    GET /v2/securityLabels/

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "securityLabel": [
          {
            "name": "TLP Amber",
            "description": "TLP Amber information requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved.",
            "dateAdded": "2017-07-13T17:50:17"
          },
          {
            "name": "TLP Green",
            "description": "TLP Green information is useful for the awareness of all participating organizations as well as with peers within the broader community or sector.",
            "dateAdded": "2017-07-13T17:50:17"
          }
        ]
      }
    }

Retrieve a Single Security Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Security Label, use a query in the following format:

.. code::

    GET /v2/securityLabels/{securityLabel}

For example, the following query will return information about the ``TLP Amber`` Security Label:

.. code::

    GET /v2/securityLabels/TLP Amber

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "securityLabel": {
          "name": "TLP Amber",
          "description": "TLP Amber information requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved.",
          "dateAdded": "2017-07-13T17:50:17"
        }
      }
    }

Retrieve Items Labeled with Security Labels
--------------------------------------------

Retrieve Labeled Groups
^^^^^^^^^^^^^^^^^^^^^^^

To view Groups labeled with a given Security Label, use a query in the following format:

.. code::

    GET /v2/securityLabels/{securityLabel}/groups

For example, the query below will retrieve all of the Groups labeled with the ``TLP Amber`` Security Label:

.. code::

    GET /v2/securityLabels/TLP Amber/groups

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

    GET /v2/securityLabels/{securityLabel}/groups/{associatedGroupType}

For example, we could use the following query to find all Incidents labeled with the ``TLP Amber`` Security Label:

.. code::

    GET /v2/securityLabels/TLP Amber/groups/incidents

We can also drill down even further by adding the ID of an associated Group to the end of the query such as:

.. code::

    GET /v2/securityLabels/TLP Amber/groups/incidents/54321

Where ``54321`` is the ID of an Incident labeled with the ``TLP Amber`` Security Label.

Retrieve Labeled Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Indicators labeled with a given Security Label, use a query in the following format:

.. code::

    GET /v2/securityLabels/{securityLabel}/indicators

For example, the query below will retrieve all of the Indicators labeled with the ``TLP Amber`` Security Label:

.. code::

    GET /v2/securityLabels/TLP Amber/indicators

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

    GET /v2/securityLabels/{securityLabel}/indicators/{associatedIndicatorType}

For example, we could use the following query to find all Address Indicators labeled with the ``TLP Amber`` Security Label:

.. code::

    GET /v2/securityLabels/TLP Amber/indicators/addresses

We can also drill down even further by adding an associated Indicator to the end of the query like:

.. code::

    GET /v2/securityLabels/TLP Amber/indicators/addresses/0.0.0.0

Retrieve Labeled Victims
^^^^^^^^^^^^^^^^^^^^^^^^

To view Victims labeled with a given Security Label, use a query in the following format:

.. code::

    GET /v2/securityLabels/{securityLabel}/victims

For example, the query below will retrieve all of the Victims labeled with the ``TLP Amber`` Security Label:

.. code::

    GET /v2/securityLabels/TLP Amber/victims

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

    GET /v2/securityLabels/TLP Amber/victims/54321

Where ``54321`` is the ID of a Victim labeled with the ``TLP Amber`` Security Label.
