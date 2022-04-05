Retrieve Workflow Tasks
-----------------------

Retrieve All Tasks
^^^^^^^^^^^^^^^^^^

To retrieve all Tasks, use the following query:

.. code::

    GET /v3/tasks/

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "xid": "bf710c31-7641-4100-9edf-461c1f6bb354",
                "name": "Read ThreatConnect's Building a Basic Workflow Blog",
                "workflowPhase": 0,
                "workflowStep": 1,
                "dueDate": "2022-03-20T23:59:59Z",
                "required": false,
                "status": "Open",
                "assignee": {
                    "type": "User",
                    "data": {
                        "id": 12,
                        "userName": "pjones",
                        "firstName": "Patrick",
                        "lastName": "Jones",
                        "pseudonym": "PFJ",
                        "role": "Administrator"
                    }
                },
                "owner": "Example Organization"
            },
            {
                "id": 2,
                "xid": "93e9aced-7419-4121-bef1-5276737936ab",
                "name": "Gather the subject line and email body",
                "workflowPhase": 0,
                "workflowStep": 2,
                "required": true,
                "dependentOnId": 8,
                "status": "Pending",
                "assignee": {
                    "type": "User",
                    "data": {
                        "id": 12,
                        "userName": "pjones",
                        "firstName": "Patrick",
                        "lastName": "Jones",
                        "pseudonym": "PFJ",
                        "role": "Administrator"
                    }
                },
                "owner": "Example Organization"
            },
            {...}
        ],
        "Status": "Success"
    }


Retrieve a Single Task
^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Task, use a query in the following format:

.. code::

    GET /v3/tasks/{taskId}

For example, the following query will return information about the Task with ID 1:

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
                "workflowPhase": 0,
                "workflowStep": 1,
                "dueDate": "2022-03-20T23:59:59Z",
                "required": false,
                "status": "Open",
                "assignee": {
                    "type": "User",
                    "data": {
                        "id": 12,
                        "userName": "pjones",
                        "firstName": "Patrick",
                        "lastName": "Jones",
                        "pseudonym": "PFJ",
                        "role": "Administrator"
                    }
                },
                "owner": "Example Organization"
            }
        ],
        "Status": "Success"
    }


Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned object, refer to `Request Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
