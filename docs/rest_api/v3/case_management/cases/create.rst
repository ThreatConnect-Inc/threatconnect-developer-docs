Create Cases
------------

The following example illustrates the basic format for creating a Case:

.. code::

    POST /v3/cases
    {
        "name": "Case name",
        "status": "Case status",
        "severity": "Case severity"
    }

For example, the following request will create a Case named "Phishing Investigation." It will also complete the following actions for the Case:

- Set the Case's severity to **Low**
- Set the Case's status to **Open**
- Assign the Case to smithj@threatconnect.com
- Create an Artifact within the Case and associate the Artifact to the existing Indicator whose ID is 2

.. hint::
    To include the ``artifacts`` field in the API response, append ``?fields=artifacts`` to the end of the request URL.

.. code::

    POST /v3/cases
    {
        "artifacts": {"data": [{"summary": "badguy.com", "type": "Host", "associatedIndicators": {"data": [{"id": "2"}]}}]},
        "assignee": {"type": "User", "data": {"userName": "smithj@threatconnect.com"}},
        "name": "Phishing Investigation",
        "severity": "Low",
        "status": "Open"
    }

JSON Response:

.. code:: json

    {
        "data": {
            "id": 1,
            "xid": "a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
            "name": "Phishing Investigation",
            "dateAdded": "2023-03-09T14:41:27Z",
            "lastUpdated": "2023-03-09T14:41:27Z",
            "caseOpenTime": "2023-03-09T14:41:27.27Z",
            "caseOpenUser": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
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
                    "owner": "Demo Organization"
                }
            },
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "owner": "Demo Organization",
            "ownerId": 1
        },
        "message": "Created",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a POST request to the ``/v3/cases`` endpoint.

Create Associations
^^^^^^^^^^^^^^^^^^^

You can create associations between Cases in your Organization and Groups, Indicators, and other Cases in your Organization. If cross-owner associations are enabled on your ThreatConnect instance, you can also create associations between Groups and Indicators in Communities and Sources to which you have access and Cases in your Organization.

When creating associations for Cases using the ThreatConnect v3 API, follow these guidelines:

- To create an association to a new Case, include `all fields required to create a Case <#available-fields>`_ when setting the ``associatedCases`` field.
- To create an association to an existing Case, use the Case's ID when setting the ``associatedCases`` field (e.g., ``"associatedCases": {"data": [{"id": 12345}]}``).
- To create an association to a new Group, include `all fields required to create the type of Group <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html#available-fields>`_ when setting the ``associatedGroups`` field. To create the Group in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Group when setting the ``associatedGroups`` field.
- To create an association to an existing Group, use the Group's ID when setting the ``associatedGroups`` field.
- To create an association to a new Indicator, include `all fields required to create the type of Indicator <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#available-fields>`_ when setting the ``associatedIndicators`` field. To create the Indicator in a Community or Source, include the ``ownerId`` or ``ownerName`` field in the request and specify the ID or name, respectively, of the Community or Source in which to create the Indicator when setting the ``associatedIndicators`` field.
- To create an association to an existing Indicator, use the Indicator's ID, or use its summary and type (e.g., ``"associatedIndicators": {"data": [{"type": "Host", "hostname": "badguy.com"}]}``), when setting the ``associatedIndicators`` field. To create an association to an Indicator in a Community or Source using the Indicator's summary and type, include the ``ownerId`` or ``ownerName`` field and specify the ID or name, respectively, of the Community or Source to which the Indicator belongs when setting the ``associatedIndicators`` field.

.. note::
    You can associate multiple Cases, Indicators, and Groups to a Case in a single POST or PUT request.