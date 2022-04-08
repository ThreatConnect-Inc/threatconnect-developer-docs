Retrieve Cases
--------------

Retrieve All Cases
^^^^^^^^^^^^^^^^^^

To retrieve all Cases, use the following query:

.. code::

    GET /v3/cases/

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "xid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
                "name": "Example Workflow Case",
                "dateAdded": "2021-04-09T14:41:27.622Z",
                "caseOpenTime": "2021-04-09T14:41:27.622Z",
                "caseOpenUser": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "role": "Api User"
                },
                "status": "Open",
                "severity": "Low",
                "resolution": "Not Specified",
                "assignee": {
                    "type": "User",
                    "data": {
                        "id": 1,
                        "userName": "jonsmith@threatconnect.com",
                        "firstName": "John",
                        "lastName": "Smith",
                        "pseudonym": "johnsmith",
                        "role": "User"
                    }
                },
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "role": "Api User"
                },
                "owner": "Example Organization",
                "ownerId": 7
            }, 
            {
                "id": 2,
                "xid": "b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2",
                "name": "Malware Investigation",
                "description": "Case to investigate new malware",
                "dateAdded": "2021-03-25T18:56:22Z",
                "caseOpenTime": "2021-03-25T18:56:22Z",
                "caseOpenUser": {
                    "id": 2,
                    "userName": "pjones+analyst@threatconnect.com",
                    "firstName": "Patrick",
                    "lastName": "Jones",
                    "pseudonym": "patjones",
                    "role": "User"
                },
                "status": "Open",
                "severity": "Critical",
                "resolution": "Not Specified",
                "createdBy": {
                    "id": 2,
                    "userName": "pjones+analyst@threatconnect.com",
                    "firstName": "Patrick",
                    "lastName": "Jones",
                    "pseudonym": "patjones",
                    "role": "User"
                },
                "owner": "Example Organization",
                "ownerId": 7
            },
            {...}
      ],
      "status": "Success"
    }


Retrieve a Single Case
^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Case, use a query in the following format:

.. code::

    GET /v3/cases/{caseId}

For example, the following query will return information about the Case with ID 3:

.. code::

    GET /v3/cases/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "xid": "c3c3c3c3-c3c3-c3c3-c3c3-c3c3c3c3c3c3",
            "name": "Phishing Investigation",
            "description": "Case to investigate new phishing threat",
            "dateAdded": "2021-04-09T14:41:27.622Z",
            "caseOpenTime": "2021-04-09T14:41:27.622Z",
            "caseOpenUser": {
                "id": 1,
                "userName": "jsmith@threatconnect.com",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "johnsmith",
                "role": "User"
            },
            "status": "Open",
            "severity": "Medium",
            "resolution": "Not Specified",
            "assignee": {
                "type": "Group",
                "data": {
                    "id": 1,
                    "name": "SOC Team",
                    "description": "Main SOC users",
                }
            },
            "createdBy": {
                "id": 1,
                "userName": "jsmith@threatconnect.com",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "johnsmith",
                "role": "User"
            },
            "owner": "Example Organization",
            "ownerId": 7
        },
        "status": "Success"
    }


Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
