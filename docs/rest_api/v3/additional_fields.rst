Include Additional Fields for Returned Objects
----------------------------------------------

When retrieving objects, you can request additional fields not included with each returned object by including the ``?fields=`` query parameter, followed by the field name(s) you want to include, in your query.

For example, the following query will return information about the Indicator with ID 12345, including Tags applied to the Indicator and Groups associated to the Indicator.

For example, the following query will return information about the Artifact with ID 3, including a related Task and a related Note:

.. code::

  GET /v3/indicators/12345?fields=tags&fields=associatedGroups

JSON Response:

.. code:: json

    {
        "data": {
            "id": 12345,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-10-26T13:05:02Z",
            "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=veryultrabadguy.com",
            "tags": {
                "data": [
                    {
                        "id": 11,
                        "name": "Targeted Attack",
                        "lastUsed": "2021-11-03T15:04:49Z"
                    }
                ]
            },
            "type": "Host",
            "lastModified": "2021-10-26T15:16:43Z",
            "summary": "badguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {
                "data": [
                    {
                        "id": 94271,
                        "type": "Incident",
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-11-03T15:04:49Z",
                        "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=94271",
                        "name": "Bad Incident",
                        "createdBy": "API User",
                        "status": "Incident Reported",
                        "eventDate": "2021-11-03T00:00:00Z"
                    }
                ]
            },
            "hostName": "badguy.com",
            "dnsActive": false,
            "whoisActive": false
        },
        "status": "Success"
    }

Additional association levels for intelligence items may also be retrieved. For example, adding ``.attributes`` to the ``?fields=associatedGroups`` query parameter in the the preceding query will return information about the Indicator with ID 12345, including Tags applied to the Indicator, Groups associated to the Indicator, and Attributes added to those associated Groups.

.. code::

  GET /v3/indicators/12345?fields=tags&fields=associatedGroups.attributes

JSON Response:

.. code:: json

    {
        "data": {
            "id": 12345,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-10-26T13:05:02Z",
            "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=veryultrabadguy.com",
            "tags": {
                "data": [
                    {
                        "id": 11,
                        "name": "Targeted Attack",
                        "lastUsed": "2021-11-03T15:04:49Z"
                    }
                ]
            },
            "type": "Host",
            "lastModified": "2021-10-26T15:16:43Z",
            "summary": "badguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "associatedGroups": {
                "data": [
                    {
                        "id": 94271,
                        "type": "Incident",
                        "ownerName": "Demo Organization",
                        "dateAdded": "2021-11-03T15:04:49Z",
                        "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=94271",
                        "name": "Bad Incident",
                        "createdBy": "API User",
                        "attributes": {
                            "data": [
                                {
                                    "id": 1077825,
                                    "type": "Additional Analysis and Context",
                                    "value": "Based on internal analysis, this incident was bad.",
                                    "source": "Phase of Intrusion",
                                    "createdBy": {
                                        "id": 39,
                                        "userName": "11112222333344445555",
                                        "firstName": "API",
                                        "lastName": "User",
                                        "pseudonym": "APIUserNFmof",
                                        "role": "Api User"
                                    },
                                    "dateAdded": "2021-11-04T19:07:01Z",
                                    "lastModified": "2021-11-04T19:07:01Z",
                                    "default": false
                                }
                            ]
                        },
                        "status": "Incident Reported",
                        "eventDate": "2021-11-03T00:00:00Z"
                    }
                ]
            },
            "hostName": "badguy.com",
            "dnsActive": false,
            "whoisActive": false
        },
        "status": "Success"
    }

.. note::
  By default, you can only retrieve one association level for threat intelligence items at a time. To retrieve more than one association level at a time, contact your System Administrator and have them do one of the following:

  - Enable the **Allow User to Exceed API Link Limit** setting on your API user account. Instructions for enabling this setting are available in the `Creating User Accounts <https://training.threatconnect.com/learn/article/creating-user-accounts-kb-article>`_ knowledge base article.
  - Update the **v3ApiIntelLinkLimit** system setting to allow for more than one association level to be retrieved at a time.

To view a list of available options to set in the ``?fields=`` query parameter for each object, use the following query:

.. code::

    OPTIONS /v3/{objectName}/fields

.. note::
    The ``?tql=`` and ``?fields=`` query parameters can be combined in a single request. For example, the following query will return all Indicators, along with their respective Tags and Attributes, that belong to the ``Demo Community`` owner:

    ``GET /v3/indicators?tql=ownerName EQ "Demo Community"&fields=tags&fields=attributes``

    Depending on the tool you're using to interact with the ThreatConnect API, it may be necessary to manually encode the URL in your request when including query parameters. For example, some tools may accept ``?tql=ownerName EQ "Demo Community"&fields=tags&fields=attributes`` as a valid URL and automatically encode it, while others may require you to manually encode the URL (e.g., ``?tql=ownerName%20EQ%20%22Demo%20Community%22&fields=tags&fields=attributes``). If you submit a request with query parameters and a ``401 Unauthorized`` error is returned, verify whether the URL in your request is encoded properly for your preferred API tool.
