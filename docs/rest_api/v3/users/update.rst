Update Users
------------

.. attention::

    Only API users with an Organization role of Organization Administrator can update users in their Organization. However, they may not update users whose System role is **Administrator**, **Community Leader**, **Operations Administrator**, or **Super User**.

The following example illustrates the basic format for updating a user in your Organization:

.. code::

    PUT /v3/security/users/{userId}
    Content-Type: application/json

    {
        {updatedField}: {updatedValue}
    }


For example, the following request will disable and lock the account for the user in your Organization whose ID is 11:

.. code::

    PUT /v3/security/users/11
    Content-Type: application/json
    
    {
        "disabled": true,
        "locked": true
    }


JSON Response

.. code:: json

    {
        "data": {
            "id": 11,
            "userName": "jeffersond@companyabc.com",
            "firstName": "Donald",
            "lastName": "Jefferson",
            "pseudonym": "DonJ",
            "owner": "Demo Organization",
            "lastPasswordChange": "2022-08-30T12:45:17Z",
            "uiTheme": "Light",
            "jobFunction": "Threat Intelligence",
            "jobRole": "Analyst",
            "termsAccepted": true,
            "logoutIntervalMinutes": 30,
            "systemRole": "User",
            "ownerRoles": {
                "Demo Organization": "Standard User",
                "Demo Community": "Director",
                "Demo Source": "Director"
            },
            "disabled": true,
            "locked": true,
            "passwordResetRequired": false,
            "twoFactorResetRequired": false
        },
        "message": "Updated",
        "status": "Success"
    }

In the next example, the request will update the Organization role for the user in your Organization whose ID is 12:

.. code::

    PUT /v3/security/users/12
    Content-Type: application/json

    {
        "owner": "Demo Organization",
        "ownerRoles": {
            "Demo Organization": "Organization Administrator"
        }
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
            "lastPasswordChange": "2024-07-09T14:35:05Z",
            "uiTheme": "Light",
            "termsAccepted": false,
            "logoutIntervalMinutes": 30,
            "systemRole": "User",
            "ownerRoles": {
                "Demo Organization": "Organization Administrator",
                "Demo Community": "Editor",
                "Demo Source": "Editor"
            },
            "disabled": false,
            "locked": false,
            "passwordResetRequired": true,
            "twoFactorResetRequired": true
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request to the ``/v3/security/users`` endpoint.

.. note:: 

    Updating users in bulk is not supported at this time.