Unified View Data for Vulnerabilities
-------------------------------------

As of ThreatConnect 7.10, you can access a unified view for Vulnerability Groups with the same name/summary in your ThreatConnect owners. The unified view includes Common Vulnerability Scoring System (CVSS) and Known Exploited Vulnerabilities (KEV) data for all versions of a given Vulnerability.

In the v3 API, you can use the ``fields`` query parameter to include unified view data in API responses.

.. note::
    The following example requests demonstrate how to retrieve unified view data for all Vulnerability Groups in your ThreatConnect owners. You can use similar requests to retrieve unified view data for a specific Vulnerability Group.

Retrieve Unified View Data for Vulnerabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following request to retrieve unified view data for all Vulnerability Groups in your ThreatConnect owners:

Request (Decoded URL)

.. code:: http

    GET /v3/groups?tql=typeName="Vulnerability"&fields=common

Request (Encoded URL)

.. code:: http

    GET /v3/groups?tql=typeName%3D%22Vulnerability%22&fields=common

When the ``fields`` query parameter's value is set to ``common``, the following fields are included in the response body for each Vulnerability Group object if such data are available for the Group:

.. code:: json

        "commonGroup": {
            "id": 1125899906899126,
            "dateAdded": "2025-04-18T21:35:42Z",
            "name": "CVE-2020-0688",
            "summary": "Microsoft Exchange Server Validation Key Remote Code Execution Vulnerability",
            "description": "A remote code execution vulnerability exists in Microsoft Exchange software when the software fails to properly handle objects in memory, aka 'Microsoft Exchange Memory Corruption Vulnerability'.",
            "source": "secure@microsoft.com",
            "sourceURLs": [
                "http://packetstormsecurity.com/files/156592/Microsoft-Exchange-2019-15.2.221.12-Remote-Code-Execution.html",
                "http://packetstormsecurity.com/files/156620/Exchange-Control-Panel-Viewstate-Deserialization.html",
                "https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0688",
                "https://www.zerodayinitiative.com/advisories/ZDI-20-258/"
            ],
            "lastModified": "2025-06-05T22:25:59Z",
            "kevProperties": {
                "shortDescription": "Microsoft Exchange Server Validation Key fails to properly create unique keys at install time, allowing for remote code execution.",
                "product": "Exchange Server",
                "vulnerabilityName": "Microsoft Exchange Server Validation Key Remote Code Execution Vulnerability",
                "links": [
                    "https://nvd.nist.gov/vuln/detail/CVE-2020-0688"
                ],
                "vendorProject": "Microsoft",
                "knownRansomwareCampaignUse": "Known",
                "requiredAction": "Apply updates per vendor instructions.",
                "dueDate": "2022-05-03T00:00:00Z",
                "dateAdded": "2021-11-03T00:00:00Z"
            },
            "products": "secure@microsoft.com",
            "criteria": "cpe:2.3:a:microsoft:exchange_server:2010:sp3_rollup_30:*:*:*:*:*:*",
            "cvss_v2": "CVSS:2.0/AV:N/AC:L/Au:S/C:C/I:C/A:C",
            "cvss_score_v2": 9.0,
            "cvss_severity_v2": "HIGH",
            "cvss_severity_v3": "NONE",
            "cvss_v3_1": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
            "cvss_score_v3_1": 8.8,
            "cvss_severity_v3_1": "HIGH",
            "cvss_severity_v4": "NONE",
            "lastPublished": "2020-02-11T22:15:15Z",
            "externalDateAdded": "2025-04-04T19:31:36Z",
            "cvssV2Properties": {
                "Authentication (Au)": "Single",
                "Availability Impact (A)": "Complete",
                "Integrity Impact (I)": "Complete",
                "Access Vector (AV)": "Network",
                "Access Complexity (AC)": "Low",
                "Confidentiality Impact (C)": "Complete"
            },
            "cvssV3_1Properties": {
                "Privileges Required (PR)": "Low",
                "Availability Impact (A)": "High",
                "Attack Complexity (AC)": "Low",
                "Scope (S)": "Unchanged",
                "Attack Vector (AV)": "Network",
                "Integrity Impact (I)": "High",
                "Confidentiality Impact (C)": "High",
                "User Interaction (UI)": "None"
            }
        }

