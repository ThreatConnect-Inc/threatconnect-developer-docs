Delete Artifacts
----------------

The most basic format to delete an Artifact is:

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

To delete Artifacts in bulk, refer to the `Delete Case Objects in Bulk <..bulk_delete.html>`__ section in this documentation.
