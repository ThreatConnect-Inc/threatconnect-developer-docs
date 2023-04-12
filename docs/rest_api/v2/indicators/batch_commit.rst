Batch Upload: Indicators
------------------------

The Batch API allows you to create and delete Indicators in bulk via the HTTP POST method. After a batch entry is created, you can upload an Indicator file. The content of the file must be valid JSON and mimic the data structure of the Bulk JSON file download. Uploading a file instantly triggers a batch job to begin processing the data.

.. attention::
    The Batch API is restricted to Indicators and will improve performance when importing large amounts of data.

.. note::
    Document storage must be enabled on your ThreatConnect instance to use the Batch API.

The Batch Create resource creates a batch entry in the system. No batch processing is triggered until the batch input file is uploaded. The table below displays the fields required for the Batch Create message.

.. list-table::
   :widths: 20 15 15 20 30
   :header-rows: 1

   * - BatchConfig Parameter
     - Required
     - Applicable Batch Version(s)
     - Value
     - Description
   * - version
     - No
     - N/A
     - V1 (default)
     - | **Basic functionality**
       | - Supports importing Indicators only
       | - Includes limited features and settings
   * -
     - 
     - 
     - V2
     - | **Enhanced functionality**
       | - Supports importing Indicators and Groups
       | - Supports creating Group-to-Group, Indicator-to-Group, and Group-to-Indicator associations
       | - Includes all features described in this table
   * - owner
     - Yes
     - V1, V2
     - <name>
     - The name of the Organization, Community or Source in which data will be imported or modified
   * - haltOnError
     - Yes
     - V1, V2
     - TRUE
     - The batch process will stop processing the entire batch the first time it encounters an error
   * - 
     - 
     - 
     - FALSE
     - The batch process will attempt to continue processing the batch after encountering an error
   * - action
     - Yes
     - V1, V2
     - Create
     - Creates new, or modifies, existing, data in the specified owner
   * - 
     - 
     - 
     - Delete
     - Deletes existing data in the specified owner that matches any of the incoming batch data
   * - attributeWriteType
     - Yes
     - V1, V2
     - Append [1]_
     - Incoming Attributes will be added to those that may already be present on existing data (duplicates may occur, as redundancy checking is NOT performed)
   * - 
     - 
     - 
     - Replace
     - Attributes will be removed from existing data before incoming Attributes are added
   * - 
     - 
     - 
     - Static
     - Incoming Attributes will be ignored, and any that may already be present on existing data will not be changed
   * - tagWriteType
     - No
     - V2
     - Append
     - Incoming Tags will be added to those that may already be present on existing data
   * - 
     - 
     - 
     - Replace (default)
     - Tags will be removed from existing data before incoming Tags are added
   * - securityLabelWriteType
     - No
     - V2
     - Append
     - Incoming Security Labels will be added to those that may already be present on existing data
   * - 
     - 
     - 
     - Replace (default)
     - Security Labels will be removed from existing data before incoming Security Labels are added
   * - fileMergeMode
     - No
     - V2
     - Distribute
     - Metadata from incoming file hashes (e.g., Threat Rating, Confidence Rating, Tags, Attributes) are applied to all matching Indicators (up to 3 possible)
   * - 
     - 
     - 
     - Merge (default)
     - Combines multiple existing Indicators (if present) into one if incoming File Indicators correlate two or more previously separate hashes
   * - hashCollisionMode
     - No
     - V2
     - Split
     - Inhibits a merge and, instead, splits the incoming data out across any offending Indicators
   * - 
     - 
     - 
     - IgnoreIncoming
     - Drops incoming Indicator from the import, leaving pre-existing data the same as it was before importing offending Indicator
   * - 
     - 
     - 
     - IgnoreExisting
     - If conflict exists between two or more existing Indicators, deleted existing File Indicators that caused conflict
   * - 
     - 
     - 
     - FavorIncoming (default)
     - Favors hashes in incoming data, overwriting hashes that conflicted within existing data
   * - 
     - 
     - 
     - FavorExisting
     - Favors hashes in existing data, ignoring hashes that conflicted from incoming data

.. [1] Denotes a setting applicable to Version V2 only

.. note::
    If ``haltOnError`` is set to ``true`` and an error occurs, then the ``status`` will be set to ``Completed``, and the value for ``errorCount`` will be greater than zero. The value for ``unprocessedCount`` will be greater than zero unless the uploaded file did not contain valid JSON.

