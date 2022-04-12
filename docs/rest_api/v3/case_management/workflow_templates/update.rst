Update Workflow Templates
-------------------------

The basic format for updating a Workflow Template is:

.. code::

    PUT /v3/workflowTemplates/{workflowTemplateId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following query will update the name and version number of the Workflow Template with ID 3 and add an Attribute Type to the Workflow Template:

.. code::

    PUT /v3/workflowTemplates/3
    {
        "name": "Example Workflow Template Version 2.0",
        "version": 2,
        "configAttribute": [{"attributeTypeId": 3}]
    }

JSON Response:

.. code:: json

{
    "data": {
        "name": "Example Workflow Template Version 2.0",
        "description": "Template for phishing investigations.",
        "active": false,
        "version": 2,
        "configAttribute": [{
                "attributeTypeId": 3
        }]
    },
    "message": "Updated",
    "status": "Success"
}

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request for the ``workflowTemplates`` object.