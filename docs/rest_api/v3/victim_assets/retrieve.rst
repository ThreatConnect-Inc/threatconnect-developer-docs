Retrieve Victim Assets
----------------------

Retrieve All Victim Assets
^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Victim Assets, use the following query:

.. code::

    GET /v3/victimAssets/

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 4,
                "type": "Phone",
                "victimId": 2,
                "phone": "0123456789"
            },
            {
                "id": 3,
                "type": "WebSite",
                "victimId": 2,
                "website": "somewebsite.com"
            },
            {
                "id": 2,
                "type": "EmailAddress",
                "victimId": 2,
                "address": "jdoe@companyabc.com",
                "addressType": "Corporate email",
            },
            {
                "id": 1,
                "type": "EmailAddress"
                "victimId": 1,
                "address": "demo@sample.com"
            }
        ],
        "status": "Success"
    }

Retrieve a Single Victim Asset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Victim, use a query in the following format:

.. code::

    GET /v3/victimAssets/{victimAssetId}

For example, the following query will return information about the Victim Asset with ID 3:

.. code::

    GET /v3/victimAssets/3

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "type": "WebSite",
            "victimId": 2,
            "website": "somewebsite.com"
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
