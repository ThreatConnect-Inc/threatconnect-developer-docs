Delete Cases
------------

The most basic format to delete a Case is:

.. code::

    DELETE /v3/cases/{caseID}

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

To delete Cases in bulk, refer to the `Delete Case Objects in Bulk <../bulk_delete.html>`__ section in this documentation.
