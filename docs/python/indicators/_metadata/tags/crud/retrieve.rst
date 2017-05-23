Retrieve Indicator Tags
"""""""""""""""""""""""

The code snippet below demonstrates how to retrieve the tags from an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner (and it works better if the host has some tags on it).

.. code-block:: python
    :emphasize-lines: 25-26

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific host indicator: example.com
    filter1 = indicators.add_filter()
    filter1.add_indicator('example.com')

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Indicators
    for indicator in indicators:
        print(indicator.indicator)

        # load the indicator's tags
        indicator.load_tags()

        # print details about each tag on the indicator
        for tag in indicator.tags:
            print(tag.name)
            print(tag.weblink)
