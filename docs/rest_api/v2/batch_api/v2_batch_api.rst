V2 Batch API
------------

The following sections describe how to use the V2 Batch API, including how to create a batch job and upload a file to the job for processing. With the V2 Batch API, you can perform the following actions:

* Import Indicators and Groups
* Create Group-to-Group, Indicator-to-Group, Group-to-Indicator, and, Indicator-to-Indicator associations
* Create and update Attributes, Tags, and Security Labels for Indicators and Groups
* Specify how to manage file hash merges and collisions for File Indicators

.. attention::
    The V2 Batch API does not support cross-owner associations.

.. note::
    To create Indicator-to-Indicator associations with the V2 Batch API, your instance must be running ThreatConnect 7.8.2 or newer.

Create a Batch Job
^^^^^^^^^^^^^^^^^^

Send a request in the following format to create a batch job that will use the V2 Batch API.

**Request**

.. code::

    POST /v2/batch
    Content-type: application/json; charset=utf-8


    {
        "version": "V2",
        "owner": "Demo Organization",
        "haltOnError": true,
        "action": "Create",
        "attributeWriteType": "Append",
        "tagWriteType": "Append",
        "securityLabelWriteType": "Append",
        "fileMergeMode": "Merge",
        "hashCollisionMode": "FavorIncoming"
    }

* ``version``: <*String*> The version of the Batch API to use. Set this field's value to ``V2`` to use the V2 Batch API.
* ``owner``: <*String*> **REQUIRED** The name of the Organization, Community, or Source in which the batch job will create or update data.
* ``haltOnError``: <*Boolean*> **REQUIRED** Specifies how the batch process should proceed if it encounters an error. Accepted values include the following:
    * **true**: The batch process will stop processing the entire batch job the first time it encounters an error.
    * **false**: The batch process will attempt to continue processing the batch job after encountering an error.
* ``action``: <*String*> **REQUIRED** The action that the batch job will perform on incoming data. Accepted values include the following:
    * **Create**: The batch job will create new and update existing data in the specified owner.
    * **Delete**: The batch job will delete existing data in the specified owner that matches any of the incoming data.
* ``attributeWriteType``: <*String*> **REQUIRED** Specifies how the batch job will handle incoming Attributes. Accepted values include the following:
    * **Append**: The batch job will append the incoming Attributes to an Indicator or Group. Note that duplicate Attributes may be added, as **redundancy checking is not performed**.
    * **Replace**: The batch job will replace *all* Attributes added to an Indicator or Group with the incoming Attributes.
    * **Singleton**: The batch job will replace existing Attributes added to an Indicator or Group only if the incoming data include Attributes with the same Attribute Type(s) as the existing Attributes. Otherwise, existing Attributes added to an Indicator or Group will remain unchanged.
    * **Static**: The batch job will ignore incoming Attributes and not update existing Attributes added to an Indicator or Group.
* ``tagWriteType``: <*String*> Specifies how the batch job will handle incoming Tags. Accepted values include the following:
    * **Append**: The batch job will append the incoming Tags to an Indicator or Group.
    * **Replace** (default): The batch job will replace all Tags added to an Indicator or Group with the incoming Tags.
* ``securityLabelWriteType``: <*String*> Specifies how the batch job will handle incoming Security Labels. Accepted values include the following:
    * **Append**: The batch job will append the incoming Security Labels to an Indicator or Group.
    * **Replace** (default): The batch job will replace all Security Labels added to an Indicator or Group with the incoming Security Labels.
* ``fileMergeMode``: <*String*> Specifies whether the batch job will perform a merge operation when the file hashes in an incoming File Indicator match two or more existing File Indicators in the specified owner (e.g., an incoming File Indicator contains an MD5 and SHA1 that each match a separate File Indicator in the specified owner). Accepted values include the following:
    * **Distribute**: The batch job will not perform a merge operation; instead, it will add the metadata (e.g., Threat and Confidence Ratings, Tags, Attributes) for the incoming File Indicator to all matching File Indicators (up to three possible) in the specified owner.
    * **Merge** (default): The batch job will perform a merge operation and combine two or more existing File Indicators with separate file hashes into a single File Indicator with all file hashes. During this process, the File Indicator with the most recent ``lastModified`` date will be used as the "primary" copy and retain its Threat and Confidence Ratings (at least, until their values are overwritten by the values for the incoming File Indicator). Attributes, Security Labels, and Tags associated with all merged File Indicators will be applied to the "primary" copy as well. Because Attributes are appended to the "primary" copy, duplicate Attributes may be present if each File Indicator that was merged had similar Attributes.
