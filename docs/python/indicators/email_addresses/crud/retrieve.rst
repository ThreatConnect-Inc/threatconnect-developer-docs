Retrieve Email Addresses
^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a Single Email Address
"""""""""""""""""""""""""""""""""

This example demonstrates how to retrieve an Email Address Indicator from the ThreatConnect platform. The ``add_indicator`` filter allows us to specify the specific Indicator we would like to retrieve.

.. code-block:: python
    :emphasize-lines: 10-12,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific Email Address Indicator
    filter1 = indicators.add_filter()
    filter1.add_indicator('badguy@example.com')

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # prove there is only one Indicator retrieved
    assert len(indicators) == 1

    # if the Email Address was found, print some information about it
    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

Retrieving Multiple Email Addresses
"""""""""""""""""""""""""""""""""""

This example demonstrates how to retrieve all Email Address Indicators in the default organization. The ``IndicatorType.EMAIL_ADDRESSES`` which is passed into the filter specifies which Indicator type we want to retrieve.

.. code-block:: python
    :emphasize-lines: 1-2,13-14,17-18

    # this import allows us to specify which Indicator type we want to retrieve
    from threatconnect.Config.IndicatorType import IndicatorType

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    # set a filter to retrieve Email Address Indicators
    filter1 = indicators.add_filter(IndicatorType.EMAIL_ADDRESSES)

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Email Addresses and print them
    for indicator in indicators:
        print(indicator)
