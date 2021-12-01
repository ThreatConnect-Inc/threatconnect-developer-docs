Update Case Attributes
----------------------

The basic format for updating a Case Attribute is:

.. code::

    PUT /v3/caseAttributes/{caseAttributeId}
    {
      "value": "Case Attribute Value"
    }

Additional fields can be included when updating a Case Attribute to a Case, Refer to the following table for a list of available fields for the ``caseAttributes`` object:

+-----------+---------------------------------------------------+----------+------------------------+
| Field     | Description                                       | Type     | Example Value(s)       |
+===========+===================================================+==========+========================+
| source    | The Attribute's source                            | String   | "Hybrid analysis"      |
+-----------+---------------------------------------------------+----------+------------------------+
| value     | The Attribute's value                             | String   | "50"                   |
+-----------+---------------------------------------------------+----------+------------------------+
  
For example, the following query will update the ``value`` of a Case Attribute with ID 1.

.. code::

    POST /v3/caseAttributes/1
    {
      "value": "75"
    }

JSON Response:

.. code:: json

    {
      "data": {
          "id": 1,
          "type": "Detection Percentage",
          "value": "75",
          "source": "Hybrid analysis"
      },
      "message": "Updated",
      "status": "Success"
    }
