Update Workflow Events
----------------------

To update a Workflow Event, the basic format is:

.. code::

    PUT /v3/workflowEvents/{workflowEventID}
    {
        {updatedField}: {updatedValue}
    }

Refer to the following table for a list of available fields that can be updated for the ``workflowEvents`` object:

+---------------+---------------------------------------------+----------+---------------------------------------------------------+
| Field         | Description                                 | Type     | Example Value(s)                                        |
+===============+=============================================+==========+=========================================================+
| eventDate     | The time that the Event is logged           | Date     | "2021-04-30T00:00:00Z"                                  |
+---------------+---------------------------------------------+----------+---------------------------------------------------------+
| notes         | A list of Notes corresponding to the Event  | String   | "{"data": [{"text": "Note for New Workflow Event"}]}}"  |
+---------------+---------------------------------------------+----------+---------------------------------------------------------+
| summary       | The summary of the Event                    | String   | "Workflow Event Summary"                                |
+---------------+---------------------------------------------+----------+---------------------------------------------------------+

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
        "systemGenerated": True,
        "notes": {
          "count": 0
        }
      },
      "message": "Updated",
      "status": "Success"
    }