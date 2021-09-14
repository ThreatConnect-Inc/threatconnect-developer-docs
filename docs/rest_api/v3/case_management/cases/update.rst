Update Cases
------------

To update a Case, the basic format is:

.. code::

    PUT /v3/cases/{caseID}
    {
        {updatedField}: {updatedValue}
    }

Refer to the following table for a list of available fields that can be updated for the ``cases`` object:

+----------------+----------+------------------------------------------------------------------------+
| Field          | Type     | Example Value(s)                                                       |
+================+==========+========================================================================+
| assignee       | String   | "{"type": "User", "data": {"userName": "jonsmith@threatconnect.com"}}" |
+----------------+----------+------------------------------------------------------------------------+
| description    | String   | "New case description"                                                 |
+----------------+----------+------------------------------------------------------------------------+
| name           | String   | "New Case"                                                             |
+----------------+----------+------------------------------------------------------------------------+
| resolution     | String   | "Containment Achieved", "False Positive"                               |
+----------------+----------+------------------------------------------------------------------------+
| severity       | String   | ""Low", "Medium", "High", or "Critical"                                |
+----------------+----------+------------------------------------------------------------------------+
| status         | String   | "Open", "Closed"                                                       |
+----------------+----------+------------------------------------------------------------------------+

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
        "dateAdded": "2021-04-09T14:41:27.622Z",
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
      },
      "message": "Updated",
      "status": "Success"
    }