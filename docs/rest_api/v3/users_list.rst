Retrieve a List of Available Assignees
======================================

To retrieve a list of users to which a Case or Task can be assigned to, use the following query:

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
        }, {
            "id": 2,
            "userName": "pjones+analyst@threatconnect.com",
            "firstName": "Pat",
            "lastName": "Jones",
            "pseudonym": "patjones",
            "role": "User"
        }, {...},
           {...}
        ],
        "count": 13,
        "status": "Success"
    }

A specific user can be retrieved by using a query in the following format:

.. code::

    GET /v3/security/users/{userId}

For more information on assigning a Case or Task to a user, see the `Cases <https://docs.threatconnect.com/en/latest/case_management/cases/cases.html>`__ and `Workflow Tasks <https://docs.threatconnect.com/en/latest/case_management/tasks/tasks.html>`__ section of this documentation, respectively.