* ``hashCollisionMode``: <*String*> Specifies how the batch job will handle file hash collisions that occur when importing or merging File Indicators (e.g., an incoming File Indicator contains an MD5 and SHA1, while an existing File Indicator contains the same MD5 but a different SHA1). Accepted values include the following:
    * **FavorExisting**: The batch job will favor hashes in the existing File Indicator and ignore conflicting hashes in the incoming File Indicator.
    * **FavorIncoming** (default): The batch job will favor hashes in the incoming File Indicator and overwrite conflicting hashes in the existing File Indicator.
    * **IgnoreExisting**: If a conflict exists between two or more existing File Indicators, the batch job will delete the existing File Indicators that caused conflict and then import the incoming File Indicator. If a conflict exists between one or more existing File Indicators and an incoming File Indicator, the batch job will ignore the existing Indicators. It will also remove their file hashes from the incoming Indicator, resulting in a new File Indicator being created without any conflicting file hashes. If all available file hashes are removed from the incoming Indicator, no new Indicator will be created.
    * **IgnoreIncoming**: The batch job will not import the incoming File Indicator causing the conflict, and existing File Indicators will not be updated.
    * **Split**: The batch job will not perform a merge; instead, it will apply the metadata (e.g., Threat and Confidence Ratings, Tags, Attributes) for the incoming File Indicator to all matching File Indicators in the specified owner.

.. note::
    If ``haltOnError`` is set to ``true`` and an error occurs during the batch process, the ``status`` for the batch job will be set to ``Completed`` and the value for ``errorCount`` will be greater than zero. Also, the value for ``unprocessedCount`` will be greater than zero unless the uploaded file did not contain valid JSON.

**Response (Success)**

.. code:: json

    HTTP/1.1 201 Created
    {
        "status": "Success",
        "data": {
            "batchId": 2446
        }
    }

**Response (Insufficient Privileges)**

.. code::

    HTTP/1.1 401 Unauthorized
    Unable to perform the requested operation due to the following error(s): You do not have permission to create Indicators; Groups; Attributes; Tags; Security Labels;

**Response (Incorrect Settings)**

.. code::

    HTTP/1.1 503 Service Unavailable
    Batch job api is not available.  Ensure that batchJobEnabled is true and document storage is enabled and configured;

.. attention::
    The parameters defined in the body of a POST request to create a batch job must be accurate. When troubleshooting issues with the Batch API, make sure the parameter names in the request body are correct and that an accepted value is provided for each parameter.

Upload an Input File to a Batch Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The V2 Batch API expects to ingest a JSON file containing one or more lists of objects, where Indicator and Group objects are contained within the ``indicator`` and ``group`` arrays. If your instance is running ThreatConnect 7.8.2 or newer, you may also define associations to create within the ``association`` array.

.. note::
    You can also define associations within the ``indicator`` and ``group`` arrays, regardless of which ThreatConnect version your instance is running. For more information, see the `"Indicator Fields" <#id3>`_ and `"Group Fields" <#id10>`_ sections.

The following is the batch input file schema for the V2 Batch API. For a list of additional fields you can use when defining Indicator and Group objects, see the `"Indicator Fields" <#id3>`_ and `"Group Fields" <#id10>`_ section, respectively.

