Create Victims
--------------

The basic format for creating a Victim is:

.. code::

    POST /v3/victims/
    {
        "name": "Victim name goes here",
        "type": "Victim"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can included in the body of a POST request for the ``victims`` object.

.. note::
    You can add multiple Attributes, Tags, and Security Labels to the Victim being created in a single POST request. Similarly, you can associate multiple Groups to the Victim being created in a single POST request.

Example POST Request
^^^^^^^^^^^^^^^^^^^^

The following query will create a Victim. Note that all optional fields available for the ``victims`` object are included in this request.

.. code::

    POST /v3/victims/
    {
        "name": "John Doe",
        "assets": {"data": [{"address": "jdoe@companyabc.com", "addressType": "Corporate email", "type": "EmailAddress"}]},
        "associatedGroups": {"data": [{"id": 12345}], [{"name": "Bad Adversary", "type": "Adversary"},
        "attributes": {"data": [{"type": "Additional Analysis and Context", "value": "Example value", "source": "Example Source"}]},
        "description": "This victim’s bank account was hacked.",
        "nationality": "American",
        "org": "Company ABC",
        "securityLabels": {"data": [{"name": "TLP:AMBER"}]},
        "suborg": "HR Department",
        "tags": {"data": [{"name": "Targeted Attack"}]},
        "workLocation": "Washington, D.C."
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
                    "id": 3,
                    "name": "TLP:AMBER",
                    "description": "This security label is used for information that requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved.",
                    "color": "FFC000",
                    "owner": "System",
                    "dateAdded": "2016-08-31T00:00:00Z"
                }],
                "count": 1
            },
            "name": "John Doe",
            "description": "This victim’s bank account was hacked.",
            "org": "Company ABC",
            "suborg": "HR Department",
            "workLocation": "Washington, D.C.",
            "nationality": "American",
            "assets": {
                "data": [{
                    "id": 2,
                    "type": "EmailAddress",
                    "victimId": 2,
                    "address": "jdoe@companyabc.com",
                    "addressType": "Corporate email"
                }],
                "count": 1
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
        "message": "Created",
        "status": "Success"
    }

.. note::
    When creating a Victim, you can apply Tags that do not yet exist in ThreatConnect to it. In this scenario, you would need to fill out `all required fields for each new Tag <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_. Upon creation of the new Victim, any Tags included in the body of the POST request that do not yet exist in ThreatConnect will also be created.

    Similarly, you can associate Groups that do not yet exist in ThreatConnect to the Victim. In this scenario, you would need to fill out `all required fields for the type of Group <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_ being associated to the Victim. Upon creation of the new Victim, any associated Groups included in the body of the POST request that do not yet exist in ThreatConnect will also be created.
