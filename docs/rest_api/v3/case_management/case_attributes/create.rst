Create Case Attributes
----------------------

The basic format for creating a Case Attribute and adding it to a Case is:

.. code::

    POST /v3/caseAttributes
    {
        "caseId": 1,
        "type": "Case Attribute Type",
        "value": "Case Attribute Value"
    }
  
For example, the following query will add a Case Attribute to the Case with ID 1.

.. code::

    POST /v3/caseAttributes
    {
        "caseId": 1,
        "type": "Phishing Open Rate",
        "value": "30"
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "type": "Phishing Open Rate",
            "value": "30",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "role": "Api User"
            },
            "dateAdded": "2022-04-06T12:40:48Z",
            "lastModified": "2022-04-06T12:40:48Z",
            "default": false
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request for the ``caseAttributes`` object.