* ``indicator``: <*Array of Objects*> The Indicators to create or update.
    * ``summary``: <*String*> **REQUIRED** The Indicator's summary. Note that you may substitute ``summary`` with the field that contains the Indicator's value for the specified Indicator type (e.g., you can use ``ip`` instead of ``summary`` to define an Address Indicator's IPv4 or IPv6 address value).
    * ``type``: <*String*> **REQUIRED** The Indicator's type.
* ``group``: <*Array of Objects*> The Groups to create or update.
    * ``name``: <*String*> **REQUIRED** The Group's name.
    * ``type``: <*String*> **REQUIRED** The Group's type.
    * ``xid``: <*String*> **REQUIRED** The Group's XID.
* ``association``: <*Array of Objects*> The associations to create. Supported association types include Indicator to Group, Group to Indicator, Group to Group, and Indicator to Indicator. (Requires ThreatConnect 7.8.2 or newer.)
    * ``ref_1``: <*String*> The summary of the Indicator or XID of the Group to use as the first object in the association. The Indicator or Group must be present in the batch input file or exist in the owner in which the batch job is processing data. (This field can be used interchangeably or in conjunction with ``id_1``. If both are provided, ``id_1`` will be favored over ``ref_1``.)
    * ``id_1``: <*Integer*> The ID of the Indicator or Group to use as the first object in the association. The Indicator or Group must exist in the owner in which the batch job is processing data. (This field can be used interchangeably or in conjunction with ``ref_1``. If both are provided, ``id_1`` will be favored over ``ref_1``.)
    * ``type_1``: <*String*> The type of Indicator or Group defined for ``ref_1`` or ``id_1``. This field is required for Indicators and optional for Groups.
    * ``ref_2``: <*String*> The summary of the Indicator or XID of the Group to use as the second object in the association. The Indicator or Group must be present in the input file or exist in the owner in which the batch job is processing data. (This field can be used interchangeably or in conjunction with ``id_2``. If both are provided, ``id_2`` will be favored over ``ref_2``.)
    * ``id_2``: <*Integer*> The ID of the Indicator or Group to use as the second object in the association. The Indicator or Group must exist in the owner in which the batch job is processing data. (This field can be used interchangeably or in conjunction with ``ref_2``. If both are provided, ``id_2`` will be favored over ``ref_2``.)
    * ``type_2``: <*String*> The type of Indicator or Group defined for ``ref_2`` or ``id_2``. This field is required for Indicators and optional for Groups.
    * ``associationType``: <*String*> For Indicator-to-Indicator associations only, the name of the association type (e.g., URL Host). This field is **required** if making an Indicator-to-Indicator association.

.. attention::
    If using the ``association`` field, it must be placed after the ``indicator`` and ``group`` fields in a batch input file.

Indicator Fields
""""""""""""""""

.. include:: ../_includes/v2_batch_api_indicator_fields.rst

Group Fields
""""""""""""

.. include:: ../_includes/v2_batch_api_group_fields.rst

.. hint::
    Exporting indicators via the `JSON Bulk Reports <https://docs.threatconnect.com/en/latest/rest_api/v2/indicators/indicators.html#json-bulk-reports>`_ endpoint will create a file in the proper format for the Batch API.

.. attention::
    The maximum number of Indicators that can be created in one batch job is 25,000. If creating more than 25,000 Indicators, use multiple batch jobs.

Example Input Files
"""""""""""""""""""

**Indicator-to-Group Association**

The following input file demonstrates how to associate Indicators to Groups using the ``associatedGroups`` field within the ``indicator`` array. When the Batch API processes the file, it will do the following:

* Create a Host Indicator (**badguyz.com**)
* Create an Incident Group (**Ransomware Attack at Company ABC**)
* Associate **badguyz.com** to **Ransomware Attack at Company ABC**

.. code:: json

    {
        "indicator": [
            {
                "summary": "badguyz.com",
                "type": "Host",
                "associatedGroups": [
                    {
                        "groupXid": "00000000-0000-0000-0000-000000000000:0001"
                    }
                ],
                "attribute": [
                    {
                        "type": "Description",
                        "value": "This host was involved in a ransomware attack that targeted employees at Company ABC.",
                        "securityLabel": [
                            {
                                "name": "TLP:AMBER"
                            }
                        ]
                    }
                ],
                "confidence": 60,
                "rating": 3,
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            }
        ],
        "group": [
            {
                "name": "Ransomware Attack at Company ABC",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0001",
                "attribute": [
                    {
                        "type": "Description",
                        "value": "A ransomware attack that targeted employees at Company ABC.",
                        "displayed": true
                    }
                ],
                "eventDate": "2024-08-04T00:00:00Z",
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            }
        ]
    }

The following input file demonstrates how to associate Indicators to Groups using the ``association`` array. When the Batch API processes the file, it will do the following:

* Create a Host Indicator (**badguyz.com**)
* Create an Incident Group (**Ransomware Attack at Company ABC**)
* Associate **badguyz.com** to **Ransomware Attack at Company ABC**
* Associate **badguyz.com** to an existing Group (the Group whose ID is 12345) in the owner in which the batch job is processing data

.. code:: json

    {
        "indicator": [
            {
                "summary": "badguyz.com",
                "type": "Host",
                "attribute": [
                    {
                        "type": "Description",
                        "value": "This host was involved in a ransomware attack that targeted employees at Company ABC.",
                        "securityLabel": [
                            {
                                "name": "TLP:AMBER"
                            }
                        ]
                    }
                ],
                "confidence": 60,
                "rating": 3,
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            }
        ],
        "group": [
            {
                "name": "Ransomware Attack at Company ABC",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0001",
                "attribute": [
                    {
                        "type": "Description",
                        "value": "A ransomware attack that targeted employees at Company ABC.",
                        "displayed": true
                    }
                ],
                "eventDate": "2024-08-04T00:00:00Z",
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            }
        ],
        "association": [
            {
                "ref_1": "badguyz.com",
                "type_1": "Host",
                "ref_2": "00000000-0000-0000-0000-000000000000:0001"
            },
            {
                "ref_1": "badguyz.com",
                "type_1": "Host",
                "id_2": 12345
            }
        ]
    }

**Group-to-Indicator Association**

.. note::
    When creating Group-to-Indicator associations, including the Indicators in the input file improves the efficiency of the batch job. Otherwise, a lookup will need to be made for each Indicator not included in the input file.

The following input file demonstrates how to associate Groups to *newly created* Indicators using the ``associatedIndicators`` field within the ``group`` array. When the Batch API processes the file, it will do the following:

* Create a URL Indicator (**http://www.badguyz.com**)
* Create an Incident Group (**Ransomware Attack at Company XYZ**)
* Associate **Ransomware Attack at Company XYZ** to **http://www.badguyz.com**

.. code:: json

    {
        "indicator": [
            {
                "summary": "http://www.badguyz.com",
                "type": "URL",
                "attribute": [
                    {
                        "type": "Description",
                        "value": "This URL was involved in a ransomware attack that targeted employees at Company XYZ.",
                        "securityLabel": [
                            {
                                "name": "TLP:AMBER"
                            }
                        ]
                    }
                ],
                "confidence": 60,
                "rating": 3,
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            }
        ],
        "group": [
            {
                "name": "Ransomware Attack at Company XYZ",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0002",
                "associatedIndicators": [
                    {
                        "summary": "http://www.badguyz.com",
                        "indicatorType": "URL"
                    }
                ],
                "attribute": [
                    {
                        "type": "Description",
                        "value": "A ransomware attack that targeted employees at Company XYZ.",
                        "displayed": true
                    }
                ],
                "eventDate": "2024-08-04T00:00:00Z",
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            }
        ]
    }

The following input file demonstrates how to associate Groups to *existing* Indicators using the ``associatedIndicators`` field within the ``group`` array. When the Batch API processes the file, it will do the following:

* Create an Incident Group (**Ransomware Attack at Company XYZ**)
* Associate **Ransomware Attack at Company XYZ** to an existing Address Indicator (**71.6.135.131**) in the owner in which the batch job is processing data

Because the Address Indicator already exists in ThreatConnect, it does not need to be defined in the ``indicator`` array in the input file.

.. code:: json

    {
        "group": [
            {
                "name": "Ransomware Attack at Company XYZ",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0002",
                "associatedIndicators": [
                    {
                        "summary": "71.6.135.131",
                        "indicatorType": "Address"
                    }
                ],
                "attribute": [
                    {
                        "type": "Description",
                        "value": "A ransomware attack that targeted employees at Company XYZ.",
                        "displayed": true
                    }
                ],
                "eventDate": "2024-08-04T00:00:00Z",
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            }
        ]
    }

The following input file demonstrates how to associate Groups to Indicators using the ``association`` array. When the Batch API processes the file, it will do the following:

* Create a URL Indicator (**http://www.badguyz.com**)
* Create an Incident Group (**Ransomware Attack at Company XYZ**)
* Associate **Ransomware Attack at Company XYZ** to **http://www.badguyz.com**
* Associate **Ransomware Attack at Company XYZ** to an existing Address Indicator (the Address Indicator whose ID is 54321) in the owner in which the batch job is processing data

.. code:: json

    {
        "indicator": [
            {
                "summary": "http://www.badguyz.com",
                "type": "URL",
                "attribute": [
                    {
                        "type": "Description",
                        "value": "This URL was involved in a ransomware attack that targeted employees at Company XYZ.",
                        "securityLabel": [
                            {
                                "name": "TLP:AMBER"
                            }
                        ]
                    }
                ],
                "confidence": 60,
                "rating": 3,
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            }
        ],
        "group": [
            {
                "name": "Ransomware Attack at Company XYZ",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0002",
                "attribute": [
                    {
                        "type": "Description",
                        "value": "A ransomware attack that targeted employees at Company XYZ.",
                        "displayed": true
                    }
                ],
                "eventDate": "2024-08-04T00:00:00Z",
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            }
        ],
        "association": [
            {
                "ref_1": "00000000-0000-0000-0000-000000000000:0002",
                "ref_2": "http://www.badguyz.com",
                "type_2": "URL"
            },
            {
                "ref_1": "00000000-0000-0000-0000-000000000000:0002",
                "id_2": 54321,
                "type_2": "Address"
            }
        ]
    }

**Group-to-Group Association**

The following input file demonstrates how to associate Groups to other Groups using the ``associatedGroupXid`` field within the ``group`` array. When the Batch API processes the file, it will do the following:

* Create two Incident Groups (**Compromised User Accounts at Company ABC** and **Leaked Credentials at Company ABC**)
* Associate **Compromised User Accounts at Company ABC** to **Leaked Credentials at Company ABC**


.. code:: json

    {
        "group": [
            {
                "name": "Compromised User Accounts at Company ABC",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0003",
                "associatedGroupXid": [
                    "00000000-0000-0000-0000-000000000000:0004"
                ],
                "attribute": [
                    {
                        "type": "Description",
                        "displayed": true,
                        "value": "An incident involving compromised user accounts at Company ABC."
                    }
                ],
                "eventDate": "2023-11-01T00:00:00Z",
                "tag": [
                    {
                        "name": "Phishing Attack"
                    }
                ]
            },
            {
                "name": "Leaked Credentials at Company ABC",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0004",
                "attribute": [
                    {
                        "type": "Description",
                        "displayed": true,
                        "value": "An incident involving leaked credentials at Company ABC."
                    }
                ],
                "eventDate": "2023-11-01T00:00:00Z"
            }
        ]
    }

The following input file demonstrates how to associate Groups to other Groups using the ``association`` array. When the Batch API processes the file, it will do the following:

* Create two Incident Groups (**Compromised User Accounts at Company ABC** and **Leaked Credentials at Company ABC**)
* Associate **Compromised User Accounts at Company ABC** to **Leaked Credentials at Company ABC**
* Associate **Compromised User Accounts at Company ABC** to an existing Group (the Group whose ID is 12345) in the owner in which the batch job is processing data
* Create an association between two existing Groups in the owner in which the batch job is processing data

.. code:: json

    {
        "group": [
            {
                "name": "Compromised User Accounts at Company ABC",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0003",
                "attribute": [
                    {
                        "type": "Description",
                        "displayed": true,
                        "value": "An incident involving compromised user accounts at Company ABC."
                    }
                ],
                "eventDate": "2023-11-01T00:00:00Z",
                "tag": [
                    {
                        "name": "Phishing Attack"
                    }
                ]
            },
            {
                "name": "Leaked Credentials at Company ABC",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0004",
                "attribute": [
                    {
                        "type": "Description",
                        "displayed": true,
                        "value": "An incident involving leaked credentials at Company ABC."
                    }
                ],
                "eventDate": "2023-11-01T00:00:00Z"
            }
        ],
        "association": [
            {
                "ref_1": "00000000-0000-0000-0000-000000000000:0003",
                "ref_2": "00000000-0000-0000-0000-000000000000:0004"
            },
            {
                "ref_1": "00000000-0000-0000-0000-000000000000:0003",
                "id_2": 12345
            },
            {
                "id_1": 100,
                "id_2": 200
            }
        ]
    }

**Indicator-to-Indicator Association**

The following input file demonstrates how to associate Indicators to other Indicators using the ``association`` array. This is the only method you can use to create Indicator-to-Indicator associations with the Batch API.

When the Batch API processes the file, it will do the following:

* Create a Host Indicator (**verybadguyz.com**)
* Create a URL Indicator (**http://www.verybadguyz.com**)
* Associate **verybadguyz.com** to **http://www.verybadguyz.com** using the URL Host association type
* Associate **verybadguyz.com** to an existing Address Indicator (the Address Indicator whose ID is 54321) in the owner in which the batch job is processing data using the Host to Indicators association type
* Create an association between two existing Indicators (an Address and an ASN) in the owner in which the batch job is processing data using the Address to Indicators association type

.. code:: json

    {
        "indicator": [
            {
                "summary": "verybadguyz.com",
                "type": "Host",
                "attribute": [
                    {
                        "type": "Description",
                        "value": "A host used by the Very Bad Guyz hacker group.",
                        "securityLabel": [
                            {
                                "name": "TLP:AMBER"
                            }
                        ]
                    }
                ],
                "confidence": 60,
                "rating": 3,
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            },
            {
                "summary": "http://www.verybadguyz.com",
                "type": "URL",
                "attribute": [
                    {
                        "type": "Description",
                        "value": "A URL used by the Very Bad Guyz hacker group.",
                        "securityLabel": [
                            {
                                "name": "TLP:AMBER"
                            }
                        ]
                    }
                ],
                "confidence": 60,
                "rating": 3,
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ]
            }
        ],
        "association": [
            {
                "ref_1": "verybadguyz.com",
                "type_1": "Host",
                "ref_2": "http://www.verybadguyz.com",
                "type_2": "URL",
                "associationType": "URL Host"
            },
            {
                "ref_1": "verybadguyz.com",
                "type_1": "Host",
                "id_2": 54321,
                "type_2": "Address",
                "associationType": "Host to Indicators"
            },
            {
                "id_1": 54321,
                "type_1": "Address",
                "id_2": 654321,
                "type_2": "ASN",
                "associationType": "Address to Indicators"
            }
        ]
    }

**Providing an AI Summary for a Group**

The following input file demonstrates how to create a Group and provide an AI-generated summary for the Group.

When the Batch API processes the file, it will create a Report Group (**APT28 Report Group**) that includes an AI-generated summary from the specified provider:

.. code:: json

    {
        "group": [
            {
                "name": "Example Report Group with AI Summary",
                "type": "Report",
                "publishDate": "2025-12-15T13:00:00Z",
                "xid": "ad4c16549f1ff37faa7a3e99b6e33e0884d9af03878e8c4c2bf1c31a674ace40",
                "insights": "###### LIVE BRIEF\n\nInitial detection of APT28 campaign targeting financial sector through CVE-2024-1234 exploitation. This is a highly sophisticated attack campaign demonstrating advanced persistent threat capabilities with multi-stage payload delivery mechanisms, utilizing previously unknown zero-day vulnerabilities in widely deployed enterprise infrastructure components. The threat actors have demonstrated exceptional operational security and advanced evasion techniques designed to bypass traditional signature-based detection systems and next-generation endpoint protection platforms. Analysis indicates this campaign has been in development for several months with careful reconnaissance and target selection based on strategic intelligence objectives. Updated: Campaign expanded to include multiple financial institutions across North America and Europe. Emotet payloads confirmed. Additional intelligence suggests coordination between multiple advanced persistent threat groups operating under state-spons...\n\n###### INTEL AGENT\n\n* Threat Actor Analysis: APT28 (Fancy Bear) has been observed conducting targeted attacks against financial institutions using sophisticated phishing campaigns and exploiting recently disclosed vulnerabilities. The threat actor group, believed to be operating under Russian military intelligence direction, has demonstrated advanced capabilities in social engineering, spear-phishing operations, and zero-day exploit development. Recent campaigns show increased sophistication in targeting supply chain vendors and trusted third-party service providers to gain initial access to high-value financial sector targets. The group maintains extensive command and control infrastructure across multiple continents with sophisticated domain generation algorithms and encrypted communication channels designed to evade network monitoring and traffic analysis systems.\n* Malware Deployment: The Emotet malware variant includes banking trojan capabilities and has been updated with new evasion techniques targeting Windows and Linux systems. This particular variant incorporates advanced anti-analysis features including virtual machine detection, sandbox evasion, and dynamic code obfuscation mechanisms that significantly complicate reverse engineering efforts. The malware demonstrates modular architecture allowing threat actors to deploy additional payloads including ransomware, credential stealers, and remote access trojans based on the specific objectives of individual operations. Network traffic analysis reveals sophisticated command and control protocols utilizing domain fronting and encrypted tunneling to maintain persistent communication channels while evading traditional intrusion detection systems.\n* Vulnerability Exploitation: CVE-2024-1234 affects multiple versions of Apache web server and all...\n\n---\nNote: Content has been truncated due to length constraints. Please refer to the Additional Analysis and Context attribute for complete details.",
                "aiProvider": "ThreatConnect AI"
            }
        ]
    }

If the **aiSummaryEnabled** system setting is turned on for your ThreatConnect instance, the AI-generated summary will display on the **AI insights** card when viewing the Group's **Details** screen in ThreatConnect.

File Indicator Considerations
"""""""""""""""""""""""""""""

File Indicators may have one or more of the following hashes: MD5, SHA1, and SHA256. When using the Batch API, you can provide values for these hashes using either of the following methods:

- Define hashes in the Indicator's summary
- Define hashes individually

**Define Hashes in the Indicator's Summary**

Use this method to define all hash values in the Indicator's ``summary`` field as a concatenated string using colon delimiters (i.e., ``md5 : sha1 : sha256``).

.. code:: json

    {
        "indicator": [
            {
                "summary": "905ad8176a569a36421bf54c04ba7f95 : a52b6986d68cdfac53aa740566cbeade4452124e : 25bdabd23e349f5e5ea7890795b06d15d842bde1d43135c361e755f748ca05d0",
                "type": "File"
            }
        ]
    }

**Define Hashes Individually**

Use this method to define each hash value using the individual ``md5``, ``sha1``, and ``sha256`` fields for the Indicator. Note that the presence of one or more of these fields will result in the Indicator's ``summary`` field being ignored during the import.

.. code:: json

    {
        "indicator": [
            {
                "md5": "905ad8176a569a36421bf54c04ba7f95",
                "sha1": "a52b6986d68cdfac53aa740566cbeade4452124e",
                "sha256": "25bdabd23e349f5e5ea7890795b06d15d842bde1d43135c361e755f748ca05d0",
                "type": "File"
            }        
        ]
    }

.. note::
    Occasionally, imported File Indicators may contain one or more hashes that existing File Indicators in the same owner also contain. Specifically, either an incoming or existing File Indicator will have additional hash type(s) that the other Indicator does not (e.g., the incoming Indicator has an MD5 and SHA1, while the existing Indicator has only the MD5, or vice versa). In this situation, the resulting File Indicator will end up with a "superset" of file hashes by either retaining the existing hash(es) or adding the new hash(es). However, certain situations may arise that require special processing when incoming file hash(es) cause conflicts with existing data (e.g., the incoming File Indicator contains an MD5 and SHA1, while the existing Indicator contains the same MD5 but a different SHA1). Use the ``fileMergeMode`` and ``hashCollisionMode`` fields to handle such situations.

Example Request
"""""""""""""""

Send a request in the following format to upload an input file to the Batch API for a batch job (the batch job whose ID is **12345** in this example).

**Request (HTTP)**

.. code::

    POST /v2/batch/12345
    Content-Type: application/octet-stream


    <batch input file>

**Request (cURL)**

.. code::

    curl --location 'https://companyabc.threatconnect.com/api/v2/batch/12345' \
    --header 'Timestamp: $UNIX_EPOCH_TIMESTAMP' \
    --header 'Authorization: TC $ACCESS_ID:$SIGNATURE' \
    --header 'Content-Type: application/octet-stream' \
    --data '@/Users/jsmith/Desktop/batchInputFile.json'

**Response (Success)**

.. code:: json

    HTTP/1.1 202 Accepted
    {
        status: "Queued"
    }

**Response (Overlarge Input File)**

.. code:: json

    HTTP/1.1 400 Bad Request
    {
        status: "Invalid",
        description: "File size greater than allowable limit of 2000000"
    }

Check the Status of a Batch Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to check the status of a file upload for a batch job (the batch job whose ID is **12345** in this example). Possible statuses include the following:

* Created
* Queued
* Running
* Completed

**Request**

.. code::

    GET /v2/batch/12345

**Response (Batch Job Still Running)**

.. code:: json

    HTTP/1.1 200 OK
    {
        status: "Running"
    }

**Response (Batch Job Completed)**

.. code:: json

    HTTP/1.1 200 OK
    {
        "status": "Success",
        "data": {
            "batchStatus": {
                "id": 12345,
                "status": "Completed",
                "errorCount": 342,
                "successCount": 405432,
                "unprocessCount": 0
            }
        }
    }

Query Parameters
""""""""""""""""

The ``/v2/batch/{batchId}`` endpoint supports the following query parameter:

* ``includeAdditional``: <*Boolean*> Specifies whether to include counts of successful and unsuccessful Indicator creations, Group creations, and associations in the response. (Default value: **false**) 


Retrieve Error Messages For a Batch Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve error messages for a batch job with an ``errorCount`` greater than zero. If there are no errors for the specified batch job, a 404 error will be returned.

**Request**

.. code::

    GET /v2/batch/12345/errors

**Response (Batch Job Still Running)**

.. code:: json

    HTTP/1.1 400 Bad Request
    {
        status: "Invalid",
        description: "Batch still in Running state"
    }

**Response (Batch Job Completed)**

.. code:: json

    HTTP/1.1 200 OK
    Content-Type: application/octet-stream ; boundary=
    Content-Length:
    Content-Encoding: gzip

.. note::
    Responses for batch jobs that ended in partial failures will include an error file that includes Tag, Attribute, or Indicator errors (fail on first).

Retrieve Error Details For a Batch Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve the details of errors for a batch job with an ``errorCount`` greater than zero. If there are no errors for the specified batch job, a 404 error will be returned.

**Request**

.. code::

    GET /v2/batch/12345/results

**Response**

.. code::

    HTTP/1.1 200 OK
    [
        {
            "code": "0x1003",
            "severity": "Error",
            "errorReason": "com.google.gson.JsonSyntaxException: java.lang.IllegalStateException: Not a JSON Object: \"name\"",
            "errorMessage": "Encountered an unexpected Exception while processing batch job. Last known JSON path: '$.group[1]': Last processed group[1] '00000000-0000-0000-0000-000000000000:0001'."
        }
    ]

Query Parameters
""""""""""""""""

The ``/v2/batch/{batchId}/results`` endpoint supports the following query parameters:

* ``code``: <*String Array*> The error code by which to filter results. Only one error code may be specified at a time, and the specified value must begin with the standard hexadecimal notation of **0x**.
* ``contains``: <*String*> The text included in the ``errorReason`` or ``errorMessage`` fields by which to filter results.
* ``severity``: <*String Array*> The severity by which to filter results. (Accepted values: **err**, **error**, **info**, **warn**, **warning**)