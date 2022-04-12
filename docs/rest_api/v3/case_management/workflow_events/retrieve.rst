Retrieve Workflow Events
------------------------

Retrieve All Workflow Events
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Workflow Events, use the following query:

.. code::

    GET /v3/workflowEvents/

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

Retrieve a Single Workflow Event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Workflow Event, use a query in the following format:

.. code::

    GET /v3/workflowEvents/{workflowEventId}

For example, the following query will return information about the Workflow Event with ID 1:

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

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
