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
- Add a Description (i.e., a default Description Attribute) to the Victim
- Apply the **Targeted Attack** standard Tag and the **T1566 - Phishing** ATT&CK® Tag to the Victim
- Configure the Victim's nationality, organization, suborganization, and work location

.. attention::
    When applying ATT&CK Tags to a Victim, do not include the corresponding technique/sub-technique ID in the Tag's name. For example, to apply the **T1566 - Phishing** ATT&CK Tag to a Victim, use **Phishing** as the Tag name.

    Also, if you applied a new Tag to a Victim and that Tag matches a synonymous Tag listed in a `Tag normalization rule <https://knowledge.threatconnect.com/docs/tag-normalization>`_, it will be converted to the main Tag listed in the rule. Similarly, if you applied a new Tag to a Victim and that Tag `matches an ATT&CK Tag <https://knowledge.threatconnect.com/docs/attack-tags#converting-standard-tags-to-attck-tags>`_, it will be converted to that ATT&CK Tag.

.. hint::
    To include the ``assets``, ``associatedGroups``, ``attributes``, and ``tags`` fields in the API response, append ``?fields=assets&fields=associatedGroups&fields=attributes&fields=tags`` to the end of the request URL.

.. code::

    POST /v3/victims
    {
        "name": "John Doe",
        "assets": {
            "data": [
                {
                    "address": "jdoe@companyabc.com",
                    "addressType": "Corporate email",
                    "type": "EmailAddress"
                }
            ]
        },
        "associatedGroups": {
            "data": [
                {
                    "id": 12345
                },
                {
                    "name": "Bad Adversary",
                    "type": "Adversary"
                }
            ]
        },
        "attributes": {
            "data": [
                {
                    "type": "Description",
                    "value": "John Doe works in the Company ABC's HR Department.",
                    "default": true
                }
            ]
        },
        "nationality": "American",
        "org": "Company ABC",
        "suborg": "HR Department",
        "tags": {
            "data": [
                {
                    "name": "Targeted Attack"
                },
                {
                    "name": "Phishing"
                }
            ]
        },
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
    By default, Victims will be created in the Organization in which your API user account resides. To create a Victim in a Community or Source, use the ``owner`` query parameter to `specify the owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_ in which to create the Victim.

.. note::
    You can add multiple `Attributes <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_attributes/victim_attributes.html>`_, `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_, and `Security Labels <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_ to the Victim being created in a single POST request.