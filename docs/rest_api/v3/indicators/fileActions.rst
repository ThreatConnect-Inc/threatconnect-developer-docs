File Actions
------------

File Indicators can model a special Indicator-to-Indicator association, which is based on their behavior once opened. These associations can be used to model the fact that malware may contain and create additional files or communicate with network devices. A File Action adds an Indicator to a File Indicator's behavior model, which can be viewed on the `Behavior tab <https://knowledge.threatconnect.com/docs/modeling-file-behavior>`_ of the File Indicator's **Details** screen.

The following table outlines the **default** File Actions available in ThreatConnect, along with the Indicator type(s) that can be associated to a File Indicator via each File Action.

.. note::
    In addition to the File Actions listed in this table, customer-configured custom File Actions are also supported. Your System Administrator can retrieve information for these File Actions, including the Indicator types the File Action supports, on the **Indicators** tab of the **System Settings** screen.


.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - File Action Name
     - Associable Indicator Type(s)
   * - File Archive
     - File
   * - File DNS Query
     - Host
   * - File Drop
     - File
   * - File Traffic
     - Address, Host, URL
   * - File Mutex
     - Mutex
   * - File Registry Key
     - Registry Key
   * - File User Agent
     - User Agent

Create a File Action
^^^^^^^^^^^^^^^^^^^^

The following table outlines the fields available when creating File Actions for a File Indicator.

.. list-table::
   :widths: 20 35 20 25
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
   * - indicator
     - The Indicator being associated to the File Indicator via the specified File Action
     - Indicator Object
     - TRUE
   * - relationship
     - The name of the File Action
     - String
     - TRUE

.. hint::
    If the Indicator being associated to the File Indicator via a File Action belongs to a Community or Source, use the Indicator's ID when setting the ``indicators`` field. For instructions on retrieving an Indicator's ID, see the `"Retrieve Indicators" section <#retrieve-indicators>`_.
    
    If the Indicator being associated to the File Indicator via a File Action belongs to an Organization, use the Indicator's ID, or use its type and summary type (e.g., ``"associatedIndicators": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``indicators`` field.

    To create an association to a new Indicator via a File Action, include `all fields required to create the type of Indicator <#available-fields>`_ when setting the ``indicators`` field.

In the following example, the query will:

- Create a new File Indicator based on an MD5 file hash
- Create a new Address Indicator and associate it to the newly created File Indicator using the File Traffic File Action
- Associate an existing File Indicator to the newly created File Indicator using the File Archive File Action

.. code::

    POST /v3/indicators

    {
        "type": "File",
        "md5": "2ea0564f33e4cb67063c4a06734eb627",
        "fileActions": {
            "data": [
                {
                    "relationship": "File Traffic",
                    "indicator": {
                    "type": "Address",
                    "ip": "66.96.146.132"
                    }
                },
                {
                    "relationship": "File Archive",
                    "indicator": {
                    "id": 12
                    }
                }
            ]
        }
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 18,
            "ownerName": "Demo Organization",
            "dateAdded": "2022-06-14T12:57:53Z",
            "webLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=2EA0564F33E4CB67063C4A06734EB627",
            "tags": {},
            "securityLabels": {},
            "type": "File",
            "lastModified": "2022-06-14T12:57:53Z",
            "summary": "2EA0564F33E4CB67063C4A06734EB627",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {},
            "associatedIndicators": {
                "data": [
                    {
                        "id": 19,
                        "ownerName": "Demo Organization",
                        "dateAdded": "2022-06-14T12:57:53Z",
                        "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=66.96.146.132",
                        "type": "Address",
                        "lastModified": "2022-06-14T12:57:53Z",
                        "summary": "66.96.146.132",
                        "privateFlag": false,
                        "active": true,
                        "activeLocked": false,
                        "ip": "66.96.146.132"
                    },
                    {
                        "id": 12,
                        "ownerName": "Demo Organization",
                        "dateAdded": "2022-05-27T12:42:28Z",
                        "webLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=FB69E1273E7A53AD8E9BBE64B80859FC",
                        "type": "File",
                        "lastModified": "2022-05-27T12:42:28Z ",
                        "summary": "FB69E1273E7A53AD8E9BBE64B80859FC",
                        "privateFlag": false,
                        "active": true,
                        "activeLocked": false,
                        "md5": "FB69E1273E7A53AD8E9BBE64B80859FC"
                    }
                ]
            },
            "fileActions": {
                "data": [
                    {
                        "relationship": "File Archive",
                        "indicator": {
                            "id": 12,
                            "ownerName": "Demo Organization",
                            "dateAdded": "2022-05-27T12:42:28Z ",
                            "webLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=FB69E1273E7A53AD8E9BBE64B80859FC",
                            "tags": {},
                            "securityLabels": {},
                            "type": "File",
                            "lastModified": "2022-05-27T12:42:28Z ",
                            "summary": "FB69E1273E7A53AD8E9BBE64B80859FC",
                            "privateFlag": false,
                            "active": true,
                            "activeLocked": false,
                            "associatedGroups": {},
                            "associatedIndicators": {
                                "data": [
                                    {
                                        "id": 18,
                                        "ownerName": "Demo Organization",
                                        "dateAdded": "2022-06-14T12:57:53Z",
                                        "webLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=2EA0564F33E4CB67063C4A06734EB627",
                                        "type": "File",
                                        "lastModified": "2022-06-14T12:57:53Z",
                                        "summary": "2EA0564F33E4CB67063C4A06734EB627",
                                        "privateFlag": false,
                                        "active": true,
                                        "activeLocked": false,
                                        "md5": "2EA0564F33E4CB67063C4A06734EB627"
                                    }
                                ]
                            },
                            "fileActions": {
                                "count": 0
                            },
                            "attributes": {},
                            "associatedCases": {},
                            "associatedArtifacts": {},
                            "md5": "FB69E1273E7A53AD8E9BBE64B80859FC"
                        }
                    },
                    {
                        "relationship": "File Traffic",
                        "indicator": {
                            "id": 19,
                            "ownerName": "Demo Organization",
                            "dateAdded": "2022-06-14T12:57:53Z",
                            "webLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=66.96.146.132",
                            "tags": {},
                            "securityLabels": {},
                            "type": "Address",
                            "lastModified": "2022-06-14T12:57:53Z",
                            "summary": "66.96.146.132",
                            "privateFlag": false,
                            "active": true,
                            "activeLocked": false,
                            "associatedGroups": {},
                            "associatedIndicators": {
                                "data": [
                                    {
                                        "id": 18,
                                        "ownerName": "Demo Organization",
                                        "dateAdded": "2022-06-14T12:57:53Z",
                                        "webLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=2EA0564F33E4CB67063C4A06734EB627",
                                        "type": "File",
                                        "lastModified": "2022-06-14T12:57:53Z",
                                        "summary": "2EA0564F33E4CB67063C4A06734EB627",
                                        "privateFlag": false,
                                        "active": true,
                                        "activeLocked": false,
                                        "md5": "2EA0564F33E4CB67063C4A06734EB627"
                                    }
                                ]
                            },
                            "fileActions": {
                                "count": 0
                            },
                            "attributes": {},
                            "associatedCases": {},
                            "associatedArtifacts": {},
                            "ip": "66.96.146.132"
                        }
                    }
                ],
                "count": 2
            },
            "attributes": {},
            "associatedCases": {},
            "associatedArtifacts": {},
            "md5": "2EA0564F33E4CB67063C4A06734EB627"
        },
        "message": "Created",
        "status": "Success"
    }

Manage an Indicator's File Actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can append, replace, and delete File Actions via the ``mode`` field. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information on using this field.