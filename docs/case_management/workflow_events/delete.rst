Delete Workflow Events
----------------------

To delete a Workflow Event, use a query in the following format:

.. code::

    DELETE /v3/workflowEvents/{workflowEventID}

    {
        "deletedReason": "Reason for deleting the Workflow Event."
    }

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