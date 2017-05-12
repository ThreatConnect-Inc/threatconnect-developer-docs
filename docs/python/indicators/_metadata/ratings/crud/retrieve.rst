Retrieve Indicator Threat and Confidence Ratings
""""""""""""""""""""""""""""""""""""""""""""""""

The code snippet below demonstrates how to retrieve the threat and confidence ratings from an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner.

.. code-block:: python
    :emphasize-lines: 20-21,23-24

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()

    # set a filter to retrieve a specific host indicator: example.com
    filter1 = indicators.add_filter()
    filter1.add_indicator('example.com')

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for indicator in indicators:
        print(indicator.indicator)

        # print the indicator's threat rating
        print(indicator.rating)

        # print the indicator's confidence rating
        print(indicator.confidence)
