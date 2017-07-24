Delete Indicators
-----------------

To delete an Indicator, the most basic format is:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}

By way of example, the query below will delete the Email Address ``bad@example.com``:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com

JSON Response:

.. code:: json

    {
        "apiCalls": 1,
        "resultCount": 0,
        "status": "Success"
    }

Delete Indicator Metadata
-------------------------

Delete Indicator Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete an attribute from an Indicator, use the following format:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}

For example, if you wanted to delete the attribute with ID 54321 from the Email Address ``bad@example.com``, you would use the following query:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com/attributes/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

To delete a Security Label from an attribute, use the following format where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the owner:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will remove the ``TLP Amber`` Security Label from the attribute with ID 54321 on the Email Address ``bad@example.com``:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com/attributes/54321/securityLabels/TLP%20Amber

Delete Indicator Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete a Security Label from an Indicator, use the following format where ``{securityLabel}`` is replaced with the name of a Security Label:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/securityLabels/{securityLabel}

For example, the query below will delete the ``TLP Amber`` Security Label to the Email Address ``bad@example.com``:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com/securityLabels/TLP%20Amber

JSON Response:

.. code:: json
    
    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Delete Indicator Tags
^^^^^^^^^^^^^^^^^^^^^

To delete a tag from an Indicator, use the following format where ``{tagName}`` is replaced with the name of the tag you wish to remove from the Indicator:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/tags/{tagName}

For example, the query below will delete the ``Nation State`` tag to the Email Address ``bad@example.com``:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com/tags/Nation%20State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Deleting File Occurrences
^^^^^^^^^^^^^^^^^^^^^^^^^

To delete a File Occurrence, use a query in the following format:

.. code::

    DELETE /v2/indicators/files/{fileHash}/fileOccurrences/{fileOccurrenceId}

For example, the query below will delete the File Occurrence with an ID of 54321 from the File Indicator represented by the hash ``aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa``:

.. code::

    DELETE /v2/indicators/files/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/fileOccurrences/54321

JSON Response:

.. code:: json

    {
      "status": "Success"
    }

Delete/Disassociate Indicator Associations
------------------------------------------

Disassociate from a Group
^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate an Indicator from a Group, use a query in the following format:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/groups/{associatedGroupType}/{associatedGroupId}

For example, the query below will disassociate the Email Address ``bad@example.com`` from an Incident with the ID 54321:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com/groups/incidents/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Disassociate from an Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate an Indicator from another Indicator, use a query in the following format:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/indicators/{associatedIndicatorType}/{associatedIndicator}

For example, the query below will disassociate the Email Address ``bad@example.com`` from the IP Address ``0.0.0.0``:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com/indicators/addresses/0.0.0.0

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Disassociate from a Victim Asset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate an Indicator from a Victim Asset, use a query in the following format:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/victimAssets/{victimAssetType}/{victimAssetId}

For example, the query below will disassociate the Email Address ``bad@example.com`` from the Victim Asset with ID 54321:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com/victimAssets/emailAddresses/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }


Disassociate from a Victim
^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate an Indicator from a Victim, use a query in the following format:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/victims/{victimId}

For example, the query below will disassociate the Email Address ``bad@example.com`` from the Victim with ID 54321:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com/victims/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }
