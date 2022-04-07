Update Workflow Templates
-------------------------

The basic format for updating a Workflow Template is:

.. code::

    PUT /v3/workflowTemplates/{workflowTemplateId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following query will update the name and version number of the Workflow Template with ID 1:

.. code::

    PUT /v3/workflowTemplates/1
    {
        "name": "Example Workflow Template Version 2.0",
        "version": 2
    }

JSON Response:

.. code:: json

    {
        "data": {
            "name": "Example Workflow Template Version 2.0",
            "description": "A description for this Workflow Template.",
            "active": false,
            "version": 2,
            "configAttribute": [{
                "attributeTypeId": 86
            }]
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request for the ``workflowTemplates`` object.