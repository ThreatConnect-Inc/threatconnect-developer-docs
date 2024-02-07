Create Artifacts
----------------

The following example illustrates the basic format for creating an Artifact:

.. code::

    POST /v3/artifacts
    {
        "caseId": 1,
        "summary": "Summary of the data contained in the Artifact",
        "type": "The Artifact's data type"
    }

For example, the following request will add an Email Address Artifact with a summary of **badguy@bad.com** to the Case whose ID is 1. It will also complete the following actions for the Artifact:

- Create a new **Bad Guy** Adversary Group and associate it to the Artifact
- Add a Note to the Artifact

.. hint::
    To include the ``associatedGroups`` and ``notes`` fields in the API response, append ``?fields=associatedGroups&fields=notes`` to the end of the request URL.


.. code::

    POST /v3/artifacts
    {
        "caseId": 1,
        "summary": "badguy@bad.com",
        "type": "Email Address",
        "associatedGroups": {"data": [{"name": "Bad Guy", "type": "Adversary"}]}, 
        "notes": {"data": [{"text": "This email address belongs to a bad guy."}]}
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
            "derivedLink": true,
            "hashCode": "a/mHEtrRoPrG9csrdltEY73kdKHihi2jow40V3WFYrU="
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request to the ``/v3/artifacts`` endpoint.

.. note::
    To create an Artifact that is displayed in the **Task Artifacts** section when viewing the Task in the ThreatConnect UI, the following conditions must be met:

    - The Artifact must be added to a Task
    - The Task to which the Artifact is added must have an Artifact Field that accepts the Artifact's type
    - The ``fieldname`` field must be defined when creating the Artifact, and the value for this field must be the Task's Artifact Field that accepts the Artifact's type

    If these conditions are not met, the Artifact will be listed as a related Artifact when viewing the Task in the ThreatConnect UI. For more information about Artifact Fields, see the `"Artifact Fields" section of the Adding Tasks to a Case <https://knowledge.threatconnect.com/docs/adding-tasks-to-a-case#artifact-fields>`_ knowledge base article.