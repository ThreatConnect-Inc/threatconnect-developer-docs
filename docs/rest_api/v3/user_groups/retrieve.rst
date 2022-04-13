Retrieve User Groups
--------------------

Retrieve All User Groups
^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all user groups in the Organization in which your API user account resides, use the following query:

.. code::

    GET /v3/security/userGroups

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "SOC Team",
                "description": "Main SOC users"
            },
            {
                "id": 2,
                "name": "IR Team",
                "description": "IR Team members, Levels 1-3"
            },
            {
                "id": 3,
                "name": "TI Team",
                "description": "Threat Intel Team, all levels"
            }
        ],
        "status": "Success"
    }

Retrieve a Single User Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific user group in the Organization in which your API user account resides, use a query in the following format:

.. code::

    GET /v3/security/userGroups/{userGroupId}

For example, the following query will return information about the user group with ID 3:

.. code::

    GET /v3/security/userGroups/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "name": "IR Team",
            "description": "IR Team members, Levels 1-3"
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
