Update Victims
--------------

The basic format for updating a Victim is:

.. code::

    PUT /v3/victims/{victimId}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can included in the body of a PUT request for the ``victims`` object.

.. note::
    When updating a Victim, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedGroups``
    - ``attributes``
    - ``securityLabels``
    - ``tags``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update-metadata.html>`_ for instructions on using the ``mode`` field.

Example PUT Request
^^^^^^^^^^^^^^^^^^^^

The following query will complete the following actions for a Victim with ID 2:

- Add a ``WebSite`` Victim Asset to the Victim
- Update the Victim’s description
- Replace the ``TLP: AMBER`` Security Label applied to the Victim with a ``TLP: RED`` Security Label.

.. code::

    PUT /v3/victims/2
    {
        "assets": {"data": [{"website": "evilll.com", "type": "WebSite"}]},
        "description": "This individual was the victim of a company-wide phishing attack.",
        "securityLabels": {"data": [{"name": "TLP:RED"}], "mode": "replace"}
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 2,
            "type": "Victim",
            "ownerName": "Demo Organization",
            "webLink": "/auth/victim/victim.xhtml?victim=2",
            "tags": {
                "data": [{
                    "id": 11,
                    "name": "Targeted Attack",
                    "lastUsed": "2021-11-05T19:16:52Z"
                }],
                "count": 1
            },
            "securityLabels": {
                "data": [{
                    "id": 4,
                    "name": "TLP:RED",
                    "description": "This security label is used for information that cannot be effectively acted upon by additional parties, and could lead to impacts on a party"s privacy, reputation, or operations if misused.",
                    "color": "FF0033",
                    "owner": "System",
                    "dateAdded": "2016-08-31T00:00:00Z"
                }],
                "count": 1
            },
            "name": "John Doe",
            "description": "This individual was the victim of a company-wide phishing attack.",
            "org": "Company ABC",
            "suborg": "HR Department",
            "workLocation": "Washington, D.C.",
            "nationality": "American",
            "assets": {
                "data": [{
                    "id": 3,
                    "type": "WebSite",
                    "victimId": 2,
                    "website": "evilll.com"
                }, {
                    "id": 2,
                    "type": "EmailAddress",
                    "victimId": 2,
                    "address": "jdoe@companyabc.com"
                }],
                "count": 2
            },
            "attributes": {
                "data": [{
                    "id": 1,
                    "type": "Additional Analysis and Context",
                    "value": "Example value",
                    "source": "Example Source",
                    "createdBy": {
                        "id": 39,
                        "userName": "62693284927610908885",
                        "firstName": "API",
                        "lastName": "User",
                        "pseudonym": "APIUserNFmof",
                        "role": "Api User"
                    },
                    "dateAdded": "2021-11-05T19:16:52Z",
                    "lastModified": "2021-11-05T19:16:52Z",
                    "default": false
                }],
                "count": 1
            }
        },
        "message": "Updated",
        "status": "Success"
    }