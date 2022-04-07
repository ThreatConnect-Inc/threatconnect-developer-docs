Update Indicators
-----------------

The basic format for updating an Indicator is:

.. code::

    PUT /v3/indicators/{indicatorId or indicatorSummary}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ and `Indicator-Specific Fields <#indicator-specific-fields>`_ sections for a list of available fields that can be included in the body of a PUT request for the ``indicators`` object.

.. note::
    When updating an Indicator, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedArtifacts``
    - ``associatedCases``
    - ``associatedGroups``
    - ``attributes``
    - ``securityLabels``
    - ``tags``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.

Example PUT Request
^^^^^^^^^^^^^^^^^^^^^

The following query will complete the following actions for the ``ultrabadguy.com`` Host Indicator:

- Disable the **DNS** feature for the Indicator
- Disassociate the ``Bad Guy`` Adversary Group from the Indicator
- Update the Indicator's Confidence Rating
- Replace a ``TLP: AMBER`` Security Label that is applied to the Indicator with a ``TLP: Red`` Security Label
- Apply a new ``Russia`` Tag to the Indicator without replacing any existing Tags applied to the Indicator.

.. code::

    PUT /v3/indicators/ultrabadguy.com
    {
        "dnsActive": false,
        "associatedGroups": {"id": 15}], "mode": "delete"},
        "attributes": {"data": [{"type": "Additional Analysis and Context", "value": "This host is very dangerous", "source": "Phase of Intrusion"}]},
        "confidence": 92,
        "securityLabels": {"data": [{"name": "TLP:RED"}], "mode": "replace"},
        "tags": {"data": [{"name": "Russia"}], "mode": "append"}
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
                    },
                    {
                        "id": 12,
                        "name": "Russia",
                        "lastUsed": "2021-11-05T17:21:07Z"
                    }
                ],
            },
            "securityLabels": {
                "data": [{
                    "id": 4,
                    "name": "TLP:RED",
                    "description": "This security label is used for information that cannot be effectively acted upon by additional parties, and could lead to impacts on a party's privacy, reputation, or operations if misused.",
                    "color": "FF0033",
                    "owner": "System",
                    "dateAdded": "2016-08-31T00:00:00Z"
                }],
            },
            "lastModified": "2021-11-05T17:21:06Z",
            "type": "Host",
            "rating": 5.0,
            "confidence": 92,
            "summary": "ultrabadguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {
                "data": [{
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
                    "lastModified": "2021-11-05T17:21:07Z",
                    "rating": 5.0,
                    "confidence": 92,
                    "source": "A Reliable Source",
                    "description": "Potentially malicious host related to malware dissemination.",
                    "summary": "ultrabadguy.com",
                    "privateFlag": false,
                    "active": true,
                    "activeLocked": false,
                    "hostName": "ultrabadguy.com",
                    "dnsActive": false,
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
                        "id": 3,
                        "userName": "11112222333344445555",
                        "firstName": "John",
                        "lastName": "Smith",
                        "pseudonym": "jsmithAPI",
                        "role": "Api User"
                    },
                    "dateAdded": "2021-11-05T16:43:17Z",
                    "lastModified": "2021-11-05T16:43:17Z",
                    "default": false
                }],
            },
            "associatedCases": {},
            "associatedArtifacts": {},
            "hostName": "ultrabadguy.com",
            "dnsActive": false,
            "whoisActive": true
        },
        "message": "Updated",
        "status": "Success"
    }
