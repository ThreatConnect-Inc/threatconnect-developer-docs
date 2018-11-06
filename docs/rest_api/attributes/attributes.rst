Attributes
==========

Attributes are key/value data sets that can be added to any Group, Indicator, Task, or Victim. This type of metadata provides an excellent way to organize, categorize, and capture the context around items in ThreatConnect.

Retrieving Attributes
---------------------

The general formats for retrieving the attributes on an item are:

- Groups: ``GET /v2/groups/{groupType}/{groupId}/attributes``
- Indicators: ``GET /v2/indicators/{indicatorType}/{indicator}/attributes``
- Tasks: ``GET /v2/tasks/{taskId}/attributes``
- Victims: ``GET /v2/victims/{victimId}/attributes``

Additional Parameters
"""""""""""""""""""""

Attributes API paths will display XID when includes=additional or includeAdditional=true:

.. code::

    /api/v2/indicators/hosts/bad.com/attributes?includes=additional
    /api/v2/indicators/hosts/bad.com/attributes/3?includes=additional

Adding Attributes
-----------------

The general formats for adding attributes on items are:

- Groups: ``POST /v2/groups/{groupType}/{groupId}/attributes``
- Indicators: ``POST /v2/indicators/{indicatorType}/{indicator}/attributes``
- Tasks: ``POST /v2/tasks/{taskId}/attributes``
- Victims: ``POST /v2/victims/{victimId}/attributes``

The body of the POST request can contain the following fields:

+-------------+----------+------------------------+
| Field       | Required | Example Value          |
+=============+==========+========================+
| type        | TRUE     | 'Description'          |
+-------------+----------+------------------------+
| value       | TRUE     | 'Example description.' |
+-------------+----------+------------------------+
| displayed\* | FALSE    | true                   |
+-------------+----------+------------------------+
| source      | FALSE    | 'Hybrid Analysis'      |
+-------------+----------+------------------------+

\* The ``displayed`` field is only applicable for Source and Description attributes.

Updating Attributes
-------------------

The general formats for updating attributes on items are:

- Groups: ``PUT /v2/groups/{groupType}/{groupId}/attributes/{attributeId}``
- Indicators: ``PUT /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}``
- Tasks: ``PUT /v2/tasks/{taskId}/attributes/{attributeId}``
- Victims: ``PUT /v2/victims/{victimId}/attributes/{attributeId}``

The body of the PUT request can contain the following fields:

+-----------+----------+------------------------+
| Field     | Required | Example Value          |
+===========+==========+========================+
| value     | TRUE     | 'Updated description.' |
+-----------+----------+------------------------+
| displayed | FALSE    | true                   |
+-----------+----------+------------------------+
| source    | FALSE    | 'Hybrid Analysis'      |
+-----------+----------+------------------------+

Deleting Attributes
-------------------

The general formats for deleting attributes from items are:

- Groups: ``DELETE /v2/groups/{groupType}/{groupId}/attributes/{attributeId}``
- Indicators: ``DELETE /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}``
- Tasks: ``DELETE /v2/tasks/{taskId}/attributes/{attributeId}``
- Victims: ``DELETE /v2/victims/{victimId}/attributes/{attributeId}``
