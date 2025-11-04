Unified View Data for Vulnerabilities
-------------------------------------

As of ThreatConnect 7.10, you can access a unified view for Vulnerability Groups with the same name/summary. The unified view includes Common Vulnerability Scoring System (CVSS) and Known Exploited Vulnerabilities (KEV) data for all versions of a given Vulnerability.

In the v3 API, you can use the ``fields`` query parameter to include unified view data for Vulnerability Groups in API responses.

.. note::
    The following example requests demonstrate how to retrieve unified view data for all Vulnerability Groups included in a unified Vulnerability Group. You can use similar requests to retrieve unified view data for a specific Vulnerability Group included in a unified Vulnerability Group.

Retrieve Unified View Data for Vulnerabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following request to retrieve unified view data for all Vulnerability Groups included in a unified Vulnerability Group:

Request (Decoded URL)

.. code:: http

    GET /v3/groups?tql=hasCommonGroup(typeName="Vulnerability")&fields=common

Request (Encoded URL)

.. code:: http

    GET /v3/groups?tql=hasCommonGroup(typeName%3D%22Vulnerability%22)&fields=common

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

Use the following request to retrieve:

- Unified view data for all Vulnerability Groups included in a unified Vulnerability Group
- Details about the Vulnerability Groups included in a given unified Vulnerability Group

Request (Decoded URL)

.. code:: http

    GET /v3/groups?tql=hasCommonGroup(typeName="Vulnerability")&fields=common&fields=linkedGroups

Request (Encoded URL)

.. code:: http

    GET /v3/groups?tql=hasCommonGroup(typeName%3D%22Vulnerability%22)&fields=common&fields=linkedGroups

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

.. hint::
    You can include additional association levels for Groups objects included in the ``linkedGroups`` field. For example, to include the Attributes added to each Group object in the ``linkedGroups`` field, set the fields query parameter's value to ``linkedGroups.attributes``. For more information, see the `"Include Additional Association Levels for a Field" section of Include Additional Fields in API Responses <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html#include-additional-association-levels-for-a-field>`_.

Filter Vulnerabilities by Unified View Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the ``hasCommonGroup()`` TQL parameter to filter Vulnerability Groups based on unified view data. For example, the following request will retrieve unified view data for all Vulnerability Groups included in a unified Vulnerability Group with at least one CVSS score greater than 7.0:

Request (Decoded URL)

.. code:: http

    GET /v3/groups?tql=typeName in ("Vulnerability") and hasCommonGroup (cvss_score_v2>7.0 OR cvss_score_v3>7.0 OR cvss_score_v3_1>7.0 OR cvss_score_v4>7.0)&fields=common

Request (Encoded URL)

.. code:: http

    GET /v3/groups?tql=typeName%20in%20(%22Vulnerability%22)%20and%20hasCommonGroup%20(cvss_score_v2%3E7.0%20OR%20cvss_score_v3%3E7.0%20OR%20cvss_score_v3_1%3E7.0%20OR%20cvss_score_v4%3E7.0)&fields=common

For more information on filtering results with TQL, see `Filter Results With TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_. For a complete list of TQL parameters you can use to filter unified Vulnerability Groups, see the `TQL Operators and Parameters <https://knowledge.threatconnect.com/docs/tql-operators-and-parameters>`_ knowledge base article.