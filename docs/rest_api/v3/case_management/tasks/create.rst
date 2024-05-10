Create Workflow Tasks
---------------------

The following example illustrates the basic format for creating a Task:

.. code::

    POST /v3/tasks
    Content-Type: application/json

    {
        "caseId": 1,
        "name": "Example Task for Workflow Case"
    }

For example, the following request will add a Task named "Create Meeting Notes Folder" to the Case whose ID is 1. It will also complete the following actions for the Task:

- Make the Task the third step of the first Workflow Phase for the Case
- Make the Task a due at 12:15 p.m. on March 29, 2022

.. code::

    POST /v3/tasks
    Content-Type: application/json
    
    {
        "caseId": 1,
        "name": "Create Meeting Notes Folder",
        "description": "If the Case listed a Severity of High or Critical, create a Meeting Notes folder inside the Case folder.",
        "dueDate": "2022-03-29T12:15:00Z",
        "workflowPhase": 1,
        "workflowStep": 3
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "xid": "559797fc-bb36-45a7-9d4d-c7c865944548",
            "name": "Create Meeting Notes Folder",
            "description": "If Case listed a Severity of High or Critical, create a Meeting Notes folder inside the Case folder.",
            "workflowPhase": 1,
            "workflowStep": 3,
            "dueDate": "2022-03-29T12:15:00Z",
            "required": false,
            "status": "Open",
            "owner": "Demo Organization"
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request to the ``/v3/tasks`` endpoint.