Retrieve Unified View Data and Linked Groups for Vulnerabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following request to retrieve unified view data for all Vulnerability Groups in your ThreatConnect owners and include details about all Vulnerability Groups with the same name/summary in your ThreatConnect owners:

Request (Decoded URL)

.. code:: http

    GET /v3/groups?tql=typeName="Vulnerability"&fields=common&fields=linkedGroups

Request (Encoded URL)

.. code:: http

    GET /v3/groups?tql=typeName%3D%22Vulnerability%22&fields=common&fields=linkedGroups

When the ``fields`` query parameter's value is set to ``common`` and ``linkedGroups``, the following fields are included in the response body for each Vulnerability Group object if such data are available for the Group:

.. code:: json

        "commonGroup": {
            "id": 1125899906899126,
            "dateAdded": "2025-04-18T21:35:42Z",
            "name": "CVE-2020-0688",
            "summary": "Microsoft Exchange Server Validation Key Remote Code Execution Vulnerability",
            "description": "A remote code execution vulnerability exists in Microsoft Exchange software when the software fails to properly handle objects in memory, aka 'Microsoft Exchange Memory Corruption Vulnerability'.",
            "source": "secure@microsoft.com",
            "sourceURLs": [
                "http://packetstormsecurity.com/files/156592/Microsoft-Exchange-2019-15.2.221.12-Remote-Code-Execution.html",
                "http://packetstormsecurity.com/files/156620/Exchange-Control-Panel-Viewstate-Deserialization.html",
                "https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0688",
                "https://www.zerodayinitiative.com/advisories/ZDI-20-258/"
            ],
            "lastModified": "2025-06-05T22:25:59Z",
            "linkedGroups": {
                "data": [
                    {
                        "id": 1125899944159843,
                        "dateAdded": "2025-04-25T09:39:08Z",
                        "ownerId": 2251799814013002,
                        "ownerName": "VulnCheck Intelligence",
                        "webLink": "https://companyabc.threatconnect.com/#/details/groups/1125899944159843",
                        "type": "Vulnerability",
                        "xid": "CVE-2020-0688",
                        "name": "CVE-2020-0688",
                        "createdBy": {
                            "userName": "ApiUser-vulncheck_intelligence",
                            "firstName": "ApiUser",
                            "lastName": "VulnCheck Intelligence",
                            "owner": "VulnCheck Intelligence"
                        },
                        "upVoteCount": "0",
                        "downVoteCount": "0",
                        "lastModified": "2025-04-25T09:39:08Z",
                        "legacyLink": "https://companyabc.threatconnect.com/auth/vulnerability/vulnerability.xhtml?vulnerability=1125899944159843"
                    }
                ]
            },
            "kevProperties": {
                "shortDescription": "Microsoft Exchange Server Validation Key fails to properly create unique keys at install time, allowing for remote code execution.",
                "product": "Exchange Server",
                "vulnerabilityName": "Microsoft Exchange Server Validation Key Remote Code Execution Vulnerability",
                "links": [
                    "https://nvd.nist.gov/vuln/detail/CVE-2020-0688"
                ],
                "vendorProject": "Microsoft",
                "knownRansomwareCampaignUse": "Known",
                "requiredAction": "Apply updates per vendor instructions.",
                "dueDate": "2022-05-03T00:00:00Z",
                "dateAdded": "2021-11-03T00:00:00Z"
            },
            "products": "secure@microsoft.com",
            "criteria": "cpe:2.3:a:microsoft:exchange_server:2010:sp3_rollup_30:*:*:*:*:*:*",
            "cvss_v2": "CVSS:2.0/AV:N/AC:L/Au:S/C:C/I:C/A:C",
            "cvss_score_v2": 9.0,
            "cvss_severity_v2": "HIGH",
            "cvss_severity_v3": "NONE",
            "cvss_v3_1": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
            "cvss_score_v3_1": 8.8,
            "cvss_severity_v3_1": "HIGH",
            "cvss_severity_v4": "NONE",
            "lastPublished": "2020-02-11T22:15:15Z",
            "externalDateAdded": "2025-04-04T19:31:36Z",
            "cvssV2Properties": {
                "Authentication (Au)": "Single",
                "Availability Impact (A)": "Complete",
                "Integrity Impact (I)": "Complete",
                "Access Vector (AV)": "Network",
                "Access Complexity (AC)": "Low",
                "Confidentiality Impact (C)": "Complete"
            },
            "cvssV3_1Properties": {
                "Privileges Required (PR)": "Low",
                "Availability Impact (A)": "High",
                "Attack Complexity (AC)": "Low",
                "Scope (S)": "Unchanged",
                "Attack Vector (AV)": "Network",
                "Integrity Impact (I)": "High",
                "Confidentiality Impact (C)": "High",
                "User Interaction (UI)": "None"
            }
        }

