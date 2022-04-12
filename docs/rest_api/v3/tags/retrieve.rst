Retrieve Tags
-------------

Retrieve All Tags
^^^^^^^^^^^^^^^^^

To retrieve all Tags, use the following query:

.. code::

    GET /v3/tags/

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

Retrieve a Single Tag
^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Tag, use a query in the following format:

.. code::

    GET /v3/tags/{tagId}

For example, the following query will return information about the Tag with ID 2:

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

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
