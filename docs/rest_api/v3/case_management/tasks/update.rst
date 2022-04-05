Update Workflow Tasks
---------------------

The basic format for updating a Task is:

.. code::

    PUT /v3/tasks/{taskId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following query will make the Task with ID 1 required to complete and will make it due at 10:30 a.m. on April 5, 2022:

.. code::

    PUT /v3/tasks/1
    {
      "dueDate": "2022-04-05T10:30:00Z",
      "required": true
    }

JSON Response:

.. code:: json

        {
            "data": {
                "id": 1,
                "xid": "bf710c31-7641-4100-9edf-461c1f6bb354",
                "name": "Read ThreatConnect's Building a Basic Workflow Blog",
                "workflowPhase": 0,
                "workflowStep": 1,
                "dueDate": "2022-04-05T10:30:00Z",
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
            "message": "Updated",
            "status": "Success"
        }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request for the ``tasks`` object.