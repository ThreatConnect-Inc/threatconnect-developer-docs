Update Victims
--------------

To update a Victim, the basic format is:

.. code::

    PUT /v2/victims/{victimId}
    {
      {updatedField}: {updatedValue}
    }

When updating a Victim, you can change any of the fields below in addition to the required ``name`` field:

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

By way of example, the query below will update the name of a Victim with ID 12345:

.. code::

    PUT /v2/victims/12345
    {
      "name": "New Victim Name",
    }

JSON Response:

.. code:: json

    {
      "status": "Success",
      "data": {
        "victim": {
          "id": 54321,
          "name": "New Victim Name",
          "webLink": "https://app.threatconnect.com/auth/victim/victim.xhtml?victim=54321"
        }
      }
    }

Update Victim Metadata
----------------------

Update Victim Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

To update a Victim's attribute, use the following format:

.. code::

    PUT /v2/victims/{victimId}/attributes/{attributeId}
    {
      {updatedField}: {updatedValue}
    }

When updating attributes, you can change the following fields:

+----------------------------+----------+
| Updatable Attribute Fields | Required |
+============================+==========+
| value                      | TRUE     |
+----------------------------+----------+
| displayed                  | FALSE    |
+----------------------------+----------+
| source                     | FALSE    |
+----------------------------+----------+

For example, if you wanted to update the value of an attribute with ID 54321 on the Victim with ID 12345, you would use the following query:

.. code::

    PUT /v2/victims/12345/attributes/54321
    {
      "value": "New attribute value."
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
          "lastModified": "2017-07-19T15:54:12Z",
          "displayed": true,
          "value": "New attribute value."
        }
      }
    }
