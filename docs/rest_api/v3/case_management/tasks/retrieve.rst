Retrieve Workflow Tasks
-----------------------

Retrieve All Tasks
^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Tasks:

.. code::

    GET /v3/tasks

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "xid": "bf710c31-7641-4100-9edf-461c1f6bb354",
                "name": "Read ThreatConnect's Building a Basic Workflow Blog",
                "workflowPhase": 1,
                "workflowStep": 1,
                "dueDate": "2022-03-20T23:59:59Z",
                "required": false,
                "status": "Open",
                "assignee": {
                    "type": "User",
                    "data": {
                        "id": 2,
                        "userName": "pjones+analyst@threatconnect.com"
                    }
                },
                "owner": "Demo Organization"
            },
            {
                "id": 2,
                "xid": "93e9aced-7419-4121-bef1-5276737936ab",
                "name": "Gather the subject line and email body",
                "workflowPhase": 1,
                "workflowStep": 2,
                "required": true,
                "dependentOnId": 8,
                "status": "Pending",
                "assignee": {
                    "type": "Group",
                    "data": {
                        "id": 1,
                        "name": "SOC Team",
                        "description": "SOC Team user group"
                    }
                },
                "owner": "Demo Organization"
            },
            {...}
        ],
        "Status": "Success"
    }


Retrieve a Specific Task
^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Task:

.. code::

    GET /v3/tasks/{taskId}

For example, the following request will retrieve data for the Task whose ID is 1:

.. code::

    GET /v3/tasks/1

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "xid": "bf710c31-7641-4100-9edf-461c1f6bb354",
                "name": "Read ThreatConnect's Building a Basic Workflow Blog",
                "workflowPhase": 1,
                "workflowStep": 1,
                "dueDate": "2022-03-20T23:59:59Z",
                "required": false,
                "status": "Open",
                "assignee": {
                    "type": "User",
                    "data": {
                        "id": 2,
                        "userName": "pjones+analyst@threatconnect.com"
                    }
                },
                "owner": "Demo Organization"
            }
        ],
        "Status": "Success"
    }