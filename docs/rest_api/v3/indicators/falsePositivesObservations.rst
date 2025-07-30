False Positives and Observations
--------------------------------

As of ThreatConnect 7.8, API users can report false positives and observations for an Indicator that belongs to their Organization, Communities, and Sources.

Requirements
^^^^^^^^^^^^

- To report false positives and observations for Indicators via the ThreatConnect v3 API, the **Include in Observations and False Positives** option must be selected for your API user account.
- To report false positives and observations for Indicators in an Organization, your API user account must have an Organization role of Standard User, Sharing User, Organization Administrator, or App Developer. Alternatively, if the **readOnlyUserUpdatesAllowed** system setting is turned on for your ThreatConnect instance, your API user account can have any Organization role.
- To report false positives and observations for Indicators in a Community or Source, your API user account must have a Community role of Contributor, Editor, or Director for the Community or Source. Alternatively, if the **readOnlyUserUpdatesAllowed** system setting is turned on for your ThreatConnect instance, your API user account can have any Community role except Banned for the Community or Source.

Report an Indicator as False Positive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating a new Indicator or updating an existing one, you can report the Indicator as false positive. The following request demonstrates how to report an existing Indicator as false positive. Because false positive data are not included in the API response by default, the ``fields`` query parameter is used and assigned a value of ``falsePositives`` to include those data in the response.

.. code::

    PUT /v3/indicators/75?fields=falsePositives
    Content-Type: application/json

    {
        "falsePositiveFlag": true
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 75,
            "dateAdded": "2024-11-07T12:55:33Z",
            "ownerId": 2,
            "ownerName": "Demo Source",
            "webLink": "https://app.threatconnect.com/#/details/indicators/75",
            "type": "Host",
            "lastModified": "2024-12-09T19:34:21Z",
            "summary": "nefarious.com",
            "falsePositives": 1,
            "falsePositiveReportedByUser": true,
            "privateFlag": false,
            "active": false,
            "activeLocked": false,
            "hostName": "nefarious.com",
            "dnsActive": false,
            "whoisActive": false,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=nefarious.com&owner=Demo+Source"
        },
        "message": "Updated",
        "status": "Success"
    }

JSON Response (Read Only)

.. code:: json

    {
        "data": {
            "type": "Host",
            "threatAssessRating": 3.59,
            "threatAssessConfidence": 20.65,
            "threatAssessScore": 273,
            "threatAssessScoreObserved": 0,
            "threatAssessScoreFalsePositive": 0,
            "summary": "nefarious.com",
            "observations": 0,
            "falsePositives": 1,
            "lastFalsePositive": "2024-12-09T00:00:00Z",
            "falsePositiveReportedByUser": true,
            "trackedUsers": {
                "John Smith": {
                    "observations": 0,
                    "falsePositives": 1,
                    "lastFalsePositive": "2024-12-09T00:00:00Z"
                },
                "Patrick Jones": {
                    "observations": 0,
                    "falsePositives": 0
                }
            }
        },
        "message": "Updated",
        "status": "Success"
    }

Report Observations for an Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating a new Indicator or updating an existing one, you can report observations for the Indicator. The following request demonstrates how to report observations for an existing Indicator. Because observation data are not included in the API response by default, the ``fields`` query parameter is used and assigned a value of ``observations`` to include those data in the response.

.. code::

    PUT /v3/indicators/75?fields=observations
    Content-Type: application/json
    
    {
        "observations": 1
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 75,
            "dateAdded": "2024-11-07T12:55:33Z",
            "ownerId": 2,
            "ownerName": "Demo Source",
            "webLink": "https://app.threatconnect.com/#/details/indicators/75",
            "type": "Host",
            "lastModified": "2024-12-09T19:34:21Z",
            "summary": "nefarious.com",
            "observations": 1,
            "lastObserved": "2024-12-09T00:00:00Z",
            "privateFlag": false,
            "active": false,
            "activeLocked": false,
            "hostName": "nefarious.com",
            "dnsActive": false,
            "whoisActive": false,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=nefarious.com&owner=Demo+Source"
        },
        "message": "Updated",
        "status": "Success"
    }

JSON Response (Read Only)

.. code:: json

    {
        "data": {
            "type": "Host",
            "threatAssessRating": 3.59,
            "threatAssessConfidence": 20.65,
            "threatAssessScore": 273,
            "threatAssessScoreObserved": 0,
            "threatAssessScoreFalsePositive": 0,
            "summary": "nefarious.com",
            "observations": 1,
            "lastObserved": "2024-12-09T20:13:50Z",
            "falsePositives": 0,
            "falsePositiveReportedByUser": false,
            "trackedUsers": {
                "John Smith": {
                    "observations": 1,
                    "lastObserved": "2024-12-09T20:13:50Z",
                    "falsePositives": 0
                },
                "Patrick Jones": {
                    "observations": 0,
                    "falsePositives": 0
                }
            }
        },
        "message": "Updated",
        "status": "Success"
    }