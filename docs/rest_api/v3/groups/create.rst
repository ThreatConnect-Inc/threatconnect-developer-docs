Create Groups
-------------

The basic format for creating a Group is:

.. code::

    POST /v3/groups/
    {
        "name": "Group name goes here",
        "type": "Group type goes here"
        //required fields for the selected Group type go here, if applicable
    }

Refer to the `Available Fields <#available-fields>`_ and `Group-Specific Fields <#group-specific-fields>`_ sections for a list of available fields that can be included in the body of a POST request for the ``groups`` object.

.. warning::
    If you submit a POST request to create a new Group but the Group already exists in ThreatConnect, the existing Group will be updated based on the fields included in the POST request.

.. note::
    You can add multiple Attributes, Tags, and Security Labels to the Group being created in a single POST request. Similarly, you can associate multiple Indicators and Groups to the Group being created in a single POST request.

Example POST Request
^^^^^^^^^^^^^^^^^^^^^

The following query will create an ``Incident`` Group for an Incident that took place on Nov. 3, 2021. The Incident will be assigned a status of ``New``, and ``Targeted Attack`` and ``Robbery`` Tags will be created and applied to it.

.. code::

    POST /v3/groups/
    {
        "type": "Incident",
        "name": "Bad Incident",
        "eventDate": "2021-11-03T10:50:00Z",
        "status": "New",
        "tags": {"data": [{"name": "Targeted Attack"}, {"name": "Robbery"}]}
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "type": "Incident",
            "ownerName": "Demo Organization",
            "dateAdded": "2021-11-03T14:57:45Z",
            "webLink": "/auth/incident/incident.xhtml?incident=3",
            "tags": {
                "data": [{
                    "id": 11,
                    "name": "Targeted Attack",
                    "lastUsed": "2021-11-02T15:01:44Z"
                },{
                    "id": 12,
                    "name": "Robbery",
                    "lastUsed": "2021-11-02T15:01:44Z"
                }],
                "count": 2
            },
            "securityLabels": {
                "count": 0
            },
            "name": "Bad Incident",
            "createdBy": "API User",
            "associatedGroups": {
                "count": 0
            },
            "associatedIndicators": {
                "count": 0
            },
            "attributes": {
                "count": 0
            },
            "status": "New",
            "eventDate": "2021-11-03T00:00:00Z"
        },
        "message": "Created",
        "status": "Success"
    }

.. note::
    When creating an Group, you can apply Tags that do not yet exist in ThreatConnect to it. In this scenario, you would need to fill out `all required fields for each new Tag <https://docs.threatconnect.com/en/latest/rest_api/v3/tags/tags.html>`_. Upon creation of the new Group, any Tags included in the body of the POST request that do not yet exist in ThreatConnect will also be created.

    Similarly, you can associate Indicators and Groups that do not yet exist in ThreatConnect to the Group. In this scenario, you would need to fill out `all required fields for the type of Indicator <https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html>`_ or Group being associated to the Group. Upon creation of the new Group, any associated objects included in the body of the POST request that do not yet exist in ThreatConnect will also be created.