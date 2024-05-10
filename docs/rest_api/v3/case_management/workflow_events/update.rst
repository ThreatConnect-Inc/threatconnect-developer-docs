Update Workflow Events
----------------------

The following example illustrates the basic format for updating a Workflow Event:

.. code::

    PUT /v3/workflowEvents/{workflowEventId}
    Content-Type: application/json

    {
        {updatedField}: {updatedValue}
    }

For example, the following request will update the summary for the Workflow Event whose ID is 4 and add a Note to the Workflow Event:

.. hint::
    To include the ``notes`` field in the API response, append ``?fields=notes`` to the end of the request URL.

.. code::

    PUT /v3/workflowEvents/4
    Content-Type: application/json
    
    {
        "summary": "New Workflow Event summary",
        "notes": {"data": [{"text": "Additional information about this Workflow Event"}]}
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 4,
            "eventDate": "2021-03-05T14:48:44Z",
            "dateAdded": "2021-03-05T14:48:44Z",
            "summary": "New Workflow Event summary",
            "systemGenerated": false,
            "link": "https://app.threatconnect.com/api/v3/cases/1"
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request to the ``/v3/workflowEvents`` endpoint.

.. attention::
    You cannot modify system-generated Workflow Events (i.e., Workflow Events with the ``systemGenerated`` field set to ``true``), but you can add Notes to them.