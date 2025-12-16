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
                "description": "Includes the name of the association if this indicator is part of an association with another indicator",
                "includedByDefault": false,
                "name": "associationName"
            },
            {
                "description": "Includes attributes related to the indicator",
                "includedByDefault": false,
                "name": "attributes"
            },
            {
                "description": "Includes indicators with custom associations to the indicator",
                "includedByDefault": false,
                "name": "customAssociations"
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
                "description": "Includes date fields defined in external applications",
                "includedByDefault": false,
                "name": "externalDates"
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
                "description": "Includes date fields specific to the sighting reported",
                "includedByDefault": false,
                "name": "sightings"
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
        "count": 23,
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
                        "techniqueId": "T1566"
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

Include an Indicator's CAL and ThreatAssess Information
=======================================================

The following request will retrieve data for the Indicator whose ID is 4, including CAL™ and ThreatAssess information for the Indicator:

.. code::

  GET /v3/indicators/4?fields=threatAssess

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
            "threatAssessRating": 4.0,
            "threatAssessConfidence": 0.0,
            "threatAssessScore": 405,
            "threatAssessScoreObserved": 0,
            "threatAssessScoreFalsePositive": 0,
            "calScore": 410,
            "summary": "ultrabadguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "hostName": "ultrabadguy.com",
            "dnsActive": false,
            "whoisActive": true,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
        },
        "status": "Success"
    }

.. attention::
    It is recommended to ignore the ``threatAssessRating`` and ``threatAssessConfidence`` fields and their values, as these are legacy fields.

Include an Indicator's Tags and Associated Groups
=================================================

The following request will retrieve data the Indicator whose ID is 4, including Tags applied to the Indicator and Groups associated to the Indicator:

.. code::

  GET /v3/indicators/4?fields=tags&fields=associatedGroups

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

Include Observations For an Indicator
=====================================

The following request will retrieve data for the **ultrabadguy.com** Host Indicator in the API user's Organization, including the number of times the Indicator has been observed and the date and time when it was last observed:

.. code::

    GET /v3/indicators/ultrabadguy.com?fields=observations

JSON Response

