Retrieve Attribute Types
------------------------

Retrieve All Attribute Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Attribute Types, use the following query:

.. code::

    GET /v3/attributeTypes/

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "Additional Analysis and Context",
                "description": "Relevant research and analysis associated with this Indicator, Signature, or Activity Group. Can be internal analysis or links to published articles, whitepapers, websites, or any reference providing amplifying information or geo-political context.",
                "maxSize": 65536,
                "allowMarkdown": true,
                "errorMessage": "Please enter valid Additional Analysis and Context.",
                "systemRequired": true
            },
            {
                "id": 2,
                "name": "Adversary Motivation Type",
                "description": "Select an overall motivation.",
                "maxSize": 21,
                "allowMarkdown": false,
                "errorMessage": "Please enter valid Adversary Motivation Type.",
                "systemRequired": false
            },
            {...}
        ],
        "status": "Success"
    }


Retrieve a Single Attribute Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Attribute Type, use a query in the following format:

.. code::

    GET /v3/attributeTypes/{attributeTypeId}

For example, the following query will return information about the Attribute Type with ID 3:

.. code::

    GET /v3/attributeTypes/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "name": "Adversary Type",
            "description": "The type of Adversary.",
            "maxSize": 50,
            "allowMarkdown": false,
            "errorMessage": "Please enter valid Adversary Type: Group, Persona.",
            "systemRequired": false
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
