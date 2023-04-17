Create Notes
-------------

The following example illustrates the basic format for creating a Note:

.. code::

    POST /v3/notes
    {
        "caseId": 1,
        "text": "This is an example note."
    }
  
For example, the following request will add a Note to the Case whose ID is 3:

.. code::

    POST /v3/notes
    {
        "caseId": 3,
        "text": "Review the contents of the malware investigation that was recently closed."
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 7,
            "caseId": 3,
            "caseXid": "d7dafb59-bf74-46fe-bf18-8da14cc59219",
            "text": "Review the contents of the malware investigation that was recently closed.",
            "summary": "Review the contents of the malware investigation that was recently closed.",
            "author": "11112222333344445555",
            "dateAdded": "2022-04-06T13:14:25Z",
            "lastModified": "2022-04-06T13:14:25Z",
            "edited": false
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request to the ``/v3/notes`` endpoint.