Update Notes
------------

The following example illustrates the basic format for updating a Note:

.. code::

    PUT /v3/notes/{noteId}
    Content-Type: application/json

    {
        "text": "{updatedNoteContents}"
    }

For example, the following request will update the contents of the Note whose ID is 2:

.. code::

    PUT /v3/notes/2
    Content-Type: application/json
    
    {
        "text": "More detailed notes about a phishing threat."
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 2,
            "caseId": 2,
            "caseXid": "b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2",
            "text": "More detailed notes about a phishing threat.",
            "summary": "More detailed notes about a phishing threat.",
            "author": "pjones+analyst@threatconnect.com",
            "dateAdded": "2021-03-17T10:15:02Z",
            "lastModified": "2021-03-18T09:31:22Z",
            "edited": true
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request to the ``/v3/notes`` endpoint.