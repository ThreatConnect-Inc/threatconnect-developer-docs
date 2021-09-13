Retrieve Workflow Tasks
-----------------------

Retrieve All Tasks
^^^^^^^^^^^^^^^^^^

To retrieve all Tasks, use the following query:

.. code::

    GET /v3/tasks/

JSON Response:

.. code:: json

    {
      "data": [{
        "id": 1,
        "name": "Create Shared Drive Folder for Case",
        "workflowPhase": 1,
        "workflowStep": 1,
        "required": False,
        "status": "Open"
      }, {
        "id": 2,
        "name": "Create Meeting Notes Folder",
        "description": "If Case listed a Severity of High or Critical, create a Meeting Notes folder inside the Case folder.",
        "workflowPhase": 1,
        "workflowStep": 2,
        "required": True,
        "status": "Open"
      }],
      "count": 2,
      "status": "Success"
    }

Retrieve a Single Task
^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Task, use a query in the following format:

.. code::

    GET /v3/tasks/{taskID}

For example, the following query will return information about the Task with ID 1:

.. code::

    GET /v3/tasks/1

JSON Response:

.. code:: json

    {
      "data": [{
        "id": 1,
        "name": "Create Shared Drive Folder for Case",
        "workflowPhase": 1,
        "workflowStep": 1,
        "required": False,
        "status": "Open"
      }],
      "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned Task, refer to the `Request Additional Fields for Returned Objects <../additional_fields.html>`__ section in this documentation.

Filter Results
^^^^^^^^^^^^^^

To filter returned Tasks using ThreatConnect Query Language (TQL), refer to the `Filter Results with TQL <../filter_results.html>`__ section in this documentation.
