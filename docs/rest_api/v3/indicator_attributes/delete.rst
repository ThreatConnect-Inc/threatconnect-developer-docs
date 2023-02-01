Delete Indicator Attributes
---------------------------

Send a request in the following format to delete an Indicator Attribute:

.. code::

    DELETE /v3/indicatorAttributes/{indicatorAttributeId}

For example, the following request will delete the Indicator Attribute whose ID is 10:

.. code::

    DELETE /v3/indicatorAttributes/10

JSON Response

.. code::

    {
        "message": "Deleted",
        "status": "Success"
    }

.. hint::
    You can also remove Indicator Attributes from an Indicator by using the ``mode`` field on the ``/v3/indicators`` endpoint. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information.
