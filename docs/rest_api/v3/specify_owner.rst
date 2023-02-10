Specify an Owner
----------------

Overview
^^^^^^^^

You can use the ``owner`` query parameter to specify the `owner <https://docs.threatconnect.com/en/latest/rest_api/v3/owners/owners.html>`_ (i.e., Organization, Community, or Source) of the object being created, retrieved, updated, or deleted in a POST, GET, PUT, or DELETE request, respectively. To specify the owner of an object in a request, append ``?owner=`` followed by the owner's name to the API request's URL.

.. note::
    Based on the type of action you want to perform (create, retrieve, update, or delete), your API user account will need appropriate permissions in the owner specified in the ``owner`` query parameter. See the `ThreatConnect Owner Roles and Permissions <https://knowledge.threatconnect.com/docs/threatconnect-owner-roles-and-permissions>`_ knowledge base category for more information about each owner role and their corresponding permissions in ThreatConnect.

Example Request
^^^^^^^^^^^^^^^

The following request will create a new Adversary Group in the owner named **Demo Community**. Note that the request's URL is encoded.

.. code::

    POST /v3/groups?owner=Demo%20Community
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
            "securityLabels": {},
            "ownerId": 3,
            "ownerName": "Demo Community",
            "webLink": "https://app.threatconnect.com/#/details/groups/35/overview",
            "tags": {},
            "type": "Adversary",
            "name": "Bad Guy",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555"
            },
            "upVoteCount": "0",
            "downVoteCount": "0",
            "associatedGroups": {},
            "associatedIndicators": {},
            "attributes": {},
            "lastModified": "2023-02-10T15:44:48Z",
            "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=35"
        },
        "message": "Created",
        "status": "Success"
    }

.. note::
    Depending on the tool you're using to interact with the ThreatConnect API, it may be necessary to encode the URL in your request manually if it includes query parameters. For example, some tools may accept ``/v3/groups?owner=Demo Community`` as a valid request URL and encode it automatically, while others may require you to encode the request's URL manually. If you submit a request with query parameters and a 401 Unauthorized error is returned, verify whether the URL in your request is encoded properly for the API tool you are using.