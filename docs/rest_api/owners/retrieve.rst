Retrieve Owners
---------------

Retrieving Multiple Owners
^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a list of all available Owners, use the following query:

.. code::

    GET /v2/owners

JSON Response:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 2,
        "owner": [
          {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          {
            "id": 2,
            "name": "Common Community",
            "type": "Community"
          }
        ]
      }
    }

Retrieving a Single Owner
^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve information about a specific Owner, you can add the ID to the end of the query as shown below:

.. code::

    GET /v2/owners/{ownerId}

Here is an example query:

.. code::

    GET /v2/owners/2

JSON Response:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "owner": {
          "id": 2,
          "name": "Common Community",
          "type": "Community"
        }
      }
    }

Retrieving Information About Your Organization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve information about your Organization, use the query below:

.. code::

    GET /v2/owners/mine

JSON Response:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "owner": {
          "id": 1,
          "name": "Example Organization",
          "type": "Organization"
        }
      }
    }

To view all members of your Organization, you can use:

.. code::

    GET /v2/owners/mine/members


JSON Response if Organization allows anonymous membership:

.. code-block:: json

    {
      "anonymous": true,
      "status": "Success",
      "resultCount": 2,
      "members": [
        {
          "pseudonym": "test"
        }, {
          "pseudonym": "test2"
        }
      ]
    }

JSON Response if Organization does not allow anonymous membership:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "user": [
          {
            "userName": "12345678901234567890",
            "firstName": "Jane",
            "lastName": "Doe"
          },
          {
            "userName": "12345678901234567891",
            "firstName": "John",
            "lastName": "Doe"
          }
        ]
      }
    }

Retrieving Information About Your Current User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To find information about your current user, you can use the following query:

.. code::

    GET /v2/whoami

JSON Response:

.. code-block:: json

    {
      "status": "Success",
      "data": {
        "user": {
          "userName": "12345678901234567890",
          "firstName": "John",
          "lastName": "Doe",
          "pseudonym": "Buck",
          "role": "Api User"
        }
      }
    }
