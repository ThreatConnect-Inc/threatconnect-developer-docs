Update Workflow Templates
-------------------------

To update a Workflow Template, the basic format is:

.. code::

    PUT /v3/workflowTemplates/{workflowTemplateID}
    {
        {updatedField}: {updatedValue}
    }
  

Refer to the following table for a list of available fields that can be updated for the ``workflowTemplates`` object:

+------------------+--------------------------------------------+----------+----------+-----------------------------------------+
| Field            | Description                                | Required | Type     | Example Value(s)                        |
+==================+============================================+==========+==========+=========================================+
| configAttribute  | The Attribute type that should be included | FALSE    | String   | "[{"attributeTypeId": 3}]"              |
|                  | in the Workflow Template                   |          |          |                                         |
+------------------+--------------------------------------------+----------+----------+-----------------------------------------+
| description      | The description of the Workflow Template   | FALSE    | String   | "Template for phishing investigations"  |
+------------------+--------------------------------------------+----------+----------+-----------------------------------------+
| name             | The name of the Workflow Template          | TRUE     | String   | "Phishing Workflow Template"            |
+------------------+--------------------------------------------+----------+----------+-----------------------------------------+
| version          | The version of the Workflow Template       | FALSE    | Integer  | 1, 2, 3                                 |
+------------------+--------------------------------------------+----------+----------+-----------------------------------------+

.. note:: To view a list of available Attribute types, refer to the `Attribute Types <../../attribute_types/attribute_types.html>`__ section of this documentation.

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
          "id": 1,
          "name": "Example Workflow Template Version 2.0",
          "description": "A description for this Workflow Template.",
          "active": False,
          "version": 2,
      },
      "message": "Updated",
      "status": "Success"
    }
