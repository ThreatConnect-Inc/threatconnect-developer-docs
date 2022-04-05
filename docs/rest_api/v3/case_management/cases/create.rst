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

For example, the following query will create a Case named ``Example Workflow Case`` that has a severity of ``Low``, has a status of ``Open``, is assigned to ``jonsmith@threatconnect.com``, and includes an Artifact that is associated to an existing Indicator:

.. code::

    POST /v3/cases/
    {
        "artifacts": {"data": [{"summary": "badguy.com", "type": "Host", "associatedIndicators": {"data": [{"id": "2"}]}}]},
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
        "tasks": {},
        "artifacts": {
        "data": [
            {
                "id": 12,
                "summary": "badguy.com",
                "type": "Host",
                "intelType": "indicator-Host",
                "dateAdded": "2021-04-09T14:41:27.27Z",
                "derivedLink": true,
                "hashCode": "fTgtpcEQ4JMzFNpXBMhfyXue7s/DchX7uCWedTcqiqA="
            }
          ]
        },
        "notes": {},
        "userAccess": {},
        "createdBy": {
            "id": 3,
            "userName": "11112222333344445555",
            "firstName": "John",
            "lastName": "Smith",
            "pseudonym": "jsmithAPI",
            "role": "Api User"
        },
        "owner": "Example Organization",
        "ownerId": 7,
        "attributes": {},
        "associatedGroups": {},
        "associatedIndicators": {},
        "associatedCases": {}
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request for the ``artifacts`` object.

.. note::
    When creating or updating a Case, you can associate Cases, Indicators, and Groups that do not yet exist in ThreatConnect to the Case. To do so, fill out all required fields for the `type of Indicator <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_, `type of Group <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_, or Case being associated to the Case. Upon creation of the new Case, any associated objects included in the body of the POST request that do not yet exist in ThreatConnect will also be created. In addition, you can associate multiple Cases, Indicators, and Groups, as well as apply multiple `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_, to the Case being created in a single POST request.