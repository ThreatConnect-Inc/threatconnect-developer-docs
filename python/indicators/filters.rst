Filtering Indicators
--------------------

This section provides the available filters which can be used when retrieving Indicators from ThreatConnect.

**Supported API Filters**

API filters use the API filtering feature to limit the result set returned from the API.

+--------------------------+-------------+------------------------------------------------+
| Filter                   | Value Type  | Description                                    |
+==========================+=============+================================================+
| ``add_adversary_id()``   | int         | Filter Indicators on associated Adversary ID.   |
+--------------------------+-------------+------------------------------------------------+
| ``add_document_id()``    | int         | Filter Indicators on associated Document ID.    |
+--------------------------+-------------+------------------------------------------------+
| ``add_email_id()``       | int         | Filter Indicators on associated Email ID.       |
+--------------------------+-------------+------------------------------------------------+
| ``add_incident_id()``    | int         | Filter Indicators on associated Incident ID.    |
+--------------------------+-------------+------------------------------------------------+
| ``add_indicator()``      | str         | Filter Indicators by Indicator value.           |
+--------------------------+-------------+------------------------------------------------+
| ``add_owner()``          | list or str | Filter Indicators by Owner.                     |
+--------------------------+-------------+------------------------------------------------+
| ``add_security_label()`` | str         | Filter Indicators on associated Security Label. |
+--------------------------+-------------+------------------------------------------------+
| ``add_signature_id()``   | int         | Filter Indicators on associated Signature ID.   |
+--------------------------+-------------+------------------------------------------------+
| ``add_tag()``            | str         | Filter Indicators on applied Tag.               |
+--------------------------+-------------+------------------------------------------------+
| ``add_threat_id()``      | int         | Filter Indicators on associated Threat ID.      |
+--------------------------+-------------+------------------------------------------------+
| ``add_victim_id()``      | int         | Filter Indicators on associated Victim ID.      |
+--------------------------+-------------+------------------------------------------------+

**Supported Post Filters**

Post filters are applied on the results returned by the API request.

+---------------------------------------+------------+------------------------------------------------+
| Filter                                | Value Type | Description                                    |
+=======================================+============+================================================+
| ``add_pf_attribute()``                | str        | Filter Indicators on Attribute type.           |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_confidence()``               | int        | Filter Indicators on Confidence value.         |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_date_added()``               | str        | Filter Indicators on date added.               |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_last_modified()``            | str        | Filter Indicators on last modified date.       |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_rating()``                   | str        | Filter Indicators on Rating.                   |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_tag()``                      | str        | Filter Indicators on Tag.                      |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_threat_assess_confidence()`` | int        | Filter Indicators on Threat Assess Confidence. |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_threat_assess_rating()``     | str        | Filter Indicators on Threat Assess Rating.     |
+---------------------------------------+------------+------------------------------------------------+
| ``add_pf_type()``                     | str        | Filter Indicators on Indicator type.           |
+---------------------------------------+------------+------------------------------------------------+
