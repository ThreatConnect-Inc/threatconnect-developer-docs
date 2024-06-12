Update Intelligence Requirements
--------------------------------

Send a request in the following format to update a specific IR. Note that ``{intelRequirementId}`` represents the value of the ``id`` field for an IR, not the value of the ``uniqueId`` field.

**Example Request**

.. code::

    PUT /v3/intelRequirements/{intelRequirementId}
    Content-Type: application/json

    {
        "<fieldName>": <fieldValue>
    }

For example, the following request will update the keywords used in the keyword query for the IR whose ID is 10 and associate the IR to the Group whose ID is 15:

.. warning::
    When updating the keywords used in an IR's keyword query, the keywords specified within the ``keywordSections`` field will replace all existing keywords used in the query.

.. hint::
    To include the ``associatedGroups`` field in the response body, append ``?fields=associatedGroups`` to the end of the request URI.

**Request**

.. code::

    PUT /v3/intelRequirements/10
    Content-Type: application/json
    
    {
        "associatedGroups": {
            "data": [
                {
                    "id": 15
                }
            ]
        },
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
                    },
                    {
                        "value": "medical device"
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

        ]
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
            "lastModified": "2023-09-18T14:24:06Z",
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
                        },
                        {
                            "value":  "medical device"
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
        "message": "Updated",
        "status": "Success"
    }