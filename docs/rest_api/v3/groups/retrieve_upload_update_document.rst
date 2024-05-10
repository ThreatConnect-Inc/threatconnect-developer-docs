Retrieve, Upload, and Update Files for Document and Report Groups
-----------------------------------------------------------------

Retrieve a Document or Report Group's File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Send a request in the following format to download the contents of the file uploaded to a Document or Report Group:

**Example Request (Group ID)**

.. code::

    GET /v3/groups/{groupId}/download

**Example Request (Group XID)**

.. code::

    GET /v3/groups/{groupXid}/download?owner={ownerName}

The contents of the file will be returned as ``Content-Type: application/octet-stream``.

Upload a File to a Document or Report Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a Document or Report Group
"""""""""""""""""""""""""""""""""

Before you can upload a file to a Document or Report Group, the Group must exist in one of your ThreatConnect owners. The following examples demonstrate how to create a Document and Report Group.

**Request (Document)**

.. code::

    POST /v3/groups
    Content-Type: application/json

    {
        "type": "Document",
        "fileName": "example_document.pdf",
        "name": "Example Document Group"
    }

**Request (Report)**

.. code::

    POST /v3/groups
    Content-Type: application/json
    
    {
        "type": "Report",
        "fileName": "example_report.pdf",
        "name": "Example Report Group"
    }

Upload a File
"""""""""""""

Send a request in the following format to upload the contents of a file to an existing Document or Report Group. Note that the ``filename`` query parameter is only required if the ``fileName`` field was not assigned a value when the Group was created.

**Example Request (Group ID)**

.. code::

    POST /v3/groups/{groupId}/upload?filename={fileName.extension}
    Content-Type: application/octet-stream

    <raw file contents>

**Example Request (Group XID)**

.. code::

    POST /v3/groups/{groupXid}/upload?filename={fileName.extension}&owner={ownerName}
    Content-Type: application/octet-stream

    <raw file contents>

.. hint::
    When uploading a file to a Group via a POST request, set the ``updateIfExists`` query parameter to ``true`` to replace any existing file uploaded to the Group. Alternatively, use a PUT request to update the file uploaded to the Group, as described in the `"Update a Document or Report Group's File"<#id27>`_ section.

If uploading a file to the `Malware Vault <https://knowledge.threatconnect.com/docs/uploading-malware>`_, complete the following steps before performing the upload:

- Create a password-protected zip file on your computer that contains the file.
- Create a new Document Group with the additional fields ``malware`` set to ``true`` and ``password`` set to the zip file's password.

.. attention::
    If uploading a file **larger than 5GB**, contact your System Administrator about increasing the allowed file size for uploads.

.. note::
    If you upload a file whose extension differs from the one specified in the ``fileName`` field when the Group was created, use the ``filename`` query parameter to update the value of this field so that the extension matches that of the uploaded file.

The following request will upload a file named **report.pdf** to the Report Group whose ID is 25. In this example, the ``filename`` query parameter is included in the request URI because the ``fileName`` field was not defined when the Group was created. If the ``fileName`` field had been defined when the Group was created, then the ``filename`` query parameter would not be required.

**Request (HTTP)**

.. code::

    POST /v3/groups/25/upload?filename=report.pdf
    Content-Type: application/octet-stream

    <raw file contents>

**Request (cURL)**

.. code::

    curl --location --request POST 'https://app.threatconnect.com/api/v3/groups/25/upload?filename=report.pdf' \
    --header 'Timestamp: $UNIX_EPOCH_TIMESTAMP' \
    --header 'Authorization: TC $ACCESS_ID:$SIGNATURE' \
    --header 'Content-Type: application/octet-stream' \
    --data '@/Users/jsmith/Desktop/report.pdf'

**Response**

.. code:: json

    {
        "message": "Upload successful",
        "status": "Success"
    }

Update a Document or Report Group's File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to update the contents of a file uploaded to a Document or Report Group:

**Example Request (Group ID)**

.. code::

    PUT /v3/groups/{groupId}/upload?filename={fileName.extension}
    Content-Type: application/octet-stream

    <new file contents>

**Example Request (Group XID)**

.. code::

    PUT /v3/groups/{groupXid}/upload?filename={fileName.extension}&owner={ownerName}
    Content-Type: application/octet-stream

    <new file contents>

The following request will update the contents of the file named **report.pdf** uploaded to the Report Group whose ID is 25:

**Request (HTTP)**

.. code::

    PUT /v3/groups/25/upload?filename=report.pdf
    Content-Type: application/octet-stream

    <new file contents>

**Request (cURL)**

.. code::

    curl --location --request PUT 'https://app.threatconnect.com/api/v3/groups/25/upload?filename=report.pdf' \
    --header 'Timestamp: $UNIX_EPOCH_TIMESTAMP' \
    --header 'Authorization: TC $ACCESS_ID:$SIGNATURE' \
    --header 'Content-Type: application/octet-stream' \
    --data '@/Users/jsmith/Desktop/report.pdf'

**Response**

.. code:: json

    {
        "message": "Upload successful",
        "status": "Success"
    }