Retrieve System Roles
---------------------

Retrieve All System Roles
^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all system roles:

.. code::

    GET /v3/security/systemRoles

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "User",
                "active": true,
                "assignable": true,
                "displayed": true
            },
            {
                "id": 2,
                "name": "Administrator",
                "active": true,
                "assignable": true,
                "displayed": true
            },
            {
                "id": 6,
                "name": "Operations Administrator",
                "active": true,
                "assignable": true,
                "displayed": true
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific System Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific system role:

.. code::

    GET /v3/security/systemRoles/{systemRoleId}

For example, the following request will retrieve data for the system role whose ID is 17:

.. code::

    GET /v3/security/systemRoles/17
    
JSON Response:

.. code:: json

    {
        "data": {
            "id": 17,
            "name": "Read Only User",
            "active": true,
            "assignable": true,
            "displayed": true
        },
        "status": "Success"
    }