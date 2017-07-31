Filtering Groups
^^^^^^^^^^^^^^^^

When retrieving Groups from ThreatConnect, it is possible to filter the results. Results can be filtered on the following data points:

+------------+-----------+--------------+
| Filter     | Data Type | Operator(s)  |
+============+===========+==============+
| name       | string    | ``=``, ``^`` |
+------------+-----------+--------------+
| dateAdded  | date      | ``<``, ``>`` |
+------------+-----------+--------------+
| fileType\* | string    | ``=``        |
+------------+-----------+--------------+

\* The ``fileType`` filter only works for Documents.

.. include:: _includes/filter_symbol_encoding_note.rst

For example, the following query will return all groups that have been added since 2017-07-13 (``dateAdded>20170713``):

.. code::

    GET /v2/groups/?filters=dateAdded%3E20170713

The following query will return all groups that start with "Fancy" (``name^Fancy``):

.. code::

    GET /v2/groups/?filters=name%5EFancy

The following query will return all groups whose name is "Fancy" (``name=Fancy``):

.. code::

    GET /v2/groups/?filters=name%3DFancy

The following query will return all Documents that are PDFs (``fileType=PDF``):

.. code::

    GET /v2/groups/documents?filters=fileType%3DPDF
