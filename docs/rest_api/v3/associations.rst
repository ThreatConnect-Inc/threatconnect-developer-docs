Create and Manage Associations
------------------------------

An association, one of the most powerful features in ThreatConnect®, models a relationship between two objects. Associating data empowers analysts to pivot to related objects and further investigate their relationships to the primary object in the association.

When creating and updating Artifacts, Cases, Groups, Indicators, Intelligence Requirements (IRs), and Victim Assets with the ThreatConnect v3 API, you may also create and manage associations for those object types.

Supported Association Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table outlines the types of associations you can create when using the API endpoints corresponding to Artifacts, Cases, Groups, Indicators, IRs, and Victim Assets and whether each endpoint supports cross-owner associations.

.. list-table::
   :widths: 33 33 34
   :header-rows: 1

   * - Endpoint
     - Associable Object Types
     - Supports Cross-Owner Associations?
   * - ``/v3/artifacts``
     - * Groups
       * Indicators
     - Yes
   * - ``/v3/cases``
     - * Cases
       * Groups
       * Indicators
     - Yes
   * - ``/v3/groups``
     - * Artifacts
       * Cases
       * Groups
       * Indicators
       * Victim Assets
     - Yes
   * - ``/v3/indicators``
     - * Artifacts
       * Cases
       * Groups
       * Indicators
     - Yes
   * - ``/v3/intelRequirements``
     - * Artifacts
       * Cases
       * Groups
       * Indicators
       * Victim Assets
     - Yes
   * - ``/v3/victimAssets``
     - Groups
     - No
   * - ``/v3/victims``
     - Groups
     - No

Create Associations
^^^^^^^^^^^^^^^^^^^

The following sections describe how to associate new and existing Artifacts, Cases, Groups, Indicators, and Victim Assets to select object types. They also provide JSON samples that can be used in the request body of POST and PUT requests to the endpoints listed in the `"Supported Association Types" <#supported-association-types>`_ section. While each sample demonstrates how to create an association to a single object, you can create associations to multiple objects in a single POST or PUT request.

Artifact Associations
=====================

You can associate newly created and existing Artifacts to Groups, Indicators, and IRs with the v3 API.

New Artifact
""""""""""""

To create an Artifact and use it in an association, include the ``associatedArtifacts`` field in the request body and define `all fields required to create the Artifact <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html#available-fields>`_.

.. code:: json

    "associatedArtifacts": {
        "data": [
            {
                "caseId": 12345,
                "summary": "badguy@bad.com",
                "type": "Email Address"
            }
        ]
    }

Existing Artifact
"""""""""""""""""

To use an existing Artifact in an association, include the ``associatedArtifacts`` field in the request body and set the value of the ``id`` field to the ID of the Artifact.

.. code:: json

    "associatedArtifacts": {
        "data": [
            {
                "id": 12345
            }
        ]
    }

Case Associations
=================

You can associate newly created and existing Cases to Groups, Indicators, and IRs with the v3 API.

New Case
""""""""

To create a Case and use it in an association, include the ``associatedCases`` field in the request body and define `all fields required to create the Case <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html#available-fields>`_.

.. code:: json

    "associatedCases": {
        "data": [
            {
                "name": "Phishing Investigation",
                "severity": "Low",
                "status": "Open"
            }
        ]
    }

Existing Case
"""""""""""""

To use an existing Case in an association, include the ``associatedCases`` field in the request body and set the value of the ``id`` field to the ID of the Case.

.. code:: json

    "associatedCases": {
        "data": [
            {
                "id": 12345
            }
        ]
    }

Group Associations
==================

You can associate newly created and existing Groups to Artifacts, Cases, Groups, Indicators, IRs, and Victim Assets with the v3 API.

New Group
"""""""""

To create a Group and use it in an association, include the ``associatedGroups`` field in the request body and define `all fields required for the type of Group <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html#available-fields>`_ being created. By default, the Group will be created in your Organization. To create the Group in one of your Communities or Sources, set the value of the ``ownerId`` or ``ownerName`` field to the ID or name, respectively, of the desired Community or Source.

.. code:: json

    "associatedGroups": {
        "data": [
            {
                "name": "Bad Guy",
                "type": "Adversary",
                "ownerName": "Demo Source"
            }
        ]
    }

