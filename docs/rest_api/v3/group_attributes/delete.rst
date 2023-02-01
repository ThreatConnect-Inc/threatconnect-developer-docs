Delete Group Attributes
-----------------------

Send a request in the following format to delete a Group Attribute:

.. code::

    DELETE /v3/groupAttributes/{groupAttributeId}

For example, the following request will delete the Group Attribute whose ID is 10:

.. code::

    DELETE /v3/groupAttributes/10

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }

.. hint::
    You can also remove Group Attributes from a Group by using the ``mode`` field on the ``/v3/groups`` endpoint. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information.