Retrieve Notes
--------------

Retrieve All Notes
^^^^^^^^^^^^^^^^^^

To retrieve all Notes, use the following query:

.. code::

    GET /v3/notes/

JSON Response:

.. code:: json

    {
      "data": [{
        "id": 1,
        "caseId": 1,
        "caseXid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        "text": "Some notes about a case artifact.",
        "summary": "Some notes about a case artifact.",
        "author": "11112222333344445555",
        "dateAdded": "2021-04-22T20:17:15Z",
        "lastModified": "2021-04-22T20:17:15Z",
        "edited": False
      }, {
        "id": 2,
        "caseId": 2,
        "caseXid": "b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2",
        "text": "Some notes about a phishing threat.",
        "summary": "Some notes about a phishing threat.",
        "author": "pjones+analyst@threatconnect.com",
        "dateAdded": "2021-03-17T10:15:02Z",
        "lastModified": "2021-03-18T09:31:22Z",
        "edited": True
      }],
      "count": 2,
      "status": "Success"
    }

Retrieve a Single Note
^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Note, use a query in the following format:

.. code::

    GET /v3/notes/{noteID}

For example, the following query will return information about the Note with ID 1:

.. code::

    GET /v3/notes/1

JSON Response:

.. code:: json

    {
      "data": {
        "id": 1,
        "caseId": 1,
        "caseXid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        "text": "Some notes about a phishing threat.",
        "summary": "Some notes about a phishing threat.",
        "author": "11112222333344445555",
        "dateAdded": "2021-04-22T20:17:15Z",
        "lastModified": "22021-04-22T20:17:15Z",
        "edited": False
      },
      "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned Note, refer to the `Request Additional Fields for Returned Objects <../additional_fields.html>`__ section in this documentation.

Filter Results
^^^^^^^^^^^^^^

To filter returned Notes using ThreatConnect Query Language (TQL), refer to the `Filter Results with TQL <../filter_results.html>`__ section in this documentation.
