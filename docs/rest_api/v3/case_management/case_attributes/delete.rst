Delete Case Attributes
----------------------

To remove a Case Attribute from a Case, use the following query:

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

To delete Case Attributes in bulk, refer to the `Delete Case Objects in Bulk <../../bulk_delete.html>`__ section in this documentation.
