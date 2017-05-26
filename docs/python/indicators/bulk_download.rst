Bulk Indicator Download
-----------------------

This section explains how to work with ThreatConnect Bulk Indicators.

**Supported API Filters**

The Bulk Download feature of the ThreatConnect API does not support any API filters.

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

Bulk Download Example
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :emphasize-lines: 1

    from threatconnect.Config.FilterOperator import FilterOperator

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # indicator object
    indicators = tc.bulk_indicators()
    owner = 'Example Community'

    # Add Post Filters
    try:
        filter1 = indicators.add_filter()
        filter1.add_owner(owner)
        filter1.add_pf_confidence(75, FilterOperator.GE)
        filter1.add_pf_rating('2.5', FilterOperator.GT)
    except AttributeError as e:
        print(e)
        sys.exit(1)

    # Retrieve Indicators and Apply Filters
    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    # Iterate Through Results
    for indicator in indicators:
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
        

This example will demonstrate how to retrieve Indicators while applying
filters. In this example, three filters will be added, one for the
Owner, one for the Confidence, and one for the Rating. The result set
returned from this example will contain any Indicators in the **"Example
Community"** Owner that has a Confidence greater than or equal to 75 and
a Rating greater than 2.5.

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial <#advanced-filtering>`__.

**Code Highlights**

+------------------------------------------+-------------------------------------------------------------------------------------------+
| Snippet                                  | Description                                                                               |
+==========================================+===========================================================================================+
| ``tc = ThreatConnect(api_access_id,...`` | Instantiate the ThreatConnect object.                                                     |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``indicators = tc.indicators()``         | Instantiate an Indicators container object.                                               |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``filter1 = indicator.add_filter()``     | Add a filter object to the Indicators container object (support multiple filter objects). |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``           | Add API filter to retrieve Indicators with the 'Example' tag.                             |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``indicator.retrieve()``                 | Trigger the API request and retrieve the Indicators intelligence data.                    |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``for indicator in indicators:``         | Iterate over the Indicators container object generator.                                   |
+------------------------------------------+-------------------------------------------------------------------------------------------+
| ``print(indicator.indicator)``           | Display the **'indicator'** property of the Indicator object.                             |
+------------------------------------------+-------------------------------------------------------------------------------------------+
