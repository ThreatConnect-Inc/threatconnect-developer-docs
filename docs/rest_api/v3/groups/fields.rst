Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/groups`` endpoint, including each field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/groups

.. hint::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request for **all** Group types.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example Value(s)
   * - associatedArtifacts
     - A list of Artifacts associated to the Group
     - `Artifact Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{ "caseId": 1, "summary": "badguy@bad.com", "type": "Email Address"}]}
   * - associatedCases
     - A list of Cases associated to the Group
     - `Case Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/cases/cases.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Hacker Investigation", "status": "Open", "severity": "Low" }]}}
   * - associatedGroups
     - A list of Groups associated to the Group
     - `Group Object <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Bad Adversary", "type": "Adversary"}]}
   * - associatedIndicators
     - A list of Indicators associated to the Group
     - `Indicator Object <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"hostName":"badguy.com", "type": "Host"}]}
   * - associatedVictimAssets
     - A list of Victim Assets associated to the Group
     - `Victim Asset Object <https://docs.threatconnect.com/en/latest/rest_api/v3/victim-assets/victim-assets.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"phone": "0123456789", "type": "Phone"}]}
   * - attributes
     - A list of Attributes corresponding to the Group 
     - `Group Attribute Object <https://docs.threatconnect.com/en/latest/rest_api/v3/group-attributes/group-attributes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"type": "Attribute Type", "value": "Attribute Value", "source": "Attribute Source"]}}
   * - name
     - The Group's name
     - String
     - TRUE
     - TRUE
     - "21-0043847: Threat Actor Capabilities"
   * - securityLabels
     - A list of Security Labels applied to the Group
     - `Security Label Object <https://docs.threatconnect.com/en/latest/rest_api/v3/security_labels/security_labels.html>`_
     - FALSE
     - TRUE
     - {"data": [{"name": "TLP:AMBER"}]}
   * - tags
     - A list of Tags applied to the Group
     - `Tag Object <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_
     - FALSE
     - TRUE
     - {"data": [{"name": "Targeted Attack"}]}
   * - type
     - The type of Group being created
     - String
     - TRUE
     - FALSE
     - "Document", "Email"

Accepted values for the ``type`` field include:

- ``Adversary``
- ``Attack Pattern``
- ``Campaign``
- ``Course of Action``
- ``Document``
- ``Email``
- ``Event``
- ``Incident``
- ``Intrusion Set``
- ``Malware``
- ``Report``
- ``Signature``
- ``Tactic``
- ``Task``
- ``Threat``
- ``Tool``
- ``Vulnerability``

.. note::
    A list of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_ can be retrieved with the following query:
    
    ``GET /v3/attributeTypes``

.. hint::
    To **associate an existing Artifact, Case, Group, or Victim Asset** to a Group, use the object's ID when setting the ``associatedArtifacts``, ``associatedCases``, ``associatedGroups``, or ``associatedVictimAssets`` field, respectively (e.g., ``{"data": [{"id": 12345}]}``). To **associate an existing Indicator to a Group**, use the Indicator's ID, or the Indicator's type and name (e.g., for a Host Indicator, use its ``hostName``), when setting the ``associatedIndicators`` field.

Group-Specific Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

Based on the type of Group being created, you may need to include additional fields in the body of a POST request. Similarly, some Group types include additional fields that may be updated via a PUT request.

The following tables lists valid fields that can be included in the body of a POST or PUT request for ``Campaign``, ``Document``, ``Email``, ``Event``, ``Incident``, ``Report``, ``Signature``, and ``Task`` Group types.

Campaign
========

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - firstSeen
     - The date and time when the Campaign was created
     - Date
     - FALSE
     - TRUE

Document
========

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - fileName
     - The file name of the Document
     - String
     - TRUE
     - TRUE
   * - malware
     - Indicates whether the Document is malware
     - Boolean
     - FALSE
     - TRUE
   * - password
     - The password associated with the Document
     - String
     - FALSE*
     - TRUE

.. note::
    \*If ``malware`` is set to ``true``, then the ``password`` field will be required

To upload the contents of a Document to ThreatConnect or update the contents of an existing Document in ThreatConnect, see the `Upload a Document or Report <#upload-a-document-or-report-2>`_ and `Update a Document or Report <#update-a-document-or-report-2>`_ sections, respectively.

