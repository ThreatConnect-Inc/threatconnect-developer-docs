Update Case Attributes
----------------------

The following example illustrates the basic format for updating a Case Attribute:

.. code::

    PUT /v3/caseAttributes/{caseAttributeId}
    {
        {updatedField}: {updatedValue}
    }
  
For example, the following query will update the value of the Case Attribute whose ID is 1:

.. code::

    PUT /v3/caseAttributes/1
    {
        "value": "75"
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 1,
            "dateAdded": "2022-02-15T20:24:04Z",
            "type": "Detection Percentage",
            "value": "75",
            "source": "Hybrid analysis",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555"
            },
            "lastModified": "2022-02-15T20:28:22Z",
            "pinned": false,
            "default": false
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request to the ``/v3/caseAttributes`` endpoint.