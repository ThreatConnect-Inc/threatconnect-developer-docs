Associations
------------

When creating or updating an IR, you can create associations between the IR and Artifacts, Cases, Groups, Indicators, and Victim Assets in your Organization, Communities, and Sources. When creating associations for IRs using the ThreatConnect v3 API, follow these guidelines:

* **Artifact**
    * **New Artifact**: Include `all fields required to create an Artifact <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html#available-fields>`_ when setting the ``associatedArtifacts`` field.
    * **Existing Artifact**: Use the Artifact's ID when setting the ``associatedArtifacts`` field (e.g., ``"associatedArtifacts": {"data": [{"id": 12345}]}``).
* **Case**
    * **New Case**: Include `all fields required to create a Case <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html#available-fields>`_ when setting the ``associatedCases`` field.
    * **Existing Case**: Use the Case's ID when setting the ``associatedCases`` field.
* **Group**
    * **New Group**: Include `all fields required to create the type of Group <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html#available-fields>`_ when setting the ``associatedGroups`` field. To create the Group in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Group when setting the ``associatedGroups`` field.
    * **Existing Group**: Use the Group's ID when setting the ``associatedGroups`` field.
* **Indicator**
    * **New Indicator**: Include `all fields required to create the type of Indicator <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#available-fields>`_ when setting the ``associatedIndicators`` field. To create the Indicator in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Indicator when setting the ``associatedIndicators`` field.
    * **Existing Indicator**: Use the Indicator's ID, or use its summary and type (e.g., ``"associatedIndicators": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``associatedIndicators`` field. To create an association to an Indicator in a Community or Source using the Indicator's summary and type, include the ``ownerId`` or ``ownerName`` field and specify the ID or name, respectively, of the Community or Source to which the Indicator belongs when setting the ``associatedIndicators`` field.
* **Victim Asset**
    * **New Victim Asset**: Include `all fields required to create a Victim Asset <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_assets/victim_assets.html#available-fields>`_ when setting the ``associatedVictimAssets`` field.
    * **Existing Victim Asset**: Use the Victim Asset's ID when setting the ``associatedVictimAssets`` field.

.. note::
    You can associate multiple Artifacts, Cases, Groups, Indicators, and Victim Assets to an IR in a single POST or PUT request.

.. hint::
    When updating an IR, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedArtifacts``
    - ``associatedCases``
    - ``associatedGroups``
    - ``associatedIndicators``
    - ``associatedVictimAssets``
    - ``tags``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.