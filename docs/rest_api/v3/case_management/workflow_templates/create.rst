Create Workflow Templates
-------------------------

The following example illustrates the basic format for creating a Workflow Template:

.. code::

    POST /v3/workflowTemplates
    {
        "name": "Example Workflow Template"
    }

For example, the following request will create a Workflow Template named **Phishing Investigation Workflow** and add a description to it:

.. code::

    POST /v3/workflowTemplates
    {
        "name": "Phishing Investigation Workflow",
        "description": "Workflow for phishing investigations."
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "name": "Phishing Investigation Workflow",
            "description": "Workflow for phishing investigations.",
            "active": false,
            "version": 1
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request to the ``/v3/workflowTemplates`` endpoint.