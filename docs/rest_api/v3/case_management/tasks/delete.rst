Delete Workflow Tasks
---------------------

The basic format to delete a Task is:

.. code::

    DELETE /v3/tasks/{taskID}

For example, the following query will delete the Task with ID 1:

.. code::

    DELETE /v3/tasks/1

JSON Response:

.. code:: json

    {
      "message": "Deleted",
      "status": "Success"
    }

Delete Tasks in Bulk
^^^^^^^^^^^^^^^^^^^^

To delete Tasks in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.
