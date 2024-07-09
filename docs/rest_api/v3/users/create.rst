Create Users
------------

.. attention::

    Only API users with an Organization role of Organization Administrator can create users. However, they may not create users whose System role is **Administrator** or **Operations Administrator**.

The following example illustrates the basic format for creating a user:

.. code::

    POST /v3/security/users
    Content-Type: application/json

    {
        "firstName": "John",
        "lastName": "Smith",
        "userName": "smithj@companyabc.com",
        "password": "Password1!",
        "owner": "Demo Organization",
        "ownerRoles": {
            "Demo Organization": "Standard User"
        },
        "systemRole": "User"
    }

For example, the following request will create a new user who will be required to reset their password and enroll in MFA after logging into ThreatConnect for the first time:

.. code::

    POST /v3/security/users
    Content-Type: application/json
    
    {
        "firstName": "Herschel",
        "lastName": "Hodges",
        "userName": "hodgesh@companyabc.com",
        "password": "Password1!",
        "owner": "Demo Organization",
        "ownerRoles": {
            "Demo Organization": "Standard User"
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

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request to the ``/v3/security/users`` endpoint.

.. note:: 

    Creating users in bulk is not supported at this time.