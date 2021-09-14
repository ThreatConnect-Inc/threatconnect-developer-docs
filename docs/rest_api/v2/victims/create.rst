Create Victims
--------------

The most basic format used to create a Victim is:

.. code::

    POST /v2/victims/
    Content-type: application/json; charset=utf-8

    {
      // add fields here...
    }

When creating a Victim, you can also add any of the fields listed below:

+--------------+----------+
| Valid Fields | Required |
+==============+==========+
| name         | TRUE     |
+--------------+----------+
| description  | FALSE    |
+--------------+----------+
| org          | FALSE    |
+--------------+----------+
| suborg       | FALSE    |
+--------------+----------+
| workLocation | FALSE    |
+--------------+----------+
| nationality  | FALSE    |
+--------------+----------+

For example, the query below will create a Victim in the default owner:

.. code::

    POST /v2/victims/
    Content-type: application/json; charset=utf-8

    {
      "name": "Example Victim",
      "description": "This victim got hacked.",
      "org": "Test Org",
      "suborg": "HR Department",
      "workLocation": "Washington D.C.",
      "nationality": "American",
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "victim": {
          "id": "54321",
          "name": "Example Victim",
          "description": "This victim got hacked.",
          "org": "Test Org",
          "suborg": "HR Department",
          "workLocation": "Washington D.C.",
          "nationality": "American",
          "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=54321"
        }
      }
    }

Create Victim Assets
--------------------

To create Victim Assets, use a query in the following format:

.. code::

    POST /v2/victims/{victimId}/victimAssets/{victimAssetType}
    Content-type: application/json; charset=utf-8

    {
      // add fields here...
    }

The available Victim Asset types are:

.. include:: ../_includes/victim_asset_types.rst

When creating a Victim Asset, there are certain fields that are required, as detailed below:

.. include:: ../_includes/victim_asset_fields.rst

For example, if you want to add a network account Victim Asset to a Victim with ID 12345, you would use the following query:

.. code::

    POST /v2/victims/12345/victimAssets/networkAccounts
    Content-type: application/json; charset=utf-8

    {
      "account": "John Doe",
      "network": "Active Directory"
    }

In the case of networkAccounts or socialNetworks, the account specifies the value of the actual account, and the network provides a classification for the network itself.

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "victimNetworkAccount": {
          "id": 398,
          "type": "NetworkAccount",
          "webLink": "https://sandbox.threatconnect.com/auth/victim/victim.xhtml?victim=12345",
          "account": "John Doe",
          "network": "Active Directory"
        }
      }
    }

Create Victim Metadata
----------------------

Create Victim Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

To add an Attribute to a Victim, use the following format:

.. code::

    POST /v2/victims/{victimId}/attributes
    Content-type: application/json; charset=utf-8

    {
      "type" : {attributeType},
      "value" : "Test Attribute",
      "displayed" : true
    }

For example, if you want to add a Description Attribute to the Victim with ID 12345, you would use the following query:

.. code::

    POST /v2/victims/12345/attributes
    Content-type: application/json; charset=utf-8

    {
      "type" : "Description",
      "value" : "Test Description",
      "displayed" : true
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "attribute": {
          "id": "54321",
          "type": "Description",
          "dateAdded": "2017-07-13T17:50:17",
          "lastModified": "2017-07-13T17:50:17",
          "displayed": true,
          "value": "Test Description"
        }
      }
    }

To add a Security Label to an Attribute, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the Owner:

.. code::

    POST /v2/victims/{victimId}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will add a ``TLP Amber`` Security Label to the Attribute on the Victim:

.. code::

    POST /v2/victims/12345/attributes/54321/securityLabels/TLP%20Amber

.. note:: In order to add a Security Label to an Attribute, the Security Label must already exist. The query above will not create a new Security Label. If you specify a Security Label that does not exist, it will return an error.

Create Victim Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add a Security Label to a Victim, use the following format, where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the Owner:

.. code::

    POST /v2/victims/{victimId}/securityLabels/{securityLabel}

For example, the query below will add a ``TLP Amber`` Security Label to the Victim with ID 12345:

.. code::

    POST /v2/victims/12345/securityLabels/TLP%20Amber

JSON Response:

.. code:: json
    
    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

.. note:: In order to add a Security Label to a Victim, the Security Label must already exist. The query above will not create a new Security Label. If you specify a Security Label that does not exist, it will return an error.

Create Victim Tags
^^^^^^^^^^^^^^^^^^

To add a Tag to a Victim, use the following format, where ``{tagName}`` is replaced with the name of the Tag you wish to add to the Victim:

.. code::

    POST /v2/victims/{victimId}/tags/{tagName}

For example, the query below will add the ``Nation State`` Tag to the Victim with ID 12345:

.. code::

    POST /v2/victims/12345/tags/Nation%20State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

.. include:: ../_includes/tag_length.rst

Create Victim Associations
--------------------------

Associate Group to Victim
^^^^^^^^^^^^^^^^^^^^^^^^^

To associate a Victim with a Group, use a query in the following format:

.. code::

    POST /v2/victims/{victimId}/groups/{associatedGroupType}/{associatedGroupId}

Replace ``{associatedGroupType}`` with one of the following Group types:

.. include:: ../_includes/group_types.rst

For example, the query below will associate a Victim with ID 12345 with an Incident with the ID 54321:

.. code::

    POST /v2/victims/12345/groups/incidents/54321

JSON Response:

.. code:: json

    {
      "status": "Success"
    }

.. include:: ../_includes/victim_asset_required_warning.rst
