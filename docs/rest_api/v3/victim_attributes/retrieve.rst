Retrieve Victim Attributes
--------------------------

The following section describes how to retrieve Victim Attributes via the ``/v3/victimAttributes`` endpoint. In addition to the methods described in this section, you can send the following request to retrieve Attributes added to a specific Victim: ``GET /v3/victims/{victimId}?fields=attributes``.

Retrieve All Victim Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Victim Attributes:

.. code::

    GET /v3/victimAttributes

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 2,
                "dateAdded": "2021-11-09T15:49:22Z",
                "type": "Description",
                "value": "Ransomware attack victim.",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com"
                },
                "lastModified": "2021-11-09T15:49:22Z",
                "pinned": false,
                "default": true
            },
            {
                "id": 1,
                "dateAdded": "2021-11-09T15:43:06Z",
                "type": "Additional Analysis and Context",
                "value": "Based on additional analysis, it was determined that this victim's bank account was hacked.",
                "source": "Phase of Intrusion",
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555"
                },
                "lastModified": "2021-11-09T15:43:06Z",
                "pinned": false,
                "default": false
            }
        ],
        "status": "Success"
    }

Retrieve a Specific Victim Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Victim Attribute:

.. code::

    GET /v3/victimAttributes/{victimAttributeId}

For example, the following request will retrieve data for the Victim Attribute whose ID is 2:

.. code::

    GET /v3/victimAttributes/2

JSON Response

.. code:: json

    {
        "data": {
            "id": 2,
            "dateAdded": "2021-11-09T15:49:22Z",
            "type": "Description",
            "value": "Ransomware attack victim.",
            "createdBy": {
                "id": 1,
                "userName": "smithj@threatconnect.com"
            },
            "lastModified": "2021-11-09T15:49:22Z",
            "pinned": false,
            "default": true
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not included in the default response, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter results using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.