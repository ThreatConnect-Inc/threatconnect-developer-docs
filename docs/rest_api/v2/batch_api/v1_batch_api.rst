V1 Batch API
------------

The following subsections describe how to create a batch job and upload a file to the job for processing with the V1 Batch API. With the V1 Batch API, you can perform the following actions:

* Import Indicators
* Create and update Attributes and Tags for Indicators

Create a Batch Job
^^^^^^^^^^^^^^^^^^

Send a request in the following format to create a batch job that will use the V1 Batch API.

**Request**

.. code::

    POST /v2/batch
    Content-type: application/json; charset=utf-8


    {
        "version": "V2",
        "owner": "Demo Organization",
        "haltOnError": true,
        "action": "Create",
        "attributeWriteType": "Append"
    }

* ``version``: <*String*> The version of the Batch API to use. Set this field's value to ``V1`` to use the V1 Batch API.
* ``owner``: <*String*> **REQUIRED** The name of the Organization, Community, or Source in which the batch job will create or update data.
* ``haltOnError``: <*Boolean*> **REQUIRED** Specifies how the batch process should proceed if it encounters an error. Accepted values include the following:
    * **true**: The batch process will stop processing the entire batch job the first time it encounters an error.
    * **false**: The batch process will attempt to continue processing the batch job after encountering an error.
* ``action``: <*String*> **REQUIRED** The action that the batch job will perform on data included in the input file. Accepted values include the following:
    * **Create**: The batch job will create new and update existing data in the specified owner.
    * **Delete**: The batch job will delete existing data in the specified owner that matches any of the incoming data included in the input file.
* ``attributeWriteType``: <*String*> **REQUIRED** Specifies how the batch job will handle incoming Attributes included in the input file. Accepted values include the following:
    * **Replace**: The batch job will remove Attributes from existing Indicators and Groups before adding incoming Attributes.
    * **Static**: The batch job will ignore incoming Attributes and not update existing Attributes added to existing Indicators and Groups.

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

The V1 Batch API expects to ingest a JSON file containing one or more lists of dictionaries. As shown in the following example, the V1 Batch API expects a single list of Indicator objects. The list of fields expected within each Indicator object matches those described in the `Indicator <https://docs.threatconnect.com/en/latest/rest_api/v2/indicators/indicators.html#create-indicators>`_ creation operation. Additionally, you must include a ``type`` field within each object that defines the particular Indicator type the object represents.

.. hint::
    Exporting indicators via the `JSON Bulk Reports <https://docs.threatconnect.com/en/latest/rest_api/v2/indicators/indicators.html#json-bulk-reports>`_ endpoint will create a file in the proper format for the Batch API.

.. attention::
    The maximum number of Indicators that can be created in one batch job is 25,000. If creating more than 25,000 Indicators, use multiple batch jobs.

Example Input File
""""""""""""""""""

When this input file is uploaded to the Batch API, the API will create two Indicators (a Host and an Address). It will also add an Attribute and Tag to the Host Indicator.

.. code:: json

    [
        {
            "rating": 3,
            "confidence": 60,
            "description": "A malicious domain",
            "summary": "super-malicious.ru",
            "type": "Host",
            "attribute": [
                {
                    "type": "Additional Analysis and Context",
                    "value": "This malicious domain has been used in ransomware attacks."
                }
            ],
            "tag": [
                {
                    "name": "Malicious Host"
                }
            ]
        },
        {
            "summary": "96.38.88.212",
            "type": "Address"
        }
    ]

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