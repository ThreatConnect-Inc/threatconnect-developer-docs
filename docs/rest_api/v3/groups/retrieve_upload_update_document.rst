Retrieve, Upload, and Update Files for Document and Report Groups
-----------------------------------------------------------------

Retrieve a Document or Report Group's File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Send a request in the following format to download the contents of the file uploaded to a Document or Report Group:

.. code::

    GET /v3/groups/{groupId}/download

The contents of the file will be returned as ``Content-Type: application/octet-stream``.

Upload a File to a Document or Report Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to upload the contents of a file to an existing Document or Report Group:

.. code::

    POST /v3/groups/{groupId}/upload
    Content-Type: application/octet-stream

    <raw report contents>

If uploading a file to the `Malware Vault <https://knowledge.threatconnect.com/docs/uploading-malware>`_, complete the following steps before performing the upload:

- Create a password-protected zip file on your computer that contains the file.
- Create a new Document Group with the additional fields ``malware`` set to ``true`` and ``password`` set to the zip file's password.

.. attention::
    If uploading a file **larger than 5GB**, contact your System Administrator about increasing the allowed file size for uploads.

.. note::
    If you upload a file whose extension differs from the one specified in the ``filename`` field for the Group, update the value of this field so that the extension matches that of the uploaded file.

Update a Document or Report Group's File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to update the contents of a file uploaded to a Document or Report Group:

.. code::

    PUT /v3/groups/{groupId}/upload
    Content-Type: application/octet-stream

    <new document contents>