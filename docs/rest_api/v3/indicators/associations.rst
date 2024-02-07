Associations
------------

Create Associations
^^^^^^^^^^^^^^^^^^^

For instructions on associating Artifacts, Cases, and Groups to an Indicator, see `Create and Manage Associations <https://docs.threatconnect.com/en/latest/rest_api/v3/associations.html>`_. For instructions on creating Indicator-to-Indicator associations, see the `"Indicator-to-Indicator Associations" <#id19>`_ section. 

Retrieve Custom Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When working with Indicators, you can retrieve data about an Indicator's custom associations, including the name of the custom association and the Indicator involved in this association.

For example, the following request will retrieve data for the Indicator whose ID is 30, including information about its custom associations.

.. code::

    GET /v3/indicators/30?fields=customAssociations

JSON Response

.. code:: json

    {
        "data": {
            "id": 30,
            "dateAdded": "2023-06-26T15:23:28Z",
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/#/details/indicators/30/overview",
            "type": "Host",
            "lastModified": "2023-09-25T13:40:12Z",
            "confidence": 0,
            "summary": "zayla.co",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "customAssociations": {
                "data": [
                    {
                        "id": 32,
                        "dateAdded": "2023-06-27T15:38:38Z",
                        "ownerId": 1,
                        "ownerName": "Demo Organization",
                        "webLink": "https://app.threatconnect.com/#/details/indicators/32/overview",
                        "type": "Address",
                        "lastModified": "2023-08-18T13:03:11Z",
                        "confidence": 0,
                        "summary": "107.180.48.66",
                        "privateFlag": false,
                        "active": true,
                        "activeLocked": false,
                        "customAssociationName": "DNS PTR Record",
                        "ip": "107.180.48.66",
                        "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=107.180.48.66&owner=Demo+Organization"
                    },
                    {
                        "id": 33,
                        "dateAdded": "2023-06-27T19:49:13Z",
                        "ownerId": 1,
                        "ownerName": "Demo Organization",
                        "webLink": "https://app.threatconnect.com/#/details/indicators/33/overview",
                        "type": "URL",
                        "lastModified": "2023-09-25T13:40:12Z",
                        "rating": 3.00,
                        "confidence": 0,
                        "summary": "http://www.badstuff.com",
                        "privateFlag": false,
                        "active": true,
                        "activeLocked": false,
                        "customAssociationName": "Host To All",
                        "text": "http://www.badstuff.com",
                        "legacyLink": "https://app.threatconnect.com/auth/indicators/details/url.xhtml?orgid=1&owner=Demo+Organization"
                    }
                ],
                "count": 2
            },
            "hostName": "zayla.co",
            "dnsActive": false,
            "whoisActive": false,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=zayla.co&owner=Demo+Organization"
        },
        "status": "Success"
    }

Indicator-to-Indicator Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In ThreatConnect, you can associate two Indicators of certain types to one another using the following methods:

- Create an Indicator-to-Indicator Association
- Create a `File Action <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#file-actions>`_ (for File Indicators)

Create an Indicator-to-Indicator Association
""""""""""""""""""""""""""""""""""""""""""""

Each type of Indicator-to-Indicator association contains one primary (or parent) Indicator type and at least one non-primary (or child) Indicator type, as defined on the **Indicators** tab of the **System Settings** screen in ThreatConnect. When creating Indicator-to-Indicator associations using the v3 API, you can only associate Indicators of the non-primary type(s) to Indicators of the primary type. For example, in an **ASN to Address** association, the ASN Indicator is the primary Indicator type and the Address Indicator is the non-primary Indicator type. This means you can associate an Address Indicator to an ASN Indicator, but you cannot associate an ASN Indicator to an Address Indicator.

