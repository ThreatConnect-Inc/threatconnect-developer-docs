Create PDF Report for Groups
----------------------------

As of ThreatConnect version 5.4, it is possible to create a report PDF for a group in ThreatConnect from the API. The general format for this request is as follows:

.. code-block::

    GET /v2/groups/{type}/{id}/pdf

This endpoint is available for all of the following group types:

- Adversaries
- Campaigns
- Emails
- Incidents
- Signatures
- Threats

.. note: This endpoint does not apply to Documents.
