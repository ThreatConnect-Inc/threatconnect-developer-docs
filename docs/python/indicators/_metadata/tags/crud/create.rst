Create Indicator Tags
"""""""""""""""""""""

The code snippet below demonstrates how to add a tag to an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner.

.. code-block:: python
    :emphasize-lines: 20-21

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

        # add the 'Test' tag to the indicator
        indicator.add_tag('Test')

        # commit the indicator with the new tag to ThreatConnect
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
