Threat Actor Profiles
---------------------

As of ThreatConnect 7.11, you can access Threat Actor Profiles—that is, a unified view for Adversary, Intrusion Set, and Threat Groups whose name/summary matches an alias of a given threat actor. In the v3 API, you can use the ``fields`` query parameter to include unified view data for Adversary, Intrusion Set, and Threat Groups in API responses.

.. note::
    The following example requests demonstrate how to retrieve unified view data for all Adversary, Intrusion Set, and Threat Groups included in a Threat Actor Profile. You can use similar requests to retrieve unified view data for a specific Adversary, Intrusion Set, or Threat Group included in a Threat Actor Profile.

Retrieve Unified View Data for Adversaries, Intrusion Sets, and Threats
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following request to retrieve unified view data for all Adversary, Intrusion Set, and Threat Groups included in a Threat Actor Profile:

Request (Decoded URL)

.. code:: http

    GET /v3/groups?tql=hasCommonGroup(typeName in ("Adversary", "Intrusion Set", "Threat"))&fields=common

Request (Encoded URL)

.. code:: http

    GET /v3/groups?tql=hasCommonGroup(typeName%20in%20(%22Adversary%22%2C%20%22Intrusion%20Set%22%2C%20%22Threat%22))&fields=common

When the ``fields`` query parameter's value is set to ``common``, the following fields are included in the response body for each Adversary, Intrusion Set, and Threat Group object if such data are available for the Group:

.. code:: json

        "commonGroup": {
            "id": 1125899937005103,
            "dateAdded": "2025-10-22T23:40:51Z",
            "name": "Molerats",
            "description": "[Molerats](https://attack.mitre.org/groups/G0021) is an Arabic-speaking, politically-motivated threat group that has been operating since 2012. The group's victims have primarily been in the Middle East, Europe, and the United States.(Citation: DustySky)(Citation: DustySky2)(Citation: Kaspersky MoleRATs April 2019)(Citation: Cybereason Molerats Dec 2020)",
            "lastModified": "2025-10-22T23:40:51Z",
            "priority": "LOW",
            "deprecated": false,
            "mitreId": "G0021",
            "mitreLink": "https://attack.mitre.org/groups/G0021",
            "externalDateAdded": "2017-05-31T21:31:55Z",
            "externalLastModified": "2024-11-17T15:50:27Z"
        }

Retrieve Unified View Data and Linked Groups for Adversaries, Intrusion Sets, and Threats
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following request to retrieve:

- Unified view data for all Adversary, Intrusion Set, and Threat Groups included in a Threat Actor Profile
- Details about the Adversary, Intrusion Set, and Threat Groups included in a given Threat Actor Profile

Request (Decoded URL)

.. code:: http

    GET /v3/groups?tql=hasCommonGroup(typeName in ("Adversary", "Intrusion Set", "Threat"))&fields=common&fields=linkedGroups

Request (Encoded URL)

.. code:: http

    GET /v3/groups?tql=hasCommonGroup(typeName%20in%20(%22Adversary%22%2C%20%22Intrusion%20Set%22%2C%20%22Threat%22))&fields=common&fields=linkedGroups

When the ``fields`` query parameter's value is set to ``common`` and ``linkedGroups``, the following fields are included in the response body for each Adversary, Intrusion Set, and Threat Group object if such data are available for the Group:

