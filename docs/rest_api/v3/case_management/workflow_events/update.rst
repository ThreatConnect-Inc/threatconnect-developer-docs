Update Workflow Events
----------------------

The basic format for updating a Workflow Event is:

.. code::

    PUT /v3/workflowEvents/{workflowEventId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following query will update the summary for the Workflow Event with ID 4 and add a Note to the Workflow Event.

.. code::

    PUT /v3/workflowEvents/4
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
            "notes": {
                "data": [
                    {
                        "id": 7,
                        "text": "Additional information about this Workflow Event",
                        "summary": "Additional information about this Workflow Event",
                        "author": "11112222333344445555",
                        "dateAdded": "2021-03-07T11:17:32Z",
                        "lastModified": "2021-03-07T11:17:32Z",
                        "edited": false,
                        "workflowEventId": 4
                    }
                ]
            }
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request for the ``workflowEvents`` object.

.. attention::
    You cannot modify system-generated Workflow Events (i.e., Workflow Events with their ``systemGenerated`` field set to ``true``). However, you can add Notes to system-generated Workflow Events.