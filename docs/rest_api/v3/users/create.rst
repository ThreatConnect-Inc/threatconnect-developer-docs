Create Users
------------

.. attention::

    Only API users with an Organization role of Organization Administrator can create users.

The basic format for creating a user is:

.. code::

    POST /v3/security/users
    {
        "firstName": "John",
        "lastName": "Smith",
        "userName": "smithj@companyabc.com",
        "password": "Password1!",
        "owner": "Demo Organization",
        "ownerRoles": {
            "Demo Organization": "Organization Administrator"
        },
        "systemRole": "User"
    }

For example, the following query will create a user account where the user will be required to reset their password and enroll in MFA after logging into ThreatConnect for the first time:

.. code::

    POST /v3/security/users
    {
        "firstName": "Herschel",
        "lastName": "Hodges",
        "userName": "hodgesh@companyabc.com",
        "password": "Password1!",
        "owner": "Demo Organization",
        "ownerRoles": {
            "Demo Organization": "Organization Administrator"
        },
        "systemRole": "User",
        "passwordResetRequired": true,
        "twoFactorResetRequired": true
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 12,
            "userName": "hodgesh@companyabc.com",
            "firstName": "Herschel",
            "lastName": "Hodges",
            "owner": "Demo Organization",
            "lastPasswordChange": "2022-09-07T12:11:13Z",
            "uiTheme": "Light",
            "termsAccepted": false,
            "logoutIntervalMinutes": 0,
            "systemRole": "User",
            "disabled": false,
            "locked": false,
            "passwordResetRequired": true,
            "twoFactorResetRequired": true
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request for the ``users`` object.

.. note:: 

    Creating users in bulk is not supported at this time.