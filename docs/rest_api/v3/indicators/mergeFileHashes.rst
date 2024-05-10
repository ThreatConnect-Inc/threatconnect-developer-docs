Merge File Hashes
-----------------

If adding a new file hash to an existing File Indicator and a File Indicator containing that file hash exists in the same owner, you can merge the two File Indicators into a single File Indicator containing both file hashes and any Attributes, Security Labels, and Tags added to each Indicator.

You can merge only File Indicators containing different file hash types. For example, you can merge a File Indicator containing an MD5 file hash with a File Indicator containing a SHA1 file hash, but you cannot merge two File Indicators containing MD5 file hashes.

.. attention::
    You cannot merge multiple hash values at once. For example, if you want to merge three separate File Indicators, each of which contains a unique file hash type, you must submit two separate requests: one to merge the first two file hash types (e.g., MD5 and SHA1) and another to merge the last file hash type (e.g., SHA256).

The following request will update an existing File Indicator containing an MD5 file hash (**AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA**) and add a SHA1 file hash (**BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB**) to it. Because another File Indicator containing this SHA1 file hash exists in the same owner as the File Indicator being updated, ``"mode": "merge"`` will be included in the body of the request to merge the two File Indicators into a single File Indicator.

.. code::

    PUT /v3/indicators/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    Content-Type: application/json

    {
        "sha1": "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
        "mode": "merge"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 28,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2023-01-27T17:03:38Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/28/overview",
            "type": "File",
            "lastModified": "2023-01-27T17:09:03Z",
            "summary": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA : BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "md5": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "sha1": "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&owner=Demo+Organization"
        },
        "message": "Updated",
        "status": "Success"
    }

To remove a single file hash from a File Indicator, include ``"mode": "delete"`` in the body of the request. For example, the following request will remove the SHA1 file hash (**BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB**) just added to the File Indicator containing an MD5 file hash (**AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA**). Note that the Indicator's summary is encoded in the URL for this request.

.. code::

    PUT /v3/indicators/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%20%3A%20BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
    Content-Type: application/json
    
    {
        "sha1": "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
        "mode": "delete"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 28,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2023-01-27T17:03:38Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/28/overview",
            "type": "File",
            "lastModified": "2023-01-27T17:15:42Z",
            "summary": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "md5": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&owner=Demo+Organization"
        },
        "message": "Updated",
        "status": "Success"
    }