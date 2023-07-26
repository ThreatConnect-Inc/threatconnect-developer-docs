Include Additional Fields in API Responses
------------------------------------------

Overview
^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to include additional fields that are not included in the API response by default.

To use the fields query parameter, append ``?fields={fieldName}`` to the end of the request URL. To include multiple fields in the API response, separate each key-value pair with an ampersand (``&``). For example, to include data for associated Groups and Tags in an API response, append ``?fields=associatedGroups&fields=tags`` to the end of the request URL.


Retrieve a List of Available Fields for an Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve a list of fields you can include in responses returned from an object's endpoint:

.. code::

  OPTIONS /v3/{objectType}/fields

For example, the following request will retrieve a list of fields you can include in responses returned from the ``/v3/indicators`` endpoint:

.. code::

    OPTIONS /v3/indicators/fields

JSON Response

.. code:: json

    {
        "data": [
            {
                "description": "Includes artifacts with a relationship to the indicator",
                "includedByDefault": false,
                "name": "associatedArtifacts"
            },
            {
                "description": "Includes cases with a relationship to the indicator",
                "includedByDefault": false,
                "name": "associatedCases"
            },
            {
                "description": "Includes groups related to the indicator",
                "includedByDefault": false,
                "name": "associatedGroups"
            },
            {
                "description": "Includes indicators related to the indicator",
                "includedByDefault": false,
                "name": "associatedIndicators"
            },
            {
                "description": "Includes attributes related to the indicator",
                "includedByDefault": false,
                "name": "attributes"
            },
            {
                "description": "Includes DNS resolution data related to the Host indicators",
                "includedByDefault": false,
                "name": "dnsResolution"
            },
            {
                "description": "Includes Enrichment data related to the indicator",
                "includedByDefault": false,
                "name": "enrichment"
            },
            {
                "description": "Includes the False Positives fields falsePositives and lastFalsePositive",
                "includedByDefault": false,
                "name": "falsePositives"
            },
            {
                "description": "Includes indicators related to the indicator by file action",
                "includedByDefault": false,
                "name": "fileActions"
            },
            {
                "description": "Includes file occurrences related to the indicator",
                "includedByDefault": false,
                "name": "fileOccurrences"
            },
            {
                "description": "Includes the following fields, over-writing the custom field names: value1, value2, and value3",
                "includedByDefault": false,
                "name": "genericCustomIndicatorValues"
            },
            {
                "description": "Includes GEO location information related to the Host and IP indicators",
                "includedByDefault": false,
                "name": "geoLocation"
            },
            {
                "description": "Includes investigation links related to the indicator type",
                "includedByDefault": false,
                "name": "investigationLinks"
            },
            {
                "description": "Includes the Observations fields observations and lastObserved",
                "includedByDefault": false,
                "name": "observations"
            },
            {
                "description": "Includes security labels related to the indicator",
                "includedByDefault": false,
                "name": "securityLabels"
            },
            {
                "description": "Includes tags related to the indicator",
                "includedByDefault": false,
                "name": "tags"
            },
            {
                "description": "Includes the Threat Assess fields threatAssessRating, threatAssessScore, and threatAssessConfidence",
                "includedByDefault": false,
                "name": "threatAssess"
            },
            {
                "description": "Includes Observations and False Positive stats of tracked users",
                "includedByDefault": false,
                "name": "trackedUsers"
            },
            {
                "description": "Includes WhoIs information related to the Host indicators",
                "includedByDefault": false,
                "name": "whoIs"
            }
        ],
        "count": 18,
        "status": "Success"
    }

Example Requests
^^^^^^^^^^^^^^^^

This section provides example requests demonstrating sample use cases for the ``fields`` query parameter.

Include Tags Applied to a Group
===============================

The following request will retrieve data for the Group whose ID is 11, including standard and ATT&CK® Tags applied to the Group:

.. code::

  GET /v3/groups/11?fields=tags

JSON Response

