Retrieve Indicator Tags
"""""""""""""""""""""""

The code snippet below demonstrates how to retrieve the tags from an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner (and it works better if the host has some tags on it).

.. code:: python

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

        # load the indicator's tags
        indicator.load_tags()

        # print details about each tag on the indicator
        for tag in indicator.tags:
            print(tag.name)
            print(tag.weblink)
