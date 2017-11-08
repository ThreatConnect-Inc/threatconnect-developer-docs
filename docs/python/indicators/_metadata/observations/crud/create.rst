Create Indicator Observations
"""""""""""""""""""""""""""""

The code snippet below demonstrates how to add observations to an Indicator.

.. code-block:: python
    :emphasize-lines: 27-28,30-31,33-34

    from datetime import datetime

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

        # add two observations to the Indicator
        indicator.add_observation(2)

        # you can also include a date observed when adding observations
        # indicator.add_observation(2, datetime.isoformat(datetime.today()) + 'Z')

        # commit the changes to ThreatConnect
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
