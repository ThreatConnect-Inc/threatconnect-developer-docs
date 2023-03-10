Create Workflow Events
----------------------

The following example illustrates the basic format for creating a Workflow Event:

.. code::

    POST /v3/workflowEvents
    {
        "caseId": 1,
        "summary": "Summary of the Workflow Event"
    }

For example, the following request will add a Workflow Event with a summary of "Notes about Case uploaded to SOC team shared drive" to the Case whose ID is 1:

.. code::

    POST /v3/workflowEvents
    {
        "caseId": 1,
        "summary": "Notes about Case uploaded to SOC team shared drive"
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 4,
            "eventDate": "2021-03-05T14:54:31Z",
            "dateAdded": "2021-03-05T14:54:31Z",
            "summary": "Notes about Case uploaded to SOC team shared drive",
            "systemGenerated": false,
            "link": "https://app.threatconnect.com/api/v3/cases/1"
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request to the ``/v3/workflowEvents`` endpoint.

.. note::
    Creating a Workflow Event only adds the Workflow Event to the Case's timeline. It does not perform the action indicated in the Workflow Event's summary.