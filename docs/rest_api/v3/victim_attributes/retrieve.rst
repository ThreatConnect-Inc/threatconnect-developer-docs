Retrieve Victim Attributes
--------------------------

The following section describes how to retrieve Victim Attributes via the ``/v3/victimAttributes`` endpoint. In addition to the methods described in this section, you can retrieve Attributes added to a specific Victim by using the following query:

.. code::

    GET /v3/victims/{victimId}?fields=attributes

Retrieve All Victim Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Victim Attributes, use the following query:

.. code::

    GET /v3/victimAttributes/

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 2,
                "type": "Description",
                "value": "Ransomware attack victim.",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmith"
                },
                "dateAdded": "2021-11-09T15:49:22Z",
                "lastModified": "2021-11-09T15:49:22Z",
                "default": true
            },
            {
                "id": 1,
                "type": "Additional Analysis and Context",
                "value": "Based on additional analysis, it was determined that this victim’s bank account was hacked.",
                "source": "Phase of Intrusion",
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "role": "Api User"
                },
                "dateAdded": "2021-11-09T15:43:06Z",
                "lastModified": "2021-11-09T15:43:06Z",
                "default": false
            }
        ],
        "status": "Success"
    }

Retrieve a Single Victim Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Victim Attribute, use a query in the following format:

.. code::

    GET /v3/victimAttributes/{victimAttributeId}

For example, the following query will return information about the Victim Attribute with ID 2:

.. code::

    GET /v3/victimAttributes/2

JSON Response

.. code:: json

    {
        "data": {
            "id": 2,
            "type": "Description",
            "value": "Ransomware attack victim.",
            "createdBy": {
                "id": 1,
                "userName": "smithj@threatconnect.com",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmith"
            },
            "dateAdded": "2021-11-09T15:49:22Z",
            "lastModified": "2021-11-09T15:49:22Z",
            "default": true
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
