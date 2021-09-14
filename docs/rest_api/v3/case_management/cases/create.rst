Create Cases
-------------

The most basic format for creating a Case is:

.. code::

    POST /v3/cases/
    {
      "name": "Case name",
      "status": "Case status",
      "severity": "Case severity"
    }

Refer to the following table for a list of available fields for the ``cases`` object:

+----------------+----------+----------+-------------------------------------------------------------------------+
| Field          | Required | Type     | Example Value(s)                                                        |
+================+==========+==========+=========================================================================+
| assignee       | FALSE    | String   | "{"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}"  |
+----------------+----------+----------+-------------------------------------------------------------------------+
| description    | FALSE    | String   | "New case description"                                                  |
+----------------+----------+----------+-------------------------------------------------------------------------+
| name           | TRUE     | String   | "New Case"                                                              |
+----------------+----------+----------+-------------------------------------------------------------------------+
| resolution     | FALSE    | String   | "Containment Achieved", "False Positive"                                |
+----------------+----------+----------+-------------------------------------------------------------------------+
| severity       | TRUE     | String   | ""Low", "Medium", "High", or "Critical"                                 |
+----------------+----------+----------+-------------------------------------------------------------------------+
| status         | TRUE     | String   | "Open", "Closed"                                                        |
+----------------+----------+----------+-------------------------------------------------------------------------+

.. include:: ../_includes/case_resolutions.rst

For example, the following query will create a Case named ``Example Workflow Case`` that has a severity of ``Low``, has a status of ``Open``, and is assigned to ``jonsmith@threatconnect.com``:

.. code::

    POST /v3/cases/
    {
      "assignee": "{"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}",
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
        "dateAdded": "2021-04-09T14:41:27.622Z",
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
      },
      "message": "Created",
      "status": "Success"
    }
