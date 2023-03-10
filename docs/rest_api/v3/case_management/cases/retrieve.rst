Retrieve Cases
--------------

Retrieve All Cases
^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Cases:

.. code::

    GET /v3/cases

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "xid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
                "name": "Phishing Investigation",
                "dateAdded": "2021-04-09T14:41:27.622Z",
                "caseOpenTime": "2021-04-09T14:41:27.622Z",
                "caseOpenUser": {
                    "id": 3,
                    "userName": "11112222333344445555"
                },
                "status": "Open",
                "severity": "Low",
                "resolution": "Not Specified",
                "assignee": {
                    "type": "User",
                    "data": {
                        "id": 1,
                        "userName": "smithj@threatconnect.com"
                    }
                },
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555"
                },
                "owner": "Demo Organization",
                "ownerId": 1
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
                    "userName": "pjones+analyst@threatconnect.com"
                },
                "status": "Open",
                "severity": "Critical",
                "resolution": "Not Specified",
                "createdBy": {
                    "id": 2,
                    "userName": "pjones+analyst@threatconnect.com"
                },
                "owner": "Demo Organization",
                "ownerId": 1
            },
            {...}
        ],
        "status": "Success"
    }

.. attention::
    Only Cases to which your API user account has viewing access will be included in the API response.

Retrieve a Specific Case
^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Case:

.. code::

    GET /v3/cases/{caseId}

For example, the following request will retrieve data for the Case whose ID is 3:

.. code::

    GET /v3/cases/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "xid": "c3c3c3c3-c3c3-c3c3-c3c3-c3c3c3c3c3c3",
            "name": "Analyze Suspicious Email and Report Findings",
            "dateAdded": "2021-04-09T14:41:27.622Z",
            "caseOpenTime": "2021-04-09T14:41:27.622Z",
            "caseOpenUser": {
                "id": 1,
                "userName": "smithj@threatconnect.com"
            },
            "status": "Open",
            "severity": "Medium",
            "resolution": "Not Specified",
            "assignee": {
                "type": "Group",
                "data": {
                    "id": 1,
                    "name": "SOC Team",
                    "description": "Members of the SOC team.",
                }
            },
            "createdBy": {
                "id": 1,
                "userName": "smithj@threatconnect.com"
            },
            "owner": "Demo Organization",
            "ownerId": 1
        },
        "status": "Success"
    }