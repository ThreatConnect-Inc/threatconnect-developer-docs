Retrieve Workflow Templates
---------------------------

Retrieve All Workflow Templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Workflow Templates, use the following query:

.. code::

    GET /v3/workflowTemplates

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "Example Template",
                "description": "A description for this Workflow Template.",
                "active": false,
                "version": 1,
                "configAttribute": [{
                    "attributeTypeId": 86
                }]
            },
            {
                "id": 2,
                "name": "Demo Template with Tasks",
                "configTask": [
                    {
                        "configPlaybook": null,
                        "fields": [],
                        "name": "Create a Meeting Notes folder",
                        "workflowId": 2,
                        "workflowPhase": 1,
                        "workflowStep": 1,
                        "assignee": {
                            "displayName": "Pat Jones",
                            "id": 2,
                            "name": "pjones+analyst@threatconnect.com",
                            "type": "User",
                            "ownerId": 7,
                            "superUser": false,
                            "firstName": "Pat",
                            "lastName": "Jones"
                        },
                        "duration": 2
                    },
                    {
                        "configPlaybook": null,
                        "fields": [
                            {
                                "artifactType": "Email Address",
                                "dataType": "String",
                                "intelType": "indicator-EmailAddress",
                                "name": "emailAddress",
                                "required": true,
                                "uiElement": "String",
                                "uiLabel": "Email Address"
                            },
                            {
                                "artifactType": "Email Subject",
                                "dataType": "String",
                                "intelType": "indicator-Email Subject",
                                "name": "emailSubject",
                                "required": true,
                                "uiElement": "String",
                                "uiLabel": "Email Subject"
                            }
                        ],
                        "name": "Analyze Email",
                        "workflowId": 2,
                        "workflowPhase": 2,
                        "workflowStep": 2,
                        "assignee": null,
                        "dependentOnTaskName": "Confirm Receipt of Email",
                        "duration": 3
                    },
                    {
                        "configPlaybook": null,
                        "fields": [],
                        "name": "Confirm Receipt of Email",
                        "workflowId": 2,
                        "workflowPhase": 2,
                        "workflowStep": 1,
                        "assignee": null
                    }
                ],
                "active": true,
                "version": 1
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Single Workflow Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Workflow Template, use a query in the following format:

.. code::

    GET /v3/workflowTemplates/{workflowTemplateId}

For example, the following query will return information about the Workflow template with ID 1:

.. code::

    GET /v3/workflowTemplates/1

JSON Response:

.. code:: json

    {
        "data": {
            "id": 1,
            "name": "Example Template",
            "description": "A description for this Workflow Template.",
            "active": false,
            "version": 1,
            "configAttribute": [{
                "attributeTypeId": 86
            }]
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
