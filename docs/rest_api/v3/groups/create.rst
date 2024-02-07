Create Groups
-------------

The following example illustrates the basic format for creating a Group:

.. code::

    POST /v3/groups
    {
        "name": "Group name goes here",
        "type": "Group type goes here"
        //required fields for the selected Group type go here, if applicable
    }

Refer to the `Available Fields <#available-fields>`_ and `Group-Specific Fields <#group-specific-fields>`_ sections for a list of available fields that can be included in the body of a POST request to the ``/v3/groups`` endpoint.

.. note::
    You can add multiple `Attributes <https://docs.threatconnect.com/en/latest/rest_api/v3/group_attributes/group_attributes.html>`_, `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_, and `Security Labels <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_ to a Group in a single POST or PUT request.

Example POST Request
^^^^^^^^^^^^^^^^^^^^^

The following request will create an Incident Group for an Incident that took place on Nov. 3, 2021. The Incident will be assigned a status of **New**, two Tags will be applied to it: the **Targeted Attack** standard Tag and the **T1566 - Phishing** ATT&CK® Tag.

.. attention::
    When applying ATT&CK Tags to a Group, do not include the corresponding technique/sub-technique ID in the Tag's name. For example, to apply the **T1566 - Phishing** ATT&CK Tag to a Group, use **Phishing** as the Tag name.

    Also, if you applied a new Tag to a Group and that Tag matches a synonymous Tag listed in a `Tag normalization rule <https://knowledge.threatconnect.com/docs/tag-normalization>`_, it will be converted to the main Tag listed in the rule. Similarly, if you applied a new Tag to a Group and that Tag `matches an ATT&CK Tag <https://knowledge.threatconnect.com/docs/attack-tags#converting-standard-tags-to-attck-tags>`_, it will be converted to that ATT&CK Tag.

.. hint::
    To include the ``tags`` field in the API response, append ``?fields=tags`` to the end of the request URL.

.. code::

    POST /v3/groups
    {
        "type": "Incident",
        "name": "Bad Incident",
        "eventDate": "2021-11-03",
        "status": "New",
        "tags": {
            "data": [
                {
                    "name": "Targeted Attack"
                },
                {
                    "name": "Phishing"
                }
            ]
        }
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-03T14:57:45Z",
            "webLink": "https://app.threatconnect.com/#/details/groups/3/overview",
            "type": "Incident",
            "name": "Bad Incident",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "upVoteCount":"0",
            "downVoteCount":"0",
            "status": "New",
            "eventDate": "2021-11-03T00:00:00Z",
            "lastModified": "2021-11-03T14:57:4511:04:12Z",
            "legacyLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=3"
        },
        "message": "Created",
        "status": "Success"
    }