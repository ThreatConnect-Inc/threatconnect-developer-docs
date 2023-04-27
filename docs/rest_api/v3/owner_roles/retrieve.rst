Retrieve Owner Roles
--------------------

Retrieve All Owner Roles
^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all owner roles:

.. code::

    GET /v3/security/ownerRoles

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "User",
                "descriptionComm": "Read only access to all data",
                "descriptionAdmin": "Read only access to all data",
                "orgRole": false,
                "commRole": true,
                "version": 1,
                "available": true
            },
            {
                "id": 2,
                "name": "Commenter",
                "descriptionComm": "Post creation",
                "descriptionAdmin": "Post creation",
                "orgRole": false,
                "commRole": true,
                "version": 1,
                "available": true
            },
            {
                "id": 3,
                "name": "Contributor",
                "descriptionComm": "Indicator, Group, and Tag creation",
                "descriptionAdmin": "Indicator, Group, and Tag creation",
                "orgRole": false,
                "commRole": true,
                "version": 1,
                "available": true
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Owner Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific owner role:

.. code::

    GET /v3/security/ownerRoles/{ownerRoleId}

For example, the following request will retrieve data for the owner role whose ID is 15, which is a custom owner role:

.. code::

    GET /v3/security/ownerRoles/15

JSON Response:

.. code:: json

    {
        "data": {
            "id": 15,
            "name": "Example Org Custom Role",
            "descriptionOrg": "This is an example custom role. Do not use.",
            "descriptionAdmin": "This is an example custom role for an Organization.",
            "orgRole": true,
            "commRole": false,
            "available": true
        },
        "status": "Success"
    }