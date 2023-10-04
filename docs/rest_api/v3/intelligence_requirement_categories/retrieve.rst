Retrieve Intelligence Requirement Categories
--------------------------------------------

Retrieve All Intelligence Requirement Categories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all IR categories on your ThreatConnect instance.

**Request**

.. code::

    GET /v3/intelRequirements/categories

**Response**

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "Nation State",
                "description": "IRs related to Nation State threat actors"
            },
            {
                "id": 2,
                "name": "Hacktivist",
                "description": "IRs related to hacktivists"
            }
        ],
        "count": 2,
        "status": "Success"
    }

Retrieve a Specific Intelligence Requirement Category
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific IR category.

**Example Request**

.. code::

    GET /v3/intelRequirements/categories/{categoryId}

For example, the following request will retrieve data for the IR category whose ID is 1.

**Request**

.. code::

    GET /v3/intelRequirements/categories/1

**Response**

.. code:: json

    {
        "data": {
            "id": 1,
            "name": "Nation State",
            "description": "IRs related to Nation State threat actors"
        },
        "status": "Success"
    }