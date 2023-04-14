Delete Tags
-----------

Send a request in the following format to delete a Tag:

.. code::

    DELETE /v3/tags/{tagId}

For example, the following request will delete the Tag whose ID is 1:

.. code::

    DELETE /v3/tags/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }

.. attention::
    Deleting a Tag will also remove the Tag from any objects to which it was applied.