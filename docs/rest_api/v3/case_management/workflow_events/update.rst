Update Workflow Events
----------------------

The basic format for updating a Workflow Event is:

.. code::

    PUT /v3/workflowEvents/{workflowEventId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following query will update the summary for the Workflow Event with ID 1.

.. code::

    PUT /v3/workflowEvents/1
    {
        "summary": "New Workflow Event summary"
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 1,
            "eventDate": "2021-03-05T14:48:44Z",
            "dateAdded": "2021-03-05T14:48:44Z",
            "summary": "New Workflow Event summary",
            "systemGenerated": true,
            "notes": {}
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request for the ``workflowEvents`` object.