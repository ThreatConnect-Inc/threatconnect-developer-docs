Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/cases`` endpoint, including each field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/cases

.. hint::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

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
     - A list of Artifacts corresponding to the Case
     - `Artifact Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html>`_
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Bad Adversary", "type": "Adversary"}]}
   * - assignee
     - The user or user group assigned to the Case
     - Assignee Object
     - FALSE
     - TRUE
     - | {"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}
       |
       | {"type": "Group", "data": {"name": "SOC Team"}}
   * - associatedCases
     - A list of Cases associated to the Case
     - Case Object
     - FALSE
     - TRUE
     - | {"data": [{"id": 12345}]}
       |
       | {"data": [{"name": "Hacker Investigation", "status": "Open", "severity": "Low" }]}
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
       | {"data": [{"hostName":"badguy.com", "type": "Host"}]}
   * - attributes
     - A list of Attributes corresponding to the Case
     - `Case Attribute Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/case_attributes/case_attributes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"type": "Case Attribute Name", value": "Case Attribute Value", "source": "Case Attribute Source"}]}
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
     - A list of Notes corresponding to the Case
     - `Note Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/notes/notes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"text": "Note about malware case"}]}
   * - resolution
     - The resolution of the Case
     - String
     - FALSE
     - TRUE
     - "Containment Achieved", "False Positive"
   * - severity
     - The severity of the Case (accepted values include "Low", "Medium", "High", and "Critical")
     - String
     - TRUE
     - TRUE
     - "Low", "Medium", "High", "Critical"
   * - status
     - The status of the Case (accepted values include "Open" and "Closed")
     - String
     - TRUE
     - TRUE
     - "Open", "Closed"
   * - tags
     - A list of Tags corresponding to the Case
     - `Tag Object <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_
     - FALSE
     - TRUE
     - {"data": [{"name": "Phishing"}]}
   * - tasks
     - A list of Tasks corresponding to the Case
     - `Task Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/tasks/tasks.html>`_
     - FALSE
     - TRUE
     - {"data": [{"name": "Investigate Phishing Email", "workflowPhase": 1, "workflowStep": 1}]}
   * - userAccess
     - A list of users that, when defined, are the only ones allowed to view or edit the Case
     - `User Object <https://docs.threatconnect.com/en/latest/rest_api/v3/users/users.html>`_
     - FALSE
     - TRUE
     - {"data": [{"userName": "jsmith@threatconnect.com"}]}
   * - workflowEvents
     - A list of Timeline Events corresponding to the Case
     - `Workflow Event Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/workflow_events/workflow_events.html>`_
     - FALSE
     - TRUE
     - {"data": [{"summary": "Case created via API", "eventDate": "2021-08-12T12:30:12Z"}]}
   * - workflowTemplate
     - The Workflow Template applied to the Case
     - `Workflow Template Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/workflow_templates/workflow_templates.html>`_
     - FALSE
     - TRUE
     - | {"name": "Example Workflow Template"}
       |
       | {"id": 12345}

.. include:: ../_includes/case_resolutions.rst

.. attention::
    Attribute Types for Cases must first be created in the System or Organization in which a Case resides before they can be added to the Case. See the `Creating Custom Attribute Types <https://training.threatconnect.com/learn/article/creating-custom-attributes-kb-article>`_ knowledge base article for more information.

.. hint::
    To **associate an existing Case or Group** to a Case, use the object's ID when setting the ``associatedCases`` or ``associatedGroups`` field, respectively (e.g., ``{"data": [{"id": 12345}]}``). To **associate an existing Indicator** to a Case, use either the Indicator's ID, or the Indicator's type and summary (e.g., for a Host Indicator, use its ``hostName``), when setting the ``associatedIndicators`` field.