Filtering Indicators
--------------------

This section provides the available filters which can be used when retrieving Indicators from ThreatConnect.

**Supported API Filters**

API filters use the API filtering feature to limit the result set returned from the API.

+--------------------------+-------------+-----------------------------------------------+
| Filter                   | Value Type  | Description                                   |
+==========================+=============+===============================================+
| ``add_adversary_id()``   | int         | Filter Indicators on associated Adversary ID. |
+--------------------------+-------------+-----------------------------------------------+
| ``add_campaign_id()``    | int         | Filter Indicators on associated Campaign ID.  |
+--------------------------+-------------+-----------------------------------------------+
| ``add_document_id()``    | int         | Filter Indicators on associated Document ID.  |
+--------------------------+-------------+-----------------------------------------------+
| ``add_email_id()``       | int         | Filter Indicators on associated Email ID.     |
+--------------------------+-------------+-----------------------------------------------+
| ``add_incident_id()``    | int         | Filter Indicators on associated Incident ID.  |
+--------------------------+-------------+-----------------------------------------------+
| ``add_indicator()``      | str         | Filter Indicators by Indicator value.         |
+--------------------------+-------------+-----------------------------------------------+
| ``add_owner()``          | list or str | Filter Indicators by Owner.                   |
+--------------------------+-------------+-----------------------------------------------+
| ``add_security_label()`` | str         | Filter Indicators on applied Security Label.  |
+--------------------------+-------------+-----------------------------------------------+
| ``add_signature_id()``   | int         | Filter Indicators on associated Signature ID. |
+--------------------------+-------------+-----------------------------------------------+
| ``add_tag()``            | str         | Filter Indicators on applied Tag.             |
+--------------------------+-------------+-----------------------------------------------+
| ``add_task_id()``        | int         | Filter Indicators on associated Task ID.      |
+--------------------------+-------------+-----------------------------------------------+
| ``add_threat_id()``      | int         | Filter Indicators on associated Threat ID.    |
+--------------------------+-------------+-----------------------------------------------+
| ``add_victim_id()``      | int         | Filter Indicators on associated Victim ID.    |
+--------------------------+-------------+-----------------------------------------------+

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


The example below demonstrates how to use each of the post filters listed above:

.. code-block:: python
    :linenos:
    :emphasize-lines: 1,3,19-20,22-23,25-28,30-31,33-34,36-37,39-40,42-43,45-46,48-49

    import datetime

    from threatconnect.Config.FilterOperator import FilterOperator

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # create an Indicators object
    indicators = tc.indicators()

    owner = 'Example Community'

    filter1 = indicators.add_filter()

    # only retrieve Indicators from the given owner
    filter1.add_owner(owner)

    # add a filter for Indicators that contain a 'Description' attribute
    filter1.add_pf_attribute('Description', FilterOperator.EQ)

    # add a filter for Indicators with a confidence rating greater than or equal to 50
    filter1.add_pf_confidence(50, FilterOperator.GE)

    # get a datestamp for the past week
    today = datetime.datetime.today()
    delta = datetime.timedelta(days = 7)
    previous_week_datestamp = (today - delta).isoformat() + 'Z'

    # add a filter for Indicators that have been added at a date greater (thus, more recent) than a week ago
    filter1.add_pf_date_added(previous_week_datestamp, FilterOperator.GT)

    # add a filter for Indicators that have been modified at a date greater (thus, more recent) than a week ago
    filter1.add_pf_last_modified(previous_week_datestamp, FilterOperator.GT)

    # add a filter for Indicators that have a threat rating greater than or equal to 3
    filter1.add_pf_rating(3, FilterOperator.GE)

    # add a filter for Indicators that have a threat assess confidence rating greater than or equal to 50
    filter1.add_pf_threat_assess_confidence(50, FilterOperator.GE)

    # add a filter for Indicators that have a threat assess threat rating greater than or equal to 3
    filter1.add_pf_threat_assess_rating(3, FilterOperator.GE)

    # add a filter for Indicators to return only Address Indicators
    filter1.add_pf_type('Address', FilterOperator.EQ)

    # alternatively, add a filter for Indicators to return all indicators that are NOT Address Indicators
    filter1.add_pf_type('Address', FilterOperator.NE)

    try:
        # retrieve Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for indicator in indicators:
        print(indicator.id)
        print(indicator.name)
        print(indicator.date_added)
        print(indicator.weblink)
        print('')

.. note:: The example above will first retrieve *all* of the Indicators from the owner and will then apply the post filter(s).
