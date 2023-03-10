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
- Apply a **Targeted Attack** Tag to the Victim
- Configure the Victim's nationality, organization, suborganization, and work location

.. hint::
    To include the ``assets``, ``associatedGroups``, ``attributes``, and ``tags`` fields in the API response, append ``?fields=assets&fields=associatedGroups&fields=attributes&fields=tags`` to the end of the request URL.

.. code::

    POST /v3/victims
    {
        "name": "John Doe",
        "assets": {"data": [{"address": "jdoe@companyabc.com", "addressType": "Corporate email", "type": "EmailAddress"}]},
        "associatedGroups": {"data": [{"id": 12345}, {"name": "Bad Adversary", "type": "Adversary"}]},
        "attributes": {"data": [{"type": "Additional Analysis and Context", "value": "Example value", "source": "Example Source"}]},
        "nationality": "American",
        "org": "Company ABC",
        "suborg": "HR Department",
        "tags": {"data": [{"name": "Targeted Attack"}]},
        "workLocation": "Washington, D.C."
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 2,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=2",
            "name": "John Doe",
            "org": "Company ABC",
            "suborg": "HR Department",
            "workLocation": "Washington, D.C.",
            "nationality": "American"
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request to the ``/v3/victims`` endpoint.

.. note::
    You can add multiple `Attributes <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_attributes/victim_attributes.html>`_, `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_, and `Security Labels <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_ to the Victim being created in a single POST request.

Create Associations
^^^^^^^^^^^^^^^^^^^

You can create associations between Victims and Groups that exist in the same owner only. When creating associations for Victims using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Group, include `all fields required to create the type of Group <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html#available-fields>`_ when setting the ``associatedGroups`` field. To create the Group in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Group when setting the ``associatedGroups`` field.
- To create an association to an existing Group, use the Group's ID when setting the ``associatedGroups`` field (e.g., ``"associatedGroups": {"data": [{"id": 12345}]}``).

.. note::
    You can associate multiple Groups to a Victim in a single POST or PUT request.