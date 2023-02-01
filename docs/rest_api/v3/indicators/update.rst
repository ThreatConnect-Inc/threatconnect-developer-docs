Update Indicators
-----------------

The following example illustrates the basic format for updating an Indicator:

.. code::

    PUT /v3/indicators/{indicatorId or indicatorSummary}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ and `Indicator-Specific Fields <#indicator-specific-fields>`_ sections for a list of available fields that can be included in the body of a PUT request for the ``indicators`` object.

.. hint::
    When updating an Indicator, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedArtifacts``
    - ``associatedCases``
    - ``associatedGroups``
    - ``associatedIndicators``
    - ``attributes``
    - ``fileActions``
    - ``fileOccurrences``
    - ``securityLabels``
    - ``tags``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.

Example PUT Request
^^^^^^^^^^^^^^^^^^^^^

The following request will make the following updates to the ultrabadguy.com Host Indicator:

- Disable the **DNS** feature for the Indicator
- Dissociate the **Bad Guy** Adversary Group from the Indicator
- Update the Indicator's Confidence Rating
- Replace any existing Security Labels applied to the Indicator with the **TLP: RED** Security Label
- Apply a new **Russia** Tag to the Indicator without replacing any existing Tags applied to the Indicator.

.. code::

    PUT /v3/indicators/ultrabadguy.com
    {
        "dnsActive": false,
        "associatedGroups": {"data": [{"id": 15}], "mode": "delete"},
        "confidence": 92,
        "securityLabels": {"data": [{"name": "TLP:RED"}], "mode": "replace"},
        "tags": {"data": [{"name": "Russia"}], "mode": "append"}
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
                    },
                    {
                        "id": 12,
                        "name": "Russia",
                        "lastUsed": "2021-11-05T17:21:07Z"
                    }
                ]
            },
            "securityLabels": {
                "data": [
                    {
                        "id": 4,
                        "name": "TLP:RED",
                        "description": "This security label is used for information that cannot be effectively acted upon by additional parties, and could lead to impacts on a party's privacy, reputation, or operations if misused.",
                        "color": "FF2B2B",
                        "owner": "System",
                        "dateAdded": "2016-08-31T00:00:00Z"
                    }
                ]
            },
            "type": "Host",
            "lastModified": "2021-11-05T17:21:06Z",
            "rating": 5.00,
            "confidence": 92,
            "summary": "ultrabadguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {
                "data": [
                    {
                        "id": 12,
                        "ownerId": 1,
                        "type": "Incident",
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-08-27T12:16:56Z",
                        "webLink": "https://app.threatconnect.com/#/details/groups/12/overview",
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
            "dnsActive": false,
            "whoisActive": true,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
        },
        "message": "Updated",
        "status": "Success"
    }