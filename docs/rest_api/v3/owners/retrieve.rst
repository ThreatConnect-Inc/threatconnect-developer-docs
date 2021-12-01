Retrieve Owners
---------------

Retrieve All Owners
^^^^^^^^^^^^^^^^^^^

To retrieve all owners in the Organization in which your API user account resides, use the following query:

.. code::

    GET /v3/security/owners

JSON Response:

.. code:: json

    {
        "data": [
            {
                "id": 2,
                "name": "Demo Source",
                "type": "Source",
                "ownerRole": "Director",
                "permIndicator": "FULL",
                "permGroup": "FULL",
                "permPost": "FULL",
                "permTrack": "FULL",
                "permVictim": "FULL",
                "permAttribute": "FULL",
                "permApps": "NONE",
                "permUsers": "FULL",
                "permSecurityLabel": "FULL",
                "permTag": "FULL",
                "permAttributeType": "FULL",
                "permSettings": "FULL",
                "permMembers": "FULL",
                "permCopyData": "FULL",
                "permInvite": "FULL",
                "permTask": "NONE",
                "permCaseTag": "NONE",
                "permArtifact": "NONE",
                "permComment": "NONE",
                "permTimeline": "NONE",
                "permWorkflowTemplate": "NONE",
                "permPublish": "FULL",
                "permPlaybooksExecute": "NONE",
                "permPlaybooks": "NONE"
            },
            {
                "id": 3,
                "name": "Demo Community",
                "type": "Community",
                "ownerRole": "Director",
                "permIndicator": "FULL",
                "permGroup": "FULL",
                "permPost": "FULL",
                "permTrack": "FULL",
                "permVictim": "FULL",
                "permAttribute": "FULL",
                "permApps": "NONE",
                "permUsers": "FULL",
                "permSecurityLabel": "FULL",
                "permTag": "FULL",
                "permAttributeType": "FULL",
                "permSettings": "FULL",
                "permMembers": "FULL",
                "permCopyData": "FULL",
                "permInvite": "FULL",
                "permTask": "NONE",
                "permCaseTag": "NONE",
                "permArtifact": "NONE",
                "permComment": "NONE",
                "permTimeline": "NONE",
                "permWorkflowTemplate": "NONE",
                "permPublish": "FULL",
                "permPlaybooksExecute": "NONE",
                "permPlaybooks": "NONE"
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Single Owner
^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific owner in the Organization in which your API user account resides, use a query in the following format:

.. code::

    GET /v3/security/owners/{ownerId}

For example, the following query will return information about the owner with ID 3:

.. code::

    GET /v3/security/owners/3

.. code:: json

    {
        "data": {
            "id": 3,
            "name": "Demo Community",
            "type": "Community",
            "ownerRole": "Director",
            "permIndicator": "FULL",
            "permGroup": "FULL",
            "permPost": "FULL",
            "permTrack": "FULL",
            "permVictim": "FULL",
            "permAttribute": "FULL",
            "permApps": "NONE",
            "permUsers": "FULL",
            "permSecurityLabel": "FULL",
            "permTag": "FULL",
            "permAttributeType": "FULL",
            "permSettings": "FULL",
            "permMembers": "FULL",
            "permCopyData": "FULL",
            "permInvite": "FULL",
            "permTask": "NONE",
            "permCaseTag": "NONE",
            "permArtifact": "NONE",
            "permComment": "NONE",
            "permTimeline": "NONE",
            "permWorkflowTemplate": "NONE",
            "permPublish": "FULL",
            "permPlaybooksExecute": "NONE",
            "permPlaybooks": "NONE"
        },
        "status": "Success"
    }

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.