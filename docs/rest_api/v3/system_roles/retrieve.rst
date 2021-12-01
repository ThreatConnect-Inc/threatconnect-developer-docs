Retrieve System Roles
---------------------

Retrieve All System Roles
^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all system roles in your ThreatConnect instance, use the following query:

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
            {
                "id": 9,
                "name": "Api User",
                "active": true,
                "assignable": false,
                "displayed": false
            },
            {
                "id": 10,
                "name": "Accounts Administrator",
                "active": true,
                "assignable": true,
                "displayed": true
            },
        {...}
        ],
        "status": "Success"
    }

Retrieve a Single System Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific system role in your ThreatConnect instance, use a query in the following format:

.. code::

    GET /v3/security/systemRoles/{systemRoleId}

For example, the following query will return information about the system role with ID 17:

.. code::

    GET /v3/security/systemRoles/17

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

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.