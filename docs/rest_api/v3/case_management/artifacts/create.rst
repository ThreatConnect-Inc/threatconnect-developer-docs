Create Artifacts
----------------

The most basic format for creating an Artifact is:

.. code::

    POST /v3/artifacts/
    {
      "caseId": 1,
      "caseXid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
      "summary": "Summary of the data contained in the Artifact",
      "type": "The Artifact's data type"
    }

Some Artifact types require additional fields when being created. Refer to the following table for a list of available fields for the ``artifacts`` object:

+--------------+----------------------------------------------------+----------+----------+
| Field        | Description                                        | Required | Type     |
+==============+====================================================+==========+==========+
| caseId       | The ID of the Case that contains the Artifact      | TRUE     | Integer  |
+--------------+----------------------------------------------------+----------+----------+
| caseXid      | The XID of the Case that contains the Artifact     | TRUE     | String   |
+--------------+----------------------------------------------------+----------+----------+
| derivedLink  | Specifies whether the Artifact should be used to   | FALSE    | Boolean  |
|              | potentially associate Cases                        |          |          |
+--------------+----------------------------------------------------+----------+----------+
| fieldName    | The name of the Artifact Field within an           | FALSE    | String   |
|              | associated Task                                    |          |          |
+--------------+----------------------------------------------------+----------+----------+
| fileData     | Base64-encoded file attachment (required only      | FALSE    | String   |
|              | for certain Artifact types)                        |          |          |
+--------------+----------------------------------------------------+----------+----------+
| hashCode     | The hash code of File-type Artifacts               | FALSE    | String   |
+--------------+----------------------------------------------------+----------+----------+
| source       | The name of the user who entered the Artifact      | FALSE    | String   |
|              | into the Case                                      |          |          |
+--------------+----------------------------------------------------+----------+----------+
| summary      | The data contained in the Artifact                 | TRUE     | String   |
+--------------+----------------------------------------------------+----------+----------+
| taskId       | The ID of the Task that the Artifact references    | FALSE    | Integer  |
+--------------+----------------------------------------------------+----------+----------+
| taskXid      | The XID of the Task that the Artifact references   | FALSE    | String   |
+--------------+----------------------------------------------------+----------+----------+
| type         | The Artifact's data type                           | TRUE     | String   |
+--------------+----------------------------------------------------+----------+----------+

.. note:: To view a list of available Artifact data types, use the following query and refer to the ``type`` field: ``OPTIONS /v3/artifacts/``. Alternatively, refer to `Artifact Types <../artifact_types/artifact_types.html>`__ section in this documentation.

.. hint:: To create an Artifact that is displayed in the *Task Artifacts* section of a Task, the Artifact must be associated with a Task, the associated Task must have an Artifact Field defined that accepts the same Artifact data type as the associated Artifact, and the ``fieldname`` field must be defined. Otherwise, the Artifact will be displayed in the *Related Artifacts* section of the Task. For more information about Artifact Fields, see the "Artifact Fields" section of `Workflow Cases <https://training.threatconnect.com/learn/article/workflow-cases-kb-article>`__.

For example, the following query will create an Artifact with the data type ``Email Address`` and a summary of ``badguy@bad.com`` for the Case with ID 1.

.. code::

    POST /v3/artifacts/
    {
      "caseId": 1,
      "caseXid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
      "summary": "badguy@bad.com",
      "type": "Email Address"
    }

JSON Response:

.. code:: json

    {
      "data": {
          "id": 1,
          "summary": "badguy@bad.com",
          "type": "Email Address",
          "intelType": "indicator-EmailAddress",
          "dateAdded": "2021-04-22T19:24:06Z",
          "derivedLink": True,
          "hashCode": "bR3jGyx3DqnOrXQ/dI/pYeYOpGOgxalv64tymVN661M="
      },
      "message": "Created",
      "status": "Success"
    }
