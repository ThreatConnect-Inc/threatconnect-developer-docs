Delete Indicator Attributes
---------------------------

The basic format for deleting an Indicator Attribute is:

.. code::

    DELETE /v3/indicatorAttributes/{indicatorAttributeId}

For example, the following query will delete the Indicator Attribute with ID 10:

.. code::

    DELETE /v3/indicatorAttributes/10

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }

.. note::
    Indicator Attributes can be removed from an Indicator via the ``mode`` field. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information.
