Create Victims
--------------

To create a Victim, the most basic format is:

.. code::

    POST /v2/victims/
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

By way of example, the query below will create a Victim in the default owner:

.. code::

    POST /v2/victims/
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

Create Victim Metadata
----------------------

Create Victim Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

To add an Attribute to a Victim, use the following format:

.. code::

    POST /v2/victims/{victimId}/attributes
    {
      "type" : {attributeType},
      "value" : "Test Attribute",
      "displayed" : true
    }

For example, if you wanted to add a Description attribute to the Victim with ID 12345, you would use the following query:

.. code::

    POST /v2/victims/12345/attributes
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

    POST /v2/victims/{victimId}/attributes/{attributeId}/securityLabels/{securityLabel}

For example, the query below will add a ``TLP Amber`` Security Label to the attribute on the Victim:

.. code::

    POST /v2/victims/12345/attributes/54321/securityLabels/TLP%20Amber

.. note:: In order to add a Security Label to an attribute, the Security Label must already exist. The query above will not create a new Security Label. If you specify a Security Label that does not exist, it will return an error.

Create Victim Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add a Security Label to a Victim, use the following format where ``{securityLabel}`` is replaced with the name of a Security Label that already exists in the owner:

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

To add a tag to a Victim, use the following format where ``{tagName}`` is replaced with the name of the tag you wish to add to the Victim:

.. code::

    POST /v2/victims/{victimId}/tags/{tagName}

For example, the query below will add the ``Nation State`` tag to the Victim with ID 12345:

.. code::

    POST /v2/victims/12345/tags/Nation%20State

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Create Victim Associations
--------------------------

Associate to a Group
^^^^^^^^^^^^^^^^^^^^

To associate a Victim with a Group, use a query in the following format:

.. code::

    POST /v2/victims/{victimId}/groups/{associatedGroupType}/{associatedGroupId}

For example, the query below will associate a Victim with ID 12345 with an Incident with the ID 54321:

.. code::

    POST /v2/victims/12345/groups/incidents/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Associate to an Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^

To associate a Victim with an Indicator, use a query in the following format:

.. code::

    POST /v2/victims/{victimId}/indicators/{associatedIndicatorType}/{associatedIndicator}

For example, the query below will associate the Victim with ID 12345 with the IP Address ``0.0.0.0``:

.. code::

    POST /v2/victims/12345/indicators/addresses/0.0.0.0

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }

Associate to a Victim
^^^^^^^^^^^^^^^^^^^^^

To associate one Victim with another, use a query in the following format:

.. code::

    POST /v2/victims/{victimId}/victims/{victimId}

For example, the query below will associate the Victim with ID 12345 to the Victim with ID 54321:

.. code::

    POST /v2/victims/12345/victims/54321

JSON Response:

.. code:: json

    {
      "apiCalls": 1,
      "resultCount": 0,
      "status": "Success"
    }
