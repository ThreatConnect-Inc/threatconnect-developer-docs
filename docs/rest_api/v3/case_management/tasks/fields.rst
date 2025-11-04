Endpoint Options
----------------

Available Fields
^^^^^^^^^^^^^^^^

Send the following request to `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_, including each field's name, description, and accepted data type, that can be included in the body of a POST or PUT request to the ``/v3/tasks`` endpoint:

.. code::

    OPTIONS /v3/tasks

.. hint::
    To include read-only fields in the response, append ``?show=readonly`` to the end of the request URL.

Alternatively, refer to the following table for a list of available fields that can be included in the body of a POST or PUT request to the ``/v3/tasks`` endpoint.

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
     - A list of Artifacts associated with the Task
     - `Artifact Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html>`_
     - FALSE
     - TRUE
     - {"data": [{"summary": "badguy@bad.com", "type": "Email Address"}]}
   * - assignee
     - The user or group Assignee object for the Task
     - Assignee Object
     - FALSE
     - TRUE
     - | {"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}
       |
       | {"type": "Group", "data": {"name": "SOC Team"}}
       |
       | {"type": "None"}
   * - caseId
     - The ID of the Case that contains the Task
     - Integer
     - TRUE [1]_
     - FALSE
     - 1, 2, 3
   * - caseXid
     - The XID of the Case that contains the Task
     - String
     - TRUE [1]_
     - FALSE
     - "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"
   * - completedDate
     - The completion date of the Task
     - Date
     - FALSE
     - TRUE
     - "2021-04-30T00:00:00Z"
   * - dependentOnId
     - The ID of another Task on which the Task is dependent
     - Integer
     - FALSE
     - TRUE
     - 1, 2, 3
   * - description
     - The description of the Task
     - String
     - FALSE
     - TRUE
     - "Example task description."
   * - dueDate
     - The date and time when the Task is due
     - Date
     - FALSE
     - TRUE
     - "2021-04-30T10:30:00Z"
   * - name
     - The name of the Task
     - String
     - TRUE
     - TRUE
     - "Example Task"
   * - notes
     - A list of Notes corresponding to the Task
     - `Note Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/notes/notes.html>`_
     - FALSE
     - TRUE
     - {"data": [{"text": "Note about Task"}]}
   * - required
     - Indicates whether the Task is required
     - Boolean
     - FALSE
     - TRUE
     - true, false
   * - status
     - The status of the Task (accepted values include "Pending", "Open", "Reopened", or "Closed")
     - String
     - FALSE
     - TRUE
     - "Pending", "Open", "Reopened", or "Closed"
   * - workflowPhase
     - The Workflow Phase where the Task takes place
     - Integer
     - FALSE
     - FALSE
     - 1, 2, 3
   * - workflowStep
     - The Workflow step where the Task takes place
     - Integer
     - FALSE
     - FALSE
     - 1, 2, 3

.. [1] When adding a Task to a Case, you must include either the ``caseId`` or ``caseXid`` field in the body of the POST request. Only one needs to be included in the body of the POST request, but both can be included, if desired.

Include Additional Fields in Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating, retrieving, or updating data, you can use the ``fields`` query parameter to `include additional fields in the API response that are not included by default <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Send the following request to retrieve a list of fields you can include in responses returned from the ``/v3/tasks`` endpoint:

.. code::

    OPTIONS /v3/tasks/fields

Filter Results
^^^^^^^^^^^^^^

When retrieving data, you can use the ``tql`` query parameter to `filter results with ThreatConnect Query Language (TQL) <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.

Send the following request to retrieve a list of valid TQL parameters you can use when including the ``tql`` query parameter in a request to the ``/v3/tasks`` endpoint:

.. code::

    OPTIONS /v3/tasks/tql