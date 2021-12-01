Retrieve Users
--------------

Retrieve All Users
^^^^^^^^^^^^^^^^^^

To retrieve all users in the Organization in which your API user account resides, use the following query:

.. code::

    GET /v3/security/users

JSON Response:

.. code:: json

    {
        "data": [{
            "id": 1,
            "userName": "smithj@threatconnect.com",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "JMS",
            "role": "Administrator"
        }, 
        {
            "id": 2,
            "userName": "pjones+analyst@threatconnect.com",
            "firstName": "Pat",
            "lastName": "Jones",
            "pseudonym": "patjones",
            "role": "User"
        }, 
        {...}
        ],
        "status": "Success"
    }

Retrieve a Single User
^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific user in the Organization in which your API user account resides, use a query in the following format:

.. code::

    GET /v3/security/users/{userId}

For example, the following query will return information about the user with ID 3:

.. code::

    GET /v3/security/users/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "userName": "52583294827510809921",
            "firstName": "API",
            "lastName": "User",
            "pseudonym": "APIUserJMS",
            "role": "Api User"
        },
        "status": "Success"
    }

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
