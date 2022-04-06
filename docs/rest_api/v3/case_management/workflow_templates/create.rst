Create Workflow Templates
-------------------------

The basic format for creating a Workflow Template is:

.. code::

    POST /v3/workflowTemplates/
    {
        "name": "Example Workflow Template"
    }

For example, the following query will create a Workflow Template with the name ``Phishing Investigation Template`` and a description of the Template:

.. code::

    POST /v3/workflowTemplates/
    {
        "name": "Phishing Investigation Template",
        "description": "Template for phishing investigations."
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "name": "Phishing Investigation Template",
            "description": "Template for phishing investigations.",
            "active": false,
            "version": 1
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request for the ``workflowTemplates`` object.