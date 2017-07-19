Create Indicators
-----------------

To create an Indicator, the most basic format is:

.. code::

    POST /v2/indicators/{indicatorType}
    {
      // required fields here...
    }

The following are all considered valid paths for creating indicators:

.. code::

    POST /v2/indicators/addresses
    POST /v2/indicators/emailAddresses
    POST /v2/indicators/files
    POST /v2/indicators/hosts
    POST /v2/indicators/urls

The table below illustrates valid fields for the body of the POST request when creating an Indicator.

+----------------+--------------+----------+
| Indicator Type | Valid Fields | Required |
+================+==============+==========+
| addresses      | ip           | TRUE     |
+----------------+--------------+----------+
|                | rating       | FALSE    |
+----------------+--------------+----------+
|                | confidence   | FALSE    |
+----------------+--------------+----------+
| emailAddresses | address      | TRUE     |
+----------------+--------------+----------+
|                | rating       | FALSE    |
+----------------+--------------+----------+
|                | confidence   | FALSE    |
+----------------+--------------+----------+
| files          | md5          | TRUE\*   |
+----------------+--------------+----------+
|                | sha1         | TRUE\*   |
+----------------+--------------+----------+
|                | sha256       | TRUE\*   |
+----------------+--------------+----------+
|                | size         | FALSE    |
+----------------+--------------+----------+
|                | rating       | FALSE    |
+----------------+--------------+----------+
|                | confidence   | FALSE    |
+----------------+--------------+----------+
| hosts          | hostName     | TRUE     |
+----------------+--------------+----------+
|                | dnsActive    | FALSE    |
+----------------+--------------+----------+
|                | whoisActive  | FALSE    |
+----------------+--------------+----------+
|                | rating       | FALSE    |
+----------------+--------------+----------+
|                | confidence   | FALSE    |
+----------------+--------------+----------+
| urls           | text         | TRUE     |
+----------------+--------------+----------+
|                | rating       | FALSE    |
+----------------+--------------+----------+
|                | confidence   | FALSE    |
+----------------+--------------+----------+

\*Files are required to be submitted with at least one valid hash.

Create Address Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: json

    POST /v2/indicators/addresses
    {
      "ip": "192.168.0.1",
      "rating": 5.0,
      "confidence": 100
    }

Create Email Address Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: json

    POST /v2/indicators/emailAddresses
    {
      "address": "badguy@example.com",
      "rating": 5.0,
      "confidence": 100
    }

Create File Indicators
^^^^^^^^^^^^^^^^^^^^^^

.. code:: json

    POST /v2/indicators/files
    {
      "md5": "2FFA00BB67FC936B01E3DE234A01A8D8",
      "sha1": "111EE6465425DF9A06CC14934DFFEE5EF36DE7E3",
      "sha256": "FD320CE6E64A816B3DC22DAE1AEA9B5D84C197E1265AE3880B3A2A45A543D051",
      "size": 5366,
      "rating": 5.0,
      "confidence": 100
    }

.. note:: A File Indicator requires only one, valid hash. It can be an md5, sha1, or sha256 (or any combination thereof).

Create Host Indicators
^^^^^^^^^^^^^^^^^^^^^^

.. code:: json

    POST /v2/indicators/hosts
    {
      "hostName": "example.com",
      "dnsActive": "false",
      "whoisActive": "true",
      "rating": 5.0,
      "confidence": 100
    }

Create URL Indicators
^^^^^^^^^^^^^^^^^^^^^

.. code:: json

    POST /v2/indicators/urls
    {
      "text": "http://example.com/bad.php",
      "rating": 5.0,
      "confidence": 100
    }

Create Indicator Metadata
-------------------------

Create Indicator Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add an attribute to an Indicator, use the following format:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/attributes
    {
      "type" : {attributeType},
      "value" : "Test Attribute",
      "displayed" : true
    }

For example, if you wanted to add a Description attribute to the Email Address ``bad@example.com``, you would use the following query:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/attributes
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

To add a Security Label to an attribute, use the following format where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the owner:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will add a ``TLP Amber`` Security Label to the attribute on the Threat:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/attributes/54321/securityLabels/TLP%20Amber

.. note:: In order to add a Security Label to an attribute, the Security Label must already exist. The query above will not create a new Security Label. If you specify a Security Label that does not exist, it will return an error.

Create Indicator Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add a Security Label to an Indicator, use the following format where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the owner:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/securityLabels/{securityLabel}

For example, the query below will add a ``TLP Amber`` Security Label to the Email Address ``bad@example.com``:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/securityLabels/TLP%20Amber

JSON Response:

.. code:: json
    
    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

.. note:: In order to add a Security Label to an Indicator, the Security Label must already exist. The query above will not create a new Security Label. If you specify a Security Label that does not exist, it will return an error.

Create Indicator Tags
^^^^^^^^^^^^^^^^^^^^^

To add a tag to an Indicator, use the following format where ``{tagName}`` is replaced with the name of the tag you wish to add to the Indicator:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/tags/{tagName}

For example, the query below will add the ``Nation State`` tag to the Email Address ``bad@example.com``:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/tags/Nation%20State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Create Indicator Associations
-----------------------------

Associate to a Group
^^^^^^^^^^^^^^^^^^^^

To associate an Indicator with a Group, use a query in the following format:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/groups/{associatedGroupType}/{associatedGroupId}

For example, the query below will associate the Email Address ``bad@example.com`` with an Incident with the ID 54321:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/groups/incidents/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Associate to an Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^

To associate an Indicator with another Indicator, use a query in the following format:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/indicators/{associatedIndicatorType}/{associatedIndicator}

For example, the query below will associate the Email Address ``bad@example.com`` with the IP Address ``0.0.0.0``:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/indicators/addresses/0.0.0.0

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Associate to a Victim
^^^^^^^^^^^^^^^^^^^^^

To associate an Indicator with a Victim, use a query in the following format:

.. code::

    POST /v2/indicators/{indicatorType}/{indicator}/victims/{victimId}

For example, the query below will associate the Email Address ``bad@example.com`` with the Victim with ID 54321:

.. code::

    POST /v2/indicators/emailAddresses/bad@example.com/victims/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }
