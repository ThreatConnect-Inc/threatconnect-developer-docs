Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the ``/v3/groups`` endpoint:

.. code::

    OPTIONS /v3/groups

.. hint::
    To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/groups`` endpoint for **all** Group types.

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
       | {"data": [{"name": "Hacker Investigation", "status": "Open", "severity": "Low" }]}
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
   * - attributes [1]_, [2]_
     - A list of Attributes added to the Group 
     - `Group Attribute Object <https://docs.threatconnect.com/en/latest/rest_api/v3/group-attributes/group-attributes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"type": "Description", "value": "A dangerous Group", "default": true}]}
   * - externalDateAdded
     - The date and time when the Group was created externally
     - DateTime
     - FALSE
     - TRUE
     - "2023-10-04T12:34:56Z"
   * - externalDateExpires
     - The date and time when the Group expires externally
     - DateTime
     - FALSE
     - TRUE
     - "2023-10-04T12:34:56Z"
   * - externalLastModified
     - The date and time when the Group was last modified externally
     - DateTime
     - FALSE
     - TRUE
     - "2023-10-04T12:34:56Z"
   * - firstSeen
     - The date and time when the Group was first seen
     - DateTime
     - FALSE
     - TRUE
     - "2023-10-04T12:34:56Z"
   * - lastSeen
     - The date and time when the Group was last seen
     - DateTime
     - FALSE
     - TRUE
     - "2023-10-04T12:34:56Z"
   * - name
     - The Group's name
     - String
     - TRUE
     - TRUE
     - "21-0043847: Threat Actor Capabilities"
   * - ownerId [3]_
     - The ID of the `owner <https://docs.threatconnect.com/en/latest/rest_api/v3/owners/owners.html>`_ to which the Group belongs
     - Integer
     - FALSE
     - FALSE
     - 1, 2, 3,...100
   * - ownerName [3]_
     - The name of the owner to which the Group belongs
     - String
     - FALSE
     - FALSE
     - "Demo Community"
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
   * - type [4]_
     - The type of Group being created
     - String
     - TRUE
     - FALSE
     - "Document", "Email"
   * - xid
     - The Group's XID
     - String
     - FALSE
     - FALSE
     - "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"

.. [1] To retrieve a list of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_, send the following request: ``GET /v3/attributeTypes``.
.. [2] To add a Description to a Group, use the ``attributes`` field to create a Description Attribute. Similarly, to add a Source to a Group, use the ``attributes`` field to create a Source Attribute.
.. [3] By default, Groups will be created in the Organization in which your API user account resides. To create a Group in a Community or Source, include the ``ownerId`` or ``ownerName`` field in your request. Alternatively, use the ``owner`` query parameter to `specify the owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_ in which to create the Group.
.. [4] The following are accepted values for the ``type`` field:

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

Group-Specific Fields
^^^^^^^^^^^^^^^^^^^^^

Based on the type of Group being created, you may need to include additional fields in the body of a POST request. Similarly, some Group types include additional fields that may be updated via a PUT request.

The following tables lists valid fields that can be included in the body of a POST or PUT request Document, Email, Event, Incident, Report, Signature, and Task Groups.

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
     - FALSE
     - TRUE
   * - malware [5]_
     - Indicates whether the Document is malware
     - Boolean
     - FALSE
     - TRUE
   * - password
     - The password associated with the Document
     - String
     - FALSE*
     - TRUE

.. [5] If ``malware`` is set to ``true``, then the ``password`` field will be required.

To upload a file to a Document Group or update the contents of a file uploaded to a Document Group, see the `Upload a File to a Document or Report Group <#upload-a-file-to-a-document-or-report-group-2>`_ and `Update a Document or Report Group's File <#update-a-document-or-report-group-s-file-2>`_ sections, respectively.

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

.. note::
    The ``to`` field for Email Groups is a read-only field. However, associating an Email Address `Victim Asset <https://docs.threatconnect.com/en/latest/rest_api/v3/victim_assets/victim_assets.html>`_ to an Email Group will populate the Email Group's ``to`` field with that Victim Asset's email address automatically.

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
   * - eventType [6]_
     - The Event's type
     - String
     - FALSE
     - TRUE
   * - status [7]_
     - The status of the Event
     - String
     - FALSE
     - TRUE

For more information on updating the status of Event Groups, see the `Event Status <#event-status>`_ section.

.. [6] The following are accepted values for an Event Group's ``eventType`` field:

    - ``Alert``
    - ``Campaign``
    - ``None``

.. [7] The following are accepted values for an Event Group's ``status`` field:

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
   * - status [8]_
     - The status of the Incident
     - String
     - FALSE
     - TRUE

.. [8] The following are accepted values for an Incident Group's ``status`` field:

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
     - FALSE
     - TRUE
   * - publishDate
     - The date and time when the Report was published
     - Date
     - FALSE
     - TRUE
   * - reviews
     - An Intelligence Review submitted for the Report (see the "Intelligence Reviews" section for more information)
     - Intelligence Review Object
     - FALSE
     - TRUE

To upload a file to a Report Group or update the contents of a file uploaded to a Report Group, see the `Upload a File to a Document or Report Group <#upload-a-file-to-a-document-or-report-group-2>`_ and `Update a Document or Report Group's File <#update-a-document-or-report-group-s-file-2>`_ sections, respectively.

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
   * - fileText [9]_
     - The file text of the Signature
     - String
     - TRUE
     - TRUE
   * - fileType [10]_
     - The file type of the Signature
     - String
     - TRUE
     - TRUE

.. [9] The ``fileText`` field contains the Signature itself, which must be properly escaped and encoded when creating or updating the Signature Group.

.. [10] The following are accepted values for a Signature Group's ``fileType`` field:

    - ``Bro``
    - ``ClamAV``
    - ``CybOX``
    - ``Iris Search Hash``
    - ``KQL``
    - ``OpenIOC``
    - ``Regex``
    - ``SPL``
    - ``Sigma``
    - ``Snort``
    - ``Suricata``
    - ``TQL Query``
    - ``YARA``

.. note::
    Accepted values for a Signature Group's ``fileType`` field may also include custom Signature types created by a System Administrator.

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
   * - status [11]_
     - The status of the Task
     - String
     - FALSE
     - FALSE
     - "In Progress", "Not Started"

.. [11] The following are accepted values for a Task Group's ``status`` field:

    - ``Not Started``
    - ``In Progress``
    - ``Completed``
    - ``Waiting on Someone``
    - ``Deferred``
  
Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/groups`` endpoint:

.. code::

    OPTIONS /v3/groups/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/groups`` endpoint:

.. code::

    OPTIONS /v3/groups/tql