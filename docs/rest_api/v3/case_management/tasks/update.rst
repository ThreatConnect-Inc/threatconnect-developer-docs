Update Workflow Tasks
---------------------

The following example illustrates the basic format for updating a Task:

.. code::

    PUT /v3/tasks/{taskId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following request will make the Task whose ID is 3 required for completion and due at 10:30 a.m. on April 5, 2022:

.. code::

    PUT /v3/tasks/3
    {
        "dueDate": "2022-04-05T10:30:00Z",
        "required": true
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "xid": "559797fc-bb36-45a7-9d4d-c7c865944548",
            "name": "Create Meeting Notes Folder",
            "description": "If the Case listed a Severity of High or Critical, create a Meeting Notes folder inside the Case folder.",
            "workflowPhase": 1,
            "workflowStep": 3,
            "dueDate": "2022-04-05T10:30:00Z",
            "required": true,
            "status": "Open",
            "owner": "Demo Organization"
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request to the ``/v3/tasks`` endpoint.