Update Cases
------------

The basic format for updating a Case is:

.. code::

    PUT /v3/cases/{caseId}
    {
        {updatedField}: {updatedValue}
    }
  
For example, the following query will update the resolution and status of the Case with ID 1. It will also create a new Adversary Group named ``Extreme Bad Guy`` that includes an associated Artifact and associate the Group to the Case:

.. code::

    PUT /v3/cases/1
    {
        "resolution": "False Positive",
        "status": "Closed",
        "associatedGroups": {"data": [{"name": "Extreme Bad Guy", "type": "Adversary", "associatedArtifacts": {"data": [{"id": 1}]}}]}
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
            ]},
            "notes": {},
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
            "associatedGroups": {
                "data": [
                    {
                        "id": 17,
                        "ownerName": "Example Organization",
                        "dateAdded": "2021-04-12T18:36.18Z",
                        "webLink": "https://app.threatconnect.com/auth/adversary/adversary.xhtml?adversary=17",
                        "type": "Adversary",
                        "name": "Extreme Bad Guy",
                        "createdBy": {
                            "id": 3,
                            "userName": "11112222333344445555",
                            "firstName": "John",
                            "lastName": "Smith",
                            "pseudonym": "jsmithAPI",
                            "role": "Api User"
                        },
                        "lastModified": "2021-04-12T18:36.18Z"
                    }
                ]
            },
            "associatedIndicators": {},
            "associatedCases": {}
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ and section for a list of available fields that can be included in the body of a PUT request for the ``cases`` object.

.. hint::
    When updating an Artifact, you can use the ``mode`` field to add or remove the following metadata:

    - ``associatedCases``
    - ``associatedGroups``
    - ``associatedIndicators``
    - ``attributes``
    - ``tags``

    See `Update an Object's Metadata <https://docs.threatconnect.com/en/latest/rest_api/v3/update_metadata.html>`_ for instructions on using the ``mode`` field.

.. warning::
    Trying to add an Attribute to a Case when the Case Attribute Type's **Max Allowed** limit has been reached will result in an error.