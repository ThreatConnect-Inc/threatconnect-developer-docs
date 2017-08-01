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
        "apiCalls": 1,
        "resultCount": 0,
        "status": "Success"
    }

Delete Group Metadata
---------------------

Delete Group Attributes
^^^^^^^^^^^^^^^^^^^^^^^

To delete an attribute from a Group, use the following format:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}/attributes/{attributeId}

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

Delete Adversary Assets
^^^^^^^^^^^^^^^^^^^^^^^

To delete an Adversary Asset, use a request in the following format:

.. code::

    DELETE /v2/groups/adversaries/{adversaryId}/adversaryAssets/{assetType}/{assetId}

For example, if you wanted to delete the Adversary Asset (which happens to be of type URL) with ID 1 on the Adversary with ID 12345, you would use the following request:

.. code::

    DELETE /v2/groups/adversaries/12345/adversaryAssets/urls/1

JSON Response:

.. code:: json

    {
      "status": "Success"
    }

Delete/Disassociate Group Associations
--------------------------------------

Disassociate from a Group
^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate one Group from another, use a query in the following format:

.. code::

    DELETE /v2/groups/{groupType}/{groupId}/groups/{associatedGroupType}/{associatedGroupId}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: _includes/group_types.rst

For example, the query below will disassociate a Threat with the ID 12345 from an Incident with the ID 54321:

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

For example, the query below will disassociate the Threat with the ID 12345 from the IP Address ``0.0.0.0``:

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

For example, the query below will disassociate the Threat with the ID 12345 from the Victim Asset with ID 54321:

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

For example, the query below will disassociate the Threat with the ID 12345 from the Victim with ID 54321:

.. code::

    DELETE /v2/groups/threats/12345/victims/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }
