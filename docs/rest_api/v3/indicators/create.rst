Create Indicators
-----------------

The basic format for creating an Indicator is:

.. code::

    POST /v3/indicators/
    {
        "type": "Indicator type goes here",
        //required fields for the selected Indicator type
    }

Refer to the `Available Fields <#available-fields>`_ and `Indicator-Specific Fields <#indicator-specific-fields>`_ sections for a list of available fields that can be included in the body of a POST request for the ``indicators`` object.

.. note::
    You can add multiple Attributes, Tags, and Security Labels to the Indicator being created in a single POST request. Similarly, you can associate multiple Artifacts, Cases, and Groups to the Indicator being created in a single POST request.

Example POST Request
^^^^^^^^^^^^^^^^^^^^^

The following query will create a Host Indicator with a host name of ``ultrabadguy.com``. Note that all optional fields available for the ``indicators`` object are included in this request.

.. code::

    POST /v3/indicators/
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
                "data": [{
                    "id": 10,
                    "name": "Malicious Host",
                    "description": "A tag that can be applied to malicious Host Indicators.",
                    "lastUsed": "2021-11-05T16:43:17Z"
                }, {
                    "id": 11,
                    "name": "Targeted Attack",
                    "lastUsed": "2021-11-05T16:43:17Z"
                }],
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
                "data": [{
                    "id": 15,
                    "type": "Adversary",
                    "ownerName": "Demo Organization",
                    "dateAdded": "2021-11-05T16:43:17Z",
                    "webLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=15",
                    "name": "Bad Guy",
                    "createdBy": "John Smith"
                }, {
                    "id": 12,
                    "type": "Incident",
                    "ownerName": "Demo Organization",
                    "dateAdded": "2021-08-27T12:16:56Z",
                    "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=12",
                    "name": "Dangerous Incident",
                    "createdBy": "Pat Jones"
                }],
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
                }],
            },
            "attributes": {
                "data": [{
                    "id": 88842457,
                    "type": "Additional Analysis and Context",
                    "value": "This host is very dangerous",
                    "source": "Phase of Intrusion",
                    "createdBy": {
                        "id": 371,
                        "userName": "89474115115672885137",
                        "firstName": "j",
                        "lastName": "smith",
                        "pseudonym": "APIUsergj03B"
                    },
                    "dateAdded": "2021-11-05T16:43:17Z",
                    "lastModified": "2021-11-05T16:43:17Z",
                    "default": false
                }],
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

.. note::
    When creating or updating an Indicator, you can apply Tags that do not yet exist in ThreatConnect to it. To do so, fill out `all required fields for each new Tag <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_. Upon creation of the new Indicator, any Tags included in the body of the POST request that do not yet exist in ThreatConnect will also be created.

    Similarly, you can associate Artifacts, Cases, and Groups that do not yet exist in ThreatConnect to the Indicator. To do so, fill out all required fields for the type of object being associated to the Indicator. Upon creation of the new Indicator, any associated Artifacts, Cases, or Groups included in the body of the POST request that do not yet exist in ThreatConnect will also be created.
