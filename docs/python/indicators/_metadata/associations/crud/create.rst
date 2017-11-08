Create Indicator Associations
"""""""""""""""""""""""""""""

The code snippet below demonstrates how to create an association between an Indicator and a Group, Indicator, or Victim in ThreatConnect. This example assumes a host indicator ``example.com`` exists in the target owner.

.. code-block:: python
    :emphasize-lines: 1,27-28,30-31,33-34,36-37

    from threatconnect.Config.ResourceType import ResourceType

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
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

        # create an association between this indicator and the incident with the ID: 123456
        indicator.associate_group(ResourceType.INCIDENTS, 123456)

        # create an association between this indicator and the URL indicator: http://example.com/
        indicator.associate_indicator(ResourceType.URLS, 'http://example.com/')

        # create an association between this indicator and the victim with the ID: 123456
        indicator.associate_victim(123456)

        # commit the changes to ThreatConnect
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
