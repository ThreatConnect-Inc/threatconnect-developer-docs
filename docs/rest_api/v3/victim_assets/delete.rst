Delete Victim Assets
--------------------

Send a request in the following format to delete a Victim Asset:

.. code::

    DELETE /v3/victimAssets/{victimAssetId}

For example, the following request will delete the Victim Asset whose ID is 1:

.. code::

    DELETE /v3/victimAssets/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }