Update Groups
-------------

The basic format for updating a Group is:

.. code::

    PUT /v3/groups/{groupId}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ and `Group-Specific Fields <#group-specific-fields>`_ sections for a list of available fields that can be included in the body of a PUT request for the ``groups`` object.

.. hint::
    When updating a Group, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedArtifacts``
    - ``associatedCases``
    - ``associatedGroups``
    - ``associatedIndicators``
    - ``associatedVictimAssets``
    - ``attributes``
    - ``securityLabels``
    - ``tags``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.

Example PUT Request
^^^^^^^^^^^^^^^^^^^^^

The following query will complete the following actions for the ``Incident`` Group with ID 3:

- Associate an Email Address Indicator (``verybadguy@bad.com``) and a Host Indicator (``ultrabadguy.com``) to the Group
- Add an ``Additional Analysis and Context`` Attribute to the Group
- Update the ``status`` of the Incident
- Remove the ``Robbery`` Tag applied to the Group.

.. code::

    PUT /v3/groups/3
    {
        "associatedIndicators": {"data": [{"id": 15}, {"hostName": "ultrabadguy.com", "type": "Host"}]},
        "attributes": {"data": [{"type": "Additional Analysis and Context", "value": "Based on internal analysis, this incident was very severe.", "source": "Example Source"}]},
        "status": "Incident Reported",
        "tags": {"data": [{"name": "Robbery"}], "mode": "delete"}
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-03T14:57:45Z",
            "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=3",
            "tags": {
                "data": [{
                    "id": 11,
                    "name": "Targeted Attack",
                    "lastUsed": "2021-11-04T18:52:29Z"
                }],
            },
            "securityLabels": {},
            "type": "Incident",
            "name": "Bad Incident",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "role": "Api User"
            },
            "associatedGroups": {},
            "associatedIndicators": {
                "data": [
                    {
                        "id": 15,
                        "type": "EmailAddress",
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-10-26T16:26:19Z",
                        "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=verybadguy%40bad.com",
                        "lastModified": "2021-11-04T19:07:01Z",
                        "summary": "verybadguy@bad.com",
                        "privateFlag": false,
                        "active": true,
                        "activeLocked": false,
                        "address": "verybadguy@bad.com"
                    },
                    {
                        "id": 9,
                        "type": "Host",
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-10-26T12:40:00Z",
                        "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=ultrabadguy.com",
                        "lastModified": "2021-11-04T13:00:29Z",
                        "rating": 4.0,
                        "confidence": 85,
                        "summary": "ultrabadguy.com",
                        "privateFlag": false,
                        "active": true,
                        "activeLocked": false,
                        "hostName": "ultrabadguy.com",
                        "dnsActive": true,
                        "whoisActive": true
                    }
                ],
            },
            "associatedCases": {},
            "associatedArtifacts": {},
            "attributes": {
                "data": [{
                    "id": 10,
                    "type": "Additional Analysis and Context",
                    "value": "Based on internal analysis, this incident was very severe.",
                    "source": "Example Source",
                    "createdBy": {
                        "id": 3,
                        "userName": "11112222333344445555",
                        "firstName": "John",
                        "lastName": "Smith",
                        "pseudonym": "jsmithAPI",
                        "role": "Api User"
                    },
                    "dateAdded": "2021-11-04T19:07:01Z",
                    "lastModified": "2021-11-04T19:07:01Z",
                    "default": false
                }],
            },
            "status": "Incident Reported",
            "eventDate": "2021-11-03T00:00:00Z",
            "lastModified": "2022-03-09T08:14:23Z"
        },
        "message": "Updated",
        "status": "Success"
    }
