Attributes
==========

Attributes are key/value data sets that can be added to any Group, Indicator, Task, or Victim. This type of metadata provides an excellent way to organize, categorize, and capture the context around items in ThreatConnect.

Retrieving Attributes
---------------------

The general formats for retrieving the Attributes on an item are:

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

The general formats for adding Attributes on items are:

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

Retrieving Available Attributes
---------------------------------

All of the available Attributes can be viewed by making a ``GET`` request to ``/v2/types/attributeTypes``. This will return the name of the Attribute. Note that this branch also supports the following filters: owner, system, allowMarkdown, and maxLength. To return an Attribute type:

.. code::

    GET /v2/types/attributeTypes/

To retrieve information about a specific Attribute, use the following GET request format:

.. code::

    GET /v2/types/attributeTypes/{attributeTypeName}/

For example, the GET request below will return details about the ``Source`` Attribute type:

.. code::

    GET /v2/types/attributeTypes/Source/

Note that an "includes=validationRule" parameter returns the validationRule objects for the attributeTypes.

Updating Attributes
-------------------

The general formats for updating Attributes on items are:

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

The general formats for deleting Attributes from items are:

- Groups: ``DELETE /v2/groups/{groupType}/{groupId}/attributes/{attributeId}``
- Indicators: ``DELETE /v2/indicators/{indicatorType}/{indicator}/attributes/{attributeId}``
- Tasks: ``DELETE /v2/tasks/{taskId}/attributes/{attributeId}``
- Victims: ``DELETE /v2/victims/{victimId}/attributes/{attributeId}``
