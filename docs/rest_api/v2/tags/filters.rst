Filtering Tags
^^^^^^^^^^^^^^

When retrieving Tags from ThreatConnect, it is possible to filter on the following data points:

+----------+-----------+---------------------+
| Filter   | Data Type | Operator(s)         |
+==========+===========+=====================+
| name     | string    | ``=``, ``^``        |
+----------+-----------+---------------------+
| weight\* | integer   | ``=``, ``<``, ``>`` |
+----------+-----------+---------------------+

\* In the context of Tags, 'weight' refers to how many times a Tag has been used.

.. include:: ../_includes/filter_symbol_encoding_note.rst

The following query will return all Tags that start with "Bad" (``name^Bad``):

.. code::

    GET /v2/tags/?filters=name%5EBad

The following query will return all Tags whose name is "Bad" (``name=Bad``):

.. code::

    GET /v2/tags/?filters=name%3DBad

The following query will return all Tags with a weight greater than 2 (``weight>2``): 

.. code::

    GET /v2/tags/?filters=weight%3E2
