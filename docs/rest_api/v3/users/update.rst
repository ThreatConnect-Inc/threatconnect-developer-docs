Update Users
------------

.. attention::

    Only API users with an Organization role of Organization Administrator can update users.

The basic format for updating a user is:

.. code::

    PUT /v3/security/users/{userId}
    {
        {updatedField}: {updatedValue}
    }


For example, the following query will disable and lock the account for the user with ID 11:

.. code::

    PUT /v3/security/users/11
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
            "owner": "Demo Organization",
            "lastPasswordChange": "2022-08-30T12:45:17Z",
            "uiTheme": "Light",
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

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request for the ``users`` object.

.. note:: 

    Updating users in bulk is not supported at this time.