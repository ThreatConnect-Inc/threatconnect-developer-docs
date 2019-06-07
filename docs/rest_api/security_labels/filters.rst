Filtering Security Labels
^^^^^^^^^^^^^^^^^^^^^^^^^

When retrieving Security Labels from ThreatConnect, it is possible to filter the results on the following data points: 

+--------+-----------+--------------+
| Filter | Data Type | Operator(s)  |
+========+===========+==============+
| name   | string    | ``=``, ``^`` |
+--------+-----------+--------------+

.. include:: ../_includes/filter_symbol_encoding_note.rst

The following query will return all Security Labels that start with "TLP" (``name^TLP``):

.. code::

    GET /v2/securityLabels/?filters=name%5ETLP

The following query will return the Security Label with the name "TLP:Green" (``name=TLP:Green``):

.. code::

    GET /v2/securityLabels/?filters=name%3DTLP%3AGreen