Email
=====

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - body
     - The Email's body
     - String
     - FALSE
     - TRUE
   * - from
     - The Email's **From:** field
     - String
     - FALSE
     - TRUE
   * - header
     - The Email's header
     - String
     - FALSE
     - TRUE
   * - subject
     - The Email's subject
     - String
     - FALSE
     - TRUE

Event
=====

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - eventDate
     - The date and time when the Event took place
     - Date
     - FALSE
     - TRUE
   * - status
     - The status of the Event
     - String
     - FALSE
     - TRUE

Accepted values for an Event's ``status`` include:

- ``Needs Review``
- ``False Positive``
- ``No Further Action``
- ``Escalated``

Incident
========

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - eventDate
     - The date when the Incident took place
     - Date
     - FALSE
     - TRUE
   * - status
     - The status of the Incident
     - String
     - FALSE
     - TRUE

Accepted values for an Incident's ``status`` include:

- ``New``
- ``Open``
- ``Stalled``
- ``Containment Achieved``
- ``Restoration Achieved``
- ``Incident Reported``
- ``Closed``
- ``Rejected``
- ``Deleted``

Report
======

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - fileName
     - The file name of the Report
     - String
     - TRUE
     - TRUE
   * - publishDate
     - The date and time when the Report was published
     - Date
     - FALSE
     - TRUE

To upload the contents of a Report to ThreatConnect or update the contents of an existing Report in ThreatConnect, see the `Upload a Document or Report <#upload-a-document-or-report-2>`_ and `Update a Document or Report <#update-a-document-or-report-2>`_ sections, respectively.

Signature
=========

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
   * - fileName
     - The file name of the Signature
     - String
     - TRUE
     - TRUE
   * - fileText
     - The file text of the Signature
     - String
     - TRUE
     - TRUE
   * - fileType
     - The file type of the Signature
     - String
     - TRUE
     - TRUE

Accepted values for a Signature's ``fileType`` include:

- ``Bro``
- ``ClamAV``
- ``CybOX``
- ``Iris Search Hash``
- ``OpenIOC``
- ``Regex``
- ``SPL``
- ``Sigma``
- ``Snort``
- ``Suricata``
- ``YARA``

.. note::
    \*The ``fileText`` field contains the Signature itself, which must be properly escaped and encoded when creating or updating the Signature Group.

Task
====

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example Value(s)
   * - assignments
     - A list of users assigned to the Task or to whom the Task will be escalated. Valid values for the type of assignment are "Assigned" and "Escalate"
     - Assignee Object
     - FALSE
     - TRUE
     - | {"data": [{"type": "Assigned", "user": {"id": 12}}]}
       |
       | {"data": [{"type": "Escalate", "user": {"id": 8}}]}
   * - dueDate
     - The date and time when the Task is due
     - Date
     - FALSE
     - TRUE
     - "2021-04-30T00:00:00Z"
   * - escalationDate
     - The date and time when the Task should be escalated
     - String
     - FALSE
     - TRUE
     - "2021-04-30T00:00:00Z"
   * - reminderDate
     - The date and time when a reminder about the Task will be sent
     - String
     - FALSE
     - TRUE
     - "2021-04-30T00:00:00Z"
   * - status
     - The status of the Task
     - String
     - FALSE
     - FALSE
     - "In Progress", "Not Started"

Accepted values for a Task's ``status`` include:

- ``Not Started``
- ``In Progress``
- ``Completed``
- ``Waiting on Someone``
- ``Deferred``