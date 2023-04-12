Update Cases
------------

The following example illustrates the basic format for updating a Case:

.. code::

    PUT /v3/cases/{caseId}
    {
        {updatedField}: {updatedValue}
    }
  
For example, the following request will make the following updates to the Case whose ID is 1:

- Set the Case's resolution to **False Positive**
- Set the Case's status to **Closed**
- Create a new Adversary Group named **Extreme Bad Guy** that is associated to the Artifact whose ID is 4, and then associate the Group to the Case

.. hint::
    To include the ``associatedGroups`` field in the API response, append ``?fields=associatedGroups`` to the end of the request URL.

.. code::

    PUT /v3/cases/1
    {
        "resolution": "False Positive",
        "status": "Closed",
        "associatedGroups": {"data": [{"name": "Extreme Bad Guy", "type": "Adversary", "associatedArtifacts": {"data": [{"id": 4}]}}]}
    }


JSON Response:

.. code:: json

    {
        "data": {
            "id": 1,
            "xid": "aa1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
            "name": "Phishing Investigation",
            "dateAdded": "2023-03-09T14:41:27.27Z",
            "lastUpdated": "2023-03-30T13:27:41Z",
            "caseOpenTime": "2023-03-09T14:41:27Z",
            "caseOpenUser": {
                "id": 3,
                "userName": "11112222333344445555"
            },
            "caseCloseTime": "2021-04-12T18:36.18Z",
            "caseCloseUser": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "status": "Closed",
            "severity": "Low",
            "resolution": "False Positive",
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
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request to the ``/v3/cases`` endpoint.

.. hint::
    When updating a Case, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedCases``
    - ``associatedGroups``
    - ``associatedIndicators``
    - ``attributes``
    - ``tags``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.

.. attention::
    If you try to add an Attribute to a Case when the Attribute Type's **Max Allowed** limit for Cases has been reached, the API will return a **400 Bad Request** error.