Retrieve Victims
----------------

Retrieve All Victims
^^^^^^^^^^^^^^^^^^^^

To retrieve all Victims, use the following query:

.. code::

    GET /v3/victims/

JSON Response

.. code:: json

    {
        "data": [{
            "id": 1,
            "type": "Victim",
            "ownerName": "Demo Organization",
            "webLink": "/auth/victim/victim.xhtml?victim=1",
            "name": "Bob Loblaw"
        }, {
            "id": 2,
            "type": "Victim",
            "ownerName": "Demo Organization",
            "webLink": "/auth/victim/victim.xhtml?victim=2",
            "name": "John Doe",
            "description": "This victim’s bank account was hacked.",
            "org": "Company ABC",
            "suborg": "HR Department",
            "workLocation": "Washington, D.C.",
            "nationality": "American"
        },
        {...}
        ],
        "status": "Success"
    }

Retrieve a Single Victim
^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Victim, use a query in the following format:

.. code::

    GET /v3/victims/{victimId}

For example, the following query will return information about the Victim with ID 3:

.. code::

    GET /v3/victims/3

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "type": "Victim",
            "ownerName": "Demo Organization",
            "webLink": "/auth/victim/victim.xhtml?victim=3",
            "name": "Bill Smith",
            "description": "This victim got hacked.",
            "org": "Company XYZ",
            "suborg": "Finance Department",
            "workLocation": "Pittsburgh, Pennsylvania",
            "nationality": "American"
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned object, refer to `Request Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.