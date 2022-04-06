Delete Workflow Templates
-------------------------

The basic format to delete a Workflow Template is:

.. code::

    DELETE /v3/workflowTemplates/{workflowTemplateId}

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

To delete Workflow Templates in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.