.. code:: json

    {
        "data": {
            "id": 18,
            "dateAdded": "2023-03-31T18:29:12Z",
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/#/details/groups/11/overview",
            "tags": {
                "data": [
                    {
                        "id": 475,
                        "name": "Phishing",
                        "description": "Adversaries may send phishing messages to gain access to victim systems. All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass malware spam campaigns.\n\nAdversaries may send victims emails containing malicious attachments or links, typically to execute malicious code on victim systems. Phishing may also be conducted via third-party services, like social media platforms. Phishing may also involve social engineering techniques, such as posing as a trusted source, as well as evasive techniques such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., [Email Hiding Rules](https://attack.mitre.org/techniques/T1564/008)).(Citation: Microsoft OAuth Spam 2022)(Citation: Palo Alto Unit 42 VBA Infostealer 2014) Another way to accomplish this is by forging or spoofing(Citation: Proofpoint-spoof) the identity of the sender which can be used to fool both the human recipient as well as automated security tools.(Citation: cyberproof-double-bounce) \n\nVictims may also receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware,(Citation: sygnia Luna Month)(Citation: CISA Remote Monitoring and Management Software) or install adversary-accessible remote management tools onto their computer (i.e., [User Execution](https://attack.mitre.org/techniques/T1204)).(Citation: Unit42 Luna Moth)",
                        "lastUsed": "2023-07-06T18:08:17Z",
                        "techniqueId": "T1566",
                        "platforms": {
                            "data": [
                                "Linux",
                                "macOS",
                                "Windows",
                                "SaaS",
                                "Office 365",
                                "Google Workspace"
                            ],
                            "count": 6
                        }
                    },
                    {
                        "id": 9,
                        "name": "Ransomware",
                        "description": "Apply this Tag to objects involved in ransomware attacks.",
                        "lastUsed": "2023-07-06T18:08:17Z"
                    }
                ]
            },
            "type": "Adversary",
            "name": "Bad Guy",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "upVoteCount": "0",
            "downVoteCount": "0",
            "lastModified": "2023-07-06T18:08:17Z",
            "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=11"
        },
        "status": "Success"
    }

ATT&CK Tags will include an additional ``techniqueId`` field in the response object. This field specifies the ID of the MITRE ATT&CK® technique or sub-technique that the Tag represents.

Include an Indicator's Tags, ThreatAssess Information, and Associated Groups
============================================================================

The following request will retrieve data the Indicator whose ID is 4, including Tags applied to the Indicator, ThreatAssess information for the Indicator, and Groups associated to the Indicator:

.. code::

  GET /v3/indicators/4?fields=tags&fields=threatAssess&fields=associatedGroups

JSON Response

.. code:: json

    {
        "data": {
            "id": 4,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2023-01-26T21:00:03Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/4/overview",
            "tags": {
                "data": [
                    {
                        "id": 11,
                        "name": "Targeted Attack",
                        "lastUsed": "2023-01-30T17:58:56Z"
                    },
                    {
                        "id": 13,
                        "name": "Created via API",
                        "description": "Apply this Tag to objects created via the ThreatConnect API.",
                        "lastUsed": "2023-01-30T18:39:32Z"
                    },
                    {
                        "id": 17,
                        "name": "Russia",
                        "lastUsed": "2023-01-27T14:25:55Z"
                    }
                ]
            },
            "type": "Host",
            "lastModified": "2023-01-27T14:25:55Z",
            "rating": 5.00,
            "confidence": 65,
            "threatAssessRating": 4.5,
            "threatAssessConfidence": 58.0,
            "threatAssessScore": 678,
            "threatAssessScoreObserved": 139,
            "threatAssessScoreFalsePositive": -167,
            "summary": "ultrabadguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {
                "data": [
                    {
                        "id": 12,
                        "ownerId": 2,
                        "ownerName": "Demo Source",
                        "dateAdded": "2023-01-26T21:00:03Z",
                        "webLink": "https://app.threatconnect.com/#/details/groups/12/overview",
                        "type": "Adversary",
                        "name": "Bad Guy",
                        "createdBy": {
                            "id": 3,
                            "userName": "11112222333344445555",
                            "firstName": "John",
                            "lastName": "Smith",
                            "pseudonym": "jsmithAPI",
                            "owner": "Demo Organization"
                        },
                        "upVoteCount": "0",
                        "downVoteCount": "0",
                        "lastModified": "2023-01-26T21:00:04Z",
                        "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=12"
                    }
                ]
            },
            "hostName": "ultrabadguy.com",
            "dnsActive": false,
            "whoisActive": true,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
        },
        "status": "Success"
    }

.. attention::
    When sending a request to the ``/v3/indicators`` endpoint with ``?fields=threatAssess`` appended to the end of the request URL, the following fields will be included in the API response:

    - ``threatAssessRating``
    - ``threatAssessConfidence``
    - ``threatAssessScore``
    - ``threatAssessScoreObserved``
    - ``threatAssessScoreFalsePositive``

    It is recommended to not use the ``threatAssessRating`` and ``threatAssessConfidence`` fields and their values, as these are legacy fields.

Include Observations and False Positives Reported by API Users
==============================================================

The following request will retrieve data for the Indicator whose ID is 4, including observations and false positives reported by API users in the Organization:

.. code::

    GET /v3/indicators/4?fields=trackedUsers

JSON Response

