Delete Victim Attributes
------------------------

Send a request in the following format to delete a Victim Attribute:

.. code::

    DELETE /v3/victimAttributes/{victimAttributeId}

For example, the following request will delete the Victim Attribute whose ID is 1:

.. code::

    DELETE /v3/victimAttributes/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }

.. hint::
    You can also remove Victim Attributes from a Victim by using the ``mode`` field on the ``/v3/victims`` endpoint. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information.