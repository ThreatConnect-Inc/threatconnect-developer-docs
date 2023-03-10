Retrieve Victims
----------------

Retrieve All Victims
^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Victims:

.. code::

    GET /v3/victims

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=1",
                "name": "Bob Loblaw"
            },
            {
                "id": 2,
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2",
                "name": "John Doe",
                "org": "Company ABC",
                "suborg": "HR Department",
                "workLocation": "Washington, D.C.",
                "nationality": "American"
            },
            {...}
        ],
        "status": "Success"
    }

.. hint::
    Use the ``owner`` query parameter to `limit the results to a specific owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_.

Retrieve a Specific Victim
^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Victim:

.. code::

    GET /v3/victims/{victimId}

For example, the following request will retrieve data for the Victim whose ID is 3:

.. code::

    GET /v3/victims/3

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=3",
            "name": "Bill Smith",
            "org": "Company XYZ",
            "suborg": "Finance Department",
            "workLocation": "Pittsburgh, Pennsylvania",
            "nationality": "American"
        },
        "status": "Success"
    }