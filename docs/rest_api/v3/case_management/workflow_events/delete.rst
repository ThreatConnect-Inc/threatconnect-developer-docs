Delete Workflow Events
----------------------

The basic format to delete a Workflow Event is:

.. code::

    DELETE /v3/workflowEvents/{workflowEventId}

    {
        "deletedReason": "Reason for deleting the Workflow Event."
    }

.. note::
    Only Workflow Events that have been manually added to a Case may be deleted.

For example, the following query will delete the Workflow Event with ID 4:

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
