Create Artifacts
----------------

The basic format for creating an Artifact is:

.. code::

    POST /v3/artifacts/
    {
        "caseId": 1,
        "summary": "Summary of the data contained in the Artifact",
        "type": "The Artifact's data type"
    }

For example, the following query will create an ``Email Address`` Artifact with a summary of ``badguy@bad.com`` for the Case with ID 1, create a new Adversary Group named ``Bad Guy`` and associate it to the Artifact, and create a Note for the Artifact:

.. code::

    POST /v3/artifacts/
    {
        "caseId": 1,
        "summary": "badguy@bad.com",
        "type": "Email Address",
        "associatedGroups": {"data": [{"name": "Bad Guy", "type": "Adversary"}]}, 
        "notes": {"data": [{"text": "Note about this artifact"}]}
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 1,
            "summary": "badguy@badguy.com",
            "type": "Email Address",
            "intelType": "indicator-EmailAddress",
            "dateAdded": "2021-04-22T19:24:06Z",
            "notes": {
                "data": [
                    {
                        "id": 5,
                        "text": "Note about this artifact",
                        "summary": "Note about this artifact",
                        "author": "06086238053146319309",
                        "dateAdded": "2021-04-22T19:24:06Z",
                        "lastModified": "2021-04-22T19:24:06Z",
                        "edited": false,
                        "artifactId": 29571
                    }
                ]
            },
            "associatedGroups": {
                "data": [
                    {
                        "id": 356316,
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-04-22T19:24:06Z",
                        "webLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=356316",
                        "type": "Adversary",
                        "name": "Bad Guy",
                        "createdBy": {
                            "id": 3,
                            "userName": "11112222333344445555",
                            "firstName": "John",
                            "lastName": "Smith",
                            "pseudonym": "jsmithAPI",
                            "role": "Api User"
                        },
                        "lastModified": "2021-04-22T19:24:06Z"
                    }
                ]
            },
            "derivedLink": true,
            "hashCode": "a/mHEtrRoPrG9csrdltEY73kdKHihi2jow40V3WFYrU="
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request for the ``artifacts`` object.

.. note::
    When creating or updating an Artifact, you can associate Indicators and Groups that do not yet exist in ThreatConnect to the Artifact. To do so, fill out all required fields for the type of `Indicator <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_ or `Group <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_ being associated to the Artifact. Upon creation of the new Artifact, any associated objects included in the body of the POST request that do not yet exist in ThreatConnect will also be created. In addition, you can associate multiple Indicators and Groups to the Artifact being created in a single POST request.

.. hint::
    To create an Artifact that is displayed in the **Task Artifacts** section of a Task, the Artifact must be associated with a Task, the associated Task must have an Artifact Field defined that accepts the same Artifact data type as the associated Artifact, and the ``fieldname`` field must be defined. Otherwise, the Artifact will be displayed in the **Related Artifacts** section of the Task. For more information about Artifact Fields, see the "Artifact Fields" section of the `Workflow Cases: Phases and Tasks <https://training.threatconnect.com/learn/article/workflow-cases-phases-and-tasks-kb-article>`_ knowledge base article.