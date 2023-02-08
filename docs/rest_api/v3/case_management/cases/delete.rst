Delete Cases
------------

Send a request in the following format to delete a Case:

.. code::

    DELETE /v3/cases/{caseId}

For example, the following request will delete the Case whose ID is 1:

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