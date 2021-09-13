Create PDF Report for Groups
----------------------------

As of ThreatConnect version 5.4, it is possible to create a PDF Report for a Group in ThreatConnect from the API. The general format for this request is as follows:

.. code::

    GET /v2/groups/{type}/{id}/pdf

.. note:: This endpoint applies to all Groups except for **Documents** and **Emails**.