When creating Indicator-to-Indicator associations using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Indicator of the non-primary type, include `all fields required to create the type of Indicator <#available-fields>`_ when setting the ``associatedIndicators`` field. To create the Indicator in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Indicator when setting the ``associatedIndicators`` field.
- To create an association to an existing Indicator of the non-primary type, use the Indicator's ID, or use its type and summary type (e.g., ``"associatedIndicators": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``associatedIndicators`` field. To create an association to an Indicator that exists in a Community or Source using the Indicator's summary and type, include the ``ownerId`` or ``ownerName`` field and specify the ID or name, respectively, of the Community or Source to which the Indicator belongs when setting the ``associatedIndicators`` field.

The following table outlines the default Indicator-to-Indicator associations in ThreatConnect and the Indicator types each association supports.

.. list-table::
   :widths: 33 33 33
   :header-rows: 1

   * - Association Name
     - Primary Indicator Type
     - Non-Primary Indicator Type(s)
   * - Address to User Agent
     - Address
     - User Agent
   * - ASN to Address
     - ASN
     - Address
   * - ASN to CIDR
     - ASN
     - CIDR
   * - CIDR to Address
     - CIDR
     - Address
   * - DNS PTR Record
     - Address
     - Host
   * - Domain Registrant Email
     - Host
     - EmailAddress
   * - Domain Registrant Email
     - Host
     - EmailAddress
   * - File Download
     - URL
     - File
   * - URL Host
     - URL
     - Host, Address

.. note::
    In addition to the association types listed in this table, customer-configured custom associations are also supported. Your System Administrator can retrieve information for these association types, including the primary and non-primary Indicator types the association supports, on the **Indicators** tab of the **System Settings** screen.

In the following example, the request will associate an existing Address Indicator to an existing ASN Indicator. Because the ``associatedIndicators`` field is not included in the API response by default, the ``fields`` query parameter is added to the request URL and assigned a value of ``associatedIndicators`` so that this field is included in the response.

.. code::

    PUT /v3/indicators/ASN204288?fields=associatedIndicators
    {
        "associatedIndicators": {
            "data": [
                {
                    "ip": "66.96.146.129",
                    "type": "Address"
                }
            ]
        }
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 15,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2022-03-11T19:25:43Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/15/overview",
            "type": "ASN",
            "lastModified": "2022-06-13T18:25:30Z",
            "summary": "ASN204288",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedIndicators": {
                "data": [
                    {
                        "id": 14,
                        "ownerId": 1,
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-10-08T13:48:05Z",
                        "webLink": "https://app.threatconnect.com/#/details/indicators/14/overview",
                        "type": "Address",
                        "lastModified": "2022-06-13T18:25:30Z",
                        "summary": "66.96.146.129",
                        "privateFlag": false,
                        "active": true,
                        "activeLocked": false,
                        "ip": "66.96.146.129",
                        "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=66.96.146.129&owner=Demo+Organization"
                    }
                ]
            },
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/customIndicator.xhtml?id=15&owner=Demo+Organization",
            "AS Number": "ASN204288"
        },
        "message": "Updated",
        "status": "Success"
    }

If you try to associate an ASN Indicator to an Address Indicator, as in the following example, an error message will be returned stating that the association cannot be applied to the Indicator types.

.. code::

    PUT /v3/indicators/66.96.146.129
    {
        "associatedIndicators": {
            "data": [
                {
                    "AS Number": "ASN204288",
                    "type": "ASN"
                }
            ]
        }
    }

JSON Response

.. code:: json

    {
        "errCode": "0x1001",
        "message": "Association cannot be applied to the indicator types.",
        "status": "Error"
    }

.. note::
    In this example, the two Indicators would be associated and no error would be returned only if your System Administrator created a custom association where Address Indicators are the primary Indicator type and ASN Indicators are the non-primary Indicator type.

Manage an Indicator's Indicator-to-Indicator Associations
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

You can append, replace, and delete Indicator-to-Indicator associations via the ``mode`` field. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information on using this field.

File Actions
^^^^^^^^^^^^

File Indicators can model a special Indicator-to-Indicator association, which is based on their behavior once opened. These associations can be used to model the fact that malware may contain and create additional files or communicate with network devices. A File Action adds an Indicator to a File Indicator's behavior model, which can be viewed on the `Behavior tab <https://knowledge.threatconnect.com/docs/modeling-file-behavior>`_ of the File Indicator's **Details** screen.

