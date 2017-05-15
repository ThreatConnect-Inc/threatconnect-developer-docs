Delete Indicator Tags
"""""""""""""""""""""

The code snippet below demonstrates how to delete a tag from an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner and is tagged 'Test'.

.. code-block:: python
    :emphasize-lines: 22-23

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

        # remove the 'Test' tag from the indicator
        indicator.delete_tag('Test')

        # commit the indicator with the removed tag to ThreatConnect
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
