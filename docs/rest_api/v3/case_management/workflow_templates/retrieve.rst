Retrieve Workflow Templates
---------------------------

Retrieve All Workflow Templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Workflow Templates, use the following query:

.. code::

    GET /v3/workflowTemplates/

JSON Response:

.. code:: json

    {
      "data": [{
        "id": 1,
          "name": "Example Workflow Template",
          "description": "A description for this Workflow Template.",
          "active": False,
          "version": 1
        }, {
          "id": 2,
          "name": "Phishing Analysis Template",
          "configTask": [{
            "configPlaybook": None,
            "fields": [],
            "name": "Analyze phishing email",
            "description": "Analyze phishing email",
            "required": True,
            "workflowPhase": 1,
            "workflowStep": 1,
            "assignee": None
        }, {
         "configPlaybook": None,
         "fields": [{
            "artifactType": "Email Subject",
            "dataType": "String",
            "intelType": "indicator-Email Subject",
            "name": "helloSubject",
            "required": False,
            "uiElement": "String",
            "uiLabel": "Subject Line"
            }, {
            "artifactType": "Email Body",
            "dataType": "String",
            "name": "helloBody",
            "required": True,
            "uiElement": "String",
            "uiLabel": "Email Body"
            }],
            "name": "Gather the subject line and email body",
            "description": "Description ",
            "required": True,
            "workflowPhase": 1,
            "workflowStep": 2,
            "assignee": {
                "id": None
            },
            "dependentOnTaskName": "Analyze Phishing Email"
        }, {
            "configPlaybook": "{"playbookApp":{"name":"Example Workflow Escalation Demo","type":"Workflow","version":"1.1.0","updated":"2021-03-15T14:54:36.000Z","programName":"e974ff4b663ee7ac4a126793957305b5","id":619},"automatic":false,"io":{"inputs":[{"name":"escalationSubject","value":"${WORKFLOW:Gather the subject line and email body:helloSubject}"},{"name":"esclationBody","value":"${WORKFLOW:Gather the subject line and email body:helloBody}"}],"outputs":[{"intelTypes":[],"name":"emailReceipient","dataType":"String","optional":true,"failOnError":true,"artifactName":"helloRecipient","artifactType":"Email Address"}]}}",
            "fields": [],
            "name": "Send Escalation Email",
            "description": "Notify Manager",
            "required": False,
            "workflowId": 13,
            "workflowPhase": 2,
            "workflowStep": 1,
            "assignee": {
                "id": None
            },
            "dependentOnTaskName": "Gather the subject line and email body"
        }],
        "active": True,
        "version": 1
        }],
      "count": 2,
      "status": "Success"
    }

Retrieve a Single Workflow Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Workflow Template, use a query in the following format:

.. code::

    GET /v3/workflowTemplates/{workflowTemplateID}

For example, the following query will return information about the Workflow template with ID 1:

.. code::

    GET /v3/workflowTemplates/1

JSON Response:

.. code:: json

    {
      "data": {
          "id": 1,
          "name": "Example Workflow Template",
          "description": "A description for this Workflow Template.",
          "active": False,
          "version": 1,
      },
      "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned Workflow Template, refer to the `Request Additional Fields for Returned Objects <../additional_fields.html>`__ section in this documentation.

Filter Results
^^^^^^^^^^^^^^

To filter returned Workflow Templates using ThreatConnect Query Language (TQL), refer to the `Filter Results with TQL <../filter_results.html>`__ section in this documentation.
