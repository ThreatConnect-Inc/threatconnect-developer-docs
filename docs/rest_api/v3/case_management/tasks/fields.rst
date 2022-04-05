Available Fields
----------------

You can `retrieve a list of available fields <https://docs.threatconnect.com/en/latest/rest_api/v3/retrieve_fields.html>`_ for the ``/v3/tasks`` endpoint, including the field's name, description, and accepted data type, by using the following query:

.. code::

    OPTIONS /v3/tasks

.. note::
    To view all fields, including read-only fields, include the ``?show=readonly`` query parameter.

Alternatively, refer to the following tables for a list of available fields that can be included in the body of a POST or PUT request for the ``tasks`` object.

.. list-table::
   :widths: 20 20 10 15 15 20
   :header-rows: 1

   * - Field
     - Description
     - Type
     - Required for Creation?
     - Updatable?
     - Example value(s)
   * - artifacts
     - A list of Artifacts associated with the Task
     - `Artifact Object <https://docs.threatconnect.com/en/latest/rest_api/v3/case_management/artifacts/artifacts.html>`_
     - FALSE
     - TRUE
     - {"data": [{"summary": "badguy@bad.com", "type": "Email Address"]}}
   * - assignee
     - The user or group Assignee object for the Task
     - Assignee Object
     - FALSE
     - TRUE
     - {"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}, {"type": "Group", "data": {"name": "SOC Team"}}
   * - caseId
     - The ID of the Case that contains the Task
     - Integer
     - TRUE*
     - FALSE
     - 1, 2, 3
   * - caseXid
     - The XID of the Case that contains the Task
     - String
     - TRUE*
     - FALSE
     - "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"
   * - completedDate
     - The completion date of the Task
     - Date
     - FALSE
     - TRUE
     - "2021-04-30T00:00:00Z"
   * - dependentOnId
     - The ID of another Task that this Task is dependent upon
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
   * - duration
     - The amount of time until the Task is due, which corresponds with the Task's durationType (e.g., 5 hours)
     - Integer
     - FALSE
     - TRUE
     - 1, 2, 3
   * - durationType
     - The unit of time that corresponds with the Task's duration. Accepted values include "Days", "Hours", and "Minutes"
     - String
     - FALSE
     - TRUE
     - "Days", "Hours", or "Minutes"
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
     - Flag indicating whether the Task is required
     - Boolean
     - FALSE
     - TRUE
     - true, false
   * - status
     - The status of the Task. Valid values are "Pending", "Open", "Reopened", or "Closed"
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
     - The step of the Workflow where the Task takes place
     - Integer
     - FALSE
     - FALSE
     - 1, 2, 3

.. note::
    When creating a Task, either ``caseId`` or ``caseXid`` must be included in the body of the POST request. Only one needs to be included in the body of the POST request, but both can be included, if desired.