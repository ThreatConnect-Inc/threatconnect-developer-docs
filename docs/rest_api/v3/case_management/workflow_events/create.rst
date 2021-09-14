Create Workflow Events
----------------------

The most basic format for creating a Workflow Event is:

.. code::

    POST /v3/workflowEvents/
    {
      "caseId": 1,
      "caseXid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
      "summary": "Summary of the Workflow Event"
    }

Some Workflow Event types require additional fields when being created. Refer to the following table for a list of available fields for the ``workflowEvents`` object:

+---------------+----------------------------------------------+----------+----------+---------------------------------------------------------+
| Field         | Description                                  | Required | Type     | Example Value(s)                                        |
+===============+==============================================+==========+==========+=========================================================+
| caseId        | The ID of the Case that contains the Event   | TRUE     | Integer  | 1, 2, 3                                                 |
+---------------+----------------------------------------------+----------+----------+---------------------------------------------------------+
| caseXid       | The XID of the Case that contains the Event  | TRUE     | String   | "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1"                  |
+---------------+----------------------------------------------+----------+----------+---------------------------------------------------------+
| eventDate     | The time that the Event is logged            | FALSE    | Date     | "2021-04-30T00:00:00Z"                                  |
+---------------+----------------------------------------------+----------+----------+---------------------------------------------------------+
| notes         | A list of Notes corresponding to the Event   | FALSE    | String   | "{"data": [{"text": "Note for New Workflow Event"}]}}"  |
+---------------+----------------------------------------------+----------+----------+---------------------------------------------------------+
| summary       | The summary of the Event                     | TRUE     | String   | "Workflow Event Summary"                                |
+---------------+----------------------------------------------+----------+----------+---------------------------------------------------------+

For example, the following query will create a Workflow Event with a summary of "Updated Case name" for the Case with ID 1.

.. code::

    POST /v3/workflowEvents/
    {
      "caseId": 1,
      "caseXid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
      "summary": "Updated Case name"
    }

JSON Response:

.. code:: json

    {
      "data": {
        "id": 4,
        "eventDate": "2021-03-05T14:54:31Z",
        "dateAdded": "2021-03-05T14:54:31Z",
        "summary": "Updated Case name",
        "systemGenerated": False
      },
      "message": "Created",
      "status": "Success"
    }

.. note:: Creating a Workflow Event only adds an Event to the Case's Timeline. It does not perform the action indicated in the Event's summary.