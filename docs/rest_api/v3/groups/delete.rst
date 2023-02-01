Delete Groups
-------------

Send a request in the following format to delete a Group:

.. code::

    DELETE /v3/groups/{groupId}

For example, the following request will delete the Group whose ID is 1:

.. code::

    DELETE /v3/groups/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }