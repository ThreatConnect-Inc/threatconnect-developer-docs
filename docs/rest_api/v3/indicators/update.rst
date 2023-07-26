Update Indicators
-----------------

The following example illustrates the basic format for updating an Indicator:

.. code::

    PUT /v3/indicators/{indicatorId or indicatorSummary}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ and `Indicator-Specific Fields <#indicator-specific-fields>`_ sections for a list of available fields that can be included in the body of a PUT request to the ``/v3/indicators`` endpoint.

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

The following request will make the following updates to the **ultrabadguy.com** Host Indicator:

- Disable the **DNS** feature for the Indicator
- Dissociate the **Bad Guy** Adversary Group from the Indicator
- Update the Indicator's Confidence Rating
- Replace any existing Security Labels applied to the Indicator with the **TLP: RED** Security Label
- Apply a new **Russia** Tag to the Indicator without replacing any existing Tags applied to the Indicator.

.. hint::
    To include the ``associatedGroups``, ``securityLabels``, and ``tags`` fields in the API response, append ``?fields=associatedGroups&fields=securityLabels&fields=tags`` to the end of the request URL.

.. code::

    PUT /v3/indicators/ultrabadguy.com
    {
        "dnsActive": false,
        "associatedGroups": {
            "data": [
                {
                    "id": 15
                }
            ],
            "mode": "delete"
        },
        "confidence": 92,
        "securityLabels": {
            "data": [
                {
                    "name": "TLP:RED"
                }
            ],
            "mode": "replace"
        },
        "tags": {
            "data": [
                {
                    "name": "Russia"
                }
            ],
            "mode": "append"
        }
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
            "type": "Host",
            "lastModified": "2021-11-05T17:21:06Z",
            "rating": 5.00,
            "confidence": 92,
            "summary": "ultrabadguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "hostName": "ultrabadguy.com",
            "dnsActive": false,
            "whoisActive": true,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com&owner=Demo+Organization"
        },
        "message": "Updated",
        "status": "Success"
    }