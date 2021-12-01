Delete Workflow Events
----------------------

The basic format to delete a Workflow Event is:

.. code::

    DELETE /v3/workflowEvents/{workflowEventId}

    {
        "deletedReason": "Reason for deleting the Workflow Event."
    }

.. note::
    You must specify a ``deletedReason`` to delete a Workflow Event.

For example, the following query will delete the Workflow Event with ID 1:

.. code::

    DELETE /v3/workflowEvents/1

    {
        "deletedReason": "No longer needed this Event."
    }

JSON Response:

.. code:: json

    {
      "message": "Deleted",
      "status": "Success"
    }
