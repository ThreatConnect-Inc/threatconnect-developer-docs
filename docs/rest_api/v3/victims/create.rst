Create Victims
--------------

The following example illustrates the basic format for creating a Victim:

.. code::

    POST /v3/victims
    {
        "name": "John Doe"
    }

For example, the following request will create a Victim named John Doe. It will also perform the following actions for the Victim:

- Create a new Email Address Victim Asset and add it to the Victim
- Associate an existing Group to the Victim, and create a new **Bad Guy** Adversary Group and associate it to the Victim
- Add an **Additional Analysis and Context** Attribute to the Victim
- Apply the **TLP:AMBER** Security Label to the Victim
- Apply a **Targeted Attack** Tag to the Victim
- Configure the Victim's nationality, organization, suborganization, and work location


.. code::

    POST /v3/victims
    {
        "name": "John Doe",
        "assets": {"data": [{"address": "jdoe@companyabc.com", "addressType": "Corporate email", "type": "EmailAddress"}]},
        "associatedGroups": {"data": [{"id": 12345}, {"name": "Bad Adversary", "type": "Adversary"}]},
        "attributes": {"data": [{"type": "Additional Analysis and Context", "value": "Example value", "source": "Example Source"}]},
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
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2",
            "tags": {
                "data": [
                    {
                        "id": 11,
                        "name": "Targeted Attack",
                        "lastUsed": "2021-11-05T19:16:52Z"
                    }
                ]
            },
            "securityLabels": {
                "data": [
                    {
                        "id": 3,
                        "name": "TLP:AMBER",
                        "description": "This security label is used for information that requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved. Information with this label can be shared with members of an organization and its clients.
                        "color": "FFC000",
                        "owner": "System",
                        "dateAdded": "2016-08-31T00:00:00Z"
                    }
                ]
            },
            "name": "John Doe",
            "org": "Company ABC",
            "suborg": "HR Department",
            "workLocation": "Washington, D.C.",
            "nationality": "American",
            "assets": {
                "data": [
                    {
                        "id": 5,
                        "type": "EmailAddress",
                        "victimId": 2,
                        "address": "jdoe@companyabc.com",
                        "addressType": "Corporate email",
                        "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2"
                    }
                ]
            },
            "attributes": {
                "data": [
                    {
                        "id": 1,
                        "dateAdded": "2021-11-05T19:16:52Z",
                        "type": "Additional Analysis and Context",
                        "value": "Example value",
                        "source": "Example Source",
                        "createdBy": {
                            "id": 3,
                            "userName": "11112222333344445555"
                        },
                        "lastModified": "2021-11-05T19:16:52Z",
                        "pinned": false
                        "default": false
                    }
                ]
            }
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request for the ``victims`` object.

.. hint::
    You can add multiple `Attributes <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_attributes/victim_attributes.html>`_, `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_, and `Security Labels <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_ to the Victim being created in a single POST request.

Create Associations
^^^^^^^^^^^^^^^^^^^

You can create associations between Victims and Groups that exist in the same owner only. When creating associations for Victims using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Group, include all fields required to create the type of Group when setting the ``associatedGroups`` field. To create the Group in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Group when setting the ``associatedGroups`` field.
- To create an association to an existing Group, use the Group's ID when setting the ``associatedGroups`` field (e.g., ``"associatedGroups": {"data": [{"id": 12345}]}``).

.. hint::
    You can associate multiple Groups to a Victim in a single POST or PUT request.