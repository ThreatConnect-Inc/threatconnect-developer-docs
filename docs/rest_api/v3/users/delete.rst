Delete Users
------------

.. attention::

    Only API users with an Organization role of Organization Administrator can delete users. However, they may not delete users whose System role is **Administrator** or **Operations Administrator**.

Send a request in the following format to delete a user:

.. code::

    DELETE /v3/security/users/{userId}

For example, the following request will delete the user whose ID is 10:

.. code::

    DELETE /v3/security/users/10

JSON Response

.. code:: json

    {
        "message": "Deleted",
        "status": "Success"
    }

.. note:: 

    Deleting users in bulk is not supported at this time.