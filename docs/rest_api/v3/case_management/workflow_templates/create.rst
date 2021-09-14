Create Workflow Templates
-------------------------

The most basic format for creating a Workflow Template is:

.. code::

    POST /v3/workflowTemplates/
    {
      "name": "Example Workflow Template"
    }

Additional fields can be included when creating a Workflow Template. Refer to the following table for a list of available fields for the ``workflowTemplates`` object:

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

.. note:: To view a list of available Attribute types, refer to the `Attribute Types <../attribute_types/attribute_types.html>`__ section of this documentation.

For example, the following query will create an Workflow Template with the name ``Example Workflow Template`` and a description of the template:

.. code::

    POST /v3/workflowTemplates/
    {
      "name": "Example Workflow Template",
      "description": "A description for this Workflow Template."
    }

JSON Response:

.. code:: json

    {
      "data": {
          "id": 1,
          "name": "Example Workflow Template",
          "description": "A description for this Workflow Template.",
          "active": False,
          "version": 1,
      },
      "message": "Created",
      "status": "Success"
    }