.. code:: json

        "commonGroup": {
            "id": 1125899936001997,
            "dateAdded": "2025-10-15T23:05:50Z",
            "name": "Molerats",
            "description": "[Molerats](https://attack.mitre.org/groups/G0021) is an Arabic-speaking, politically-motivated threat group that has been operating since 2012. The group's victims have primarily been in the Middle East, Europe, and the United States.(Citation: DustySky)(Citation: DustySky2)(Citation: Kaspersky MoleRATs April 2019)(Citation: Cybereason Molerats Dec 2020)",
            "lastModified": "2025-10-15T23:05:50Z",
            "linkedGroups": {
                "data": [
                    {
                        "id": 1125899944148673,
                        "dateAdded": "2025-04-25T02:41:26Z",
                        "ownerId": 2251799814013002,
                        "ownerName": "VulnCheck Intelligence",
                        "webLink": "https://app.threatconnect.com/#/details/groups/1125899944148673",
                        "type": "Adversary",
                        "xid": "Molerats",
                        "name": "Molerats",
                        "createdBy": {
                            "userName": "ApiUser-vulncheck_intelligence",
                            "firstName": "ApiUser",
                            "lastName": "VulnCheck Intelligence",
                            "owner": "VulnCheck Intelligence"
                        },
                        "upVoteCount": "0",
                        "downVoteCount": "0",
                        "lastModified": "2025-10-22T23:40:52Z",
                        "legacyLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=1125899944148673"
                    },
                    {
                        "id": 2251799841195252,
                        "dateAdded": "2025-01-28T15:23:19Z",
                        "ownerId": 2251799814002000,
                        "ownerName": "CAL Automated Threat Library",
                        "webLink": "https://app.threatconnect.com/#/details/groups/2251799841195252",
                        "type": "Intrusion Set",
                        "xid": "MOLERATSintrusion set",
                        "name": "MOLERATS",
                        "createdBy": {
                            "userName": "ApiUser-cal_automated_threat_library",
                            "firstName": "ApiUser",
                            "lastName": "CAL Automated Threat Library",
                            "owner": "CAL Automated Threat Library"
                        },
                        "upVoteCount": "0",
                        "downVoteCount": "0",
                        "lastModified": "2025-10-22T23:40:53Z",
                        "legacyLink": "https://app.threatconnect.com/auth/intrusionset/intrusionset.xhtml?intrusionset=2251799841195252"
                    },
                    ...
                ]
            },
            "priority": "LOW",
            "deprecated": false,
            "mitreId": "G0021",
            "mitreLink": "https://attack.mitre.org/groups/G0021",
            "externalDateAdded": "2017-05-31T21:31:55Z",
            "externalLastModified": "2024-11-17T15:50:27Z"
        }

.. hint::
    You can include additional association levels for Groups objects included in the ``linkedGroups`` field. For example, to include the Attributes added to each Group object in the ``linkedGroups`` field, set the fields query parameter's value to ``linkedGroups.attributes``. For more information, see the `"Include Additional Association Levels for a Field" section of Include Additional Fields in API Responses <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html#include-additional-association-levels-for-a-field>`_.

Retrieve Unified View Data and Aliases for Adversaries, Intrusion Sets, and Threats
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following request to retrieve:

- Unified view data for all Adversary, Intrusion Set, and Threat Groups included in a Threat Actor Profile
- Custom and MITRE® aliases for a given Threat Actor Profile

Request (Decoded URL)

.. code:: http

    GET /v3/groups?tql=hasCommonGroup(typeName in ("Adversary", "Intrusion Set", "Threat"))&fields=common&fields=aliases

Request (Encoded URL)

.. code:: http

    GET /v3/groups?tql=hasCommonGroup(typeName%20in%20(%22Adversary%22%2C%20%22Intrusion%20Set%22%2C%20%22Threat%22))&fields=common&fields=aliases

When the ``fields`` query parameter's value is set to ``common`` and ``aliases``, the following fields are included in the response body for each Adversary, Intrusion Set, and Threat Group object if such data are available for the Group:

.. code:: json

        "commonGroup": {
            "id": 1125899937005103,
            "dateAdded": "2025-10-22T23:40:51Z",
            "name": "Molerats",
            "description": "[Molerats](https://attack.mitre.org/groups/G0021) is an Arabic-speaking, politically-motivated threat group that has been operating since 2012. The group's victims have primarily been in the Middle East, Europe, and the United States.(Citation: DustySky)(Citation: DustySky2)(Citation: Kaspersky MoleRATs April 2019)(Citation: Cybereason Molerats Dec 2020)",
            "lastModified": "2025-10-22T23:40:51Z",
            "mitreAliases": {
                "data": [
                    {
                        "id": 1125899915000493,
                        "alias": "Gaza Cybergang",
                        "lastModified": "2025-10-22T23:40:51Z"
                    },
                    {
                        "id": 1125899915000380,
                        "alias": "Molerats",
                        "lastModified": "2025-10-22T23:40:51Z"
                    },
                    {
                        "id": 1125899915000441,
                        "alias": "Operation Molerats",
                        "lastModified": "2025-10-22T23:40:51Z"
                    }
                ],
                "count": 3
            },
            "priority": "LOW",
            "deprecated": false,
            "mitreId": "G0021",
            "mitreLink": "https://attack.mitre.org/groups/G0021",
            "externalDateAdded": "2017-05-31T21:31:55Z",
            "externalLastModified": "2024-11-17T15:50:27Z"
        }