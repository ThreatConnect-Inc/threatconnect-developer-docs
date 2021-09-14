Retrieve Attribute Types
------------------------

Retrieve All Attribute Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Attribute types, use the following query:

.. code::

    GET /v3/attributeTypes/

JSON Response:

.. code:: json

    {
        "data": [{
            "id": 1,
            "name": "Additional Analysis and Context",
            "description": "Relevant research and analysis associated with this Indicator, Signature, or Activity Group. Can be internal analysis or links to published articles, whitepapers, websites, or any reference providing amplifying information or geo-political context.",
            "maxSize": 65536,
            "allowMarkdown": True,
            "errorMessage": "Please enter valid Additional Analysis and Context.",
            "systemRequired": True
        }, {
            "id": 2,
            "name": "Adversary Motivation Type",
            "description": "Select an overall motivation.",
            "maxSize": 21,
            "allowMarkdown": False,
            "errorMessage": "Please enter valid Adversary Motivation Type.",
            "systemRequired": False
        }, {...},
           {...}
        ],
        "count": 80,
        "status": "Success"
    }


Retrieve a Single Attribute Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Attribute type, use a query in the following format:

.. code::

    GET /v3/attributeTypes/{attributeTypeID}

For example, the following query will return information about the Attribute type with ID 3:

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
        "allowMarkdown": False,
        "errorMessage": "Please enter valid Adversary Type: Group, Persona.",
        "systemRequired": False
    },
    "status": "Success"
    }

Filter Results
^^^^^^^^^^^^^^

To filter returned Attribute types using ThreatConnect Query Language (TQL), refer to the `Filter Results with TQL <../filter_results.html>`__ section in this documentation.
