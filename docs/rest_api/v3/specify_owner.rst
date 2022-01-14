Specify an Owner
----------------

The ``?owner=`` query parameter allows you to specify the owner (i.e., Organization, Community, or Source) of the data being requested, sent, or deleted in a GET, POST/PUT, or DELETE request, respectively.

For example, the following query will create a new Tag with ``Demo Community`` as the owner:

.. code::

    POST /v3/tags?owner=Demo Community
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

.. note::
    Depending on the tool you're using to interact with the ThreatConnect API, it may be necessary to encode the URL in your request when including query parameters. For example, some tools may accept ``?owner=Demo Community`` as a valid URL, while others require the URL be encoded (e.g., ``?owner=Demo%20Community``). If you submit a request with query parameters and a ``401 Unauthorized`` error is returned, verify whether the URL in your request is encoded properly for your preferred API tool.