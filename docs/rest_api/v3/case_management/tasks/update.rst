Update Workflow Tasks
---------------------

The basic format for updating a Task is:

.. code::

    PUT /v3/tasks/{taskID}
    {
        {updatedField}: {updatedValue}
    }
  

Refer to the following table for a list of available fields that can be updated for the ``tasks`` object:

+----------------+------------------------------------------------------+----------+-------------------------------------------------------------------------+
| Field          | Description                                          | Type     | Example Value(s)                                                        |
+================+======================================================+==========+=========================================================================+
| artifacts      | A list of Artifacts associated with the Task         | String   | {"data": [{"summary": "badguy@bad.com", "type": "Email Address"]}}      |
+----------------+------------------------------------------------------+----------+-------------------------------------------------------------------------+
| assignee       | The user or group Assignee object for the Task       | String   | {"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}    |
+----------------+------------------------------------------------------+----------+-------------------------------------------------------------------------+
| description    | The description of the Task                          | String   | "New task description"                                                  |
+----------------+------------------------------------------------------+----------+-------------------------------------------------------------------------+
| dueDate        | The due date of the Task                             | Date     | "2021-04-30T00:00:00Z"                                                  |
+----------------+------------------------------------------------------+----------+-------------------------------------------------------------------------+
| name           | The name of the Task                                 | String   | "New Workflow Task Name"                                                |
+----------------+------------------------------------------------------+----------+-------------------------------------------------------------------------+
| notes          | A list of Notes corresponding to the Task            | String   | {"data": [{"text": "Note about task"}]}                                 |
+----------------+------------------------------------------------------+----------+-------------------------------------------------------------------------+
| required       | Flag indicating whether or not the Task is required  | Boolean  | true, false                                                             |
+----------------+------------------------------------------------------+----------+-------------------------------------------------------------------------+
| status         | The status of the Task                               | String   | "Pending", "Open", "Reopened", or "Closed"                              |
+----------------+------------------------------------------------------+----------+-------------------------------------------------------------------------+

For example, the following query will make the Task with ID 1 required to complete and assign it a due date of April 30, 2021:

.. code::

    PUT /v3/tasks/1
    {
      "dueDate": "2021-04-30",
      "required": true
    }

JSON Response:

.. code:: json

    {
      "data": {
          "id": 1,
          "xid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
          "name": "Create Shared Drive Folder for Case",
          "description": "If Case listed a Severity of High or Critical, create a Meeting Notes folder inside the Case folder.",
          "workflowPhase": 1,
          "workflowStep": 1,
          "dueDate": "2021-04-30T00:00:00Z",
          "required": true,
          "status": "Open",
          "notes": {
              "count": 0
          }
      },
      "message": "Updated",
      "status": "Success"
    }
