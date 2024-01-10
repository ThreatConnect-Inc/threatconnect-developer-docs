V2 Batch API
------------

The following sections describe how to use the V2 Batch API, including how to create a batch job and upload a file to the job for processing. With the V2 Batch API, you can perform the following actions:

* Import Indicators and Groups
* Create Group-to-Group, Indicator-to-Group, and Group-to-Indicator associations
* Create and update Attributes, Tags, and Security Labels for Indicators and Groups
* Specify how to manage file hash merges and collisions for File Indicators

.. attention::
    The V2 Batch API does not support cross-owner associations.

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
    * **Merge** (default): The batch job will perform a merge operation and combine two or more existing File Indicators with separate file hashes into a single File Indicator with all file hashes. During this process, the File Indicator with the most recent lastModified date will be used as the "primary" copy and retain its Threat and Confidence Ratings (at least, until their values are overwritten by the values for the incoming File Indicator). Attributes, Security Labels, and Tags associated with all merged File Indicators will be applied to the "primary" copy as well. Because Attributes are appended to the "primary" copy, duplicate Attributes may be present if each File Indicator that was merged had similar Attributes.
* ``hashCollisionMode``: <*String*> Specifies how the batch job will handle file hash collisions that occur when importing or merging File Indicators (e.g., an incoming File Indicator contains an MD5 and SHA1, while an existing File Indicator contains the same MD5 but a different SHA1). Accepted values include the following:
    * **FavorExisting**: The batch job will favor hashes in the existing File Indicator and ignore conflicting hashes in the incoming File Indicator.
    * **FavorIncoming** (default): The batch job will favor hashes in the incoming File Indicator and overwrite conflicting hashes in the existing File Indicator.
    * **IgnoreExisting**: If a conflict exists between two or more existing File Indicators, the batch job will delete the existing File Indicators that caused conflict and then import the incoming File Indicator. If a conflict exists between one or more existing File Indicators and an incoming File Indicator, the batch job will ignore the existing Indicators. It will also remove their file hashes from the incoming Indicator, resulting in a new File Indicator being created without any conflicting file hashes. If all available file hashes are removed from the incoming Indicator, no new Indicator will be created.
    * **IgnoreIncoming**: The batch job will not import the incoming File Indicator causing the conflict, and existing File Indicators will not be updated.
    * **Split**: The batch job will not perform a merge; instead, it will apply the metadata (e.g., Threat and Confidence Ratings, Tags, Attributes) for the incoming File Indicator to all matching File Indicators in the specified owner.

.. note::
    If ``haltOnError`` is set to ``true`` and an error occurs during the batch process, the status for the batch job will be set to ``Completed`` and the value for ``errorCount`` will be greater than zero. Also, the value for ``unprocessedCount`` will be greater than zero unless the uploaded file did not contain valid JSON.

**Response (Success)**

