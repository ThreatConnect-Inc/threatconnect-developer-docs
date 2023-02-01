Create Indicators
-----------------

The follow example illustrates the basic format for creating an Indicator:

.. code::

    POST /v3/indicators
    {
        "type": "Indicator type goes here",
        //required fields for the selected Indicator type
    }

Refer to the `Available Fields <#available-fields>`_ and `Indicator-Specific Fields <#indicator-specific-fields>`_ sections for a list of available fields that can be included in the body of a POST request for the ``indicators`` object.

.. hint::
    You can add multiple `Attributes <https://docs.threatconnect.com/en/latest/rest_api/v3/group_attributes/indicator_attributes.html>`_, `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_, and `Security Labels <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_ to an Indicator in a single POST or PUT request.

Example POST Request
^^^^^^^^^^^^^^^^^^^^

The following request will create an **ultrabadguy.com** Host Indicator. It will also complete the following actions for the Indicator:

- Activate the **DNS** and **Whois** features for the Indicator
- Set the Indicator Status for the Indicator to active
- Associate the existing Group whose ID is 12 to the Indicator, and create a new **Bad Guy** Adversary Group in a Source and associate it to the Indicator
- Add an **Additional Analysis and Context** Attribute to the Indicator
- Set the Indicator's Threat and Confidence Ratings
- Apply the **TLP:AMBER** Security Label to the Indicator
- Apply **Targeted Attack** and **Malicious Host** Tags to the Indicator

.. code::

    POST /v3/indicators
    {
        "type": "Host",
        "hostName": "ultrabadguy.com",
        "dnsActive": true,
        "whoisActive": true,
        "active": true,
        "associatedGroups": {"data": [{"id": 12}, {"name": "Bad Guy", "type": "Adversary", "ownerName": "Demo Source"}]},
        "attributes": {"data": [{"type": "Additional Analysis and Context", "value": "This host is very dangerous", "source": "Phase of Intrusion"}]},
        "confidence": 85,
        "rating": 5,
        "securityLabels": {"data": [{"name": "TLP:AMBER"}]},
        "tags": {"data": [{"name": "Targeted Attack"}, {"name": "Malicious Host"}]}
    }


JSON Response

.. code:: json

    {
        "data": {
            "id": 4,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-05T16:43:17Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/4/overview",
            "tags": {
                "data": [
                    {
                        "id": 10,
                        "name": "Malicious Host",
                        "description": "A tag that can be applied to malicious Host Indicators.",
                        "lastUsed": "2021-11-05T16:43:17Z"
                    },
                    {
                        "id": 11,
                        "name": "Targeted Attack",
                        "lastUsed": "2021-11-05T16:43:17Z"
                    }
                ]
            },
            "securityLabels": {
                "data": [
                    {
                        "id": 3,
                        "name": "TLP:AMBER",
                        "description": "This security label is used for information that requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved. Information with this label can be shared with members of an organization and its clients."
                        "color": "FFC000",
                        "owner": "System",
                        "dateAdded": "2016-08-31T00:00:00Z"
                    }
                ]
            },
            "type": "Host",
            "lastModified": "2021-11-05T16:43:17Z",
            "rating": 5.00,
            "confidence": 85,
            "summary": "ultrabadguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {
                "data": [
                    {
                        "id": 15,
                        "ownerId": 2,
                        "ownerName": "Demo Source",
                        "dateAdded": "2021-11-05T16:43:17Z",
                        "webLink": "https://app.threatconnect.com/#/details/groups/15/overview",
                        "type": "Adversary",
                        "name": "Bad Guy",
                        "createdBy": {
                            "id": 3,
                            "userName": "11112222333344445555"
                        },
                        "upVoteCount": "0",
                        "downVoteCount": "0",
                        "lastModified": "2021-11-05T16:43:17Z",
                        "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=15"
                    },
                    {
                        "id": 12,
                        "ownerId": 1,
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-08-27T12:16:56Z",
                        "webLink": "https://app.threatconnect.com/#/details/groups/12/overview",
                        "type": "Incident",
                        "name": "Dangerous Incident",
                        "createdBy": {
                            "id": 1,
                            "userName": "smithj@threatconnect.com"
                        },
                        "upVoteCount": "0",
                        "downVoteCount": "0",
                        "lastModified": "2021-11-05T16:43:17Z",
                        "legacyLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=12"
                    }
                ]
            },
            "associatedIndicators": {},
            "fileActions": {
                "count": 0
            },
            "attributes": {
                "data": [
                    {
                        "id": 24,
                        "dateAdded": "2021-11-05T16:43:17Z",
                        "type": "Additional Analysis and Context",
                        "value": "This host is very dangerous",
                        "source": "Phase of Intrusion",
                        "createdBy": {
                            "id": 3,
                            "userName": "11112222333344445555"
                        },
                        "lastModified": "2021-11-05T16:43:17Z",
                        "pinned": false,
                        "default": false
                    }
                ]
            },
            "associatedCases": {},
            "associatedArtifacts": {},
            "hostName": "ultrabadguy.com",
            "dnsActive": true,
            "whoisActive": true,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
        },
        "message": "Created",
        "status": "Success"
    }

Create Associations
^^^^^^^^^^^^^^^^^^^

You can create associations between Indicators and Artifacts, Cases, Groups, and Indicators that exist in the same owner. If cross-owner associations are enabled on your ThreatConnect instance, you can also create associations between Indicators and Groups and other Indicators that exist in any owner to which you have access.
When creating associations for Indicators using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Artifact, include `all fields required to create an Artifact <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html#available-fields>`_  when setting the ``associatedArtifacts`` field.
- To create an association to an existing Artifact, use the Artifact's ID when setting the ``associatedArtifacts`` field (e.g., ``"associatedArtifacts": {"data": [{"id": 12345}]}``).
- To create an association to a new Case, include `all fields required to create a Case <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html#available-fields>`_ when setting the ``associatedCases`` field.
- To create an association to an existing Case, use the Case's ID when setting the ``associatedCases`` field.
- To create an association to a new Group, include `all fields required to create the type of Group <#available-fields>`_ when setting the ``associatedGroups`` field. To create the Group in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Group when setting the ``associatedGroups`` field.
- To create an association to an existing Group, use the Group's ID when setting the ``associatedGroups`` field.
- If creating an Indicator-to-Indicator associations, see the `"Indicator-to-Indicator Associations" section <#indicator-to-indicator-associations>`_ for further instruction.

.. hint::

    You can associate multiple Artifacts, Cases, Groups, and Indicators to an Indicator in a single POST or PUT request.