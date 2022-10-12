Delete Cases
------------

The basic format to delete a Case is:

.. code::

    DELETE /v3/cases/{caseId}

For example, the following query will delete the Case with ID 1:

.. code::

    DELETE /v3/cases/1

JSON Response:

.. code:: json

    {
        "message": "Deleted",
        "status": "Success"
    }

Delete Cases in Bulk
^^^^^^^^^^^^^^^^^^^^

For instructions on deleting Cases in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.
