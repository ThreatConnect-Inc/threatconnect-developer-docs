Retrieve Notes
--------------

Retrieve All Notes
^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Notes:

.. code::

    GET /v3/notes

JSON Response:

.. code:: json

{
    "data": [
        {
            "id": 1,
            "text": "Some notes about a case artifact.",
            "summary": "Some notes about a case artifact.",
            "author": "11112222333344445555",
            "dateAdded": "2021-04-22T20:17:15Z",
            "lastModified": "2021-04-22T20:17:15Z",
            "edited": false,
            "artifactId": 12
        },
        {
            "id": 2,
            "caseId": 2,
            "caseXid": "b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2",
            "text": "Some notes about a phishing threat.",
            "summary": "Some notes about a phishing threat.",
            "author": "pjones+analyst@threatconnect.com",
            "dateAdded": "2021-03-17T10:15:02Z",
            "lastModified": "2021-03-18T09:31:22Z",
            "edited": true
        },
        {...}
    ],
    "status": "Success"
}

Retrieve a Specific Note
^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Note:

.. code::

    GET /v3/notes/{noteId}

For example, the following request will retrieve data for the Note whose ID is 1:

.. code::

    GET /v3/notes/1

JSON Response:

.. code:: json

    {
        "data": {
            "id": 1,
            "text": "Some notes about a case artifact.",
            "summary": "Some notes about a case artifact.",
            "author": "11112222333344445555",
            "dateAdded": "2021-04-22T20:17:15Z",
            "lastModified": "2021-04-22T20:17:15Z",
            "edited": false,
            "artifactId": 12
        },
        "status": "Success"
    }