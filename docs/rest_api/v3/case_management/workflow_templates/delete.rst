Delete Workflow Templates
-------------------------

Send a request in the following format to delete a Workflow Template:

.. code::

    DELETE /v3/workflowTemplates/{workflowTemplateId}

For example, the following request will delete the Workflow Template whose ID is 1:

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

For instructions on deleting Workflow Templates in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.