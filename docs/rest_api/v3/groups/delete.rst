Delete Groups
-------------

Send a request in the following format to delete a Group:

**Example Request (Group ID)**

.. code::

    DELETE /v3/groups/{groupId}

**Example Request (Group XID)**

.. code::

    DELETE /v3/groups/{groupXid}?owner={ownerName}

For example, the following request will delete the Group whose ID is 1:

.. code::

    DELETE /v3/groups/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }