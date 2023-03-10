Retrieve Groups
---------------

Retrieve All Groups
^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Groups:

.. code::

    GET /v3/groups

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 10,
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "dateAdded": "2021-10-21T19:54:59Z",
                "webLink": "https://app.threatconnect.com/auth/document/document.xhtml?document=10",
                "type": "Document",
                "name": "Bad Document",
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555"
                },
                "upVoteCount":"0",
                "downVoteCount":"0",
                "fileName": "indicators.txt",
                "fileSize": 36,
                "status": "Success",
                "documentType": "Text",
                "documentDateAdded": "2021-10-21T19:54:59Z",
                "lastModified": "2022-03-09T12:44:04Z",
                "legacyLink": "https://app.threatconnect.com/auth/document/document.xhtml?document=10"
            },
            {
                "id": 9,
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "dateAdded": "2021-09-17T12:52:49Z",
                "webLink": "https://app.threatconnect.com/auth/email/email.xhtml?email=9",
                "type": "Email",
                "name": "Your Amazon.com order for demo@sample.com",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com"
                },
                "upVoteCount":"0",
                "downVoteCount":"0",
                "to": "demo@sample.com",
                "from": "auto-confirm@bad.com",
                "subject": "Your Amazon.com order for demo@sample.com",
                "header": "<email header goes here>",
                "body": "Please visit bad.com to see your order and give us all your money. Muahahahaha!",
                "scoreIncludesBody": true,
                "emailDate": "2021-09-17T12:50:19Z",
                "scoreBreakdown": "Rule SPF Neutral was matched against 'neutral'.\t100\nRule Host was matched against 'bad.com'.\t282\n",
                "lastModified": "2022-03-09T20:39:52Z",
                "legacyLink": "https://app.threatconnect.com/auth/email/email.xhtml?email=9"
            },
            {...}
        ],
        "status": "Success"
    }

.. hint::
    Use the ``owner`` query parameter to `limit the results to a specific owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_.

Retrieve a Specific Group
^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Group:

.. code::

    GET /v3/groups/{groupId}

For example, the following request will retrieve data for the Group whose ID is 3:

.. code::

    GET /v3/groups/3

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-03T14:57:45Z",
            "webLink": "https://app.threatconnect.com/#/details/groups/3/overview",
            "type": "Incident",
            "name": "Bad Incident",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555"
            },
            "upVoteCount":"0",
            "downVoteCount":"0",
            "status": "New",
            "eventDate": "2021-11-03T00:00:00Z",
            "lastModified": "2021-11-03T14:57:45Z2022-02-16T18:54:23Z",
            "legacyLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=3",
        },
        "status": "Success"
    }