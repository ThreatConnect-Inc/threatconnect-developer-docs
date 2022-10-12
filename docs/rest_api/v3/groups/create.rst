Create Groups
-------------

The basic format for creating a Group is:

.. code::

    POST /v3/groups
    {
        "name": "Group name goes here",
        "type": "Group type goes here"
        //required fields for the selected Group type go here, if applicable
    }

Refer to the `Available Fields <#available-fields>`_ and `Group-Specific Fields <#group-specific-fields>`_ sections for a list of available fields that can be included in the body of a POST request for the ``groups`` object.

.. note::
    You can add multiple `Attributes <https://docs.threatconnect.com/en/latest/rest_api/v3/group_attributes/group_attributes.html>`_, `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_, and `Security Labels <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_ to a Group in a single POST or PUT request.

Example POST Request
^^^^^^^^^^^^^^^^^^^^^

The following query will create an ``Incident`` Group for an Incident that took place on Nov. 3, 2021. The Incident will be assigned a status of ``New``, and ``Targeted Attack`` and ``Robbery`` Tags will be created and applied to it.

.. code::

    POST /v3/groups
    {
        "type": "Incident",
        "name": "Bad Incident",
        "eventDate": "2021-11-03",
        "status": "New",
        "tags": {"data": [{"name": "Targeted Attack"}, {"name": "Robbery"}]}
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
                "data": [
                    {
                        "id": 11,
                        "name": "Targeted Attack",
                        "lastUsed": "2021-11-02T15:01:44Z"
                    },
                    {
                        "id": 12,
                        "name": "Robbery",
                        "lastUsed": "2021-11-02T15:01:44Z"
                    }
                ]
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
                "owner": "Demo Organization",
                "systemRole": "Api User"
            },
            "associatedGroups": {},
            "associatedIndicators": {},
            "associatedCases": {},
            "associatedArtifacts": {},
            "attributes": {},
            "status": "New",
            "eventDate": "2021-11-03T00:00:00Z",
            "lastModified": "2021-11-03T14:57:45Z"
        },
        "message": "Created",
        "status": "Success"
    }

Create Associations
^^^^^^^^^^^^^^^^^^^

In ThreatConnect, you can create associations between Groups and Artifacts, Cases, Groups, Indicators, and Victim Assets that exist in the same owner (e.g., you can only associate Artifacts, Cases, Groups, Indicators, and Victim Assets in your Organization to a Group in your Organization). If cross-owner associations are enabled on your ThreatConnect instance, you can also create associations between Groups and Indicators in Communities and Sources to which you have access and Groups in your Organization. 

When creating associations for Groups using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Artifact, include `all fields required to create an Artifact <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html#available-fields>`_when setting the ``associatedArtifacts`` field. The new Artifact will be created in the Organization to which your API user account belongs.
- To create an association to an existing Artifact, use the Artifact's ID when setting the ``associatedArtifacts`` field (e.g., ``"associatedArtifacts": {"data": [{"id": 12345}]}``).
- To create an association to a new Case, include `all fields required to create a Case <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html#available-fields>`_ when setting the ``associatedCases`` field. The new Case will be created in the Organization to which your API user account belongs.
- To create an association to an existing Case, use the Case's ID when setting the ``associatedCases`` field.
- To create an association to a new Group, include `all fields required to create the type of Group <#available-fields>`_ when setting the ``associatedGroups`` field. The new Group will be created in the Organization to which your API user account belongs.
- To create an association to an existing Group that belongs to an Organization, Community, or Source, use the Group's ID when setting the ``associatedGroups`` field.
- To create an association to a new Indicator, include `all fields required to create the type of Indicator <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_ when setting the ``associatedIndicators`` field. The new Indicator will be created in the Organization to which your API user account belongs.
- To create an association to an existing Indicator that belongs to an Organization, use the Indicator's ID, or its summary and type (e.g., ``"associatedIndicators": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``associatedIndicators`` field.
- To create an association to an existing Indicator that belongs to a Community or Source, use the Indicator's ID when setting the ``associatedIndicators`` field.
- To create an association to a new Victim Asset, include `all fields required to create a Victim Asset <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_assets/victim_assets.html#available-fields>`_ when setting the ``associatedVictimAssets`` field. The new Victim Asset will be created in the Organization to which your API user account belongs.
- To create an association to an existing Victim Asset, use the Victim Asset's ID when setting the ``associatedVictimAssets`` field.

.. note::

    You can associate multiple Artifacts, Cases, Groups, Indicators, and Victim Assets to a Group in a single POST or PUT request.