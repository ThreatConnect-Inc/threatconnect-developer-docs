Update Workflow Templates
-------------------------

To update a Workflow Template, the basic format is:

.. code::

    PUT /v3/workflowTemplates/{workflowTemplateID}
    {
        {updatedField}: {updatedValue}
    }
  

Refer to the following table for a list of available fields that can be updated for the ``workflowTemplates`` object:

+----------------+--------------------------------------------+----------+
| Field          | Description                                | Type     |
+================+============================================+==========+
| description    | The description of the Workflow Template   | String   |
+----------------+--------------------------------------------+----------+
| name           | The name of the Workflow Template          | String   |
+----------------+--------------------------------------------+----------+
| version        | The version of the Workflow Template       | Integer  |
+----------------+--------------------------------------------+----------+

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