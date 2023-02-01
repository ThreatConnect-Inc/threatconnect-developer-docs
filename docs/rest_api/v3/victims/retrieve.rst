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
                "ownerName": "Demo Organization",
                "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=1",
                "name": "Bob Loblaw"
            },
            {
                "id": 2,
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
    To limit the results to a specific owner, append the ``?owner=`` query parameter to your request. For more information about the ``?owner=`` query parameter, see `Specify an Owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_.

Retrieve a Single Victim
^^^^^^^^^^^^^^^^^^^^^^^^

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

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not include in the default response, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter results using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.