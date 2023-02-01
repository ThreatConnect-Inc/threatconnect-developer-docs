Delete Victims
--------------

Send a request in the following format to delete a Victim:

.. code::

    DELETE /v3/victims/{victimId}

For example, the following request will delete the Victim whose ID is 1:

.. code::

    DELETE /v3/victims/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }