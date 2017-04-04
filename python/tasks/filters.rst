Filtering Tasks
---------------

This section provides the available filters which can be used when retrieving Tasks from ThreatConnect.

**Supported API Filters**

API filters use the API filtering feature to limit the result set returned from the API.

+--------------------------+-------------+--------------------------------------------+
| Filter                   | Value Type  | Description                                |
+==========================+=============+============================================+
| ``add_id()``             | int         | Filter Tasks by ID.                        |
+--------------------------+-------------+--------------------------------------------+
| ``add_adversary_id()``   | int         | Filter Tasks on associated Adversary ID.   |
+--------------------------+-------------+--------------------------------------------+
| ``add_document_id()``    | int         | Filter Tasks on associated Document ID.    |
+--------------------------+-------------+--------------------------------------------+
| ``add_email_id()``       | int         | Filter Tasks on associated Email ID.       |
+--------------------------+-------------+--------------------------------------------+
| ``add_incident_id()``    | int         | Filter Tasks on associated Incident ID.    |
+--------------------------+-------------+--------------------------------------------+
| ``add_indicator()``      | str         | Filter Tasks on associated Indicator.      |
+--------------------------+-------------+--------------------------------------------+
| ``add_owner()``          | list or str | Filter Tasks on associated Owner.          |
+--------------------------+-------------+--------------------------------------------+
| ``add_security_label()`` | str         | Filter Tasks on associated Security Label. |
+--------------------------+-------------+--------------------------------------------+
| ``add_signature_id()``   | int         | Filter Tasks on associated Signature ID.   |
+--------------------------+-------------+--------------------------------------------+
| ``add_tag()``            | str         | Filter Tasks on applied Tag.               |
+--------------------------+-------------+--------------------------------------------+
| ``add_threat_id()``      | int         | Filter Tasks on associated Threat ID.      |
+--------------------------+-------------+--------------------------------------------+
| ``add_victim_id()``      | int         | Filter Tasks on associated Victim ID.      |
+--------------------------+-------------+--------------------------------------------+

**Supported Post Filters**

Post filters are applied on the results returned by the API request.

+-------------------------+------------+-----------------------------+
| Filter                  | Value Type | Description                 |
+=========================+============+=============================+
| ``add_pf_name()``       | str        | Filter Tasks on name.       |
+-------------------------+------------+-----------------------------+
| ``add_pf_date_added()`` | str        | Filter Tasks on date added. |
+-------------------------+------------+-----------------------------+
