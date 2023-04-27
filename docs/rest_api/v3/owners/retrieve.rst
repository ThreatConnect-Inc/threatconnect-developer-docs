Retrieve Owners
---------------

Retrieve All Owners
^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all owners:

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
            {
                "id": 1,
                "name": "Demo Organization",
                "type": "Organization",
                "ownerRole": "Organization Administrator",
                "permIndicator": "FULL",
                "permGroup": "FULL",
                "permPost": "FULL",
                "permTrack": "FULL",
                "permVictim": "FULL",
                "permAttribute": "FULL",
                "permApps": "BUILD",
                "permUsers": "FULL",
                "permSecurityLabel": "FULL",
                "permTag": "FULL",
                "permAttributeType": "FULL",
                "permSettings": "FULL",
                "permMembers": "READ",
                "permCopyData": "FULL",
                "permInvite": "FULL",
                "permTask": "FULL",
                "permCaseTag": "FULL",
                "permArtifact": "FULL",
                "permComment": "FULL",
                "permTimeline": "FULL",
                "permWorkflowTemplate": "FULL",
                "permPublish": "FULL",
                "permPlaybooksExecute": "FULL",
                "permPlaybooks": "FULL"
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Owner
^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific owner:

.. code::

    GET /v3/security/owners/{ownerId}

For example, the following request will retrieve data for the owner whose ID is 3:

.. code::

    GET /v3/security/owners/3

JSON Response:

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