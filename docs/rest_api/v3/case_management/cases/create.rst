Create Cases
------------

The basic format for creating a Case is:

.. code::

    POST /v3/cases/
    {
      "name": "Case name",
      "status": "Case status",
      "severity": "Case severity"
    }

Refer to the following table for a list of available fields for the ``cases`` object:

+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| Field               | Description                                     | Required  | Type    | Example Value(s)                                                        |
+=====================+=================================================+===========+=========+=========================================================================+
| artifacts           | A list of Artifacts corresponding to the Case   | FALSE     | String  | {"data": [{"summary": "badguy@bad.com", "type": "Email Address"}]}      |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| assignee            | The user or group Assignee object for the Case  | FALSE     | String  | {"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}    |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| attributes          | A list of Attributes corresponding to the Case  | FALSE     | String  | {"data": [{"type": "Case Attribute Name",                               |
|                     |                                                 |           |         | "value": "Case Attribute Value", "source": "Case Attribute Source"}]}   |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| caseCloseTime       | The date and time a Case was closed             | FALSE     | Date    | "2021-04-30T00:00:00Z"                                                  |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| caseDetectionTime   | The date and time a security incident or        | FALSE     | Date    | "2021-04-30T00:00:00Z"                                                  |
|                     | threat was detected (e.g., by a security team)  |           |         |                                                                         |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| caseOccurrence Time | The date and time a security incident or        | FALSE     | Date    | "2021-04-30T00:00:00Z"                                                  |
|                     | threat occurred                                 |           |         |                                                                         |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| caseOpenTime        | The date and time a Case was opened             | FALSE     | Date    | "2021-04-30T00:00:00Z"                                                  |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| description         | A description of the Case                       | FALSE     | String  | "New case description"                                                  |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| name                | The name of the Case                            | TRUE      | String  | "New Case"                                                              |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| notes               | A list of Notes corresponding to the Case       | FALSE     | String  | {"data": [{"text": "Note about malware case"}]}                         |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| resolution          | The resolution of the Case                      | FALSE     | String  | "Containment Achieved", "False Positive"                                |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| severity            | The severity of the Case. Valid values are      | TRUE      | String  | ""Low", "Medium", "High", or "Critical"                                 |
|                     | "Low", "Medium", "High", or "Critical"          |           |         |                                                                         |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| status              | The status of the Case                          | TRUE      | String  | "Open", "Closed"                                                        |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| tags                | A list of Tags corresponding to the Case        | FALSE     | String  | {"data": [{"name": "Phishing"}]}                                        |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| tasks               | A list of Tasks corresponding to the Case       | FALSE     | String  | {"data": [{"name": "Investigate Phishing Email", "workflowPhase": 1,    |
|                     |                                                 |           |         | "workflowStep": 1}]}                                                    |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| userAccess          | A list of users that, when defined, are the     | FALSE     | String  | {"data": [{"userName": "jsmith@threatconnect.com"}]}                    |
|                     | only ones allowed to view or edit the Case      |           |         |                                                                         |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| workflowEvents      | A list of Timeline events corresponding to      | FALSE     | String  | {"data": [{"summary": "Case created via API", "eventDate":              |
|                     | the Case                                        |           |         | "2021-08-12T12:30:12Z"}]}                                               |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+
| workflowTemplate    | The Workflow Template applied to the Case       | FALSE     | String  | {"name": "Example Workflow Template"}                                   |
+---------------------+-------------------------------------------------+-----------+---------+-------------------------------------------------------------------------+

.. note::
    Attribute Types for Cases must first be created in the System or Organization in which a Case resides before they can be added to the Case. See the `Creating Custom Attribute Types <https://training.threatconnect.com/learn/article/creating-custom-attributes-kb-article>`_ knowledge base article for more information.

.. include:: ../_includes/case_resolutions.rst

.. note::
    Setting the ``tags`` field will replace any existing tag(s) with the one(s) specified.

For example, the following query will create a Case named ``Example Workflow Case`` that has a severity of ``Low``, has a status of ``Open``, and is assigned to ``jonsmith@threatconnect.com``:

.. code::

    POST /v3/cases/
    {
      "assignee": {"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}},
      "name": "Example Workflow Case",
      "severity": "Low",
      "status": "Open"
    }

JSON Response:

.. code:: json

    {
    "data": {
        "id": 1,
        "xid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        "name": "Example Workflow Case",
        "dateAdded": "2021-04-09T14:41:27Z",
        "caseOpenTime": "2021-04-09T14:41:27.27Z",
        "caseOpenUser": {
            "id": 3,
            "userName": "11112222333344445555",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "jsmithAPI",
            "role": "Api User"
        },
        "status": "Open",
        "severity": "Low",
        "resolution": "Not Specified",
        "assignee": {
          "type": "User",
          "data": {
            "id": 1,
            "userName": "jonsmith@threatconnect.com",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "johnsmith",
            "role": "User"
          }
        },
        "tasks": {
          "count": 0,
        },
        "artifacts": {
          "count": 0,
        },
        "notes": {
          "count": 0,
        },
        "userAccess": {
          "count": 0,
        },
        "createdBy": {
          "id": 3,
          "userName": "11112222333344445555",
          "firstName": "John",
          "lastName": "Smith",
          "pseudonym": "jsmithAPI",
          "role": "Api User"
        },
        "owner": "Example Organization",
        "attributes": {
          "count": 0,
        },
      },
      "message": "Created",
      "status": "Success"
    }
