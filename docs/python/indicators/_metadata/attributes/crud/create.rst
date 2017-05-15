Create Indicator Attributes
"""""""""""""""""""""""""""

The code snippet below demonstrates how to create an attribute on an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner.

.. code-block:: python
    :emphasize-lines: 25-26,28-29

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

        # add a description attribute that is displayed at the top of the indicator's page in ThreatConnect
        indicator.add_attribute('Description', 'Description Example', True)

        # add a description attribute that is not displayed at the top of the indicator's page in ThreatConnect
        indicator.add_attribute('Description', 'Description Example')

        # commit the changes
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
