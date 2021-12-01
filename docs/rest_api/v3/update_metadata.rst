Update an Object's Metadata
---------------------------

Overview
^^^^^^^^

When updating an Indicator, Group, Victim, or Victim Asset, you can use the ``mode`` field to add or remove metadata. The ``mode`` field accepts three values, each of which is defined in the following table.

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
    If no value is assigned to the ``mode`` field when updating an object’s metadata, append will be used by default.

The following table lists the metadata that can be updated for each object’s respective endpoint.

+-----------------+-------------------------+
| Object          | Updatable Metadata      |
+=================+=========================+
| indicators      | associatedGroups        |
+-----------------+-------------------------+
|                 | attributes              |
+-----------------+-------------------------+
|                 | securityLabels          |
+-----------------+-------------------------+
|                 | tags                    |
+-----------------+-------------------------+
| groups          | associatedGroups        |
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

.. note::
    To disassociate a Group from an Indicator, Group, Victim, or Victim Asset, you must use the Group’s ID when setting the ``associatedGroups`` field.

Example Request
^^^^^^^^^^^^^^^

The following query will complete the following actions for the ``ultrabadguy.com`` Host Indicator:

- Disassociate the Group with ID ``15`` from the Indicator
- Replace the ``TLP: AMBER`` Security Label that is applied to the Indicator with the ``TLP: Red`` Security Label
- Apply a new ``Russia`` Tag to the Indicator without replacing any existing Tags applied to the Indicator.

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
            "type": "Host",
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-05T16:43:17Z",
            "webLink": "/auth/indicators/details/host.xhtml?host=ultrabadguy.com",
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
                }, {
                    "id": 12,
                    "name": "Russia",
                    "lastUsed": "2021-11-05T17:21:07Z"
                }],
                "count": 3
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
                "count": 1
            },
            "lastModified": "2021-11-05T17:21:06Z",
            "rating": 5.0,
            "confidence": 92,
            "source": "A Reliable Source",
            "description": "Potentially malicious host related to malware dissemination.",
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
                    "webLink": "/auth/incident/incident.xhtml?incident=12",
                    "name": "Dangerous Incident",
                    "createdBy": "Pat Jones"
                }],
                "count": 1
            },
            "associatedIndicators": {
                "data": [{
                    "id": 4,
                    "type": "Host",
                    "ownerName": "Demo Organization",
                    "dateAdded": "2021-11-05T16:43:17Z",
                    "webLink": "/auth/indicators/details/host.xhtml?host=ultrabadguy.com",
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
                "count": 1
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
                "count": 1
            },
            "hostName": "ultrabadguy.com",
            "dnsActive": false,
            "whoisActive": true
        },
        "message": "Updated",
        "status": "Success"
    }
