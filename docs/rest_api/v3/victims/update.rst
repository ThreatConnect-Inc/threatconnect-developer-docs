Update Victims
--------------

The basic format for updating a Victim is:

.. code::

    PUT /v3/victims/{victimId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following query will complete the following actions for a Victim with ID 2:

- Add a ``WebSite`` Victim Asset to the Victim;
- Update the Victim's name;
- Replace the ``TLP: AMBER`` Security Label applied to the Victim with a ``TLP: RED`` Security Label.

.. code::

    PUT /v3/victims/2
    {
        "assets": {"data": [{"website": "evilll.com", "type": "WebSite"}]},
        "name": "Jane Doe",
        "securityLabels": {"data": [{"name": "TLP:RED"}], "mode": "replace"}
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 2,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2",
            "tags": {
                "data": [{
                    "id": 11,
                    "name": "Targeted Attack",
                    "lastUsed": "2021-11-05T19:16:52Z"
                }]
            },
            "securityLabels": {
                "data": [{
                    "id": 4,
                    "name": "TLP:RED",
                    "description": "This security label is used for information that cannot be effectively acted upon by additional parties, and could lead to impacts on a party"s privacy, reputation, or operations if misused.",
                    "color": "FF0033",
                    "owner": "System",
                    "dateAdded": "2016-08-31T00:00:00Z"
                }]
            },
            "name": "Jane Doe",
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
                }]
            },
            "attributes": {
                "data": [{
                    "id": 1,
                    "type": "Additional Analysis and Context",
                    "value": "Example value",
                    "source": "Example Source",
                    "createdBy": {
                        "id": 3,
                        "userName": "11112222333344445555",
                        "firstName": "John",
                        "lastName": "Smith",
                        "pseudonym": "jsmithAPI",
                        "role": "Api User"
                    },
                    "dateAdded": "2021-11-05T19:16:52Z",
                    "lastModified": "2021-11-05T19:16:52Z",
                    "default": false
                }]
            }
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request for the ``victims`` object.

.. hint::
    When updating a Victim, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedGroups``
    - ``attributes``
    - ``securityLabels``
    - ``tags``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.