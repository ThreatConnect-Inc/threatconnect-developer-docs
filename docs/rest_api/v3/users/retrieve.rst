Retrieve Users
--------------

When retrieving data for users, additional fields will be included in the response for API users with an Organization role of Organization Administrator. In the examples used in the following subsections, the response an API user with an Organization role of Organization Administrator will receive is labeled **JSON Response (Organization Administrator):**.

Retrieve All Users
^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all users in the Organization in which your API user account resides:

.. code::

    GET /v3/security/users

JSON Response:

.. code:: json

{
    "data": [
        {
            "id": 1,
            "userName": "smithj@threatconnect.com"
        }, 
        {
            "id": 2,
            "userName": "pjones+analyst@threatconnect.com"
        },
        {
            "id": 3,
            "userName": "11112222333344445555"
        },
        {...}
    ],
    "status": "Success"
}

Retrieve a Specific User
^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific user in the Organization in which your API user account resides:

.. code::

    GET /v3/security/users/{userId}

For example, the following request will retrieve data for the user whose ID is 3:

.. code::

    GET /v3/security/users/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "userName": "11112222333344445555",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "jsmithAPI",
            "owner": "Demo Organization"
        },
        "status": "Success"
    }

JSON Response (Organization Administrator):

.. code:: json

    {
        "data": {
            "id": 3,
            "userName": "11112222333344445555",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "jsmithAPI",
            "owner": "Demo Organization",
            "lastPasswordChange": "2022-05-03T14:51:55Z",
            "termsAccepted": false,
            "logoutIntervalMinutes": 30,
            "systemRole": "Administrator",
            "ownerRoles": {
                "Demo Organization": "Organization Administrator",
                "Demo Community": "Director",
                "Demo Source": "Director"
            },
            "disabled": false,
            "locked": false,
            "passwordResetRequired": false,
            "twoFactorResetRequired": false
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not included in the default response, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter results using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.