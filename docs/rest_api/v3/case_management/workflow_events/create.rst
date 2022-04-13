Create Workflow Events
----------------------

The basic format for creating a Workflow Event is:

.. code::

    POST /v3/workflowEvents
    {
        "caseId": 1,
        "summary": "Summary of the Workflow Event"
    }

For example, the following query will create a Workflow Event with a summary of "Updated Case name" for the Case with ID 1.

.. code::

    POST /v3/workflowEvents
    {
        "caseId": 1,
        "summary": "New Security Breach Detected by TI Team"
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 4,
            "eventDate": "2021-03-05T14:54:31Z",
            "dateAdded": "2021-03-05T14:54:31Z",
            "summary": "Updated Case name",
            "systemGenerated": false,
            "link": "https://app.threatconnect.com/api/v3/cases/1"
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request for the ``workflowEvents`` object.

.. note::
    Creating a Workflow Event only adds the Workflow Event to the Case's timeline. It does not perform the action indicated in the Workflow Event's summary.