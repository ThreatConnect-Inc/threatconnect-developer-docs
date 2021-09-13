Delete Workflow Tasks
---------------------

To delete a Task, use the following query:

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

To delete Tasks in bulk, refer to the `Delete Case Objects in Bulk <../bulk_delete.html>`__ section in this documentation.
