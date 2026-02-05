Retrieve Intelligence Requirements
----------------------------------

Retrieve All Intelligence Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all IRs:

**Request**

.. code::

    GET /v3/intelRequirements

**Response**

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmith",
                    "owner": "Demo Organization"
                },
                "lastModified": "2023-08-29T14:58:55Z",
                "webLink": "https://app.threatconnect.com/#/details/intel-requirements/1/overview",
                "dateAdded": "2023-08-29T13:18:01Z",
                "uniqueId": "IR-001",
                "requirementText": "Double Secret Probation",
                "subtype": {
                    "name": "Intelligence Requirement (IR)",
                    "description": "Threats of overall concern to the organization (e.g., cyber, fraud, geopolitical/physical threats)"
                },
                "category": {
                    "name": "CISO Priorities",
                    "description": "IRs prioritized for the CISO"
                },
                "description": "Keeping an eye on Delta House",
                "keywordSections": [
                    {
                        "compareValue": "includes",
                        "keywords": [
                            {
                                "value": "Higher Education"
                            }
                        ]
                    }
                ],
                "resultsLink": "https://app.threatconnect.com/v3/intelRequirements/results?tql=intelReqId=1",
                "active": true
            },
            {
                "id": 2,
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmith",
                    "owner": "Demo Organization"
                },
                "lastModified": "2023-08-29T14:54:44Z",
                "webLink": "https://app.threatconnect.com/#/details/intel-requirements/2/overview",
                "dateAdded": "2023-08-29T13:23:15Z",
                "uniqueId": "IR-002",
                "requirementText": "SHINRA",
                "subtype": {
                    "name": "Priority Intelligence Requirement (PIR)",
                    "description": "Focus on threat actors' motives, TTPs, targeting, impact, or attribution in association with IRs"
                },
                "description": "Intel on Shinra Electric Corp",
                "keywordSections": [
                    {
                        "compareValue": "includes",
                        "keywords": [
                            {
                                "value": "Electric"
                            },
                            {
                                "value": "Electric Infrastructure"
                            },
                            {
                                "value": "Grid Infrastructure"
                            },
                            {
                                "value": "Electric Grid"
                            }
                        ]
                    }
                ],
                "resultsLink": "https://app.threatconnect.com/v3/intelRequirements/results?tql=intelReqId=2",
                "active": true
            },
            ...
        ],
        "status": "Success"
    }

Retrieve a Specific Intelligence Requirement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific IR. Note that ``{id}`` represents the value of the ``id`` field for an IR, not the value of the ``uniqueId`` field.

**Example Request**

.. code::

    GET /v3/intelRequirements/{id}

For example, the following request will retrieve data for the IR whose ID is 10:

**Request**

.. code::

    GET /v3/intelRequirements/10

**Response**

.. code:: json

    {
        "data": {
            "id": 10,
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "lastModified": "2023-09-18T14:06:26Z",
            "webLink": "https://app.threatconnect.com/#/details/intel-requirements/10/overview",
            "dateAdded": "2023-09-18T14:06:24Z",
            "uniqueId": "IR-010",
            "requirementText": "Threats to Medical Device Companies",
            "subtype": {
                "name": "Intelligence Requirement (IR)",
                "description": "Threats of overall concern to the organization (e.g., cyber, fraud, geopolitical/physical threats)"
            },
            "category": {
                "name": "CISO Priorities",
                "description": "IRs prioritized for the CISO"
            },
            "description": "This IR is used to track threats to medical device companies.",
            "keywordSections": [
                {
                    "compareValue": "includes",
                    "keywords": [
                        {
                            "value": "medical device companies"
                        },
                        {
                            "value": "healthcare"
                        },
                        {
                            "value": "mangled spider"
                        },
                        {
                            "value":  "threats to medical"
                        }    
                    ]
                },
                {
                    "compareValue": "excludes",
                    "keywords": [
                        {
                            "value": "mrap"
                        }    
                    ]
                }
            ],
            "resultsLink": "https://app.threatconnect.com/v3/intelRequirements/results?tql=intelReqId=10",
            "active": true
        },
        "status": "Success"
    }