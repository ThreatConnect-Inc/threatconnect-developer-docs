Create Workflow Tasks
---------------------

The basic format for creating a Task is:

.. code::

    POST /v3/tasks/
    {
        "caseId": 1,
        "name": "Example Task for Workflow Case"
    }

For example, the following query will create a new Task for the Case with ID 1. This Task's name will be "Create Shared Drive Folder for Case" and it will be the second step of the first Workflow Phase:

.. code::

    POST /v3/tasks/
    {
        "caseId": 1,
        "name": "Create Meeting Notes Folder",
        "description": "If Case listed a Severity of High or Critical, create a Meeting Notes folder inside the Case folder.",
        "dueDate": "2022-03-29T12:15:00Z",
        "workflowPhase": 1,
        "workflowStep": 2
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
            "workflowStep": 2,
            "dueDate": "2022-03-29T12:15:00Z",
            "required": false,
            "status": "Open",
            "notes": {},
            "owner": "Example Organization"
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request for the ``tasks`` object.