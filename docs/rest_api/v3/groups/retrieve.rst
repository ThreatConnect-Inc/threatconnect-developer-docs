Retrieve Groups
---------------

Retrieve All Groups
^^^^^^^^^^^^^^^^^^^

To retrieve all Groups, use the following query:

.. code::

    GET /v3/groups/

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 10,
                "type": "Document",
                "ownerName": "Demo Organization",
                "dateAdded": "2021-10-21T19:54:59Z",
                "webLink": "/auth/document/document.xhtml?document=181449",
                "name": "Bad Document",
                "createdBy": "John Smith",
                "fileName": "indicators.txt",
                "fileSize": 36,
                "status": "Success",
                "documentType": "Text",
                "documentDateAdded": "2021-10-21T19:54:59Z"
            },
            {
                "id": 9,
                "type": "Email",
                "ownerName": "Demo Organization",
                "dateAdded": "2021-09-17T12:52:49Z",
                "webLink": "/auth/email/email.xhtml?email=181443",
                "name": "Your Amazon.com order for demo@sample.com",
                "createdBy": "John Smith",
                "from": "demo@sample.com",
                "subject": "Your Amazon.com order for demo@sample.com",
                "header": "Delivered-To: [MY EMAIL ADDRESS]\r\nReceived: by 10.182.3.66 with SMTP id a2csp104490oba;\r\nFri, 17 Sep 2021 08:50:19 -0400\r\n\r\nReceived: by 10.14.212.72 with SMTP id x48mr8232338eeo.40.1344724334578;\r\n\r\nFri, 17 Sep 2021 08:50:19 -0400\r\n\r\nReturn-Path: <e.vwidxus@yahoo.com>\r\n\r\nReceived: from 72-255-12-30.client.stsn.net (72-255-12-30.client.stsn.net. [72.255.12.30])\r\n\r\nby mx.google.com with ESMTP id c41si1698069eem.38.2012.08.11.15.32.13;\r\n\r\nFri, 17 Sep 2021 08:50:19 -0400\r\n\r\nReceived-SPF: neutral (google.com: 72.255.12.30 is neither permitted nor denied by best guess record for domain of e.vwidxus@yahoo.com) client-ip=72.255.12.30;\r\n\r\nAuthentication-Results: mx.google.com; spf=neutral (google.com: 72.255.12.30 is neither permitted nor denied by best guess record for domain of e.vwidxus@yahoo.com) smtp.mail=e.vwidxus@yahoo.com\r\n\r\nReceived: by vwidxus.net id hnt67m0ce87b for <[MY EMAIL ADDRESS]>; Fri, 17 Sep 2021 08:50:19 -0400 (envelope-from <e.vwidxus@yahoo.com>)\r\n\r\nReceived: from vwidxus.net by web.vwidxus.net with local (Mailing Server 4.69)\r\n\r\nid 34597139-886586-27/./PV3Xa/WiSKhnO+7kCTI+xNiKJsH/rC/\r\n\r\nfor root@vwidxus.net; Fri, 17 Sep 2021 08:50:19 -0400",
                "body": "Please visit bad.com to see your order and give us all your money. Muahahahaha!\r\n\r\n",
                "scoreIncludesBody": true,
                "emailDate": "2021-09-17T12:50:19Z",
                "scoreBreakdown": "Rule SPF Neutral was matched against 'neutral'.\t100\nRule Host was matched against 'bad.com'.\t282\n"
            }
        {...}
        ],
        "status": "Success"
    }

Retrieve a Single Group
^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Group, use a query in the following format:

.. code::

    GET /v3/groups/{groupId}

For example, the following query will return information about the Group with ID 3:

.. code::

    GET /v3/groups/3

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "type": "Incident",
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-03T14:57:45Z",
            "webLink": "/auth/incident/incident.xhtml?incident=3",
            "name": "Bad Incident",
            "createdBy": "API User",
            "status": "New",
            "eventDate": "2021-11-03T00:00:00Z"
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically provided with each returned object, refer to `Request Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.