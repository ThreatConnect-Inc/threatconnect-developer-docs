Update Groups
-------------

The following example illustrates the basic format for updating a Group:

.. code::

    PUT /v3/groups/{groupId}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ and `Group-Specific Fields <#group-specific-fields>`_ sections for a list of available fields that can be included in the body of a PUT request to the ``/v3/groups`` endpoint.

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
^^^^^^^^^^^^^^^^^^^

The following request will make the following updates to the Incident Group whose ID is 3:

- Associate an Email Address Indicator (**verybadguy@bad.com**) that exists in Demo Community to the Group
- Create a new Host Indicator (**ultrabadguy.com**) in the API user's Organization and associate it to the Group
- Add an **Additional Analysis and Context Attribute** to the Group
- Update the status of the Incident
- Remove the **Targeted Attack** Tag applied to the Group

.. hint::
    To include the ``associatedIndicators``, ``attributes``, and ``tags`` fields in the API response, append ``?fields=associatedIndicators&fields=attributes&fields=tags`` to the end of the request URL.

.. code::

    PUT /v3/groups/3
    {
        "associatedIndicators": {
            "data": [
                {
                    "address": "verybadguy@bad.com",
                    "type": "EmailAddress",
                    "ownerName": "Demo Community"
                },
                {
                    "hostName": "ultrabadguy.com",
                    "type": "Host"
                }
            ]
        },
        "attributes": {
            "data": [
                {
                    "type": "Additional Analysis and Context",
                    "value": "Based on internal analysis, this incident was very severe.",
                    "source": "Example Source"
                }
            ]
        },
        "status": "Incident Reported",
        "tags": {
            "data": [
                {
                    "name": "Targeted Attack"
                }
            ],
            "mode": "delete"
        }

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-03T14:57:45Z",
            "webLink": "https://app.threatconnect.com/#/details/groups/3/overview",
            "type": "Incident",
            "name": "Bad Incident",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "upVoteCount":"0",
            "downVoteCount":"0",
            "status": "Incident Reported",
            "eventDate": "2021-11-03T00:00:00Z",
            "lastModified": "2022-03-09T08:14:23Z",
            "legacyLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=3"
        },
        "message": "Updated",
        "status": "Success"
    }