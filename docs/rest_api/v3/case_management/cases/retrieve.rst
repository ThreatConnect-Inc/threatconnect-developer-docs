Retrieve Cases
--------------

Retrieve All Cases
^^^^^^^^^^^^^^^^^^

To retrieve all Cases, use the following query:

.. code::

    GET /v3/cases/

JSON Response:

.. code:: json

    {
      "data": [{
        "id": 1,
        "xid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        "name": "Example Workflow Case",
        "dateAdded": "2021-04-09T14:41:27.622Z",
        "status": "Open",
        "severity": "Low",
        "resolution": "Not Specified",
        "createdBy": {
          "id": 3,
          "userName": "11112222333344445555",
          "firstName": "John",
          "lastName": "Smith",
          "pseudonym": "jsmithAPI",
          "role": "Api User"
        },
        "owner": "Example Organization",
      }, {
        "id": 2,
        "xid": "b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2",
        "name": "Malware Invesigation",
        "description": "Case to investigate new malware",
        "dateAdded": "2021-03-25T18:56:22Z",
        "status": "Open",
        "severity": "Critical",
        "resolution": "Not Specified",
        "createdBy": {
          "id": 2,
          "userName": "pjones+analyst@threatconnect.com",
          "firstName": "Patrick",
          "lastName": "Jones",
          "pseudonym": "patjones"
        },
        "owner": "Example Organization"
      }],
      "count": 2,
      "status": "Success"
    }

Retrieve a Single Case
^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Case, use a query in the following format:

.. code::

    GET /v3/cases/{caseID}

For example, the following query will return information about the Case with ID 3:

.. code::

    GET /v3/cases/3

JSON Response:

.. code:: json

    {
      "data": {
        "id": 3,
        "xid": "c3c3c3c3-c3c3-c3c3-c3c3-c3c3c3c3c3c3",
        "name": "Phishing Investigation",
        "description": "Case to investigate new phishing threat",
        "dateAdded": "2021-04-09T14:41:27.622Z",
        "status": "Open",
        "severity": "Medium",
        "resolution": "Not Specified",
        "assignee": {
          "type": "User",
          "data": {
            "id": 1,
            "userName": "jsmith@threatconnect.com",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "johnsmith",
            "role": "User"
          }
        },
        "createdBy": {
          "id": 1,
          "userName": "jsmith@threatconnect.com",
          "firstName": "John",
          "lastName": "Smith",
          "pseudonym": "johnsmith"
        },
        "owner": "Example Organization"
      },
      "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned Case, refer to the `Request Additional Fields for Returned Objects <../additional_fields.html>`__ section in this documentation.

Filter Results
^^^^^^^^^^^^^^

To filter returned Cases using ThreatConnect Query Language (TQL), refer to the `Filter Results with TQL <../filter_results.html>`__ section in this documentation.
