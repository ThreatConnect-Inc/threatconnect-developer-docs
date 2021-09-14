Request Additional Fields for Returned Objects
----------------------------------------------

When retrieving all or specific Case objects, including Artifacts, Cases, Notes, Tasks, Workflow Events, and Workflow Templates, additional fields not automatically provided with each returned object can be requested. To request additional fields, include ``?fields=`` in the query parameter followed by the field name(s) you want to include.

.. note::If requesting multiple additional fields, separate each field with an ampersand. For example, to request the Assignees and Task fields, include ``?field=notes&fields=task`` in the query parameter.

For example, the following query will return information about the Artifact with ID 3, including a related Task and a related Note:

.. code::

    GET /v3/artifacts/3?fields=notes&fields=task

JSON Response:

.. code:: json

    {
      "data": {
        "id": 3,
        "summary": "URGENT - APPROVAL IS REQUIRED!!!",
        "type": "Email Subject",
        "fieldName": "helloSubject",
        "intelType": "indicator-Email Subject",
        "source": "patjones",
        "dateAdded": "2021-03-15T10:16:40Z",
        "task": {
          "id": 6,
          "xid": "f6f6f6f6-f6f6-f6f6-f6f6-f6f6f6f6f6f6",
          "name": "Investigate intel related to this case",
          "description": "Case description made via API",
          "configTask": [{
              "artifactType": "Email Address",
              "dataType": "String",
              "intelType": "indicator-EmailAddress",
              "name": "emailAddress",
              "required": False,
              "uiElement": "String",
              "uiLabel": "Email Address"
          }],
          "workflowPhase": 0,
          "workflowStep": 1,
          "required": False,
          "status": "Open"
        },
        "notes": {
          "data": [{
              "id": 5,
              "text": "An important note about this email subject.",
              "summary": "An important note about this email subject.",
              "author": "pjones@threatconnect.com",
              "dateAdded": "2021-04-23T12:39:12Z",
              "lastModified": "2021-04-23T12:39:12Z",
              "edited": False,
              "artifactId": 3
          }],
          "count": 1
        },
        "derivedLink": "True",
        "hashCode": "fec31a1f2937c37b110d467cf78c03d820954596"
      },
      "status": "Success"
    }

To view a list of available options to set in the ``?fields=`` query parameter for each Case object, use the following query:

.. code::

    OPTIONS /v3/{caseObject}/fields
