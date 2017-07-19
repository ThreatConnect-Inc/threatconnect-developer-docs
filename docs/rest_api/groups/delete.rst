Delete Groups
-------------

To delete a Group, the most basic format is:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}

The ``{groupType}`` can be any one of the available group types:

- ``adversaries``
- ``campaigns``
- ``documents``
- ``emails``
- ``incidents``
- ``signatures``
- ``threats``
  
By way of example, the query below will delete the threat with the ID 12345:

.. code::

    DELETE /v2/groups/threats/12345

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "incident": {
          "id": "54321",
          "name": "Test Incident",
          "owner": {
            "id": 1,
            "name": "Example Organization",
            "type": "Organization"
          },
          "dateAdded": "2017-07-13T17:50:17",
          "webLink": "https://app.threatconnect.com/auth/incident/incident.xhtml?incident=54321",
          "eventDate": "2017-7-13T00:00:00-04:00"
        }
      }
    }

Delete Group Metadata
---------------------

Delete Group Attributes
^^^^^^^^^^^^^^^^^^^^^^^

To add an attribute to a Group, use the following format:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}/attributes/{attributeID}

For example, if you wanted to delete the attribute with ID 54321 from the threat with the ID 12345, you would use the following query:

.. code::

    DELETE /v2/groups/threats/12345/attributes/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

To delete a Security Label from an attribute, use the following format where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the owner:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will remove the ``TLP Amber`` Security Label from the attribute with ID 54321 on the Threat:

.. code::

    DELETE /v2/groups/threats/12345/attributes/54321/securityLabels/TLP%20Amber

Delete Group Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete a Security Label from a Group, use the following format where ``{securityLabel}`` is replaced with the name of a Security Label:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}/securityLabels/{securityLabel}

For example, the query below will delete the ``TLP Amber`` Security Label to the Threat with ID 12345:

.. code::

    DELETE /v2/groups/threats/12345/securityLabels/TLP%20Amber

JSON Response:

.. code:: json
    
    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Delete Group Tags
^^^^^^^^^^^^^^^^^

To delete a tag from a Group, use the following format where ``{tagName}`` is replaced with the name of the tag you wish to remove from the Group:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}/tags/{tagName}

For example, the query below will delete the ``Nation State`` tag to the Threat with ID 12345:

.. code::

    DELETE /v2/groups/threats/12345/tags/Nation%20State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Delete/Disassociate Group Associations
--------------------------------------

Disassociate from a Group
^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate one Group from another, use a query in the following format:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}/groups/{associatedGroupType}/{associatedGroupId}

For example, the query below will disassociate a Threat with the ID 12345 with an Incident with the ID 54321:

.. code::

    DELETE /v2/groups/threats/12345/groups/incidents/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Disassociate from an Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Group from an Indicator, use a query in the following format:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}/indicators/{associatedIndicatorType}/{associatedIndicator}

For example, the query below will associate the Threat with the ID 12345 with the IP Address ``0.0.0.0``:

.. code::

    DELETE /v2/groups/threats/12345/indicators/addresses/0.0.0.0

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Disassociate from a Victim Asset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Group from a Victim Asset, use a query in the following format:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}/victimAssets/{victimAssetType}/{victimAssetId}

For example, the query below will disassociate the Threat with the ID 12345 with the Victim Asset with ID 54321:

.. code::

    DELETE /v2/groups/threats/12345/victimAssets/emailAddresses/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }


Disassociate from a Victim
^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Group from a Victim, use a query in the following format:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}/victims/{victimId}

For example, the query below will disassociate the Threat with the ID 12345 with the Victim with ID 54321:

.. code::

    DELETE /v2/groups/threats/12345/victims/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }
