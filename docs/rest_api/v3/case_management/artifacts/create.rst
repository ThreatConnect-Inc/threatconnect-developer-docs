Create Artifacts
----------------

The basic format for creating an Artifact is:

.. code::

    POST /v3/artifacts
    {
        "caseId": 1,
        "summary": "Summary of the data contained in the Artifact",
        "type": "The Artifact's data type"
    }

For example, the following query will create an ``Email Address`` Artifact with a summary of ``badguy@bad.com`` for the Case with ID 1, create a new Adversary Group named ``Bad Guy`` and associate it to the Artifact, and create a Note for the Artifact:

.. code::

    POST /v3/artifacts
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
                        "author": "11112222333344445555",
                        "dateAdded": "2021-04-22T19:24:06Z",
                        "lastModified": "2021-04-22T19:24:06Z",
                        "edited": false,
                        "artifactId": 1
                    }
                ]
            },
            "associatedGroups": {
                "data": [
                    {
                        "id": 13,
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-04-22T19:24:06Z",
                        "webLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=13",
                        "type": "Adversary",
                        "name": "Bad Guy",
                        "createdBy": {
                            "id": 3,
                            "userName": "11112222333344445555",
                            "firstName": "John",
                            "lastName": "Smith",
                            "pseudonym": "jsmithAPI",
                            "owner": "Demo Organization",
                            "systemRole": "Api User"
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
    To create an Artifact that is displayed in the **Task Artifacts** section of a Task, the following conditions must be met:

    - The Artifact must correspond to a Task;
    - The corresponding Task must have an **Artifact Field** that accepts the same data type as the Artifact;
    - The ``fieldname`` field must be defined when creating the Artifact.

    Otherwise, the Artifact will be displayed in the **Related Artifacts** section of the Task. For more information about Artifact Fields, see the "Artifact Fields" section of the `Adding Tasks to a Case <https://knowledge.threatconnect.com/docs/adding-tasks-to-a-case#artifact-fields>`_ knowledge base article.

Create Associations
^^^^^^^^^^^^^^^^^^^

In ThreatConnect, you can create associations between Artifacts in your Organization and Groups and Indicators in your Organization.

When creating associations for Artifacts using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Group, include `all fields required to create the type of Group <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html#available-fields>`_ when setting the ``associatedGroups`` field. The new Group will be created in the Organization to which your API user account belongs.
- To create an association to an existing Group, use the Group's ID when setting the ``associatedGroups`` field (e.g., ``"associatedGroups": {"data": [{"id": 12345}]}``).
- To create an association to a new Indicator, include `all fields required to create the type of Indicator <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#available-fields>`_ when setting the ``associatedIndicators`` field. The new Indicator will be created in the Organization to which your API user account belongs.
- To create an association to an existing Indicator, use the Indicator's ID, or its summary and type (e.g., ``"associatedIndicators": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``associatedIndicators`` field.

.. note::

    You can associate multiple Indicators and Groups to an Artifact in a single POST or PUT request.