Create Tasks
------------

The most basic format used for creating a Task is:

.. code::

    POST /v2/tasks/
    Content-type: application/json; charset=utf-8

    {
      "name": "Test Task"
    }

Some Task types require additional fields when being created. Refer to the table below for the available fields for Tasks:

+----------------+----------+------------------------------------------------+
| Valid Fields   | Required | Example Value                                  |
+================+==========+================================================+
| name           | TRUE     | "New Task"                                     |
+----------------+----------+------------------------------------------------+
| assignee       | FALSE    | [ {"userName" : "analyst@threatconnect.com"} ] |
+----------------+----------+------------------------------------------------+
| escalatee      | FALSE    | [ {"userName" : "manager@threatconnect.com"} ] |
+----------------+----------+------------------------------------------------+
| dueDate        | FALSE    | "2018-03-20T13:36:53-04:00"                    |
+----------------+----------+------------------------------------------------+
| escalationDate | FALSE    | "2018-07-13T13:36:53-04:00"                    |
+----------------+----------+------------------------------------------------+
| description    | FALSE    | "Send to IR team for triage."                  |
+----------------+----------+------------------------------------------------+

For example, the query below will create a Task in the default Owner with the name ``Test Task`` that is due on ``2017-07-13``:

.. code::

    POST /v2/tasks/
    Content-type: application/json; charset=utf-8

    {
      "name": "Test Task",
      "dueDate": "2017-07-13T13:36:53-04:00"
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "task": {
          "id": "54321",
          "name": "Test Task",
          "owner": {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "webLink": "https://app.threatconnect.com/auth/task/task.xhtml?task=54321",
          "dueDate": "2017-07-13T13:36:53-04:00"
        }
      }
    }

The code below will function as the code above, but it will also assign the Task to the user with the username ``johndoe@example.com``:

.. code::

    POST /v2/tasks/
    Content-type: application/json; charset=utf-8

    {
      "name": "Test Task",
      "dueDate": "2017-07-13T13:36:53-04:00",
      "assignee": [
        {
          "userName": "johndoe@example.com"
        }
      ]
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "task": {
          "id": "54321",
          "name": "Test Task",
          "owner": {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "webLink": "https://app.threatconnect.com/auth/task/task.xhtml?task=54321",
          "dueDate": "2017-07-13T13:36:53-04:00",
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

The code below will function as the code above, but it will also assign the Task to the two users whose usernames are ``johndoe@example.com`` and ``janedoe@example.com``:

.. code::

    POST /v2/tasks/
    Content-type: application/json; charset=utf-8

    {
      "name": "Test Task",
      "dueDate": "2017-07-13T13:36:53-04:00",
      "assignee": [
        {
          "userName": "johndoe@example.com"
        },
        {
          "userName": "janedoe@example.com"
        }
      ]
    }

The code below will function as the code above, but instead of assigning the Task to the users ``johndoe@example.com`` and ``janedoe@example.com``, it will assign the Task to ``johndoe@example.com`` and set ``janedoe@example.com`` as the escalatee:

.. code::

    POST /v2/tasks/
    Content-type: application/json; charset=utf-8

    {
      "name": "Test Task",
      "dueDate": "2017-07-13T13:36:53-04:00",
      "assignee": [
        {
          "userName": "johndoe@example.com"
        }
      ],
      "escalatee": [
        {
          "userName": "janedoe@example.com"
        }
      ]
    }

Create Task Metadata
--------------------

Create Task Attributes
^^^^^^^^^^^^^^^^^^^^^^

To add an attribute to a Task, use the following format:

.. code::

    POST /v2/tasks/{taskId}/attributes
    Content-type: application/json; charset=utf-8

    {
      "type" : {attributeType},
      "value" : "Test Attribute",
      "displayed" : true
    }

For example, if you wanted to add a Description Attribute to the Task with ID 12345, you would use the following query:

.. code::

    POST /v2/tasks/12345/attributes
    Content-type: application/json; charset=utf-8

    {
      "type" : "Description",
      "value" : "Test Description",
      "displayed" : true
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "attribute": {
          "id": "54321",
          "type": "Description",
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-07-13T17:50:17",
          "displayed": true,
          "value": "Test Description"
        }
      }
    }

To add a Security Label to an Attribute, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the Owner:

.. code::

    POST /v2/tasks/{taskId}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will add a ``TLP Amber`` Security Label to the Attribute on the Task:

.. code::

    POST /v2/tasks/12345/attributes/54321/securityLabels/TLP%20Amber

.. note:: In order to add a Security Label to an Attribute, the Security Label must already exist. The query above will not create a new Security Label. If you specify a Security Label that does not exist, it will return an error.

Create Task Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add a Security Label to a Task, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the Owner:

.. code::

    POST /v2/tasks/{taskId}/securityLabels/{securityLabel}

For example, the query below will add a ``TLP Amber`` Security Label to the Task with ID 12345:

.. code::

    POST /v2/tasks/12345/securityLabels/TLP%20Amber

JSON Response:

.. code:: json
    
    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

.. note:: In order to add a Security Label to a Task, the Security Label must already exist. The query above will not create a new Security Label. If you specify a Security Label that does not exist, it will return an error.

Create Task Tags
^^^^^^^^^^^^^^^^

To add a Tag to a Task, use the following format, where ``{tagName}`` is replaced with the name of the Tag you wish to add to the Task:

.. code::

    POST /v2/tasks/{taskId}/tags/{tagName}

For example, the query below will add the ``Nation State`` Tag to the Task with ID 12345:

.. code::

    POST /v2/tasks/12345/tags/Nation%20State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

.. include:: ../_includes/tag_length.rst

Create Task Associations
------------------------

Associate Group to Task
^^^^^^^^^^^^^^^^^^^^^^^

To associate a Task with a Group, use a query in the following format:

.. code::

    POST /v2/tasks/{taskId}/groups/{associatedGroupType}/{associatedGroupId}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, the query below will associate a Task with ID 12345 with an Incident with the ID 54321:

.. code::

    POST /v2/tasks/12345/groups/incidents/54321

JSON Response:

.. code:: json

    {
      "status": "Success"
    }

Associate Indicator to Task
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To associate a Task with an Indicator, use a query in the following format:

.. code::

    POST /v2/tasks/{taskId}/indicators/{associatedIndicatorType}/{associatedIndicator}

For example, the query below will associate the Task with ID 12345 with the IP Address ``0.0.0.0``:

.. code::

    POST /v2/tasks/12345/indicators/addresses/0.0.0.0

JSON Response:

.. code:: json

    {
      "status": "Success"
    }

Associate Victim to Task
^^^^^^^^^^^^^^^^^^^^^^^^

To associate a Task with a Victim, use a query in the following format:

.. code::

    POST /v2/tasks/{taskId}/victims/{victimId}

For example, the query below will associate the Task with ID 12345 with the Victim with ID 54321:

.. code::

    POST /v2/tasks/12345/victims/54321

JSON Response:

.. code:: json

    {
      "status": "Success"
    }

.. include:: ../_includes/victim_asset_required_warning.rst
