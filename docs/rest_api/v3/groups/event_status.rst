Event Status
------------

API users can update the status of Event Groups that belong to their Organization, Communities, and Sources. Typically, API users need edit permissions in an Event Group's owner to update the status of the Event Group. However, depending on your ThreatConnect instance's configuration, API users with read-only permissions in an Event Group's owner may be able to update the status of Event Groups.

Requirements
^^^^^^^^^^^^

- To update the status of Event Groups in an Organization, your API user account must have an Organization role of Standard User, Sharing User, Organization Administrator, or App Developer. Alternatively, if the **readOnlyUserUpdatesAllowed** system setting is turned on for your ThreatConnect instance, your API user account can have any Organization role.
- To update the status of Event Groups in a Community or Source, your API user account must have a Community role of Contributor, Editor, or Director for the Community or Source. Alternatively, if the **readOnlyUserUpdatesAllowed** system setting is turned on for your ThreatConnect instance, your API user account can have any Community role except Banned for the Community or Source.

.. note::
    API users with read-only permissions cannot update the status of Incident Groups, regardless of whether the **readOnlyUserUpdatesAllowed** system setting is turned on for your ThreatConnect instance.

Update Event Status
^^^^^^^^^^^^^^^^^^^

When creating a new Event Group or updating an existing one, you can update its status. The following request demonstrates how to update an existing Event Group's status:

.. code:: http

    PUT /v3/groups/217301
    Content-Type: application/json

    {
        "status": "No Further Action"
    }


JSON Response

.. code:: json

    {
        "data": {
            "id": 217301,
            "dateAdded": "2025-07-19T16:28:47Z",
            "ownerId": 2,
            "ownerName": "Demo Source",
            "webLink": "https:// app.threatconnect.com/#/details/groups/217301",
            "type": "Event",
            "name": "Cyber Attack",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "upVoteCount": "0",
            "downVoteCount": "0",
            "status": "No Further Action",
            "eventDate": "2025-07-19T00:00:00Z",
            "eventType": "NONE",
            "lastModified": "2025-07-19T16:40:06Z",
            "legacyLink": "https://app.threatconnect.com/auth/event/event.xhtml?event=217301"
        },
        "message": "Updated",
        "status": "Success"
    }

The response is identical for API users with edit permissions and API users with read-only permissions in the Group's owner.