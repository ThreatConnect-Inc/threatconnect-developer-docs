Update Tasks
-------------

To update a Task, the basic format is:

.. code::

    PUT /v2/tasks/{taskId}
    {
      {updatedField}: {updatedValue}
    }

When updating the fields on a Task itself, you can change any of the following fields:

+--------------+------------------------------------------------+
| Valid Fields | Example Value                                  |
+==============+================================================+
| name         | "New Task"                                     |
+--------------+------------------------------------------------+
| assignee     | { "userName" : ["analyst@threatconnect.com"] } |
+--------------+------------------------------------------------+
| escalatee    | { "userName" : ["manager@threatconnect.com"] } |
+--------------+------------------------------------------------+
| dueDate      | {"2016-03-20T13:36:53-04:00"}                  |
+--------------+------------------------------------------------+
| description  | {"Send to IR team for triage."}                |
+--------------+------------------------------------------------+
  
By way of example, the query below will update the name and due date of the Task with ID 12345:

.. code::

    PUT /v2/tasks/12345
    {
      "name": "New Task Name",
      "dueDate": {"2017-07-13T13:36:53-04:00"}
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "task": {
          "id": "12345",
          "name": "New Task Name",
          "owner": {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "webLink": "https://app.threatconnect.com/auth/task/task.xhtml?task=12345",
          "dueDate": "2017-07-13T13:36:53-04:00"
        }
      }
    }

Update Task Metadata
--------------------

Update Task Attributes
^^^^^^^^^^^^^^^^^^^^^^

To update a Task's attribute, use the following format:

.. code::

    PUT /v2/tasks/{taskId}/attributes/{attributeId}
    {
      {updatedField}: {updatedValue}
    }

When updating attributes, you can change the following fields:

+----------------------------+
| Updatable Attribute Fields |
+============================+
| value                      |
+----------------------------+
| displayed                  |
+----------------------------+

For example, if you wanted to update the value of an attribute with ID 54321 on the Task with ID 12345, you would use the following query:

.. code::

    PUT /v2/tasks/12345/attributes/54321
    {
      "value": "A new attribute value."
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
          "lastModified": "2017-07-19T15:54:12Z",
          "displayed": true,
          "value": "A new attribute value."
        }
      }
    }
