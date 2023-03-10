Delete Workflow Events
----------------------

Send a request in the following format to delete a Workflow Event:

.. code::

    DELETE /v3/workflowEvents/{workflowEventId}

    {
        "deletedReason": "Reason for deleting the Workflow Event."
    }

.. attention::
    Only Workflow Events that have been manually added to a Case may be deleted.

For example, the following request will delete the Workflow Event whose ID is 4:

.. code::

    DELETE /v3/workflowEvents/4

    {
        "deletedReason": "No longer needed this Workflow Event."
    }

JSON Response:

.. code:: json

    {
        "message": "Deleted",
        "status": "Success"
    }

Delete Workflow Events in Bulk
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For instructions on deleting Workflow Evemts in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.