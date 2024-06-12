Retrieve Playbooks
------------------

Retrieve All Playbooks
^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Playbooks in your Organization:

**Request**

.. code::

    GET /v3/playbooks

**Response**

.. code:: json

    {
        "data": [
            {
                "id": 10,
                "groupXid": "Jisp3U1A",
                "name": "Vulnerability Content Pack - Manual Vulnerability Enrichment from NIST NVD",
                "description": "This playbook goes out to NVD NIST via a User Action Trigger to search for a CVE and bring back the Summary, CVSS Score, CVSS Severity and Metrics Matrix, and the References associated with the CVE. It will also associate and add the Technical Blogs and Reports by CVE tag to the Vulnerability object.",
                "webLink": "https://app.threatconnect.com/#/playbooks/designer/12345",
                "groupWebLink": "https://app.threatconnect.com/#/playbooks/designer/Jisp3U1A",
                "version": "1.172",
                "comment": "Auto-Saved on Thu Oct 26 15:52:48 UTC 2023",
                "type": "Playbook",
                "triggerType": "UserAction",
                "active": true,
                "basicAuthEnabled": false,
                "logLevel": "WARN",
                "updated": "2023-10-26T15:46:16Z",
                "labels": [
                    "NVD CVE Use Case ",
                    "Vulnerability Content Pack"
                ],
                "priority": 7,
                "status": "Active",
                "zoom": 1.1471,
                "panX": -94.0,
                "panY": 930.0,
                "roiDollarsPerHour": 75,
                "roiMinutes": 10,
                "apiUser": "John Smith",
                "enableNotifications": true,
                "notifyEmailList": "smithj@threatconnect.com",
                "notifyIncludeLogFiles": false,
                "notifyEmailCount": 0,
                "ownerName": "Demo Organization"
            },
            {
                "id": 9,
                "groupXid": "23llBiwt",
                "name": "Vulnerability Use Case - Vulnerability Enrichment Manual User Action R1",
                "webLink": "https://app.threatconnect.com/#/playbooks/designer/12344",
                "groupWebLink": "https://app.threatconnect.com/#/playbooks/designer/23llBiwt",
                "version": "1.27",
                "comment": "Auto-Saved on Thu Oct 26 15:49:52 UTC 2023",
                "type": "Component",
                "triggerType": "PipeConfig",
                "active": true,
                "basicAuthEnabled": false,
                "logLevel": "WARN",
                "updated": "2023-10-26T15:46:13Z",
                "labels": [
                    "NVD CVE Use Case "
                ],
                "priority": 6,
                "status": "Active",
                "zoom": 0.8,
                "panX": -129.0,
                "panY": 273.0,
                "roiDollarsPerHour": 75,
                "roiMinutes": 10,
                "apiUser": "John Smith",
                "enableNotifications": false,
                "notifyIncludeLogFiles": false,
                "notifyEmailCount": 0,
                "ownerName": "Demo Organization"
            },
            {...}
        ],
        "status": "Success"
    }

.. hint::

    To include details about a Playbook's most recent execution in the API response, append ``?fields=lastExecution`` to the end of the request URL.

Retrieve a Specific Playbook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following requests demonstrate how to use TQL to retrieve data for a specific Playbook.

Filter by ID Number
"""""""""""""""""""

In the following example, the API request will retrieve data only for the Playbook whose ID number is **12345**:

**Request (Decoded URL)**

.. code::

    GET /v3/playbooks?tql=id = 12345

**Request (Encoded URL)**

.. code::

    GET /v3/playbooks?tql=id%20%3D%2012345

Filter by XID
"""""""""""""

In the following example, the API request will retrieve data only for the Playbook whose XID is **GiTVUWaN**:

**Request (Decoded URL)**

.. code::

    GET /v3/playbooks?tql=groupXid = "GiTVUWaN"

**Request (Encoded URL)**

.. code::

    GET /v3/playbooks?tql=groupXid%20%3D%20%22GiTVUWaN%22

Filter by Name
""""""""""""""

In the following example, the API request will retrieve data only for the Playbook whose name is **Send IR Results to SIEM**:

**Request (Decoded URL)**

.. code::

    GET /v3/playbooks?tql=name = "Send IR Results to SIEM"

**Request (Encoded URL)**

.. code::

    GET /v3/playbooks?tql=name%20%3D%20%22Send%20IR%20Results%20to%20SIEM%22