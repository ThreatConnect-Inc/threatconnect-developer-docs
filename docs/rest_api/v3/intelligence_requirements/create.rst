Create Intelligence Requirements
--------------------------------

Send a request in the following format to create an IR in your Organization. Note that the request body in this example includes only a subset of the fields that can be included.

**Request**

.. code::

    POST /v3/intelRequirements
    {
        "category": {
            "name": "CISO Priorities"
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
                        "value": "threats to medical"
                    }
                ],
                "sectionNumber": 0
            },
            {
                "compareValue": "excludes",
                "keywords": [
                    {
                        "value": "mrap"
                    }    
                ],
                "sectionNumber": 0
            }
        ],
        "requirementText": "Threats to Medical Device Companies",
        "subtype": {
            "id": 1
        },
        "uniqueId": "IR-010"
    }

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
            "lastModified": "2023-09-18T14:06:26Z ",
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
                            "value": "threats to medical"
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
            "resultsLink": "https://app.threatconnect.com/v3/intelRequirements/results?tql=intelReqId=10"
        },
        "message": "Created",
        "status": "Success"
    }