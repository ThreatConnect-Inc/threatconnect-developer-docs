Delete Workflow Templates
-------------------------

To delete a Workflow Template, use the following query:

.. code::

    DELETE /v3/workflowTemplates/{workflowTemplateID}

For example, the following query will delete the Workflow Template with ID 1:

.. code::

    DELETE /v3/workflowTemplates/1

JSON Response:

.. code:: json

    {
      "message": "Deleted",
      "status": "Success"
    }

Delete Workflow Templates in Bulk
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete Workflow Templates in bulk, refer to the `Delete Case Objects in Bulk <../bulk_delete.html>`__ section in this documentation.
