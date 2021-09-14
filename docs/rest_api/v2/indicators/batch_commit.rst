Batch Upload: Indicators
------------------------

The Batch API allows bulk Indicator creation and deletion via the HTTP
POST method. After creating a batch, an Indicator file is uploaded. The
content of the file must be valid JSON, with content and format
mimicking the data structure of the Bulk JSON file download. A file
upload instantly triggers a batch job to begin processing the data. The
Batch API is restricted to Indicators and will improve performance when
importing large amounts of data.

.. note:: Document Storage is required to use the Batch API.

The Batch Create resource creates a batch entry in the system. No batch processing is triggered until the batch input file is uploaded. The table below displays the fields required for the Batch Create message.

+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| BatchConfig Parameter  | Required | Applicable Batch Version(s)  |         Value           |                                                              Description                                                                         |
+========================+==========+==============================+=========================+==================================================================================================================================================+
| version                |    No    |              NA              |       V1 (default)      | Basic functionality: For Indicator import only with limited available features/settings                                                          |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |           V2            | Enhanced functionality: Allows import of Group items, Associations, and other options as described below                                         |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| owner                  |    Yes   |             V1, V2           |         <name>          | The name of the Organization, Community or Source in which to import/modify data                                                                 |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| haltOnError            |    Yes   |             V1, V2           |          TRUE           | Batch process stops processing entire batch first time it reaches an error during processing.                                                    |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |          FALSE          | Batch process attempts to continue after encountering problems during processing.                                                                |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| action                 |    Yes   |             V1, V2           |          Create         | Creates new, or modifies, existing data in the specified Owner                                                                                   |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |          Delete         | Deletes existing data in the specified Owner that matches any of the incoming batch data                                                         |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| attributeWriteType     |    Yes   |             V1, V2           |          Append*        | Incoming Attributes will add to those that may already be present on existing data (may cause duplicates; redundancy checking is NOT performed). |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |          Replace        | Attributes will be removed from existing data before adding incoming Attributes.                                                                 |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |          Static         | Incoming Attributes will be ignored, leaving any that may already be present on existing data alone.                                             |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| tagWriteType           |    No    |             V2               |          Append         | Incoming Tags will be added to those that may already be present on existing data.                                                               |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |    Replace (default)    | Tags will be removed from existing data before adding incoming Tags.                                                                             |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| securityLabelWriteType |    No    |             V2               |          Append         | Incoming Security Labels will add to those that may already be present on existing data.                                                         |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |    Replace (default)    | Security Labels will be removed from existing data before adding incoming Security Labels.                                                       |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| fileMergeMode          |    No    |             V2               |        Distribute       | Rating, Confidence, Tags, Attributes, etc., from incoming file hashes are applied to all matching Indicators (up to 3 possible).                 |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |      Merge (default)    | Combines multiple existing Indicators (if present) into one, if incoming file Indicators correlate two or more previously separate hashes        | 
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| hashCollisionMode      |    No    |             V2               |           Split         | Inhibits a merge and, instead, splits the incoming data out across any offending Indicators                                                      | 
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |      IgnoreIncoming     | Drops incoming Indicator from the import, leaving pre-existing data the same as it was before importing offending Indicator                      | 
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |      IgnoreExisting     | If conflict exists between two or more existing Indicators, existing file Indicators that caused conflict are deleted.                           |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              | FavorIncoming (default) | Favors hashes in incoming data, overwriting hashes that conflicted within existing data                                                          |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                        |          |                              |      FavorExisting      | Favors hashes in existing data, ignoring hashes that conflicted from incoming data                                                               |
+------------------------+----------+------------------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
*Denotes a setting applicable to Version V2 only

.. note:: If ``haltOnError`` is set to ‘true’ and an error occurs, then the status will be set to ‘Completed’, and ‘errorCount’ will be greater than zero. The ‘unprocessedCount’ field will be greater than zero, unless the uploaded file did not contain valid JSON.

.. note:: Occasionally, imported File Indicators may overlap one or more hashes with other File Indicators already present within the system. In the typical situation, either the incoming data or the existing data will contain additional hash type[s] that the other item did not have (e.g., Incoming data has both an md5 and sha1, while the existing data has only the md5, or vice versa). In this typical situation, the resulting File Indicator will end up with the "superset" of file hashes by either retaining the existing hash[es] or adding in the new hash[es]. However, certain non-typical situations may exist that require special processing when incoming file hash[es] cause conflicts with existing data (e.g., Incoming data has an md5 and sha1, while the existing data has the same md5 but a different sha1). The behavior in situations like these are controlled by the ``fileMergeMode`` and ``hashCollisionMode`` parameters defined in the above table.

Batch Indicator Input File Format (V1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: json

 [{
	"indicator": [{
		"rating": 3,
		"confidence": 60,
		"summary": "super-malicious.ru",
		"type": "Host",
		"associatedGroups": ["00000000-0000-0000-0000-000000000000:1234"],
		"attribute": [{
				"type": "Description",
				"value": "a malicious domain"
			},
			{
				"type": "AttributeName",
				"value": "MyAttribute"
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
 }]

The Batch Upload feature expects to ingest a JSON file consisting of list(s) of dictionaries. As shown in the above examples, the default/legacy "V1" Batch operation expects a single list of Indicator objects only. For enhanced "V2" Batch operation, both Indicator and Group objects are supported, where each is to be contained inside of its own "indicator" and/or "group" array definition.
Generally speaking, the list of fields expected within each Indicator or Group item parallels those described in the Indicator and Group creation operations (specified `here <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#create-indicators>`_ and `here <https://docs.threatconnect.com/en/latest/rest_api/groups/groups.html#create-groups>`_). Additionally, a 'type' field is required within each item corresponding to the particular Indicator or Group type being specified (e.g., "Host", "Address", etc., for Indicators and "Incident", "Adversary", etc., for Groups).

.. note:: File Indicators may have any or all of MD5, SHA1, and/or SHA256 hash values. The hashes may be provided in either of two ways: (1) concatenated using 'space-colon-space' into the 'summary' field of the Indicator, or; (2) presented as individual 'md5', 'sha1', and 'sha256' hash values. The presence of any hashes using this second method will cause the summary field to be ignored during import. For example, consider a File Indicator with the md5 hash ``905ad8176a569a36421bf54c04ba7f95``, sha1 hash ``a52b6986d68cdfac53aa740566cbeade4452124e`` and sha256 hash ``25bdabd23e349f5e5ea7890795b06d15d842bde1d43135c361e755f748ca05d0``, which could be imported in either of the two following ways:

   ``Option 1``
   
   {
   "summary": "905ad8176a569a36421bf54c04ba7f95: a52b6986d68cdfac53aa740566cbeade4452124e:
   25bdabd23e349f5e5ea7890795b06d15d842bde1d43135c361e755f748ca05d0",
   "type": "File",
   ...
   }
   
   ``Option 2``
   
   {
   "md5": "905ad8176a569a36421bf54c04ba7f95",
   "sha1": "a52b6986d68cdfac53aa740566cbeade4452124e",
   "sha256": "25bdabd23e349f5e5ea7890795b06d15d842bde1d43135c361e755f748ca05d0",
   "type": "File",
   ...
   }        

.. note:: Exporting indicators via the `JSON Bulk Reports <https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html#json-bulk-reports>`__ endpoint will create a file in this format.

.. warning:: The maximum number of Indicators that can be created in one batch job is 25,000. If you need to create more Indicators, you will have to use multiple batch jobs.

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