.. code:: json

    HTTP/1.1 201 Created
    {
        batchId: "12345"
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
    When creating a batch job, the parameters defined in the body of the POST request must be accurate. When troubleshooting issues with the Batch API, make sure the parameter names in the request body are correct and that an accepted value is provided for each parameter.

Upload an Input File to a Batch Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The V2 Batch API expects to ingest a JSON file containing one or more lists of dictionaries. As shown in the following examples, the V2 Batch API expects Indicator and Group objects to be contained within their own ``indicator`` and ``group`` array, respectively. At a minimum, you must include the following fields for each object in each array:

* **indicator**
    * ``summary``: <*String*> The Indicator's summary.
    * ``type``: <*String*> The Indicator's type.
* **group**
    * ``name``: <*String*> The Group's name.
    * ``type``: <*String*> The Group's type.
    * ``xid``: <*String*> The Group's XID.

See the following tables for a list of additional fields that you may also include for Indicator and Group objects in their respective array.

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

When this input file is uploaded to the Batch API, the API will create a Host Indicator (**super-malicious.ru**) and Incident Group (**Ransomware Attack**) and then associate the Indicator to the Group. It will also add an Attribute, Security Label, and Tag to the Indicator and Group.

.. code:: json

    {
        "indicator": [
            {
                "rating": 3,
                "confidence": 60,
                "summary": "super-malicious.ru",
                "type": "Host",
                "externalDateAdded": "2023-08-25T18:23:43Z",
                "externalLastModified": "2023-08-26T18:23:43Z",
                "externalDateExpires": "2023-08-30T18:23:43Z",
                "firstSeen": "2023-08-25T18:23:43Z",
                "lastSeen": "2023-08-26T18:23:43Z",
                "associatedGroups": [
                    {
                        "groupXid": "00000000-0000-0000-0000-000000000000:0001"
                    }
                ],
                "attribute": [
                    {
                        "type": "Description",
                        "value": "A malicious domain"
                    }
                ],
                "securityLabel": [
                    {
                        "name": "TLP:AMBER"
                    }
                ],
                "tag": [
                    {
                        "name": "Malicious Host"
                    }
                ]
            }
        ],
        "group": [
            {
                "name": "Ransomware Attack",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0001",
                "eventDate": "2023-08-04T00:00:00Z",
                "externalDateAdded": "2023-08-25T18:23:43Z",
                "externalLastModified": "2023-08-26T18:23:43Z",
                "externalDateExpires": "2023-08-30T18:23:43Z",
                "firstSeen": "2023-08-25T18:23:43Z",
                "lastSeen": "2023-08-26T18:23:43Z",
                "attribute": [
                    {
                        "type": "Description",
                        "displayed": true,
                        "value": "A ransomware attack that targeted employees at Company ABC."
                    }
                ],
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

**Group-to-Indicator Association (New Indicator)**

When this input file is uploaded to the Batch API, the API will create a Host Indicator (**badguy.com**) and Incident Group (**Ransomware Attack Involving badguy.com**) and then associate the Group to the Indicator. It will also add an Attribute and Tag to the Indicator and Group.

.. code:: json

    {
        "indicator": [
            {
                "rating": 3,
                "confidence": 0,
                "summary": "badguy.com",
                "type": "Host",
                "attribute": [
                    {
                        "type": "Description",
                        "value": "A malicious domain"
                    }
                ],
                "tag": [
                    {
                        "name": "Malicious Host"
                    }
                ]
            }
        ],
        "group": [
            {
                "name": "Ransomware Attack Involving badguy.com",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0002",
                "eventDate": "2023-08-04T00:00:00Z",
                "firstSeen": "2023-08-25T18:23:43Z",
                "lastSeen": "2023-08-26T18:23:43Z",
                "attribute": [
                    {
                        "type": "Additional Analysis and Context",
                        "pinned": true,
                        "value": "This ransomware attack involved the badguy.com domain."
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ],
                "associatedIndicators": [
                    {
                        "summary": "badguy.com",
                        "indicatorType": "Host"
                    }
                ]
            }
        ]
    }

**Group-to-Indicator Association (Existing Indicator)**

When this input file is uploaded to the Batch API, the API will create an Incident Group (**Ransomware Attack Involving verybadguy.com**) and then associate an existing Host Indicator (**verybadguy.com**) to it. It will also add an Attribute and Tag to the Group.

.. code:: json

    {
        "group": [
            {
                "name": "Ransomware Attack Involving verybadguy.com",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0003",
                "eventDate": "2023-08-04T00:00:00Z",
                "externalDateAdded": "2023-08-25T18:23:43Z",
                "externalLastModified": "2023-08-26T18:23:43Z",
                "externalDateExpires": "2023-08-30T18:23:43Z",
                "attribute": [
                    {
                        "type": "Description",
                        "displayed": true,
                        "value": "A ransomware attack that involved the verybadguy.com Host Indicator."
                    }
                ],
                "tag": [
                    {
                        "name": "Ransomware"
                    }
                ],
                "associatedIndicators": [
                    {
                        "summary": "verybadguy.com",
                        "indicatorType": "Host"
                    }
                ]
            }
        ]
    }

.. note::
    When creating Group-to-Indicator associations, including the Indicator(s) in the JSON file will improve the efficiency of the batch job. Otherwise, a lookup will need to be made for each Indicator not included in the JSON file.

**Group-to-Group Association**

When this input file is uploaded to the Batch API, the API will create two Incident Groups and associate them to each other. It will also add an Attribute and Tag to each Group.

.. code:: json

    {
        "group": [
            {
                "name": "Compromised User Accounts",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0004",
                "associatedGroupXid": [
                    "00000000-0000-0000-0000-000000000000:0005"
                ],
                "eventDate": "2023-11-01T00:00:00Z",
                "attribute": [
                    {
                        "type": "Additional Analysis and Context",
                        "pinned": true,
                        "value": "A phishing email was used to compromise 53 user accounts at Company ABC."
                    }
                ],
                "tag": [
                    {
                        "name": "Phishing Email"
                    }
                ]
            },
            {
                "name": "Leaked Credentials",
                "type": "Incident",
                "xid": "00000000-0000-0000-0000-000000000000:0005",
                "eventDate": "2023-11-01T00:00:00Z",
                "attribute": [
                    {
                        "type": "Description",
                        "displayed": true,
                        "value": "An incident involving leaked credentials."
                    }
                ],
                "tag": [
                    {
                        "name": "Data Breach"
                    }
                ]
            }
        ]
    }

File Indicator Considerations
"""""""""""""""""""""""""""""

File Indicators may have one or more of the following hashes: MD5, SHA1, and SHA256. When using the Batch API, you can provide values for these hashes using either of the following methods.

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
        status: "Completed",
        errorCount: 3420,
        successCount: 405432,
        unprocessCount: 0
    }

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