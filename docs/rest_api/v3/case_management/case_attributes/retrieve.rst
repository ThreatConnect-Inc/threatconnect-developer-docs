Retrieve Case Attributes
------------------------

The following section describes how to retrieve Case Attributes via the ``/v3/caseAttributes`` endpoint. In addition to the methods described in this section, you can send the following request to retrieve Attributes added to a specific Case: ``GET /v3/cases/{caseId}?fields=attributes``.

Retrieve All Case Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Case Attributes:

.. code::

    GET /v3/caseAttributes

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "dateAdded": "2022-02-15T20:24:04Z",
                "type": "Detection Percentage",
                "value": "50",
                "source": "Hybrid analysis",
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "owner": "Demo Organization"
                },
                "lastModified": "2022-02-15T20:24:16Z",
                "pinned": false,
                "default": false
            },
            {
                "id": 2,
                "dateAdded": "2022-02-15T20:24:18Z",
                "type": "Phishing Open Rate",
                "value": "20",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmith",
                    "owner": "Demo Organization"
                },
                "lastModified": "2022-02-15T20:24:37Z",
                "pinned": false,
                "default": false
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Case Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Case Attribute:

.. code::

    GET /v3/caseAttributes/{caseAttributeId}

For example, the following request will retrieve data for the Case Attribute whose ID is 3:

.. code::

    GET /v3/caseAttributes/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "dateAdded": "2022-02-15T20:24:04Z",
            "type": "Summary of Case Findings",
            "value": "After analyzing the threat for which this Case was opened, it was determined that the threat does not pose a risk to Company ABC.",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "lastModified": "2022-02-15T21:13:16Z",
            "pinned": false,
            "default": false
        },
        "status": "Success"
    }