.. code::

    {
        "data": {
            "id": 4,
            "dateAdded": "2023-01-26T21:00:03Z ",
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/#/details/indicators/4",
            "type": "Host",
            "lastModified": "2023-01-27T14:25:55Z ",
            "rating": 4.00,
            "confidence": 51,
            "source": "Host used by hacker conglomerate tracked to Iran.",
            "description": "Indicator associated with malware-connected VPN network.",
            "summary": "ultrabadguy.com",
            "observations": 5,
            "lastObserved": "2023-01-27T03:16:30Z",
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

Include False Positive Reports For an Indicator
===============================================

The following request will retrieve data for the **ultrabadguy.com** Host Indicator in the API user's Organization, including the number of times the Indicator was reported as a false positive and the date and time when it was last reported as a false positive:

.. code::

    GET /v3/indicators/ultrabadguy.com?fields=falsePositives

JSON Response

.. code::

    {
        "data": {
            "id": 4,
            "dateAdded": "2023-01-26T21:00:03Z ",
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/#/details/indicators/4",
            "type": "Host",
            "lastModified": "2023-01-27T14:25:55Z ",
            "rating": 4.00,
            "confidence": 51,
            "source": "Host used by hacker conglomerate tracked to Iran.",
            "description": "Indicator associated with malware-connected VPN network.",
            "summary": "ultrabadguy.com",
            "falsePositives": 2,
            "lastFalsePositive": "2023-01-27T00:00:00Z",
            "falsePositiveReportedByUser": false,
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

Include Sightings and External Timestamps
=========================================

When working with Groups and Indicators, you can specify details about when the object was first and last seen. You can also provide external date and time information for the object, including when it was created, when it was last modified, and when it expires externally.

The following request will retrieve data for the Group whose ID is 20, including when it was first and last seen (``sightings``) and external date and time information for the Group (``externalDates``):

.. code::

    GET /v3/groups/20?fields=sightings&fields=externalDates

JSON Response

.. code::

    {
        "data": {
            "id": 20,
            "dateAdded": "2023-08-25T12:44:47Z",
            "ownerId": 3,
            "ownerName": "Demo Source",
            "webLink": "https://app.threatconnect.com/#/details/groups/20/overview",
            "type": "Adversary",
            "name": "Nefarious",
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
            "externalDateAdded": "2023-08-25T18:23:43Z",
            "externalLastModified": "2023-08-26T18:23:43Z",
            "externalDateExpires": "2023-08-30T18:23:43Z",
            "firstSeen": "2023-08-25T18:23:43Z",
            "lastSeen": "2023-08-26T18:23:43Z",
            "lastModified": "2023-09-25T12:44:47Z",
            "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=20"
        },
        "status": "Success"
    }

Include an AI Summary of a Group
================================

Artificial intelligence (AI) summaries may be generated for Document and Report Groups in ThreatConnect. Using the v3 API, you can retrieve a Group's AI summary, if one is available.

Depending on how a Group's AI summary was generated, you can retrieve the AI summary by assigning the ``fields`` query parameter one of the following values:

- ``AIsummary``: Use this value if the Group has a user-generated AI summary (that is, a user clicked **Generate** on the **AI insights** card on the Group's **Details** screen to generate the AI summary).
- ``insights``: Use this value if the Group has an AI summary generated by CAL Doc Analysis.

In the following example, the request will retrieve data for the Report Group whose ID is 213638, including an AI summary generated by CAL Doc Analysis:

.. code::

    GET /v3/groups/213638?fields=insights

JSON Response

.. code::

    {
        "data": {
            "id": 213638,
            "dateAdded": "2024-02-13T19:21:55Z",
            "ownerId": 284,
            "ownerName": "CAL Automated Threat Library",
            "webLink": "https://app.threatconnect.com/#/details/groups/213638",
            "type": "Report",
            "xid": "0b6925305b9b934bc0255a380023530be74245b4c8e9cfe282b993cb6e9e7d32",
            "name": "CSC Partners With NetDiligence to Help Mitigate Cyber Risks",
            "createdBy": {
                "userName": "ApiUser-cal_automated_threat_library",
                "firstName": "ApiUser",
                "lastName": "CAL Automated Threat Library",
                "owner": "CAL Automated Threat Library"
            },
            "upVoteCount": "0",
            "downVoteCount": "0",
            "generatedReport": false,
            "fileName": "None",
            "status": "Awaiting Upload",
            "documentType": "Unrecognized",
            "insights": {
                "summary": "CSC, an enterprise-class domain registrar and leader in mitigating domain security, DNS, and digital brand threats, has partnered with NetDiligence, a leader in cyber risk readiness and response solutions, to provide domain security and digital brand protection solutions to the cyber insurance industry. The partnership will provide cyber insurance carriers, brokers, and clients with new ways to address risk and cyber threats such as phishing, business email compromise, and ransomware. The blog highlights the importance of domain security and digital brand protection for corporations operating multiple brands with hundreds or thousands of domains within their portfolios.",
                "app": "TextSummarizer",
                "bullets": [
                    "The blog announces CSC's partnership with NetDiligence, a leader in cyber risk readiness and response solutions, to provide domain security and digital brand protection solutions to the cyber insurance industry.",
                    "CSC's innovative technology allows cyber insurance carriers, brokers, and clients to proactively protect their businesses against cyber threats and online brand abuse.",
                    "The partnership will provide cyber insurance carriers, brokers, and clients with new ways to address risk and cyber threats such as phishing, business email compromise, and ransomware.",
                    "The blog highlights the importance of domain security and digital brand protection for corporations operating multiple brands with hundreds or thousands of domains within their portfolios.",
                    "CSC's solutions will be categorized into three services: digital brand protection, domain registrar services, and fraud protection, within the eRiskHub platform.",
                    "CSC's Chief Technology Officer Ihab Shraim and AXA XL's Gwenn Cujdik will be speaking on the Pathways to Resilience panel, Domain Security: Addressing Cybersecurity at the Source of the Problem."
                ]
            },
            "documentDateAdded": "2024-02-13T19:21:56Z",
            "publishDate": "2024-02-12T00:00:00Z",
            "lastModified": "2024-02-13T19:21:55Z",
            "legacyLink": "https://app.threatconnect.com/auth/report/report.xhtml?report=213638"
        },
        "status": "Success"
    }

.. attention::
    Artificial intelligence (AI) summarizers use algorithms and AI to condense text into shorter summaries, saving time and effort. However, summaries generated from non-English content may have lower accuracy than those generated from English content. 

Include Additional Association Levels for a Field
=================================================

When using the ``fields`` query parameter, you can request additional association levels for a field (e.g., requesting an object's Attributes and the Security Labels applied to the Attributes). To accomplish this, use dot notation when setting the value for the fields query parameter.

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

  - Enable the **Allow User to Exceed API Link Limit** setting on your API user account. Instructions for enabling this setting are available in the `"Creating an API User" section of Managing User Accounts <https://knowledge.threatconnect.com/docs/managing-user-accounts#creating-an-api-user>`_.
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