Retrieve Users
--------------

When retrieving users, additional fields will be included in the response for API users with an Organization role of Organization Administrator. In the examples used in the following subsections, the response an API user with an Organization role of Organization Administrator will receive is labeled **JSON Response (Organization Administrator):**.

Retrieve All Users
^^^^^^^^^^^^^^^^^^

To retrieve all users in the Organization in which your API user account resides, use the following query:

.. code::

    GET /v3/security/users

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "userName": "smithj@threatconnect.com",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "JMS",
                "owner": "Demo Organization",
                "systemRrole": "Administrator"
            }, 
            {
                "id": 2,
                "userName": "pjones+analyst@threatconnect.com",
                "firstName": "Pat",
                "lastName": "Jones",
                "pseudonym": "patjones",
                "owner": "Demo Organization",
                "systemRrole": "User"
            },
            {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization",
                "systemRrole": "Api User"
            },
            {...}
        ],
        "status": "Success"
    }

JSON Response (Organization Administrator):

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "userName": "smithj@threatconnect.com",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "JMS",
                "owner": "Demo Organization",
                "lastLogin": "2022-09-07T12:19:42Z",
                "lastPasswordChange": "2022-08-04T16:24:25Z",
                "uiTheme": "Light",
                "jobFunction": "Threat Intelligence",
                "jobRole": "Analyst",
                "termsAccepted": true,
                "logoutIntervalMinutes": 240,
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
            {
                "id": 2,
                "userName": "pjones+analyst@threatconnect.com",
                "firstName": "Pat",
                "lastName": "Jones",
                "pseudonym": "patjones",
                "owner": "Demo Organization",
                "lastLogin": "2022-09-07T11:27:12Z",
                "lastPasswordChange": "2022-09-02T09:13:02Z",
                "uiTheme": "Dark",
                "jobFunction": "Incident Response",
                "jobRole": "Analyst",
                "termsAccepted": true,
                "logoutIntervalMinutes": 30,
                "systemRole": "User",
                "ownerRoles": {
                    "Demo Organization": "Standard User",
                    "Demo Community": "Director",
                    "Demo Source": "Director"
                },
                "disabled": false,
                "locked": false,
                "passwordResetRequired": false,
                "twoFactorResetRequired": false
            },
            {
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
            "userName": "11112222333344445555",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "jsmithAPI",
            "owner": "Demo Organization",
            "systemRole": "Api User"
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

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
