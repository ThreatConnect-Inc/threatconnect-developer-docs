Filtering Groups
^^^^^^^^^^^^^^^^

When retrieving Groups from ThreatConnect, it is possible to filter the results. Results can be filtered on the following data points:

+-------------------------------+-----------+--------------+
| Filter                        | Data Type | Operator(s)  |
+===============================+===========+==============+
| name                          | string    | ``=``, ``^`` |
+-------------------------------+-----------+--------------+
| dateAdded                     | date      | ``<``, ``>`` |
+-------------------------------+-----------+--------------+
| **Campaign Specific Filters** |           |              |
+-------------------------------+-----------+--------------+
| firstSeen                     | date      | ``<``, ``>`` |
+-------------------------------+-----------+--------------+
| **Document Specific Filters** |           |              |
+-------------------------------+-----------+--------------+
| fileType                      | string    | ``=``        |
+-------------------------------+-----------+--------------+
| **Incident Specific Filters** |           |              |
+-------------------------------+-----------+--------------+
| eventDate                     | date      | ``<``, ``>`` |
+-------------------------------+-----------+--------------+

.. include:: _includes/filter_symbol_encoding_note.rst

The following query will return all Groups that start with "Fancy" (``name^Fancy``):

.. code::

    GET /v2/groups/?filters=name%5EFancy

The following query will return all Groups whose name is "Fancy" (``name=Fancy``):

.. code::

    GET /v2/groups/?filters=name%3DFancy

For example, the following query will return all Groups that have been added since 2017-07-13 (``dateAdded>20170713``):

.. code::

    GET /v2/groups/?filters=dateAdded%3E20170713

The following query will return all Campaigns that have an first-seen date after 2017-07-13 (``firstSeen>2017-07-13T00:00``):

.. code::

    GET /v2/groups/incidents?filters=firstSeen%3E2017-07-13T00:00

The following query will return all Documents that are PDFs (``fileType=PDF``):

.. code::

    GET /v2/groups/documents?filters=fileType%3DPDF

The following query will return all Incidents that have an event date after 2017-07-13 (``eventDate>2017-07-13T00:00``):

.. code::

    GET /v2/groups/incidents?filters=eventDate%3E2017-07-13T00:00
