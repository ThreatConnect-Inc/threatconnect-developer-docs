Retrieve Owner Roles
--------------------

Retrieve All Owner Roles
^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all owner roles, including custom owner roles, in your ThreatConnect instance, use the following query:

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

Retrieve a Single Owner Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific owner role in your ThreatConnect instance, use a query in the following format:

.. code::

    GET /v3/security/ownerRoles/{ownerRoleId}

For example, the following query will return information about the owner role with ID 15, which is a custom owner role:

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

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