.. code::

    {
        "data": {
            "id": 4,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2023-01-26T21:00:03Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/4/overview",
            "type": "Host",
            "lastModified": "2023-01-27T14:25:55Z",
            "rating": 5.00,
            "summary": "ultrabadguy.com",
            "trackedUsers": {
                "John Smith": {
                    "observations": 5,
                    "lastObserved": "2023-01-27T03:16:30Z",
                    "falsePositives": 1,
                    "lastFalsePositive": "2023-01-27T00:00:00Z"
                }
            },
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "hostName": "ultrabadguy.com",
            "dnsActive": false,
            "whoisActive": false,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
        },
        "status": "Success"
    }

Include Additional Association Levels for a Field
=================================================

When using the ``fields`` query parameter, you can request additional association levels for a field by appending ``.{fieldName}`` to the field's name. 

For example, the following request will retrieve data for the Indicator whose ID is 4 and include Groups associated to the Indicator and Attributes added to those Groups in the response. To accomplish this, ``?fields=associatedGroups.attributes`` is appended to the end of the request URL.

.. code::

  GET /v3/indicators/4?fields=associatedGroups.attributes

JSON Response

.. code:: json

    {
        "data": {
            "id": 4,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2023-01-26T21:00:03Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/4/overview",
            "type": "Host",
            "lastModified": "2023-01-27T14:25:55Z",
            "rating": 5.00,
            "confidence": 65,
            "summary": "ultrabadguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {
                "data": [
                    {
                        "id": 12,
                        "ownerId": 2,
                        "ownerName": "Demo Source",
                        "dateAdded": "2023-01-26T21:00:03Z",
                        "webLink": "https://app.threatconnect.com/#/details/groups/12/overview",
                        "type": "Adversary",
                        "name": "Bad Guy",
                        "createdBy": {
                            "id": 3,
                            "userName": "11112222333344445555",
                            "firstName": "John",
                            "lastName": "Smith",
                            "pseudonym": "jsmithAPI",
                            "owner": "Demo Organization"
                        },
                        "upVoteCount": "0",
                        "downVoteCount": "0",
                        "attributes": {
                            "data": [
                                {
                                    "id": 10,
                                    "dateAdded": "2023-02-02T18:26:06Z",
                                    "type": "Adversary Type",
                                    "value": "This is a very bad Adversary type.",
                                    "createdBy": {
                                        "id": 3,
                                        "userName": "11112222333344445555",
                                        "firstName": "John",
                                        "lastName": "Smith",
                                        "pseudonym": "jsmithAPI",
                                        "owner": "Demo Organization"
                                    },
                                    "lastModified": "2023-02-02T18:26:06Z",
                                    "pinned": true,
                                    "default": true
                                }
                            ]
                        },
                        "lastModified": "2023-02-02T18:26:06Z",
                        "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=12"
                    }
                ]
            },
            "hostName": "ultrabadguy.com",
            "dnsActive": false,
            "whoisActive": true,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
        },
        "status": "Success"
    }

By default, you can retrieve only **one association level at a time**. To retrieve more than one association level at a time, contact your System Administrator and have them complete one of the following actions:

  - Enable the **Allow User to Exceed API Link Limit** setting on your API user account. Instructions for enabling this setting are available in the `"Creating an API User Account" section of the Creating User Accounts <https://knowledge.threatconnect.com/docs/creating-user-accounts#creating-an-api-user>`_ knowledge base article.
  - Update the v3 API link limit in system settings to allow for more than one association level to be retrieved at a time.

The following example demonstrates how to retrieve two association levels in a single request. The request will retrieve data for the Indicator whose ID is 4 and include the following data in the API response:

- Groups associated to the Indicator
- Attributes added to those Groups (the first association level)
- Security Labels applied to those Attributes (the second association level)

To accomplish this, ``?fields=associatedGroups.attributes.securityLabels`` is appended to the end of the request URL.

.. code::

  GET /v3/indicators/4?fields=associatedGroups.attributes.securityLabels

JSON Response