When creating File Actions using the v3 API, follow these guidelines:

- To create an association to a new Indicator via a File Action, include `all fields required to create the type of Indicator <#available-fields>`_ when setting the ``indicator`` field. To create the Indicator in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Indicator when setting the ``indicator`` field.
- To create an association to an existing Indicator of the non-primary type, use the Indicator's ID, or use its type and summary type (e.g., ``"indicator": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``indicator`` field. To create an association to an Indicator that exists in a Community or Source using the Indicator's summary and type, include the ``ownerId`` or ``ownerName`` field and specify the ID or name, respectively, of the Community or Source to which the Indicator belongs when setting the ``indicator`` field.

The following table outlines the **default** File Actions available in ThreatConnect, along with the Indicator type(s) that can be associated to a File Indicator via each File Action.

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

.. note::
    In addition to the File Actions listed in this table, customer-configured custom File Actions are also supported. Your System Administrator can retrieve information for these File Actions, including the Indicator types the File Action supports, on the **Indicators** tab of the **System Settings** screen.

Create a File Action
""""""""""""""""""""

The following table outlines the fields you must include in your request when creating File Actions for a File Indicator.

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

In the following example, the request will perform the following actions:

- Create a new File Indicator based on an MD5 file hash
- Create a new Address Indicator and associate it to the newly created File Indicator using the **File Traffic** File Action
- Associate the existing File Indicator whose ID is 12 to the newly created File Indicator using the **File Archive** File Action

Because the ``fileActions`` field is not included in the API response by default, the ``fields`` query parameter is added to the request URL and assigned a value of ``fileActions`` so that this field is included in the response.

.. code::

    POST /v3/indicators?fields=fileActions
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
            "ownerId": 18,
            "ownerName": "Demo Organization",
            "dateAdded": "2022-06-14T12:57:53Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/18/overview",
            "type": "File",
            "lastModified": "2022-06-14T12:57:53Z",
            "summary": "2EA0564F33E4CB67063C4A06734EB627",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "fileActions": {
                "data": [
                    {
                        "relationship": "File Archive",
                        "indicator": {
                            "id": 12,
                            "id": 1,
                            "ownerName": "Demo Organization",
                            "dateAdded": "2022-05-27T12:42:28Z ",
                            "webLink": "https://app.threatconnect.com/#/details/indicators/12/overview",
                            "type": "File",
                            "lastModified": "2022-05-27T12:42:28Z ",
                            "summary": "FB69E1273E7A53AD8E9BBE64B80859FC",
                            "privateFlag": false,
                            "active": true,
                            "activeLocked": false,
                            "fileActions": {
                                "count": 0
                            },
                            "md5": "FB69E1273E7A53AD8E9BBE64B80859FC",
                            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=FB69E1273E7A53AD8E9BBE64B80859FC&owner=Demo+Organization"
                        }
                    },
                    {
                        "relationship": "File Traffic",
                        "indicator": {
                            "id": 19,
                            "ownerId": 1,
                            "ownerName": "Demo Organization",
                            "dateAdded": "2022-06-14T12:57:53Z",
                            "webLink": "https://app.threatconnect.com/#/details/indicators/19/overview",
                            "type": "Address",
                            "lastModified": "2022-06-14T12:57:53Z",
                            "summary": "66.96.146.132",
                            "privateFlag": false,
                            "active": true,
                            "activeLocked": false,
                            "fileActions": {
                                "count": 0
                            },
                            "ip": "66.96.146.132",
                            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=66.96.146.132&owner=Demo+Organization"
                        }
                    }
                ],
                "count": 2
            },
            "md5": "2EA0564F33E4CB67063C4A06734EB627",
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=2EA0564F33E4CB67063C4A06734EB627&owner=Demo+Organization"
        },
        "message": "Created",
        "status": "Success"
    }

Manage an Indicator's File Actions
""""""""""""""""""""""""""""""""""

You can append, replace, and delete File Actions via the ``mode`` field. See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for more information on using this field.