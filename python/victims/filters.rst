Filtering Victims
-----------------

This section provides the available filters which can be used when retrieving Victims from ThreatConnect.

**Supported API Filters**

API filters use the API filtering feature to limit the result set returned from the API.

+------------------------+-------------+--------------------------------------------+
| Filter                 | Value Type  | Description                                |
+========================+=============+============================================+
| ``add_id()``           | int         | Filter Victims by ID.                      |
+------------------------+-------------+--------------------------------------------+
| ``add_adversary_id()`` | int         | Filter Victims on associated Adversary ID. |
+------------------------+-------------+--------------------------------------------+
| ``add_document_id()``  | int         | Filter Victims on associated Document ID.  |
+------------------------+-------------+--------------------------------------------+
| ``add_email_id()``     | int         | Filter Victims on associated Email ID.     |
+------------------------+-------------+--------------------------------------------+
| ``add_incident_id()``  | int         | Filter Victims on associated Incident ID.  |
+------------------------+-------------+--------------------------------------------+
| ``add_indicator()``    | str         | Filter Victims on associated Indicator.    |
+------------------------+-------------+--------------------------------------------+
| ``add_owner()``        | list or str | Filter Victims on associated Owner.        |
+------------------------+-------------+--------------------------------------------+
| ``add_signature_id()`` | int         | Filter Victims on associated Signature ID. |
+------------------------+-------------+--------------------------------------------+
| ``add_threat_id()``    | int         | Filter Victims on associated Threat ID.    |
+------------------------+-------------+--------------------------------------------+

**Supported Post Filters**

Post filters are applied on the results returned by the API request.

+-------------------------+------------+-------------------------------+
| Filter                  | Value Type | Description                   |
+=========================+============+===============================+
| ``add_pf_name()``       | str        | Filter Victims on name.       |
+-------------------------+------------+-------------------------------+
| ``add_pf_date_added()`` | str        | Filter Victims on date added. |
+-------------------------+------------+-------------------------------+
