Create Case Attributes
----------------------

The following example illustrates the basic format for creating a Case Attribute:

.. code::

    POST /v3/caseAttributes
    {
        "caseId": 1,
        "type": "Case Attribute Type",
        "value": "Case Attribute Value"
    }
  
For example, the following request will add a Case Attribute to the Case whose ID is 1:

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
            "dateAdded": "2022-04-06T12:40:48Z",
            "type": "Phishing Open Rate",
            "value": "30",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555"
            },
            "lastModified": "2022-04-06T12:40:48Z",
            "pinned": false,
            "default": false
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request to the ``/v3/caseAttributes`` endpoint.

.. hint::
    Case Attributes can also be created and added to a Case when creating the Case. See the “Create Cases” section of `Cases <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html>`_ for more information.