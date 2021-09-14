Delete Indicators
-----------------

To delete an Indicator, the most basic format is:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}?owner=owner

For example, the query below will delete the Email Address ``bad@example.com``:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com?owner=owner

JSON Response:

.. code:: json

    {
        "apiCalls": 1,
        "resultCount": 0,
        "status": "Success"
    }

Viewing Recently Deleted Indicators
-----------------------------------

As of ThreatConnect version 5.4, it is possible to view a list of Indicators that have been recently deleted from an Owner. The general format for this request is as follows:

.. code::

    GET /v2/indicators/deleted

JSON Response:

.. code::

    {
      "status": "Success",
      "data": {
        "resultCount": 1,
        "indicator": [
          {
            "ownerName": "Example Org",
            "type": "File",
            "dateAdded": "2017-10-31T18:32:13Z",
            "lastModified": null,
            "summary": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
          }
        ]
      }
    }

By default, this will return all of the Indicators recently deleted in the API key’s default Organization. The number of days for which the Indicators will be listed on this API branch before being removed is specified by the ``indicatorDeleteRetentionTime`` system setting.

To view Indicators that have been recently deleted from a Community or Source that is not the default Owner, append the ``owner={ownerName}`` parameter to the query, as demonstrated below:

.. code::

    GET /v2/indicators/deleted?owner=Example%20Community

Delete Indicator Metadata
-------------------------

Delete Indicator Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete an attribute from an Indicator, use the following format:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}

For example, if you want to delete the Attribute with ID 54321 from the Email Address ``bad@example.com``, you would use the following query:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com/attributes/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

To delete a Security Label from an Attribute, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the Owner:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will remove the ``TLP Amber`` Security Label from the Attribute with ID 54321 on the Email Address ``bad@example.com``:

.. code::

    DELETE /v2/indicators/emailAddresses/bad@example.com/attributes/54321/securityLabels/TLP%20Amber

Delete Indicator Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete a Security Label from an Indicator, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label:

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

To delete a Tag from an Indicator, use the following format, where ``{tagName}`` is replaced with the name of the Tag you wish to remove from the Indicator:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/tags/{tagName}

For example, the query below will delete the ``Nation State`` Tag to the Email Address ``bad@example.com``:

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

Disassociate Group from Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disassociate an Indicator from a Group, use a query in the following format:

.. code::

    DELETE /v2/indicators/{indicatorType}/{indicator}/groups/{associatedGroupType}/{associatedGroupId}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

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

Disassociate Indicator from Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Disassociate Victim Asset from Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Disassociate Victim from Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
