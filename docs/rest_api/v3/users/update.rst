Update Users
------------

.. attention::

    Only API users with an Organization role of Organization Administrator can update users. However, they may not update users whose System role is **Administrator** or **Operations Administrator**.

The following example illustrates the basic format for updating a user:

.. code::

    PUT /v3/security/users/{userId}
    Content-Type: application/json

    {
        {updatedField}: {updatedValue}
    }


For example, the following request will disable and lock the account for the user whose ID is 11:

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

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request to the ``/v3/security/users`` endpoint.

.. note:: 

    Updating users in bulk is not supported at this time.