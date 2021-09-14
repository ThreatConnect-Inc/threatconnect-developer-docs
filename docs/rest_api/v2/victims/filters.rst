Filtering Victims
^^^^^^^^^^^^^^^^^

When retrieving Victims from ThreatConnect, it is possible to filter the results on the following data points:

+--------+-----------+----------+
| Filter | Data Type | Operator |
+========+===========+==========+
| name   | string    | ``=``    |
+--------+-----------+----------+

.. include:: ../_includes/filter_symbol_encoding_note.rst

The following query will return all Victims that start with "Example" (``name^Example``): 

.. code::

    GET /v2/victims/?filters=name%5EExample

The following query will return all Victims whose name is "Example Organization" (``name=Example Organization``):

.. code::

    GET /v2/victims/?filters=name%3DExample%20Organization