.. note::
    Occasionally, imported File Indicators may contain one or more hashes that other File Indicators in the same owner also contain. Specifically, either the incoming data or the existing data will contain additional hash type(s) that the other item did not have (e.g., the incoming data contains an MD5 and SHA1, while the existing data contains only the MD5, or vice versa). In this situation, the resulting File Indicator will end up with the "superset" of file hashes by either retaining the existing hash(es) or adding in the new hash(es). However, certain situations may arise that require special processing when incoming file hash(es) cause conflicts with existing data (e.g., the incoming data contains an MD5 and SHA1, while the existing data contains the same MD5 but a different SHA1). Use the ``fileMergeMode`` and ``hashCollisionMode`` parameters defined in the preceding table to handle such situations.

Batch Indicator Input File Formats
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Batch Upload feature expects to ingest a JSON file consisting of list(s) of dictionaries. As shown in the following examples, the V1 Batch operation expects a single list of Indicator objects only, whereas the enhanced V2 Batch operation expects Indicator and Group objects to be contained within its own ``indicator`` and ``group`` array definition, respectively. The list of fields expected within each Indicator or Group item parallels those described in the Indicator and Group creation operations. Additionally, you must include a ``type`` field within each item that defines the particular Indicator or Group type the item represents.

Batch Indicator Input File Format (V1)
"""""""""""""""""""""""""""""""""""""""

.. code:: json

 [{
        "rating": 3,
        "confidence": 60,
        "description": "a malicious domain",
        "summary": "super-malicious.ru",
        "type": "Host",
        "attribute": [{
               "type": "AttributeName",
               "value": "MyAttribute"
        }],
        "tag": [{
               "name": "MyTag"
        }]
 }]
    
Batch Indicator Input File Format (V2)
"""""""""""""""""""""""""""""""""""""""

**Indicator-to-Group Association**

.. code:: json

    {
          "indicator": [{
                  "rating": 3,
                  "confidence": 60,
                  "summary": "super-malicious.ru",
                  "type": "Host",
                  "associatedGroups": [{"groupXid":"00000000-0000-0000-0000-000000000000:1234"}],
                  "attribute": [{
                                  "type": "Description",
                                  "value": "a malicious domain"
                          }
                  ],
                  "tag": [{
                          "name": "MyTag"
                  }]
          }],
          "group": [{
                  "name": "New Incident",
                  "type": "Incident",
                  "xid": "00000000-0000-0000-0000-000000000000:1234",
                  "eventDate": "2019-11-26T00:00:00Z",
                  "attribute": [{
                          "type": "Description",
                          "displayed": true,
                          "value": "Ryuk C2"
                  }],
                  "tag": [{
                          "name": "MyOtherTag"
                  }]
          }]
    }

**Group-to-Indicator Association (New Indicator)**

.. code:: json

    {
          "indicator": [{
                  "rating": 3,
                  "confidence": 0,
                  "summary": "host123.com",
                  "type": "Host",
                  "attribute": [{
                                  "type": "Description",
                                  "value": "a malicious domain"
                          }
                  ],
                  "tag": [{
                          "name": "MyTag"
                  }]
          }],
          "group": [{
                  "name": "New Incident with Indicator 1",
                  "type": "Incident",
                  "xid": "00000000-0000-0000-0000-000000000000:0001",
                  "eventDate": "2019-11-26T00:00:00Z",
                  "attribute": [{
                          "type": "Description",
                          "displayed": true,
                          "value": "Ryuk C2"
                  }],
                  "tag": [{
                          "name": "MyOtherTag"
                  }],
            "associatedIndicators": [
              {
                "summary":"host123.com",
                "indicatorType":"Host"
              }
            ]

          }]
    }

**Group-to-Indicator Association (Existing Indicator)**

.. code:: json

    {
          "group": [{
                  "name": "New Incident with Existing Indicator 1",
                  "type": "Incident",
                  "xid": "00000000-0000-0000-0000-000000000000:0003",
                  "eventDate": "2019-11-26T00:00:00Z",
                  "attribute": [{
                          "type": "Description",
                          "displayed": true,
                          "value": "Ryuk C2"
                  }],
                  "tag": [{
                          "name": "MyOtherTag"
                  }],
            "associatedIndicators": [
              {
                "summary":"host123.com",
                "indicatorType":"Host"
              }
            ]

          }]
    }

.. note::
    When creating Group-to-Indicator associations, including the Indicator(s) in the JSON file will improve the efficiency of the batch job. Otherwise, a lookup will need to be made for each Indicator not included in the JSON file.

**Group-to-Group Association**

