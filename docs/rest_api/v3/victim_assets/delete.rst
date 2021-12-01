Delete Victim Assets
--------------------

The basic format for deleting a Victim Asset is:

.. code::

    DELETE /v3/victimAssets/{victimAssetId}

For example, the following query will delete the Victim Asset with ID 1:

.. code::

    DELETE /v3/victimAssets/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }