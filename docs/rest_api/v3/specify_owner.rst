Specify an Owner
----------------

The ``?owner=`` query parameter allows you to specify the owner (i.e., Organization, Community, or Source) of the data being requested, sent, or deleted in a GET, POST/PUT, or DELETE request, respectively.

For example, the following query will create a new Tag with ``Demo Community`` as the owner:

.. code::

    POST /v3/tags?owner=Demo%20Community
    {
        "name": "Nation State"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 32,
            "name": "Nation State",
            "owner": "Demo Community",
            "lastUsed": "2021-11-22T20:27:51Z"
        },
        "message": "Created",
        "status": "Success"
    }

.. note::
    Based on the type of action you want to perform (retrieve, create, update, or delete), you will need appropriate permissions in the specified owner. See the `ThreatConnect Owner Roles and Permissions <https://training.threatconnect.com/learn/article/threatconnect-owner-roles-and-permissions-kb-article>`_ knowledge base article for more information about each owner role and their corresponding permissions in ThreatConnect.
