Specify an Owner
----------------

Overview
^^^^^^^^

You can use the ``owner`` query parameter to specify the `owner <https://docs.threatconnect.com/en/latest/rest_api/v3/owners/owners.html>`_ (i.e., Organization, Community, or Source) of the object being created, retrieved, updated, or deleted in a POST, GET, PUT, or DELETE request, respectively.

To use the ``owner`` query parameter, append ``?owner={ownerName}`` to the end of the request URL.

.. attention::
    Based on the type of action you want to perform (create, retrieve, update, or delete), your API user account will need appropriate permissions in the owner specified in the ``owner`` query parameter. See `ThreatConnect Owner Roles and Permissions <https://knowledge.threatconnect.com/docs/threatconnect-owner-roles-and-permissions>`_ on the ThreatConnect knowledge base for more information about each owner role and their corresponding permissions.

Example Requests
^^^^^^^^^^^^^^^^

Create an Object in a Community or Source
=========================================

The following request will create a new Adversary Group in the owner named **Demo Community**. Note that the request URL is encoded.

.. code::

    POST /v3/groups?owner=Demo%20Community
    Content-Type: application/json
    
    {
        "type": "Adversary",
        "name": "Bad Guy"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 35,
            "dateAdded": "2023-02-10T15:44:48Z",
            "ownerId": 3,
            "ownerName": "Demo Community",
            "webLink": "https://app.threatconnect.com/#/details/groups/35/overview",
            "type": "Adversary",
            "name": "Bad Guy",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555"
            },
            "upVoteCount": "0",
            "downVoteCount": "0",
            "lastModified": "2023-02-10T15:44:48Z",
            "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=35"
        },
        "message": "Created",
        "status": "Success"
    }

Retrieve Data for Objects in a Community or Source
==================================================

The following request will retrieve data for all Groups in the owner named Demo Community only. Note that the request URL is encoded.

.. code::

    GET /v3/groups?owner=Demo%20Community

.. note::
    Depending on the tool you are using to interact with the ThreatConnect API, it may be necessary to encode the request URL manually if it includes query parameters. For example, some tools may accept ``/v3/groups?owner=Demo Community`` as a valid request URL and encode it automatically, while others may require you to encode the request URL manually. If you submit a request with query parameters and a **401 Unauthorized** error is returned, verify whether the request URL is encoded properly for the API tool you are using.