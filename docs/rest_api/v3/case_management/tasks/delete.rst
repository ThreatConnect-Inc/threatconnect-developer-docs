Delete Workflow Tasks
---------------------

Send a request in the following format to delete a Task:

.. code::

    DELETE /v3/tasks/{taskId}

For example, the following request will delete the Task whose ID is 1:

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

For instructions on deleting  Tasks in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.