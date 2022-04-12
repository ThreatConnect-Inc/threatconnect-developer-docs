Delete Tags
-----------

The basic format to delete a Tag is:

.. code::

    DELETE /v3/tags/{tagId}

For example, the following query will delete the Tag with ID 1:

.. code::

    DELETE /v3/tags/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }

.. note::
    Deleted Tags will be automatically removed from any objects to which they are applied.