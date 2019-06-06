Filtering Groups
^^^^^^^^^^^^^^^^

Filters Parameter
"""""""""""""""""

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

.. include:: ../_includes/filter_symbol_encoding_note.rst

**Examples**

The following query will return all Groups that start with "Fancy" (``name^Fancy``):

.. code::

    GET /v2/groups/?filters=name%5EFancy

The following query will return all Groups whose name is "Fancy" (``name=Fancy``):

.. code::

    GET /v2/groups/?filters=name%3DFancy

The following query will return all Groups that have been added since 2017-07-13 (``dateAdded>2017-07-13``):

.. code::

    GET /v2/groups/?filters=dateAdded%3E2017-07-13

The following query will return all Campaigns that have an first-seen date after 2017-07-13 (``firstSeen>2017-07-13T00:00``):

.. code::

    GET /v2/groups/campaigns?filters=firstSeen%3E2017-07-13T00:00

The following query will return all Documents that are PDFs (``fileType=PDF``):

.. code::

    GET /v2/groups/documents?filters=fileType%3DPDF

The following query will return all Incidents that have an event date after 2017-07-13 (``eventDate>2017-07-13T00:00``):

.. code::

    GET /v2/groups/incidents?filters=eventDate%3E2017-07-13T00:00

Owner Parameter
"""""""""""""""

By default, all API calls will operate in the API user account's default organization. To specify a different Owner, use the ``owner`` URL parameter as in ``?owner={ownerName}``. For example, the following query will return all Incidents in the Common Community:

.. code::

    GET /v2/groups/incidents/?owner=Common%20Community
    
Additional Parameters
"""""""""""""""""""""

Group API paths will display XID when includes=additional or includeAdditional=true:

.. code::

    /api/v2/groups/adversaries/4?includeAdditional=True
    /api/v2/groups/adversaries/4?includes=additional
