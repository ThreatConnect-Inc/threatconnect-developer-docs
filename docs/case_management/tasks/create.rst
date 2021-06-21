Create Workflow Tasks
---------------------

The most basic format for creating a Task is:

.. code::

    POST /v3/tasks/
    {
      "caseId": 1,
      "caseXid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
      "name": "Example Task for Workflow Case"
    }

Additional fields can be included when creating a Task. Refer to the following table for a list of available fields for the ``tasks`` object:

+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| Field          | Description                                               | Required | Type     | Example Value(s)                                                        |
+================+===========================================================+==========+==========+=========================================================================+
| artifacts      | A list of Artifacts associated with the Task              | FALSE    | String   | "{"data": [{"summary": "badguy@bad.com", "type": "Email Address"]}}"    |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| assignee       | The user or group Assignee object for the Task            | FALSE    | String   | "{"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}"  |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| caseId         | The ID of the Case that contains the Task                 | TRUE     | Integer  | 1, 2, 3                                                                 |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| caseXid        | The XID of the Case that contains the Task                | TRUE     | Integer  | "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"                                  |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| completedDate  | The completion date of the Task                           | FALSE    | Date     | "2021-04-30T00:00:00Z"                                                  |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| dependentOnId  | The ID of another Task that this Task is dependent upon   | FALSE    | Integer  | 1, 2, 3                                                                 |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| description    | The description of the Task                               | FALSE    | String   | "Example task description."                                             |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| dueDate        | The due date of the Task                                  | FALSE    | Date     | "2021-04-30T00:00:00Z"                                                  |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| name           | The name of the Task                                      | TRUE     | String   | "Example Task"                                                          |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| required       | Flag indicating whether or not the Task is required       | FALSE    | Boolean  | True, False                                                             |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| status         | The status of the Task                                    | FALSE    | String   | "Pending", "Open", "Reopened", or "Closed"                              |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| workflowPhase  | The Workflow phase where the Task takes place             | FALSE    | Integer  | 1, 2, 3                                                                 |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+
| workflowStep   | The step of the Workflow where the Task takes place       | FALSE    | Integer  | 1, 2, 3                                                                 |
+----------------+-----------------------------------------------------------+----------+----------+-------------------------------------------------------------------------+

For example, the following query will create a new Task for the Case with ID 1. This Task's name will be "Create Shared Drive Folder for Case" and it will be the second step of the first Workflow phase:

.. code::

    POST /v3/tasks/
    {
      "caseId": 1,
      "caseXid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
      "name": "Create Meeting Notes Folder",
      "description": "If Case listed a Severity of High or Critical, create a Meeting Notes folder inside the Case folder.",
      "workflowPhase": 1,
      "workflowStep": 2
    }

JSON Response:

.. code:: json

    {
      "data": {
          "id": 2,
          "xid": "b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2",
          "name": "Create Meeting Notes Folder",
          "description": "If Case lists a Severity of High or Critical, create a Meeting Notes folder inside the Case folder.",
          "workflowPhase": 1,
          "workflowStep": 2,
          "required": False,
          "status": "Open",
          "notes": {
              "count": 0
          }
      },
      "message": "Created",
      "status": "Success"
    }
