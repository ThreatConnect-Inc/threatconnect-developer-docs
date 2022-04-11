Update Case Attributes
----------------------

The basic format for updating a Case Attribute is:

.. code::

    PUT /v3/caseAttributes/{caseAttributeId}
    {
        "value": "Case Attribute Value"
    }
  
For example, the following query will update the ``value`` of a Case Attribute with ID 1.

.. code::

    POST /v3/caseAttributes/1
    {
        "value": "75"
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 1,
            "type": "Detection Percentage",
            "value": "75",
            "source": "Hybrid analysis",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "role": "Api User"
            },
            "dateAdded": "2022-02-15T20:24:04Z",
            "lastModified": "2022-02-15T20:28:22Z",
            "default": false
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request for the ``caseAttributes`` object.