Existing Group
""""""""""""""

To use an existing Group in an association, include the ``associatedGroups`` field in the request body and set the value of the ``id`` field to the ID of the Group.

.. code:: json

    "associatedGroups": {
        "data": [
            {
                "id": 12345
            }
        ]
    }

Indicator Associations
======================

You can associate newly created and existing Indicators to Artifacts, Cases, Groups, Indicators, and IRs with the v3 API.

.. note::
    If creating Indicator-to-Indicator associations, see the `"Indicator-to-Indicator Associations" section of Indicators Overview <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#indicator-to-indicator-associations>`_ for further instruction.

New Indicator
"""""""""""""

To create a new Indicator and use it in an association, include the ``associatedIndicators`` field in the request body and define `all required fields for the type of Indicator <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#available-fields>`_ being created. By default, the Indicator will be created in your Organization. To create the Indicator in one of your Communities or Sources, set the value of the ``ownerId`` or ``ownerName`` field to the ID or name, respectively, of the desired Community or Source.

.. code:: json

    "associatedIndicators": {
        "data": [
            {
                "hostName": "badguy.com",
                "type": "Host",
                "ownerName": "Demo Source"
            }
        ]
    }

Existing Indicator
""""""""""""""""""

To use an existing Indicator in an association, include the ``associatedIndicators`` field in the request body and set the value of the ``id`` field to the ID of the Indicator. Alternatively, identify the Indicator by using the ``type`` field and the field representing its summary.

.. note::
    If using an Indicator's type and summary, the API request will search for the Indicator in your Organization. If the Indicator exists in one of your Communities or Sources, include the ``ownerId`` or ``ownerName`` field and set its value to the ID or name, respectively, of the Community or Source.

**Example (Indicator ID)**

.. code:: json

    "associatedIndicators": {
        "data": [
            {
                "id": 12345
            }
        ]
    }

**Example (Indicator Type and Summary)**

.. code:: json

    "associatedIndicators": {
        "data": [
            {
                "type": "Address",
                "ip": "71.6.135.131"		
            }
        ]
    }

Victim Asset Associations
=========================

You can associate newly created and existing Victim Assets to Groups and IRs with the v3 API.

New Victim Asset
""""""""""""""""

To create a Victim Asset and use it in an association, include the ``associatedVictimAssets`` field in the request body and define `all fields required to create the Victim Asset <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_assets/victim_assets.html#available-fields>`_.

.. code:: json

    "associatedVictimAssets": {
        "data": [
            {
                "address": "jsmith@companyabc.com",
                "type": "EmailAddress",
                "victimId": 12345
            }
        ]
    }

Existing Victim Asset
"""""""""""""""""""""

To use an existing Victim Asset in an association, include the ``associatedVictimAssets`` field in the request body and set the value of the ``id`` field to the ID of the Victim Asset.

.. code:: json

    "associatedVictimAssets": {
        "data": [
            {
                "id": 12345
            }
        ]
    }

Retrieve Associations
^^^^^^^^^^^^^^^^^^^^^

When retrieving Artifacts, Cases, Groups, Indicators, IRs, Victims, or Victim Assets, use the ``fields`` `query parameter <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_ to include the object's associations in the response.

**Example**

.. code::

    GET /v3/indicators/badguy.com?fields=associatedGroups&fields=associatedIndicators

To retrieve a list of accepted values for the ``fields`` query parameter for each API endpoint, send a request in the following format:

.. code::

    OPTIONS /v3/{objectType}/fields

Remove Associations
^^^^^^^^^^^^^^^^^^^

When updating an Artifact, Case, Group, Indicator, IR, Victim, or Victim Asset, use the ``mode`` field and set its value to ``delete`` to remove an association for the object. For more information on using the ``mode`` field, see `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_.

.. attention::
    When dissociating an object from an Artifact, Case, Group, Indicator, IR, Victim, or Victim Asset, you must identify the object by its ID.

.. code::

    PUT /v3/indicators/badguy.com
    Content-Type: application/json
    
    {
        "associatedGroups": {
            "data": [
                {
                    "id": 12345
                }
            ],
            "mode": "delete"
        }
    }