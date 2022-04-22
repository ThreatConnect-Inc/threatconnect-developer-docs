Retrieve, Upload, and Update a Document
---------------------------------------

Retrieve a Document, Report, or Signature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To download the contents of a Document, Report, or Signature in ThreatConnect, use a query in the following format:

.. code::

    GET /v3/groups/{groupId}/download

The contents of a Document will be returned as ``Content-Type: application/octet-stream``. The contents of a Signature will be returned as ``Content-Type: text/plain``.

Upload a Document or Report
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To upload the contents of a Document or Report in ThreatConnect, use a query in the following format:

.. code::

    PUT /v3/groups/{groupId}/upload
    Content-Type: application/octet-stream

    <raw report contents>

If uploading a document to the `Malware Vault <https://training.threatconnect.com/learn/article/uploading-malware-kb-article>`_, the following steps must be completed before uploading the document:

- Create a password-protected zip file on your computer that contains the document.
- Create a new Document Group with the additional fields ``malware`` set to ``true`` and ``password`` set to the zip file's password.

.. attention::
    If you're **uploading a file larger than 5GB**, contact your System Administrator about increasing the allowed file size for uploads.

Update a Document or Report
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To update the contents of an existing Document or Report in ThreatConnect, use a query in the following format:

.. code::

    PUT /v3/groups/{groupId}/upload
    Content-Type: application/octet-stream

    New Document contents go here.