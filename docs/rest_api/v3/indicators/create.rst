Create Indicators
-----------------

The basic format for creating an Indicator is:

.. code::

    POST /v3/indicators
    {
        "type": "Indicator type goes here",
        //required fields for the selected Indicator type
    }

Refer to the `Available Fields <#available-fields>`_ and `Indicator-Specific Fields <#indicator-specific-fields>`_ sections for a list of available fields that can be included in the body of a POST request for the ``indicators`` object.

.. note::
    You can add multiple `Attributes <https://docs.threatconnect.com/en/latest/rest_api/v3/group_attributes/indicator_attributes.html>`_, `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_, and `Security Labels <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_ to an Indicator in a single POST or PUT request.

Example POST Request
^^^^^^^^^^^^^^^^^^^^

The following query will create a Host Indicator with a host name of ``ultrabadguy.com``. Note that all optional fields available for the ``indicators`` object are included in this request.

.. code::

    POST /v3/indicators
    {
        "type": "Host",
        "hostName": "ultrabadguy.com",
        "dnsActive": true,
        "whoisActive": true,
        "active": true,
        "activeLocked": false,
        "associatedGroups": {"data": [{"id": 12}, {"name": "Bad Guy", "type": "Adversary"}]},
        "attributes": {"data": [{"type": "Additional Analysis and Context", "value": "This host is very dangerous", "source": "Phase of Intrusion"}]},
        "confidence": 85,
        "privateFlag": false,
        "rating": 5,
        "securityLabels": {"data": [{"name": "TLP:AMBER"}]},
        "tags": {"data": [{"name": "Targeted Attack"}, {"name": "Malicious Host"}]}
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 4,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-05T16:43:17Z",
            "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com",
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
                "data": [{
                    "id": 3,
                    "name": "TLP:AMBER",
                    "description": "This security label is used for information that requires support to be effectively acted upon, yet carries risks to privacy, reputation, or operations if shared outside of the organizations involved.",
                    "color": "FFC000",
                    "owner": "System",
                    "dateAdded": "2016-08-31T00:00:00Z"
                }]
            },
            "type": "Host",
            "lastModified": "2021-11-05T16:43:17Z",
            "rating": 5.0,
            "confidence": 85,
            "summary": "ultrabadguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {
                "data": [
                    {
                        "id": 15,
                        "type": "Adversary",
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-11-05T16:43:17Z",
                        "webLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=15",
                        "name": "Bad Guy",
                        "createdBy": {
                            "id": 3,
                            "userName": "11112222333344445555",
                            "firstName": "John",
                            "lastName": "Smith",
                            "pseudonym": "jsmithAPI",
                            "owner": "Demo Organization",
                            "systemRole": "Api User"
                        }
                    },
                    {
                        "id": 12,
                        "type": "Incident",
                        "ownerName": "Demo Source",
                        "dateAdded": "2021-08-27T12:16:56Z",
                        "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=12",
                        "name": "Dangerous Incident",
                        "createdBy": {
                            "id": 1,
                            "userName": "smithj@threatconnect.com",
                            "firstName": "John",
                            "lastName": "Smith",
                            "pseudonym": "JMS",
                            "owner": "Demo Organization",
                            "systemRole": "Administrator"
                        }
                    }
                ]
            },
            "associatedIndicators": {
                "data": [{
                    "id": 4,
                    "type": "Host",
                    "ownerName": "Demo Organization",
                    "dateAdded": "2021-11-05T16:43:17Z",
                    "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com",
                    "lastModified": "2021-11-05T16:43:17Z",
                    "rating": 5.0,
                    "confidence": 85,
                    "source": "A Reliable Source",
                    "description": "Potentially malicious host related to malware dissemination.",
                    "summary": "ultrabadguy.com",
                    "privateFlag": false,
                    "active": true,
                    "activeLocked": false,
                    "hostName": "ultrabadguy.com",
                    "dnsActive": true,
                    "whoisActive": true
                }]
            },
            "fileActions": {
                "count": 0
            },
            "attributes": {
                "data": [{
                    "id": 24,
                    "type": "Additional Analysis and Context",
                    "value": "This host is very dangerous",
                    "source": "Phase of Intrusion",
                    "createdBy": {
                        "id": 3,
                        "userName": "11112222333344445555",
                        "firstName": "John",
                        "lastName": "Smith",
                        "pseudonym": "jsmithAPI",
                        "owner": "Demo Organization",
                        "systemRole": "Api User"
                    },
                    "dateAdded": "2021-11-05T16:43:17Z",
                    "lastModified": "2021-11-05T16:43:17Z",
                    "default": false
                }]
            },
            "associatedCases": {},
            "associatedArtifacts": {},
            "hostName": "ultrabadguy.com",
            "dnsActive": true,
            "whoisActive": true
        },
        "message": "Created",
        "status": "Success"
    }

Create Associations
^^^^^^^^^^^^^^^^^^^

In ThreatConnect, you can create associations between Indicators and Artifacts, Cases, Groups, and Indicators that exist in the same owner (e.g., you can only associate Artifacts, Cases, Groups, and Indicators in your Organization to an Indicator in your Organization). If cross-owner associations are enabled on your ThreatConnect instance, you can also create associations between Groups and Indicators in Communities and Sources to which you have access and Indicators in your Organization.

When creating associations for Indicators using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Artifact, include `all fields required to create an Artifact <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html#available-fields>`_when setting the ``associatedArtifacts`` field. The new Artifact will be created in the Organization to which your API user account belongs.
- To create an association to an existing Artifact, use the Artifact's ID when setting the ``associatedArtifacts`` field (e.g., ``"associatedArtifacts": {"data": [{"id": 12345}]}``).
- To create an association to a new Case, include `all fields required to create a Case <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html#available-fields>`_ when setting the ``associatedCases`` field. The new Case will be created in the Organization to which your API user account belongs.
- To create an association to an existing Case, use the Case's ID when setting the ``associatedCases`` field.
- To create an association to a new Group, include `all fields required to create the type of Group <#available-fields>`_ when setting the ``associatedGroups`` field. The new Group will be created in the Organization to which your API user account belongs.
- To create an association to an existing Group that belongs to an Organization, Community, or Source, use the Group's ID when setting the ``associatedGroups`` field.
- If creating an Indicator-to-Indicator associations, see the `"Indicator-to-Indicator Associations" section <#indicator-to-indicator-associations>`_ for further instruction.

.. note::

    You can associate multiple Artifacts, Cases, Groups, and Indicators to an Indicator in a single POST or PUT request.