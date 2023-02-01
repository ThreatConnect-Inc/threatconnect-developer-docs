Update an Object's Metadata
---------------------------

Overview
^^^^^^^^

When updating an Artifact, Case, Indicator, Group, Victim, or Victim Asset, you can use the ``mode`` field to add or remove metadata. The ``mode`` field accepts three values, each of which is defined in the following table.

+----------+-------------------------------------------------------------------------------+
| Value    | Description                                                                   |
+==========+===============================================================================+
| append   | This mode adds new metadata to an object without removing existing metadata.  |
+----------+-------------------------------------------------------------------------------+
| delete   | This mode removes metadata from an object.                                    |
+----------+-------------------------------------------------------------------------------+
| replace  | This mode replaces all existing Associations, Attributes, Security Labels,    |
|          | or Tags with the new Associations, Attributes, Security Labels, and Tags,     |
|          | respectively, defined in the body of the PUT request.                         |
+----------+-------------------------------------------------------------------------------+

.. note::
    If no value is assigned to the ``mode`` field when updating an object's metadata, append will be used by default.

The following table lists the metadata that can be updated for each object's respective endpoint.

+-----------------+-------------------------+
| Object          | Updatable Metadata      |
+=================+=========================+
| artifacts       | associatedGroups        |
+-----------------+-------------------------+
|                 | associatedIndicators    |
+-----------------+-------------------------+
| cases           | associatedCases         |
+-----------------+-------------------------+
|                 | associatedGroups        |
+-----------------+-------------------------+
|                 | associatedIndicators    |
+-----------------+-------------------------+
|                 | attributes              |
+-----------------+-------------------------+
|                 | tags                    |
+-----------------+-------------------------+
| indicators      | associatedArtifacts     |
+-----------------+-------------------------+
|                 | associatedCases         |
+-----------------+-------------------------+
|                 | associatedGroups        |
+-----------------+-------------------------+
|                 | associatedIndicators    |
+-----------------+-------------------------+
|                 | attributes              |
+-----------------+-------------------------+
|                 | fileActions             |
+-----------------+-------------------------+
|                 | fileOccurrences         |
+-----------------+-------------------------+
|                 | securityLabels          |
+-----------------+-------------------------+
|                 | tags                    |
+-----------------+-------------------------+
| groups          | associatedArtifacts     |
+-----------------+-------------------------+
|                 | associatedCases         |
+-----------------+-------------------------+
|                 | associatedGroups        |
+-----------------+-------------------------+
|                 | associatedIndicators    |
+-----------------+-------------------------+
|                 | associatedVictimAssets  |
+-----------------+-------------------------+
|                 | attributes              |
+-----------------+-------------------------+
|                 | securityLabels          |
+-----------------+-------------------------+
|                 | tags                    |
+-----------------+-------------------------+
| victims         | associatedGroups        |
+-----------------+-------------------------+
|                 | attributes              |
+-----------------+-------------------------+
|                 | securityLabels          |
+-----------------+-------------------------+
|                 | tags                    |
+-----------------+-------------------------+
| victimAssets    | associatedGroups        |
+-----------------+-------------------------+

.. attention::
    To dissociate an object from an Artifact, Case, Indicator, Group, Victim, or Victim Asset, you must use the object's ID when setting its respective field (e.g., to dissociate an Indicator from an object, use the Indicator's ID when setting the ``associatedIndicators`` field).

Example Request
^^^^^^^^^^^^^^^

The following request will make the following updates to the **ultrabadguy.com** Host Indicator:

- Dissociate the Group whose ID is 15 from the Indicator
- Replace any Security Labels applied to the Indicator with the **TLP: RED** Security Label
- Apply a new **Russia** Tag to the Indicator without replacing any existing Tags applied to it

.. code::

    PUT /v3/indicators/ultrabadguy.com
    {
        "associatedGroups": {"data": [{"id": 15}], "mode": "delete"},
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
                        "webLink": "https://app.threatconnect.com/#/details/groups/12/overview ",
                        "name": "Dangerous Incident",
                        "createdBy": {
                            "id": 1,
                            "userName": "smithj@threatconnect.com"
                        },
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