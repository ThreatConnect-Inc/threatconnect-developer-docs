Delete Victims
-------------

To delete a Victim, the most basic format is:

.. code::

    DELETE /v2/victims/{victimId}

By way of example, the query below will delete the Victim with ID 12345:

.. code::

    DELETE /v2/victims/12345

JSON Response:

.. code:: json

    {
        "apiCalls": 1,
        "resultCount": 0,
        "status": "Success"
    }

Delete Victim Metadata
----------------------

Delete Victim Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

To delete an attribute from a Victim, use the following format:

.. code::

    DELETE /v2/victims/{victimId}/attributes/{attributeId}

For example, if you wanted to delete the attribute with ID 54321 from the Victim with ID 12345, you would use the following query:

.. code::

    DELETE /v2/victims/12345/attributes/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

To delete a Security Label from an attribute, use the following format where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the owner:

.. code::

    DELETE /v2/victims/{victimId}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will remove the ``TLP Amber`` Security Label from the attribute with ID 54321 on the Victim:

.. code::

    DELETE /v2/victims/12345/attributes/54321/securityLabels/TLP%20Amber

Delete Victim Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete a Security Label from a Victim, use the following format where ``{securityLabel}`` is replaced with the name of a Security Label:

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

To delete a tag from a Victim, use the following format where ``{tagName}`` is replaced with the name of the tag you wish to remove from the Victim:

.. code::

    DELETE /v2/victims/{victimId}/tags/{tagName}

For example, the query below will delete the ``Nation State`` tag to the Victim with ID 12345:

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

Disassociate from a Group
^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Victim from a Group, use a query in the following format:

.. code::

    DELETE /v2/victims/{victimId}/groups/{associatedGroupType}/{associatedGroupId}

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

Disassociate from an Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Victim from an Indicator, use a query in the following format:

.. code::

    DELETE /v2/victims/{victimId}/indicators/{associatedIndicatorType}/{associatedIndicator}

For example, the query below will disassociate the Victim with ID 12345 from the IP Address ``0.0.0.0``:

.. code::

    DELETE /v2/victims/12345/indicators/addresses/0.0.0.0

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Disassociate from a Victim Asset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Victim from a Victim Asset, use a query in the following format:

.. code::

    DELETE /v2/victims/{victimId}/victimAssets/{victimAssetType}/{victimAssetId}

For example, the query below will disassociate the Victim with ID 12345 from the Victim Asset with ID 54321:

.. code::

    DELETE /v2/victims/12345/victimAssets/emailAddresses/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }


Disassociate from a Victim
^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate a Victim from a Victim, use a query in the following format:

.. code::

    DELETE /v2/victims/{victimId}/victims/{victimId}

For example, the query below will disassociate the Victim with ID 12345 from the Victim with ID 54321:

.. code::

    DELETE /v2/victims/12345/victims/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }
