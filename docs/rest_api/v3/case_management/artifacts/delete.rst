Delete Artifacts
----------------

Send a request in the following format to delete an Artifact:

.. code::

    DELETE /v3/artifacts/{artifactId}

For example, the following request will delete the Artifact whose ID is 1:

.. code::

    DELETE /v3/artifacts/1

JSON Response:

.. code:: json

    {
        "message": "Deleted",
        "status": "Success"
    }

Delete Artifacts in Bulk
^^^^^^^^^^^^^^^^^^^^^^^^

For instructions on deleting Artifacts in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.