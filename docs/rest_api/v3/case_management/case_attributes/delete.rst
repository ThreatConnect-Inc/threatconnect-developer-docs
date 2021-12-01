Delete Case Attributes
----------------------

The basic format to delete a Case Attribute and remove it from a Case is:

.. code::

    DELETE /v3/caseAttributes/{caseAttributeID}

For example, the following query will delete the Case Attribute with ID 1:

.. code::

    DELETE /v3/caseAttributes/1

JSON Response:

.. code:: json

    {
      "message": "Deleted",
      "status": "Success"
    }

Delete Case Attributes in Bulk
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete Case Attributes in bulk, refer to `Delete Case Objects in Bulk <https://docs.threatconnect.com/en/latest/rest_api/v3/bulk_delete.html>`_.
