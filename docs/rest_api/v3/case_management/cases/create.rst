Create Cases
------------

The basic format for creating a Case is:

.. code::

    POST /v3/cases
    {
        "name": "Case name",
        "status": "Case status",
        "severity": "Case severity"
    }

For example, the following query will create a Case named ``Example Workflow Case`` that has a severity of ``Low``, has a status of ``Open``, is assigned to ``jonsmith@threatconnect.com``, and includes an Artifact that is associated to an existing Indicator:

.. code::

    POST /v3/cases
    {
        "artifacts": {"data": [{"summary": "badguy.com", "type": "Host", "associatedIndicators": {"data": [{"id": "2"}]}}]},
        "assignee": {"type": "User", "data": {"userName": "smithj@threatconnect.com"}},
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
                "owner": "Demo Organization",
                "systemRole": "Api User"
            },
            "status": "Open",
            "severity": "Low",
            "resolution": "Not Specified",
            "assignee": {
                "type": "User",
                "data": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "JMS",
                    "owner": "Demo Organization",
                    "systemRole": "Administrator"
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
                "owner": "Demo Organization",
                "systemRole": "Api User"
            },
            "owner": "Demo Organization",
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

   You can apply multiple `Tags <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_ to a Case in a single POST or PUT request. When setting the tags field, use a Tag's ID to apply an existing Tag to a Case, or include `all required fields to create a Tag <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html#available-fields>`_ to apply a new Tag to a Case.

Create Associations
^^^^^^^^^^^^^^^^^^^

In ThreatConnect, you can create associations between Cases in your Organization and Groups and Indicators in your Organization. If cross-owner associations are enabled on your ThreatConnect instance, you can also create associations between Groups and Indicators in Communities and Sources to which you have access and Cases in your Organization.

When creating associations for Cases using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Case, include `all fields required to create a Case <#available-fields>`_ when setting the ``associatedCases`` field. The new Case will be created in the Organization to which your API user account belongs.
- To create an association to an existing Case, use the Case's ID when setting the ``associatedCases`` field (e.g., ``"associatedCases": {"data": [{"id": 12345}]}``).
- To create an association to a new Group, include `all fields required to create the type of Group <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html#available-fields>`_ when setting the ``associatedGroups`` field. The new Group will be created in the Organization to which your API user account belongs.
- To create an association to an existing Group that belongs to an Organization, Community, or Source, use the Group's ID when setting the ``associatedGroups`` field.
- To create an association to a new Indicator, include `all fields required to create the type of Indicator <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#available-fields>`_ when setting the ``associatedIndicators`` field. The new Indicator will be created in the Organization to which your API user account belongs.
- To create an association to an existing Indicator that belongs to an Organization, use the Indicator's ID, or its summary and type (e.g., ``"associatedIndicators": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``associatedIndicators`` field.
- To create an association to an existing Indicator that belongs to a Community or Source, use the Indicator's ID when setting the ``associatedIndicators`` field.

.. note::

    You can associate multiple Cases, Indicators, and Groups to a Case in a single POST or PUT request.