Retrieve Unified View Data, Linked Groups, and Linked Attributes for Vulnerabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following request to retrieve unified view data for all Vulnerability Groups in your ThreatConnect owners and include details about Vulnerability Groups with the same name/summary in your ThreatConnect owners and Attributes added to those Groups:

Request (Decoded URL)

.. code:: http

    GET /v3/groups?tql=typeName="Vulnerability"&fields=common&fields=linkedGroups&fields=linkedGroups.attributes

Request (Encoded URL)

.. code:: http

    GET /v3/groups?tql=typeName%3D%22Vulnerability%22&fields=common&fields=linkedGroups&fields=linkedGroups.attributes

When the ``fields`` query parameter's value is set to ``common``, ``linkedGroups``, and ``linkedGroups.attributes``, the following fields are included in the response body for each Vulnerability Group object if such data are available for the Group:

.. code:: json

        "commonGroup": {
            "id": 1125899906899126,
            "dateAdded": "2025-04-18T21:35:42Z",
            "name": "CVE-2020-0688",
            "summary": "Microsoft Exchange Server Validation Key Remote Code Execution Vulnerability",
            "description": "A remote code execution vulnerability exists in Microsoft Exchange software when the software fails to properly handle objects in memory, aka 'Microsoft Exchange Memory Corruption Vulnerability'.",
            "source": "secure@microsoft.com",
            "sourceURLs": [
                "http://packetstormsecurity.com/files/156592/Microsoft-Exchange-2019-15.2.221.12-Remote-Code-Execution.html",
                "http://packetstormsecurity.com/files/156620/Exchange-Control-Panel-Viewstate-Deserialization.html",
                "https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0688",
                "https://www.zerodayinitiative.com/advisories/ZDI-20-258/"
            ],
            "lastModified": "2025-06-05T22:25:59Z",
            "linkedGroups": {
                "data": [
                    {
                        "id": 1125899944159843,
                        "dateAdded": "2025-04-25T09:39:08Z",
                        "ownerId": 2251799814013002,
                        "ownerName": "VulnCheck Intelligence",
                        "webLink": "https://companyabc.threatconnect.com/#/details/groups/1125899944159843",
                        "type": "Vulnerability",
                        "xid": "CVE-2020-0688",
                        "name": "CVE-2020-0688",
                        "createdBy": {
                            "userName": "ApiUser-vulncheck_intelligence",
                            "firstName": "ApiUser",
                            "lastName": "VulnCheck Intelligence",
                            "owner": "VulnCheck Intelligence"
                        },
                        "upVoteCount": "0",
                        "downVoteCount": "0",
                        "attributes": {
                            "data": [
                                {
                                    "id": 2251799860219320,
                                    "dateAdded": "2025-04-25T09:39:09Z",
                                    "type": "CPE Product",
                                    "value": "exchange_server",
                                    "source": "https://vulncheck.com",
                                    "lastModified": "2025-04-25T09:39:09Z",
                                    "pinned": false,
                                    "default": false
                                },
                                ...
                                {
                                    "id": 2251799860219272,
                                    "dateAdded": "2025-04-25T09:39:09Z",
                                    "type": "CVSS Severity",
                                    "value": "HIGH",
                                    "source": "https://vulncheck.com",
                                    "lastModified": "2025-04-25T09:39:09Z",
                                    "pinned": false,
                                    "default": false
                                }
                            ]
                        },
                        "lastModified": "2025-04-25T09:39:08Z",
                        "legacyLink": "https://companyabc.threatconnect.com/auth/vulnerability/vulnerability.xhtml?vulnerability=1125899944159843"
                    }
                ]
            },
            "kevProperties": {
                "shortDescription": "Microsoft Exchange Server Validation Key fails to properly create unique keys at install time, allowing for remote code execution.",
                "product": "Exchange Server",
                "vulnerabilityName": "Microsoft Exchange Server Validation Key Remote Code Execution Vulnerability",
                "links": [
                    "https://nvd.nist.gov/vuln/detail/CVE-2020-0688"
                ],
                "vendorProject": "Microsoft",
                "knownRansomwareCampaignUse": "Known",
                "requiredAction": "Apply updates per vendor instructions.",
                "dueDate": "2022-05-03T00:00:00Z",
                "dateAdded": "2021-11-03T00:00:00Z"
            },
            "products": "secure@microsoft.com",
            "criteria": "cpe:2.3:a:microsoft:exchange_server:2010:sp3_rollup_30:*:*:*:*:*:*",
            "cvss_v2": "CVSS:2.0/AV:N/AC:L/Au:S/C:C/I:C/A:C",
            "cvss_score_v2": 9.0,
            "cvss_severity_v2": "HIGH",
            "cvss_severity_v3": "NONE",
            "cvss_v3_1": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
            "cvss_score_v3_1": 8.8,
            "cvss_severity_v3_1": "HIGH",
            "cvss_severity_v4": "NONE",
            "lastPublished": "2020-02-11T22:15:15Z",
            "externalDateAdded": "2025-04-04T19:31:36Z",
            "cvssV2Properties": {
                "Authentication (Au)": "Single",
                "Availability Impact (A)": "Complete",
                "Integrity Impact (I)": "Complete",
                "Access Vector (AV)": "Network",
                "Access Complexity (AC)": "Low",
                "Confidentiality Impact (C)": "Complete"
            },
            "cvssV3_1Properties": {
                "Privileges Required (PR)": "Low",
                "Availability Impact (A)": "High",
                "Attack Complexity (AC)": "Low",
                "Scope (S)": "Unchanged",
                "Attack Vector (AV)": "Network",
                "Integrity Impact (I)": "High",
                "Confidentiality Impact (C)": "High",
                "User Interaction (UI)": "None"
            }
        }

Filter Vulnerabilities by Unified View Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the following TQL parameters to filter Vulnerability Groups by unified view data:

- ``criteria``: <*String*> The criteria of the Vulnerability.
- ``cvss_v2``: <*String*> The CVSS V2 vector string of the Vulnerability.
- ``cvss_v3``: <*String*> The CVSS V3 vector string of the Vulnerability.
- ``products``: <*String*> The products affected by the Vulnerability.
- ``source``: <*String*> The source of the Vulnerability.
- ``title``: <*String*> The summary of the Vulnerability.

For more information on filtering results with TQL, see `Filter Results With TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.