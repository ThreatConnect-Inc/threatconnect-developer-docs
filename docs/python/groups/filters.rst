Filtering Groups
----------------

This section provides the available filters which can be used when retrieving Groups from ThreatConnect.

**Supported API Filters**

API filters use the API filtering feature to limit the result set returned from the API.

+--------------------------+-------------+-------------------------------------------+
| Filter                   | Value Type  | Description                               |
+==========================+=============+===========================================+
| ``add_id()``             | int         | Filter Groups by ID.                      |
+--------------------------+-------------+-------------------------------------------+
| ``add_adversary_id()``   | int         | Filter Groups on associated Adversary ID. |
+--------------------------+-------------+-------------------------------------------+
| ``add_campaign_id()``    | int         | Filter Groups on associated Campaign ID.  |
+--------------------------+-------------+-------------------------------------------+
| ``add_document_id()``    | int         | Filter Groups on associated Document ID.  |
+--------------------------+-------------+-------------------------------------------+
| ``add_email_id()``       | int         | Filter Groups on associated Email ID.     |
+--------------------------+-------------+-------------------------------------------+
| ``add_incident_id()``    | int         | Filter Groups on associated Incident ID.  |
+--------------------------+-------------+-------------------------------------------+
| ``add_indicator()``      | str         | Filter Groups on associated Indicator.    |
+--------------------------+-------------+-------------------------------------------+
| ``add_owner()``          | list or str | Filter Groups on Owner.                   |
+--------------------------+-------------+-------------------------------------------+
| ``add_security_label()`` | str         | Filter Groups on applied Security Label.  |
+--------------------------+-------------+-------------------------------------------+
| ``add_signature_id()``   | int         | Filter Groups on associated Signature ID. |
+--------------------------+-------------+-------------------------------------------+
| ``add_tag()``            | str         | Filter Groups on applied Tag.             |
+--------------------------+-------------+-------------------------------------------+
| ``add_task_id()``        | int         | Filter Groups on associated Task ID.      |
+--------------------------+-------------+-------------------------------------------+
| ``add_threat_id()``      | int         | Filter Groups on associated Threat ID.    |
+--------------------------+-------------+-------------------------------------------+
| ``add_victim_id()``      | int         | Filter Groups on associated Victim ID.    |
+--------------------------+-------------+-------------------------------------------+

**Supported Post Filters**

Post filters are applied on the results returned by the API request.

+-------------------------+------------+------------------------------+
| Filter                  | Value Type | Description                  |
+=========================+============+==============================+
| ``add_pf_name()``       | str        | Filter Groups on name.       |
+-------------------------+------------+------------------------------+
| ``add_pf_date_added()`` | str        | Filter Groups on date added. |
+-------------------------+------------+------------------------------+
