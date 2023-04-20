Retrieve Victim Assets
----------------------

Retrieve All Victim Assets
^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Victim Assets:

.. code::

    GET /v3/victimAssets

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 4,
                "type": "Phone",
                "victimId": 2,
                "phone": "0123456789",
                "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2"
            },
            {
                "id": 3,
                "type": "WebSite",
                "victimId": 2,
                "website": "somewebsite.com",
                "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2"
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Victim Asset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Victim Asset:

.. code::

    GET /v3/victimAssets/{victimAssetId}

For example, the following request will retrieve data for the Victim Asset whose ID is 3:

.. code::

    GET /v3/victimAssets/3

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "type": "WebSite",
            "victimId": 2,
            "website": "somewebsite.com",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2"
        },
        "status": "Success"
    }