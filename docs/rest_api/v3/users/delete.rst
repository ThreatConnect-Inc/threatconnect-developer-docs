Delete Users
------------

.. attention::

    Only API users with an Organization role of Organization Administrator can delete users.

The basic format to delete a user is:

.. code::

    DELETE /v3/security/users/{userId}

For example, the following query will delete the user with ID 10:

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