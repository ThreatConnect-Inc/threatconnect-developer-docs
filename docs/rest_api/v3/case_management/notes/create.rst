Create Notes
-------------

The most basic format for creating a Note is:

.. code::

    POST /v3/notes/
    {
      "caseId": 1,
      "caseXid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
      "text": "This is an example note."
    }

Refer to the following table for a list of available fields for the ``notes`` object:

+------------------+---------------------------------------------------+----------+----------+
| Field            | Description                                       | Required | Type     |
+==================+===================================================+==========+==========+
| artifactId       | The ID of the Artifact on which to apply the Note | FALSE    | Integer  |
+------------------+---------------------------------------------------+----------+----------+
| caseId           | The ID of the Case on which to apply the Note     | TRUE     | Integer  |
+------------------+---------------------------------------------------+----------+----------+
| caseXid          | The XID of the Case on which to apply the Note    | TRUE     | String   |
+------------------+---------------------------------------------------+----------+----------+
| taskId           | The ID of the Task on which to apply the Note     | FALSE    | Integer  |
+------------------+---------------------------------------------------+----------+----------+
| taskXid          | The XID of the Task on which to apply the Note    | FALSE    | String   |
+------------------+---------------------------------------------------+----------+----------+
| text             | The contents of the Note itself                   | TRUE     | String   |
+------------------+---------------------------------------------------+----------+----------+
| workflowEventId  | The ID of the Event on which to apply the Note    | FALSE    | Integer  |
+------------------+---------------------------------------------------+----------+----------+
  
For example, the following query will create a Note for the Case with ID 1 and apply it to the Artifact with ID 4.

.. code::

    POST /v3/notes/
    {
      "caseId": 1,
      "caseXid": "aa1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
      "text": "Some notes about a case artifact.",
      "artifactId": 4
    }

JSON Response:

.. code:: json

    {
      "data": {
          "id": 1,
          "text": "Some notes about a case artifact.",
          "summary": "Some notes about a case artifact.",
          "author": "11112222333344445555",
          "dateAdded": "2021-04-22T20:17:15Z",
          "lastModified": "2021-04-22T20:17:15Z",
          "edited": False,
          "artifactId": 4
      },
      "message": "Created",
      "status": "Success"
    }
