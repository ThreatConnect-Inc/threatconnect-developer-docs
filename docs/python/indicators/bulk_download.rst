Bulk Indicator Download
-----------------------

This section explains how to work with ThreatConnect Bulk Indicators.

**Supported API Filters**

+-----------------+-------------+-----------------------------+
| Filter          | Value Type  | Description                 |
+=================+=============+=============================+
| ``add_owner()`` | list or str | Filter Indicators by Owner. |
+-----------------+-------------+-----------------------------+

**Supported Post Filters**

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

Bulk Download Example
^^^^^^^^^^^^^^^^^^^^^

The ThreatConnect Python SDK has functionality to download Indicators from the ThreatConnect platform in bulk. The code snippet below demonstrates this capability

.. code-block:: python
    :emphasize-lines: 1,9-10,27-28

    from threatconnect.Config.FilterOperator import FilterOperator

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # Bulk Indicator object
    indicators = tc.bulk_indicators()

    owner = 'Example Community'

    # add a Filter and Post Filters
    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        # only download Indicators with a confidence rating greater than or equal to 75
        filter1.add_pf_confidence(75, FilterOperator.GE)
        # only download Indicators with a threat rating greater than 2.5
        filter1.add_pf_rating('2.5', FilterOperator.GT)
    except AttributeError as e:
        print(e)
        sys.exit(1)

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    # iterate through the results
    for indicator in indicators:
        # if the Indicator is a File Indicator or custom Indicator, print it out appropriately
        if isinstance(indicator.indicator, dict):
            for indicator_type, indicator_value in indicator.indicator.items():
                print('{0}: {1}'.format(indicator_type, indicator_value))
        else:
            print(indicator.indicator)

        print(indicator.id)
        print(indicator.owner_name)
        print(indicator.date_added)
        print(indicator.last_modified)
        print(indicator.rating)
        print(indicator.threat_assess_rating)
        print(indicator.confidence)
        print(indicator.threat_assess_confidence)
        print(indicator.type)
        print(indicator.weblink)

.. warning:: In order to use the bulk download capability, the "Enable Bulk Indicators" setting must be selected for the owner from which you want to download the data. Check with your ThreatConnect System Administrator if you have any questions.
