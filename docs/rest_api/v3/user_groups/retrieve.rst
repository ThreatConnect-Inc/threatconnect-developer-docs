Retrieve User Groups
--------------------

Retrieve All User Groups
^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all user groups in the Organization to which your API user account belongs:

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
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific User Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific user group in the Organization to which your API user account belongs:

.. code::

    GET /v3/security/userGroups/{userGroupId}

For example, the following request will retrieve data for the user group whose ID is 3:

.. code::

    GET /v3/security/userGroups/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "name": "TI Team",
            "description": "Threat Intel Team, all levels"
        },
        "status": "Success"
    }