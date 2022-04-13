Delete Group Attributes
-----------------------

The basic format for deleting a Group Attribute is:

.. code::

    DELETE /v3/groupAttributes/{groupAttributeId}

For example, the following query will delete the Group Attribute with ID 10:

.. code::

    DELETE /v3/groupAttributes/10

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }

.. hint::
    Group Attributes can be removed from a Group via the ``mode`` field. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information.
