Retrieve Workflow Events
------------------------

Retrieve All Workflow Events
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Workflow Events:

.. code::

    GET /v3/workflowEvents

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "eventDate": "2021-03-05T14:48:44Z",
                "dateAdded": "2021-03-05T14:48:44Z",
                "summary": "Case created",
                "systemGenerated": true,
                "link": "https://app.threatconnect.com/api/v3/cases/1"
            }, 
            {
                "id": 2,
                "eventDate": "2021-03-05T14:49:24Z",
                "dateAdded": "2021-03-05T14:49:24Z",
                "summary": "Added a note",
                "systemGenerated": true,
                "link": "https://app.threatconnect.com/api/v3/notes/1"
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Workflow Event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Workflow Event:

.. code::

    GET /v3/workflowEvents/{workflowEventId}

For example, the following request will retrieve data for the Workflow Event whose ID is 1:

.. code::

    GET /v3/workflowEvent/1

JSON Response:

.. code:: json

    {
        "data": {
            "id": 1,
            "eventDate": "2021-03-05T14:48:44Z",
            "dateAdded": "2021-03-05T14:48:44Z",
            "summary": "Case created",
            "systemGenerated": true,
            "link": "https://app.threatconnect.com/api/v3/cases/1"
        },
        "status": "Success"
    }