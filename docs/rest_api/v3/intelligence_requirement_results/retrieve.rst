Retrieve Intelligence Requirement Results
-----------------------------------------

Retrieve All Intelligence Requirement Results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all results for all IRs in your Organization.

**Request**

.. code::

    GET /v3/intelRequirements/results

**Response**

.. code:: json

    {
        "next": "https://app.threatconnect.com/api/v3/intelRequirements/results?resultStart=100&resultLimit=100",
        "data": [
            {
                "id": 1,
                "matchedDate": "2023-08-29T16:46:58Z",
                "name": "CC9E6578A47182A941A478B276320E06 : CB872EDD1F532C10D0167C99530A65C4D4532A1E : 40AE43B7D6C413BECC92B07076FA128B875C8DBB4DA7C036639ECCF5A9FC784F",
                "ownerId": 83,
                "ownerName": "ThreatConnect Intelligence",
                "itemId": 100,
                "itemType": "File",
                "internal": false,
                "falsePositive": false,
                "associated": false,
                "archived": false
            },
            {
                "id": 2,
                "matchedDate": "2023-08-29T17:15:51Z",
                "name": "Stop DJVU - A ransomware family wreaking havoc among home users",
                "ownerId": 115,
                "ownerName": "Intel 471 Malware Intelligence",
                "itemId": 75,
                "itemType": "report",
                "internal": true,
                "falsePositive": false,
                "associated": false,
                "archived": false,
                "score": 1946    
            },
            {...}
        ]
    }

.. hint::
    To filter results based on whether they've been archived, associated to their corresponding IR, or marked as a false positive, include the ``tql`` query parameter in the request URI and assign it a value of ``isArchived``, ``isAssociated``, or ``isFalsePositive``, respectively.

Retrieve a Specific Intelligence Requirement Result
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific result.

**Example Request**

.. code::

    GET /v3/intelRequirements/results/{resultId}

For example, the following request will retrieve data for the result whose ID is 2.

**Request**

.. code::

    GET /v3/intelRequirements/result/2

**Response**

.. code:: json

    {
        "data": {
            "id": 2,
            "matchedDate": "2023-08-29T17:15:51Z",
            "name": "Stop DJVU - A ransomware family wreaking havoc among home users",
            "ownerId": 115,
            "ownerName": "Intel 471 Malware Intelligence",
            "itemId": 2629735,
            "itemType": "report",
            "internal": true,
            "falsePositive": false,
            "associated": false,
            "archived": false,
            "score": 1946
        },
        "status": "Success"
    }