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
                "dateAdded": "2023-03-09T14:41:27.622Z",
                "lastUpdated": "2023-03-09T14:41:27.622Z",
                "caseOpenTime": "2023-03-09T14:41:27.622Z",
                "caseOpenUser": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "owner": "Demo Organization"
                },
                "detectionOverdue": false,
                "responseOverdue": false,
                "status": "Open",
                "severity": "Low",
                "resolution": "Not Specified",
                "assignee": {
                    "type": "User",
                    "data": {
                        "id": 1,
                        "userName": "smithj@threatconnect.com",
                        "firstName": "John",
                        "lastName": "Smith",
                        "pseudonym": "JMS",
                        "owner": "Demo Organization"
                    }
                },
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "owner": "Demo Organization"
                },
                "owner": "Demo Organization",
                "ownerId": 1
            }, 
            {
                "id": 2,
                "xid": "b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2",
                "name": "Malware Investigation",
                "description": "Case to investigate new malware",
                "dateAdded": "2025-04-09T09:51:54Z",
                "lastUpdated": "2025-04-09T09:55:54Z",
                "caseOpenTime": "2025-04-09T09:51:54Z",
                "caseCloseTime": "2025-04-09T09:55:45Z",
                "caseOpenUser": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "JMS",
                    "owner": "Demo Organization"
                },
                "caseCloseUser": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "JMS",
                    "owner": "Demo Organization"
                },
                "caseOccurrenceTime": "2025-04-09T09:20:00Z",
                "caseOccurrenceUser": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "JMS",
                    "owner": "Demo Organization"
                },
                "caseDetectionTime": "2025-04-09T09:53:43Z",
                "caseDetectionUser": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "JMS",
                    "owner": "Demo Organization"
                },
                "detectionDue": "2025-04-09T09:50:00Z",
                "timeToDetect": 2023,
                "detectionOverdue": true,
                "responseDue": "2025-04-09T10:21:54Z",
                "timeToRespond": 230,
                "responseOverdue": false,
                "status": "Closed",
                "severity": "Critical",
                "resolution": "Deferred / Delayed",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "JMS",
                    "owner": "Demo Organization"
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
            "dateAdded": "2023-03-19T14:41:27.622Z",
            "lastUpdated": "2023-03-21T09:22:39.622Z",
            "caseOpenTime": "2023-03-09T14:41:27.622Z",
            "caseOpenUser": {
                "id": 1,
                "userName": "smithj@threatconnect.com",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "JMS",
                "owner": "Demo Organization"
            },
            "detectionOverdue": false,
            "responseOverdue": false,
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
                "userName": "smithj@threatconnect.com",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "JMS",
                "owner": "Demo Organization"
            },
            "owner": "Demo Organization",
            "ownerId": 1
        },
        "status": "Success"
    }