.. code:: json

    {
          "group": [{
                  "name": "New Incident 2",
                  "type": "Incident",
                  "xid": "00000000-0000-0000-0000-000000000000:0001",
            "associatedGroupXid": ["00000000-0000-0000-0000-000000000000:0002"],
                  "eventDate": "2019-11-26T00:00:00Z",
                  "attribute": [{
                          "type": "Description",
                          "displayed": true,
                          "value": "Ryuk C2"
                  }],
                  "tag": [{
                          "name": "MyOtherTag"
                  }]
          },
        {
                  "name": "New Incident 3",
                  "type": "Incident",
                  "xid": "00000000-0000-0000-0000-000000000000:0002",
                  "eventDate": "2019-11-26T00:00:00Z",
                  "attribute": [{
                          "type": "Description",
                          "displayed": true,
                          "value": "Ryuk C2"
                  }],
                  "tag": [{
                          "name": "MyOtherTag"
                  }]
          }]
    }

.. note::
    File Indicators may have any or all of MD5, SHA1, and/or SHA256 hash values. The hashes may be provided in either of two ways: (1) concatenated using 'space-colon-space' in the Indicator's ``summary`` field, or; (2) presented as individual ``md5``, ``sha1``, and ``sha256`` hash values. The presence of any hashes using this second method will cause the summary field to be ignored during import. For example, you could import a File Indicator with the MD5 hash ``905ad8176a569a36421bf54c04ba7f95``, SHA1 hash ``a52b6986d68cdfac53aa740566cbeade4452124e`` and SHA256 hash ``25bdabd23e349f5e5ea7890795b06d15d842bde1d43135c361e755f748ca05d0`` using either of the following:

    **Option 1**
    
    ``{"summary": "905ad8176a569a36421bf54c04ba7f95: a52b6986d68cdfac53aa740566cbeade4452124e: 25bdabd23e349f5e5ea7890795b06d15d842bde1d43135c361e755f748ca05d0", "type": "File", ...}``
    
    **Option 2**
    
    ``{"md5": "905ad8176a569a36421bf54c04ba7f95", "sha1": "a52b6986d68cdfac53aa740566cbeade4452124e", "sha256": "25bdabd23e349f5e5ea7890795b06d15d842bde1d43135c361e755f748ca05d0", "type": "File", ...}``        

.. note::
    Exporting indicators via the `JSON Bulk Reports <https://docs.threatconnect.com/en/latest/rest_api/v2/indicators/indicators.html#json-bulk-reports>`__ endpoint will create a file in this format.

.. warning::
    The maximum number of Indicators that can be created in one batch job is 25,000. If you need to create more Indicators, you will have to use multiple batch jobs.

**Sample Batch Create request**

.. code::

    POST /v2/batch/
    Content-type: application/json; charset=utf-8

    {
      "haltOnError": "false",
      "attributeWriteType": "Replace",
      "action": "Create",
      "owner": "Common Community"
      "version": "V2"
    }

**Server Response on Success**

.. code::

    HTTP/1.1 201 Created
    {
      batchId: "123"
    }

**Server Response on Insufficient Privileges**

.. code::

    HTTP/1.1 403 Forbidden
    {
      status: "Not Authorized",
      description: "Organization not authorized for batch"
    }

**Server Response on Incorrect Settings**

.. code::

    HTTP/1.1 403 Forbidden
    {
      status: "Not Authorized",
      description: "Document storage not enabled for this instance"
    }

**Sample Batch Upload Input File request**

Batch files should be sent as HTTP POST data to a REST endpoint, including the relevant ``batchId``, as shown in the format below.

.. code::

    POST /v2/batch/{batchId}

For example:

.. code::

    POST /v2/batch/123

    Content-Type: application/octet-stream
    Body: The JSON payload goes here.

**Server Response on Success**

.. code::

    HTTP/1.1 202 Accepted
    {
      status: "Queued"
    }

**Server Response on Overlarge Input File**

.. code::

    HTTP/1.1 400 Bad Request
    {
      status: "Invalid",
      description: "File size greater than allowable limit of 2000000"
    }

**Sample Batch Status Check request**

Use this request to check the status of a running batch-upload job. Possible GET response statuses are:

-  Created
-  Queued
-  Running
-  Completed

.. code::

    GET /v2/batch/123

**Server Response on Success (job still running)**

.. code::

    HTTP/1.1 200 OK
    {
      status: "Running"
    }

**Server Response on Success (job finished)**

.. code::

    HTTP/1.1 200 OK
    {
      status: "Completed",
      errorCount: 3420,
      successCount: 405432,
      unprocessCount: 0
    }

**Sample Batch Error Message request**

.. code::

    GET /v2/batch/123/errors

**Server Response on Success (job still running)**

.. code::

    HTTP/1.1 400 Bad Request
    {
      status: "Invalid",
      description: "Batch still in Running state"
    }

**Server Response on Success (job finished)**

.. code::

    HTTP/1.1 200 OK
    Content-Type: application/octet-stream ; boundary=
    Content-Length:
    Content-Encoding: gzip

.. note:: Batch jobs that end in partial failures will have an error file with a response having a 'reason text', which includes Tag, Attribute, or Indicator errors (fail on first).
