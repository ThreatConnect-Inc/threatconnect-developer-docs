Retrieve Case Attributes
------------------------

Retrieve All Case Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Case Attributes, use the following query:

.. code::

    GET /v3/caseAttributes/

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "type": "Detection Percentage",
                "value": "50",
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
                "lastModified": "2022-02-15T20:24:16Z",
                "default": false
            },
            {
                "id": 2,
                "type": "Phishing Open Rate",
                "value": "20",
                "createdBy": {
                    "id": 1,
                    "userName": "jsmith",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmith",
                    "role": "User"
                },
                "dateAdded": "2022-02-15T20:24:18Z",
                "lastModified": "2022-02-15T20:24:37Z",
                "default": false
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Single Case Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Case Attribute, use a query in the following format:

.. code::

    GET /v3/caseAttributes/{caseAttributeId}

For example, the following query will return information about the Case Attribute with ID 1:

.. code::

    GET /v3/notes/1

JSON Response:

.. code:: json

    {
      "data": {
          "id": 1,
          "type": "Detection Percentage",
          "value": "50",
          "createdBy": {
              "id": 79,
              "userName": "jsmith",
              "firstName": "John",
              "lastName": "Smith",
              "pseudonym": "jsmith"
          },
          "dateAdded": "2022-02-15T20:24:04Z",
          "lastModified": "2022-02-15T20:24:16Z",
          "default": false
      },
      "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
