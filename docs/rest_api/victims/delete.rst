Delete Victims
--------------

The most basic format used to delete a Victim is:

.. code::

    DELETE /v2/victims/{victimId}

For example, the query below will delete the Victim with ID 12345:

.. code::

    DELETE /v2/victims/12345

JSON Response:

.. code:: json

    {
        "apiCalls": 1,
        "resultCount": 0,
        "status": "Success"
    }

Delete Victim Assets
--------------------

To delete a Victim's Asset, use a query in the following format:

.. code::

    DELETE /v2/victims/{victimId}/victimAssets/{victimAssetType}/{victimAssetId}

For example, the query below will delete the email address Victim Asset with ID 54321 from the Victim with ID 12345:

.. code::

    DELETE /v2/victims/12345/victimAssets/emailAddresses/54321

JSON Response:

.. code:: json

    {
      "status": "Success"
    }

Delete Victim Metadata
----------------------

Delete Victim Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

To delete an Attribute from a Victim, use the following format:

.. code::

    DELETE /v2/victims/{victimId}/attributes/{attributeId}

For example, if you want to delete the Attribute with ID 54321 from the Victim with ID 12345, you would use the following query:

.. code::

    DELETE /v2/victims/12345/attributes/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

To delete a Security Label from an Attribute, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the Owner:

.. code::

    DELETE /v2/victims/{victimId}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will remove the ``TLP Amber`` Security Label from the Attribute with ID 54321 on the Victim:

.. code::

    DELETE /v2/victims/12345/attributes/54321/securityLabels/TLP%20Amber

Delete Victim Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete a Security Label from a Victim, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label:

.. code::

    DELETE /v2/victims/{victimId}/securityLabels/{securityLabel}

For example, the query below will delete the ``TLP Amber`` Security Label to the Victim with ID 12345:

.. code::

    DELETE /v2/victims/12345/securityLabels/TLP%20Amber

JSON Response:

.. code:: json
    
    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Delete Victim Tags
^^^^^^^^^^^^^^^^^^

To delete a Tag from a Victim, use the following format, where ``{tagName}`` is replaced with the name of the Tag you wish to remove from the Victim:

.. code::

    DELETE /v2/victims/{victimId}/tags/{tagName}

For example, the query below will delete the ``Nation State`` Tag to the Victim with ID 12345:

.. code::

    DELETE /v2/victims/12345/tags/Nation%20State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Delete/Disassociate Victim Associations
---------------------------------------

Disassociate Group from Victim
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Victim from a Group, use a query in the following format:

.. code::

    DELETE /v2/victims/{victimId}/groups/{associatedGroupType}/{associatedGroupId}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, the query below will disassociate a Victim with ID 12345 from an Incident with the ID 54321:

.. code::

    DELETE /v2/victims/12345/groups/incidents/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }
