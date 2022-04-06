Delete Notes
------------

The basic format to delete a Note is:

.. code::

    DELETE /v3/notes/{noteID}

For example, the following query will delete the Note with ID 1:

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

To delete Cases in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.
