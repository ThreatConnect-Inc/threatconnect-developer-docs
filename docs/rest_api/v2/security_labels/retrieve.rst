Retrieve Security Labels
------------------------

.. include:: filters.rst

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
            "resultCount": 6,
            "securityLabel": [
                {
                    "name": "TLP:AMBER",
                    "description": "This security label is used for information that requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved. Information with this label can be shared with members of an organization and its clients.",
                    "dateAdded": "2016-08-31T00:00:00Z"
                },
                {
                    "name": "TLP:AMBER+STRICT",
                    "description": "This security label is used for information that requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved and the source of the information wants to restrict sharing of the information to only the organizations involved. Information with this label can only be shared with members of an organization.",
                    "dateAdded": "2022-08-31T00:00:00Z"
                },
                {
                    "name": "TLP:CLEAR",
                    "description": "This security label is used for information that carries minimal or no foreseeable risk of misuse, in accordance with applicable rules and procedures for public release.",
                    "dateAdded": "2022-08-31T00:00:00Z"
                },
                {
                    "name": "TLP:GREEN",
                    "description": "This security label is used for information that is useful for the awareness of all participating organizations as well as with peers within the broader community or sector.",
                    "dateAdded": "2016-08-31T00:00:00Z"
                },
                {
                    "name": "TLP:RED",
                    "description": "This security label is used for information that cannot be effectively acted upon by additional parties, and could lead to impacts on a party's privacy, reputation, or operations if misused.",
                    "dateAdded": "2016-08-31T00:00:00Z"
                },
                {
                    "name": "TLP:WHITE",
                    "description": "This security label is used for information that carries minimal or no foreseeable risk of misuse, in accordance with applicable rules and procedures for public release.",
                    "dateAdded": "2016-08-31T00:00:00Z"
                }
            ]
        }
    }

Retrieve a Single Security Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Security Label, use a query in the following format:

.. code::

    GET /v2/securityLabels/{securityLabel}

For example, the following query will return information about the ``TLP:AMBER`` Security Label:

.. code::

    GET /v2/securityLabels/TLP%3AAMBER

JSON Response:

.. code:: json

    {
        "status": "Success",
        "data": {
            "securityLabel": {
                "name": "TLP:AMBER",
                "description": "This security label is used for information that requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved. Information with this label can be shared with members of an organization and its clients.",
                "dateAdded": "2016-08-31T00:00:00Z"
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

For example, the query below will retrieve all of the Groups labeled with the ``TLP:AMBER`` Security Label:

.. code::

    GET /v2/securityLabels/TLP%3AAMBER/groups

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
            "lastModified": "2017-07-13T17:51:17"
            "webLink": "https://app.threatconnect.com/auth/document/document.xhtml?document=54321"
          }
        ]
      }
    }

You can also find associated Groups of a given type using the following format:

.. code::

    GET /v2/securityLabels/{securityLabel}/groups/{associatedGroupType}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, we could use the following query to find all Incidents labeled with the ``TLP:AMBER`` Security Label:

.. code::

    GET /v2/securityLabels/TLP%3AAMBER/groups/incidents

You can delve further by adding the ID of an associated Group to the end of the query:

.. code::

    GET /v2/securityLabels/TLP%3AAMBER/groups/incidents/54321

Where ``54321`` is the ID of an Incident labeled with the ``TLP:AMBER`` Security Label.

Retrieve Labeled Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Indicators labeled with a given Security Label, use a query in the following format:

.. code::

    GET /v2/securityLabels/{securityLabel}/indicators

For example, the query below will retrieve all of the Indicators labeled with the ``TLP:AMBER`` Security Label:

.. code::

    GET /v2/securityLabels/TLP%3AAMBER/indicators

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
            "threatAssessScore": 833,
            "calIndicatorStatus": 1,
            "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=0.0.0.0&owner=Example+Organization",
            "summary": "0.0.0.0"
          }
        ]
      }
    }

You can also find associated Indicators of a given type using the following format:

.. code::

    GET /v2/securityLabels/{securityLabel}/indicators/{associatedIndicatorType}

For example, you could use the following query to find all Address Indicators labeled with the ``TLP:AMBER`` Security Label:

.. code::

    GET /v2/securityLabels/TLP%3AAMBER/indicators/addresses

You can delve further by adding an associated Indicator to the end of the query like:

.. code::

    GET /v2/securityLabels/TLP%3AAMBER/indicators/addresses/0.0.0.0

Retrieve Labeled Tasks
^^^^^^^^^^^^^^^^^^^^^^

To view Tasks labeled with a given Security Label, use a query in the following format:

.. code::

    GET /v2/securityLabels/{securityLabel}/tasks

For example, the query below will retrieve all of the Tasks labeled with the ``TLP:AMBER`` Security Label:

.. code::

    GET /v2/securityLabels/TLP%3AAMBER/tasks

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "task": [
          {
            "id": 12345,
            "name": "Send Related Updates to IR Team",
            "ownerName": "Example Organization",
            "dateAdded": "2017-06-12T19:12:14Z",
            "webLink": "https://app.threatconnect.com/auth/workflow/task.xhtml?task=12345",
            "status": "Completed",
            "escalated": true,
            "reminded": true,
            "overdue": false,
            "dueDate": "2017-06-15T00:00:00Z",
            "reminderDate": "2017-06-16T05:07:00Z",
            "escalationDate": "2017-06-17T06:07:00Z"
          }
        ]
      }
    }

You can delve further by adding the ID of an associated Task to the end of the query:

.. code::

    GET /v2/securityLabels/TLP%3AAMBER/tasks/12345

Where ``12345`` is the ID of a Task labeled with the ``TLP:AMBER`` Security Label.

Retrieve Labeled Victims
^^^^^^^^^^^^^^^^^^^^^^^^

To view Victims labeled with a given Security Label, use a query in the following format:

.. code::

    GET /v2/securityLabels/{securityLabel}/victims

For example, the query below will retrieve all of the Victims labeled with the ``TLP:AMBER`` Security Label:

.. code::

    GET /v2/securityLabels/TLP%3AAMBER/victims

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

    GET /v2/securityLabels/TLP%3AAMBER/victims/54321

Where ``54321`` is the ID of a Victim labeled with the ``TLP:AMBER`` Security Label.
