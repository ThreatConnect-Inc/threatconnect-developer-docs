Delete Notes
------------

To delete a Note, use the following query:

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

Delete Notes in Bulk
^^^^^^^^^^^^^^^^^^^^

To delete Notes in bulk, refer to the `Delete Case Objects in Bulk <../bulk_delete.html>`__ section in this documentation.
