Retrieve Tags
-------------

Retrieve All Tags
^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Tags:

.. code::

    GET /v3/tags

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "Phishing",
                "owner": "Demo Organization",
                "description": "Apply this Tag to objects related to phishing attacks.",
                "lastUsed": "2021-11-08T18:01:36Z"
            },
            {
                "id": 2,
                "name": "Malicious Host",
                "owner": "Demo Organization",
                "lastUsed": "2021-11-14T13:54:20Z"
            },
            {
                "id": 3,
                "name": "Robbery",
                "owner": "Demo Organization",
                "lastUsed": "2021-11-14T18:52:38Z"
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Tag
^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Tag:

.. code::

    GET /v3/tags/{tagId}

For example, the following request will retrieve data for the Tag whose ID is 2:

.. code::

    GET /v3/tags/2

JSON Response

.. code:: json

    {
        "data": {
            "id": 2,
            "name": "Malicious Host",
            "owner": "Demo Organization",
            "lastUsed": "2021-11-14T13:54:20Z"
        },
        "status": "Success"
    }