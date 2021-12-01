Delete Artifacts
----------------

The basic format to delete an Artifact is:

.. code::

    DELETE /v3/artifacts/{artifactID}

For example, the following query will delete the Artifact with ID 1:

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

To delete Artifacts in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.
