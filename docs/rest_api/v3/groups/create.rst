Create Groups
-------------

The following example illustrates the basic format for creating a Group:

.. code::

    POST /v3/groups
    {
        "name": "Group name goes here",
        "type": "Group type goes here"
        //required fields for the selected Group type go here, if applicable
    }

Refer to the `Available Fields <#available-fields>`_ and `Group-Specific Fields <#group-specific-fields>`_ sections for a list of available fields that can be included in the body of a POST request to the ``/v3/groups`` endpoint.

.. note::
    You can add multiple `Attributes <https://docs.threatconnect.com/en/latest/rest_api/v3/group_attributes/group_attributes.html>`_, `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_, and `Security Labels <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_ to a Group in a single POST or PUT request.

Example POST Request
^^^^^^^^^^^^^^^^^^^^^

The following request will create an Incident Group for an Incident that took place on Nov. 3, 2021. The Incident will be assigned a status of **New**, and **Targeted Attack** and **Robbery** Tags will be applied to it.

.. hint::
    To include the ``tags`` field in the API response, append ``?fields=tags`` to the end of the request URL.

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
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-03T14:57:45Z",
            "webLink": "https://app.threatconnect.com/#/details/groups/3/overview",
            "type": "Incident",
            "name": "Bad Incident",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555"
            },
            "upVoteCount":"0",
            "downVoteCount":"0",
            "status": "New",
            "eventDate": "2021-11-03T00:00:00Z",
            "lastModified": "2021-11-03T14:57:4511:04:12Z",
            "legacyLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=3"
        },
        "message": "Created",
        "status": "Success"
    }

Create Associations
^^^^^^^^^^^^^^^^^^^

You can create associations between Groups and Artifacts, Cases, Groups, Indicators, and Victim Assets that exist in the same owner. If cross-owner associations are enabled on your ThreatConnect instance, you can also create associations between Groups and Indicators and other Groups that exist in any owner to which you have access.

When creating associations for Groups using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Artifact, include `all fields required to create an Artifact <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html#available-fields>`_ when setting the ``associatedArtifacts`` field.
- To create an association to an existing Artifact, use the Artifact's ID when setting the ``associatedArtifacts`` field (e.g., ``"associatedArtifacts": {"data": [{"id": 12345}]}``).
- To create an association to a new Case, include `all fields required to create a Case <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html#available-fields>`_ when setting the ``associatedCases`` field.
- To create an association to an existing Case, use the Case's ID when setting the ``associatedCases`` field.
- To create an association to a new Group, include `all fields required to create the type of Group <#available-fields>`_ when setting the ``associatedGroups`` field. To create the Group in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Group when setting the ``associatedGroups`` field.
- To create an association to an existing Group, use the Group's ID when setting the ``associatedGroups`` field.
- To create an association to a new Indicator, include `all fields required to create the type of Indicator <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#available-fields>`_ when setting the ``associatedIndicators`` field. To create the Indicator in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Indicator when setting the associatedIndicators field.
- To create an association to an existing Indicator, use the Indicator's ID, or use its summary and type (e.g., ``"associatedIndicators": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``associatedIndicators`` field. To create association to an Indicator in a Community or Source using the Indicator's summary and type, include the ``ownerId`` or ``ownerName`` field and specify the ID or name, respectively, of the Community or Source to which the Indicator belongs when setting the ``associatedIndicators`` field.
- To create an association to a new Victim Asset, include `all fields required to create a Victim Asset <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_assets/victim_assets.html#available-fields>`_ when setting the ``associatedVictimAssets`` field.
- To create an association to an existing Victim Asset, use the Victim Asset's ID when setting the ``associatedVictimAssets`` field.

.. note::
    You can associate multiple Artifacts, Cases, Groups, Indicators, and Victim Assets to a Group in a single POST or PUT request.