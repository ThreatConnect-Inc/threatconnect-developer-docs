Delete Notes
------------

Send a request in the following format to delete a Note:

.. code::

    DELETE /v3/notes/{noteId}

For example, the following request will delete the Note whose ID is 1:

.. code::

    DELETE /v3/notes/1

JSON Response:

.. code:: json

    {
        "message": "Deleted",
        "status": "Success"
    }

Delete Cases in Bulk
^^^^^^^^^^^^^^^^^^^^

For instructions on deleting Notes in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.