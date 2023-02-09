Delete Case Attributes
----------------------

Send a request in the following format to delete a Case Attribute:

.. code::

    DELETE /v3/caseAttributes/{caseAttributeId}

For example, the following request will delete the Case Attribute whose ID is 1:

.. code::

    DELETE /v3/caseAttributes/1

JSON Response:

.. code:: json

    {
        "message": "Deleted",
        "status": "Success"
    }

.. hint::
    You can also remove Case Attributes from a Case by using the ``mode`` field on the ``/v3/cases`` endpoint. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information.