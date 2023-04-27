Retrieve Workflow Templates
---------------------------

Retrieve All Workflow Templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Workflow Templates:

.. code::

    GET /v3/workflowTemplates

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 1,
                "name": "Example Workflow",
                "description": "This is an example Workflow.",
                "active": false,
                "version": 1,
                "configAttribute": [
                    {
                        "attributeTypeId": 271
                    }
                ]
            },
            {
                "id": 2,
                "name": "Email Analysis",
                "description": "Workflow for analyzing suspicious emails.",
                "configTask": [
                    {
                        "configPlaybook": null,
                        "fields": [],
                        "name": "Create a Meeting Notes folder",
                        "required": true,
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
                        "durationType": "Hours",
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
                        "description": "Perform analysis of suspicious email.",
                        "required": true,
                        "workflowId": 2,
                        "workflowPhase": 2,
                        "workflowStep": 2,
                        "workflowStep": 1,
                        "assignee": {
                            "displayName": "SOC Team",
                            "id": 1,
                            "name": "SOC Team",
                            "type": "Group",
                            "ownerId": 7,
                            "superUser": false
                        },
                        "dependentOnTaskName": "Confirm Receipt of Email",
                        "durationType": "Days",
                        "duration": 3
                    },
                    {
                        "configPlaybook": null,
                        "fields": [],
                        "name": "Confirm Receipt of Email",
                        "required": false,
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


Retrieve a Specific Workflow Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Workflow Template:

.. code::

    GET /v3/workflowTemplates/{workflowTemplateId}

For example, the following request will retrieve data for the Workflow Template whose ID is 3:

.. code::

    GET /v3/workflowTemplates/3

JSON Response:

.. code:: json

    {
        "data": {
            "id": 3,
            "name": "Phishing Investigation Workflow",
            "description": "Workflow for phishing investigations.",
            "active": false,
            "version": 1
        },
        "status": "Success"
    }