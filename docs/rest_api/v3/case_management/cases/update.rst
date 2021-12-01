Update Cases
------------

The basic format for updating a Case is:

.. code::

    PUT /v3/cases/{caseID}
    {
        {updatedField}: {updatedValue}
    }

Refer to the following table for a list of available fields that can be updated for the ``cases`` object:

+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| Field               | Description                                     | Type    | Example Value(s)                                                        |
+=====================+=================================================+=========+=========================================================================+
| artifacts           | A list of Artifacts corresponding to the Case   | String  | {"data": [{"summary": "badguy@bad.com", "type": "Email Address"}]}      |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| assignee            | The user or group Assignee object for the Case  | String  | {"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}    |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| attributes          | A list of Attributes corresponding to the Case  | String  | {"data": [{"type": "Case Attribute Name",                               |
|                     |                                                 |         | "value": "Case Attribute Value", "source": " Case Attribute Source"}]}  |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| caseCloseTime       | The date and time a Case was closed             | Date    | "2021-04-30T00:00:00Z"                                                  |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| caseDetectionTime   | The date and time a security incident or        | Date    | "2021-04-30T00:00:00Z"                                                  |
|                     | threat was detected (e.g., by a security team)  |         |                                                                         |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| caseOccurrenceTime  | The date and time a security incident or        | Date    | "2021-04-30T00:00:00Z"                                                  |
|                     | threat occurred                                 |         |                                                                         |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| caseOpenTime        | The date and time a Case was opened             | Date    | "2021-04-30T00:00:00Z"                                                  |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| description         | A description of the Case                       | String  | "New case description"                                                  |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| name                | The name of the Case                            | String  | "New Case"                                                              |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| notes               | A list of Notes corresponding to the Case       | String  | {"data": [{"text": "Note about malware case"}]}                         |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| resolution          | The resolution of the Case                      | String  | "Containment Achieved", "False Positive"                                |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| severity            | The severity of the Case. Valid values are      | String  | ""Low", "Medium", "High", or "Critical"                                 |
|                     | "Low", "Medium", "High", or "Critical"          |         |                                                                         |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| status              | The status of the Case                          | String  | "Open", "Closed"                                                        |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| tags                | A list of Tags corresponding to the Case        | String  | {"data": [{"name": "Phishing"}]}                                        |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| tasks               | A list of Tasks corresponding to the Case       | String  | {"data": [{"name": "Investigate Phishing Email", "workflowPhase": 1,    |
|                     |                                                 |         | "workflowStep": 1}]}                                                    |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| userAccess          | A list of users that, when defined, are the     | String  | {"data": [{"userName": "jsmith@threatconnect.com"}]}                    |
|                     | only ones allowed to view or edit the Case      |         |                                                                         |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+
| workflowEvents      | A list of Timeline events corresponding to      | String  | {"data": [{"summary": "Case created via API", "eventDate":              |
|                     | the Case                                        |         | "2021-08-12T12:30:12Z"}]}                                               |
+---------------------+-------------------------------------------------+---------+-------------------------------------------------------------------------+

.. note::
    Attribute Types for Cases must first be created in the System or Organization in which a Case resides before they can be added to the Case. See the `Creating Custom Attribute Types <https://training.threatconnect.com/learn/article/creating-custom-attributes-kb-article>`_ knowledge base article for more information.

.. warning::
    Trying to add an Attribute to a Case when the Case Attribute Type's **Max Allowed** limit has been reached will result in an error.

.. include:: ../_includes/case_resolutions.rst
  
For example, the following query will update the resolution and status of the Case with ID 1:

.. code::

    PUT /v3/cases/1
    {
      "resolution": "False Positive",
      "status": "Closed"
    }

JSON Response:

.. code:: json

    {
      "data": {
        "id": 1,
        "xid": "aa1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        "name": "Example Workflow Case",
        "dateAdded": "2021-04-09T14:41:27.27Z",
        "caseOpenTime": "2021-04-09T14:41:27Z",
        "caseOpenUser": {
            "id": 3,
            "userName": "11112222333344445555",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "jsmithAPI",
            "role": "Api User"
        },
        "caseCloseTime": "2021-04-12T18:36.18Z",
        "caseCloseUser": {
            "id": 3,
            "userName": "11112222333344445555",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "jsmithAPI",
            "role": "Api User" 
        },
        "status": "Closed",
        "severity": "Medium",
        "resolution": "False Positive",
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
      "message": "Updated",
      "status": "Success"
    }
