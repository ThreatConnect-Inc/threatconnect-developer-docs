Retrieve Tasks
---------------

.. include:: filters.rst

Retrieve Multiple Tasks
^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Tasks in the default Owner, use the following query:

.. code::

    GET /v2/tasks

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "task": [
          {
            "id": "54321",
            "name": "Send Domains to IR Team",
            "ownerName": "Example Organization",
            "dateAdded": "2017-07-13T17:50:17",
            "webLink": "https://app.threatconnect.com/auth/workflow/task.xhtml?task=54321",
            "status": "Not Started",
            "escalated": false,
            "reminded": false,
            "overdue": false,
            "dueDate": "2017-07-24T00:00:00Z"
          }
        ]
      }
    }

Retrieve a Single Task
^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a single Task, use a query in the following format:

.. code::

    GET /v2/tasks/{taskId}

For example, if you want to retrieve the Task with ID 12345, you would use the following query:

.. code::

    GET /v2/tasks/12345

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "task": {
          "id": "54321",
          "name": "Test",
          "owner": {
            "id": 5,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "webLink": "https://app.threatconnect.com/auth/workflow/task.xhtml?task=54321",
          "status": "Not Started",
          "escalated": false,
          "reminded": false,
          "overdue": false,
          "dueDate": "2017-07-24T00:00:00Z",
          "assignee": [
            {
              "userName": "johndoe@example.com",
              "firstName": "John",
              "lastName": "Doe"
            }
          ]
        }
      }
    }

Retrieve Task Metadata
----------------------

Retrieve Task Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a Task's Attributes, use the following format:

.. code::

    GET /v2/tasks/{taskId}/attributes

For example, if you want to retrieve the Attributes on the Task with ID 12345, you would use the following query:

.. code::

    GET /v2/tasks/12345/attributes

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

    GET /v2/tasks/{taskId}/attributes/{attributeId}/securityLabels

Here is an example query:

.. code::

    GET /v2/tasks/12345/attributes/54321/securityLabels

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

Retrieve Task Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve the Security Labels for a Task, use a query in the following format:

.. code::

    GET /v2/tasks/{taskId}/securityLabels

For example, the query below will retrieve all Security Labels for the Task with ID 12345:

.. code::

    GET /v2/tasks/12345/securityLabels

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

Retrieve Task Tags
^^^^^^^^^^^^^^^^^^

To retrieve the Tags for a Task, use a query in the following format:

.. code::

    GET /v2/tasks/{taskId}/tags

For example, the query below will retrieve all Tags for the Task with ID 12345:

.. code::

    GET /v2/tasks/12345/tags

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

Retrieve Task Associations
--------------------------

Group to Task Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Groups associated with a given Task, use a query in the following format:

.. code::

    GET /v2/tasks/{taskId}/groups

For example, the query below will retrieve all of the Groups associated with a Task with ID 12345:

.. code::

    GET /v2/tasks/12345/groups

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "task": [
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

    GET /v2/tasks/{taskId}/{associatedGroupType}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, you could use the following query to find all Incidents associated with the Task with ID 12345:

.. code::

    GET /v2/tasks/12345/incidents

You can also delve further by adding the ID of an associated Group to the end of the query:

.. code::

    GET /v2/tasks/12345/incidents/54321

Where ``54321`` is the ID of an Incident associated with Task 12345.

Indicator to Task Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Indicators associated with a given Task, use a query in the following format:

.. code::

    GET /v2/tasks/{taskId}/indicators

For example, the query below will retrieve all of the Indicators associated with a Task with ID 12345:

.. code::

    GET /v2/tasks/12345/indicators

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

    GET /v2/tasks/{taskId}/indicators/{associatedIndicatorType}

For example, you could use the following query to find all Address Indicators associated with the Task with ID 12345:

.. code::

    GET /v2/tasks/12345/indicators/addresses

Victim Asset to Task Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victim Assets associated with a given Task, use a query in the following format:

.. code::

    GET /v2/tasks/{taskId}/victimAssets

For example, the query below will retrieve all of the Victim Assets associated with a Task with ID 12345:

.. code::

    GET /v2/tasks/12345/victimAssets

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

    GET /v2/tasks/{taskId}/victimAssets/{victimAssetType}

The available Victim Asset types are:

.. include:: ../_includes/victim_asset_types.rst

For example, you could use the following query to find all Victim Assets that are Email Addresses which are associated with the Task with ID 12345:

.. code::

    GET /v2/tasks/12345/victimAssets/emailAddresses

You can delve further by adding the ID of an associated Victim Asset to the end of the query:

.. code::

    GET /v2/tasks/12345/victimAssets/emailAddresses/54321

Where ``54321`` is the ID of a Victim Asset associated with Task 12345.

Victim to Task Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view Victims associated with a given Task, use a query in the following format:

.. code::

    GET /v2/tasks/{taskId}/victims

For example, the query below will retrieve all of the Victims associated with a Task with ID 12345:

.. code::

    GET /v2/tasks/12345/victims

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

    GET /v2/tasks/12345/victims/54321

Where ``54321`` is the ID of a Victim associated with Task 12345.
