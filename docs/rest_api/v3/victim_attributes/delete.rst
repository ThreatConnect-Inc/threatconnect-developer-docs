Delete Victim Attributes
------------------------

The basic format for deleting a Victim Attribute is:

.. code::

    DELETE /v3/victimAttributes/{victimAttributeId}

For example, the following query will delete the Victim Attribute with ID 1:

.. code::

    DELETE /v3/victimAttributes/1

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }

.. note::
    Victim Attributes can be removed from a Victim via the ``mode`` field. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information.
