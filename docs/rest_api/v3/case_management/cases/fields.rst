Available Fields
----------------

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, for the ``/v3/cases`` endpoint:

.. code::

    OPTIONS /v3/cases

.. hint::
    To include read-only fields in the response, append the ``?show=readonly`` query parameter to the OPTIONS request.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request for the ``cases`` object.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example Value(s)
   * - artifacts
     - A list of Artifacts added to the Case
     - `Artifact Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html>`_
     - FALSE
     - TRUE
     - {"data": [{"summary": "badguy.com", "type": "Host"}]}
   * - assignee
     - The user or user group assigned to the Case
     - Assignee Object
     - FALSE
     - TRUE
     - | {"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}
       |
       | {"type": "Group", "data": {"name": "SOC Team"}}
       |
       | {"type": "User", "data": {"id": 3}}
   * - associatedCases
     - A list of Cases associated to the Case
     - Case Object
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Hacker Investigation", "status": "Open", "severity": "Low"}]}
   * - associatedGroups
     - A list of Groups associated to the Case
     - `Group Object <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Bad Adversary", "type": "Adversary"}]}
   * - associatedIndicators
     - A list of Indicators associated to the Case
     - `Indicator Object <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"ip":"66.96.146.129", "type": "Address"}]}
   * - attributes [1]_
     - A list of Attributes added to the Case
     - `Case Attribute Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/case_attributes/case_attributes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"type": "Attribute Type", "value": "Attribute Value", "source": "Attribute Source"]}}
   * - caseCloseTime
     - The date and time the Case was closed
     - Date
     - FALSE
     - TRUE
     - "2021-04-30T00:00:00Z"
   * - caseDetectionTime
     - The date and time a security incident or threat was detected (e.g., by a security team)
     - Date
     - FALSE
     - TRUE
     - "2021-04-30T00:00:00Z"
   * - caseOccurrenceTime
     - The date and time a security incident or threat occurred
     - Date
     - FALSE
     - TRUE
     - "2021-04-30T00:00:00Z"
   * - caseOpenTime
     - The date and time the Case was opened
     - Date
     - FALSE
     - TRUE
     - "2021-04-30T00:00:00Z"
   * - description
     - A description of the Case
     - String
     - FALSE
     - TRUE
     - "This Case is an investigation of a high-level hacker incident that occurred on critical systems."
   * - name
     - The name of the Case
     - String
     - TRUE
     - TRUE
     - "Hacker Investigation"
   * - notes
     - A list of Notes added to the Case
     - `Note Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/notes/notes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"text": "Upload all relevant research performed for this Case to the SOC Team shared drive."}]}
   * - resolution [2]_
     - The resolution of the Case
     - String
     - FALSE
     - TRUE
     - "Containment Achieved", "False Positive"
   * - severity [3]_
     - The severity of the Case (accepted values include "Low", "Medium", "High", and "Critical")
     - String
     - TRUE
     - TRUE
     - "Low", "Medium", "High", "Critical"
   * - status [4]_
     - The status of the Case (accepted values include "Open" and "Closed")
     - String
     - TRUE
     - TRUE
     - "Open", "Closed"
   * - tags
     - A list of Tags applied to the Case
     - `Tag Object <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_
     - FALSE
     - TRUE
     - {"data": [{"name": "Phishing"}]}
   * - tasks
     - A list of Tasks added to the Case
     - `Task Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/tasks/tasks.html>`_
     - FALSE
     - TRUE
     - {"data": [{"name": "Investigate Phishing Email", "workflowPhase": 1, "workflowStep": 1}]}
   * - userAccess
     - A list of users that, when defined, are the only ones allowed to view and edit the Case
     - `User Object <https://docs.threatconnect.com/en/latest/rest_api/v3/users/users.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"userName": "jsmith@threatconnect.com"}]}
       |
       | {"data": [{"id": 3}]}
   * - workflowEvents
     - A list of Timeline Events for the Case
     - `Workflow Event Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/workflow_events/workflow_events.html>`_
     - FALSE
     - TRUE
     - {"data": [{"summary": "Case created via API", "eventDate": "2021-08-12T12:30:12Z"}]}
   * - workflowTemplate
     - The Workflow applied to the Case
     - `Workflow Template Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/workflow_templates/workflow_templates.html>`_
     - FALSE
     - TRUE
     - | {"name": "Phishing Email Analysis"}
       |
       | {"id": 12345}

.. [1] Attribute Types for Cases must first be created at the System- or Organization-level before you can add Attributes to a Case, as detailed in the `Creating Custom Attribute Types <https://knowledge.threatconnect.com/docs/creating-custom-attribute-types>`_ knowledge base article. To retrieve a list of available `Attribute Types <https://docs.threatconnect.com/en/latest/rest_api/v3/attribute_types/attribute_types.html>`_ and determine whether an Attribute Type applies to Cases, send the following request and then review the ``attributeTypeMappings`` field included in the response: ``GET /v3/attributeTypes?fields=mapping``.

.. [2] The following are accepted values for the ``resolution`` field:

    - ``Containment Achieved``
    - ``Deferred / Delayed``
    - ``Escalated``
    - ``False Positive``
    - ``In Progress / Investigating``
    - ``Not Specified``
    - ``Rejected``
    - ``Restoration Achieved``

.. [3] The following are accepted values for the ``severity`` field:

    - ``Low``
    - ``Medium``
    - ``High``
    - ``Critical``

.. [4] The following are accepted values for the ``status`` field:

    - ``Open``
    - ``Closed``