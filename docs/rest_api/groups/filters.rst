Filtering Groups
^^^^^^^^^^^^^^^^

When retrieving Groups from ThreatConnect, it is possible to filter the results. Results can be filtered on the following data points:

+------------+-----------+-------------+
| Filter     | Data Type | Operator(s) |
+============+===========+=============+
| name       | string    | =           |
+------------+-----------+-------------+
| dateAdded  | date      | =<>         |
+------------+-----------+-------------+
| fileType\* | string    | =           |
+------------+-----------+-------------+

\* The ``fileType`` filter only works for Documents.

For example, the following query will return all groups that have been added since 2017-07-13 (``dateAdded>2017-07-13``):

.. code::

    GET /v2/groups/?filters=dateAdded%3E2017-07-13

The following query will return all groups that start with "Fancy" (``name^Fancy``):

.. code::

    GET /v2/groups/?filters=name%5EFancy

The following query will return all groups whose name is "Fancy" (``name=Fancy``):

.. code::

    GET /v2/groups/?filters=name%3DFancy
