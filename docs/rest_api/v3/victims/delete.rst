Delete Victims
--------------

The basic format for deleting a Victim is:

.. code::

    DELETE /v3/victims/{victimId}

For example, the following query will delete the Group with ID 1:

.. code::

    DELETE /v3/victims/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }