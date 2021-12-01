Delete Groups
-------------

The basic format for deleting a Group is:

.. code::

    DELETE /v3/groups/{groupId}

For example, the following query will delete the Group with ID 1:

.. code::

    DELETE /v3/groups/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }