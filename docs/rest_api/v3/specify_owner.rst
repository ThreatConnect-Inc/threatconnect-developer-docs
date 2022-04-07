Specify an Owner
----------------

The ``?owner=`` query parameter allows you to specify the owner (i.e., Organization, Community, or Source) of the data being requested, sent, or deleted in a GET, POST/PUT, or DELETE request, respectively.

For example, the following query will create a new Tag with ``Demo Community`` as the owner:

.. code::

    POST /v3/groups?owner=Demo Community
    {
        "type": "Incident",
        "name": "Dangerous Incident",
        "eventDate": "2022-04-07",
        "status": "New"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 35,
            "ownerName": "Demo Community",
            "dateAdded": "2022-04-07T14:55:23Z",
            "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=35",
            "tags": {},
            "securityLabels": {},
            "type": "Incident",
            "name": "Dangerous Incident",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "role": "Api User"
            },
            },
            "associatedGroups": {},
            "associatedIndicators": {},
            "associatedCases": {},
            "associatedArtifacts": {},
            "attributes": {},
            "status": "New",
            "eventDate": "2022-04-07T00:00:00Z",
            "lastModified": "2022-04-07T14:55:23Z"
        },
        "message": "Created",
        "status": "Success"
    }

.. note::
    Based on the type of action you want to perform (retrieve, create, update, or delete), you will need appropriate permissions in the specified owner. See the `ThreatConnect Owner Roles and Permissions <https://training.threatconnect.com/learn/article/threatconnect-owner-roles-and-permissions-kb-article>`_ knowledge base article for more information about each owner role and their corresponding permissions in ThreatConnect.

.. note::
    Depending on the tool you're using to interact with the ThreatConnect API, it may be necessary to manually encode the URL in your request when including query parameters. For example, some tools may accept ``?owner=Demo Community`` as a valid URL and automatically encode it, while others may require you to manually encode the URL (e.g., ``?owner=Demo%20Community``). If you submit a request with query parameters and a ``401 Unauthorized`` error is returned, verify whether the URL in your request is encoded properly for your preferred API tool.