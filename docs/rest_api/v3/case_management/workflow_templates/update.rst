Update Workflow Templates
-------------------------

The following example illustrates the basic format for updating a Workflow Template:

.. code::

    PUT /v3/workflowTemplates/{workflowTemplateId}
    Content-Type: application/json

    {
        {updatedField}: {updatedValue}
    }

For example, the following request will update the version number of the Workflow Template whose ID is 3 and add two Attribute Types to it:

.. code::

    PUT /v3/workflowTemplates/3
    Content-Type: application/json
    
    {
        "version": 2,
        "configAttribute": [
            {
                "attributeTypeId": 269
            },
            {
                "attributeTypeId": 271
            }
        ]
    }

JSON Response:

.. code:: json

    {
        "data": {
            "name": "Phishing Investigation Workflow",
            "description": "Workflow for phishing investigations.",
            "active": false,
            "version": 2,
            "configAttribute": [
                {
                    "attributeTypeId": 269
                },
                {
                    "attributeTypeId": 271
                }
            ]
        },
        "message": "Updated",
        "status": "Success"
    }


Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request to the ``/v3/workflowTemplates`` endpoint.