Create Cases
------------

The following example illustrates the basic format for creating a Case:

.. code::

    POST /v3/cases
    Content-Type: application/json

    {
        "name": "Case name",
        "status": "Case status",
        "severity": "Case severity"
    }

For example, the following request will create a Case named "Phishing Investigation." It will also complete the following actions for the Case:

- Set the Case's severity to **Low**
- Set the Case's status to **Open**
- Assign the Case to smithj@threatconnect.com
- Create an Artifact within the Case and associate the Artifact to the existing Indicator whose ID is 2
- Apply the **T1566 - Phishing** ATT&CK® Tag to the Case

.. attention::
    To apply an ATT&CK Tag to a Case, use either the corresponding technique ID or name. For example, to apply the **T1566 - Phishing** ATT&CK Tag to a Case, either set ``name`` to ``"Phishing"`` or ``techniqueId`` to ``"T1566"`` when defining the ATT&CK Tag object in the request body.

    Also, if you applied a new Tag to a Case and that Tag matches a synonymous Tag listed in a `Tag normalization rule <https://knowledge.threatconnect.com/docs/tag-normalization>`_, it will be converted to the main Tag listed in the rule. Similarly, if you applied a new Tag to a Case and that Tag `matches an ATT&CK Tag <https://knowledge.threatconnect.com/docs/attack-tags#converting-standard-tags-to-attck-tags>`_, it will be converted to that ATT&CK Tag.

.. hint::
    To include the ``artifacts`` and ``tags`` fields in the API response, append ``?fields=artifacts&fields=tags`` to the end of the request URL.

.. code::

    POST /v3/cases
    Content-Type: application/json
    
    {
        "artifacts": {
            "data": [
                {
                    "summary": "badguy.com",
                    "type": "Host",
                    "associatedIndicators": {
                        "data": [
                            {
                                "id": "2"
                            }
                        ]
                    }
                }
            ]
        },
        "assignee": {
            "type": "User",
            "data": {
                "userName": "smithj@threatconnect.com"
            }
        },
        "name": "Phishing Investigation",
        "severity": "Low",
        "status": "Open",
        "tags": {
            "data": [
                {
                    "techniqueId": "T1566"
                }
            ]
        }
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 1,
            "xid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
            "name": "Phishing Investigation",
            "dateAdded": "2023-03-09T14:41:27Z",
            "lastUpdated": "2023-03-09T14:41:27Z",
            "caseOpenTime": "2023-03-09T14:41:27.27Z",
            "caseOpenUser": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "detectionOverdue": false,
            "responseOverdue": false,
            "status": "Open",
            "severity": "Low",
            "resolution": "Not Specified",
            "assignee": {
                "type": "User",
                "data": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "JMS",
                    "owner": "Demo Organization"
                }
            },
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "owner": "Demo Organization",
            "ownerId": 1
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request to the ``/v3/cases`` endpoint.