.. code:: json

    {
        "data": {
            "id": 4,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2023-01-26T21:00:03Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/4/overview",
            "type": "Host",
            "lastModified": "2023-01-27T14:25:55Z",
            "rating": 5.00,
            "confidence": 65,
            "summary": "ultrabadguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {
                "data": [
                    {
                        "id": 12,
                        "ownerId": 2,
                        "ownerName": "Demo Source",
                        "dateAdded": "2023-01-26T21:00:03Z",
                        "webLink": "https://app.threatconnect.com/#/details/groups/12/overview",
                        "type": "Adversary",
                        "name": "Bad Guy",
                        "createdBy": {
                            "id": 3,
                            "userName": "11112222333344445555",
                            "firstName": "John",
                            "lastName": "Smith",
                            "pseudonym": "jsmithAPI",
                            "owner": "Demo Organization"
                        },
                        "upVoteCount": "0",
                        "downVoteCount": "0",
                        "attributes": {
                            "data": [
                                {
                                    "id": 10,
                                    "dateAdded": "2023-02-02T18:26:06Z",
                                    "securityLabels": {
                                        "data": [
                                            {
                                                "id": 3,
                                                "name": "TLP:AMBER",
                                                "description": "This security label is used for information that requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved. Information with this label can be shared with members of an organization and its clients.",
                                                "color": "FFC000",
                                                "owner": "System",
                                                "dateAdded": "2016-08-31T00:00:00Z"
                                            }
                                        ]
                                    },
                                    "type": "Adversary Type",
                                    "value": "This is a very bad Adversary type.",
                                    "createdBy": {
                                        "id": 3,
                                        "userName": "11112222333344445555",
                                        "firstName": "John",
                                        "lastName": "Smith",
                                        "pseudonym": "jsmithAPI",
                                        "owner": "Demo Organization"
                                    },
                                    "lastModified": "2023-02-02T18:26:06Z",
                                    "pinned": true,
                                    "default": true
                                }
                            ]
                        },
                        "lastModified": "2023-02-02T18:26:06Z",
                        "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=12"
                    }
                ]
            },
            "hostName": "ultrabadguy.com",
            "dnsActive": false,
            "whoisActive": true,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
        },
        "status": "Success"
    }

Include Details About the User Who Created an Object
====================================================

Responses for some objects include a ``createdBy`` field, which includes subfields that provide details about the user who created the object. By default, the ``createdBy`` field includes the following subfields:

- ``id``
- ``username``
- ``firstName``
- ``lastName``
- ``pseudonym``
- ``owner``

To include more details about the user that created an object, append ``?fields=userDetails`` to the end of the request URL. Note that additional subfields will be included within the ``createdBy`` field only for API users with Read permission for user accounts (i.e., API user accounts with an Organization role of Organization Administrator).

For example, the following request will retrieve data for the Group whose ID is 12 and return additional details about the user who created the Group.

.. code::

  GET /v3/groups/12?fields=userDetails

JSON Response (Without Read Permissions)

.. code:: json
    
    {
        "data": {
            "id": 12,
            "ownerId": 2,
            "ownerName": "Demo Source",
            "dateAdded": "2023-01-26T21:00:03Z",
            "webLink": "https://app.threatconnect.com/#/details/groups/12/overview",
            "type": "Adversary",
            "name": "Bad Guy",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization",
            },
            "upVoteCount": "0",
            "downVoteCount": "0",
            "lastModified": "2023-02-02T18:26:06Z",
            "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=12"
        },
        "status": "Success"
    }

JSON Response (With Read Permissions)

.. code:: json
    
    {
        "data": {
            "id": 12,
            "ownerId": 2,
            "ownerName": "Demo Source",
            "dateAdded": "2023-01-26T21:00:03Z",
            "webLink": "https://app.threatconnect.com/#/details/groups/12/overview",
            "type": "Adversary",
            "name": "Bad Guy",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization",
                "lastPasswordChange": "2022-10-13T14:31:59Z",
                "termsAccepted": false,
                "logoutIntervalMinutes": 30,
                "systemRole": "Api User",
                "ownerRoles": {
                    "Demo Community": "Director",
                    "Demo Organization": "Organization Administrator",
                    "Demo Source": "Director"
                },
                "disabled": false,
                "locked": false,
                "passwordResetRequired": false,
                "twoFactorResetRequired": false
            },
            "upVoteCount": "0",
            "downVoteCount": "0",
            "lastModified": "2023-02-02T18:26:06Z",
            "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=12"
        },
        "status": "Success"
    }

Combine the "tql" and "fields" Query Parameters
===============================================

You can combine the ``tql`` and ``fields`` query parameters in a single API request, allowing you to `filter results using ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_ and include additional fields in the API response.

For example, the following request will retrieve data for all Indicators with a Threat Rating greater than or equal to 4 and include data for Tags and Attributes added to each Indicator in the API response.

Request (Decoded URL)

.. code::

  GET /v3/indicators?tql=rating GEQ 4&fields=tags&fields=attributes

Request (Encoded URL)

.. code::

  GET /v3/indicators?tql=rating%20GEQ%204&fields=tags&fields=attributes

.. note::
    Depending on the tool you are using to interact with the ThreatConnect API, it may be necessary to encode the request URL manually if it includes query parameters. For example, some tools may accept ``/v3/indicators?tql=ownerName GEQ 4&fields=tags&fields=attributes`` as a valid request URL and encode it automatically, while others may require you to encode the request URL manually. If you send a request with query parameters and a **401 Unauthorized** error is returned, verify whether the request URL is encoded properly for the API tool you are using.

----

*MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation.*