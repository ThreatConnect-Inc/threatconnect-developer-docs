Retrieve Email Addresses
^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a Single Email Address
"""""""""""""""""""""""""""""""""

This example demonstrates how to retrieve an Email Address Indicator from the ThreatConnect platform. The ``add_indicator`` filter allows us to specify the specific Indicator we would like to retrieve.

.. code-block:: python
    :linenos:
    :emphasize-lines: 8-10,13-14

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate an Indicators object
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

    # prove that there is only one Indicator retrieved
    assert len(indicators) == 1

    # if the Email Address was found, print some information about it
    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

Retrieving Multiple Email Addresses
"""""""""""""""""""""""""""""""""""

This example demonstrates how to retrieve all Email Address Indicators in the default organization. The ``IndicatorType.EMAIL_ADDRESSES`` which is passed into the filter specifies which Indicator type we want to retrieve.

.. code-block:: python
    :linenos:
    :emphasize-lines: 1-2,11-12,15-16

    # this import allows us to specify which Indicator type we want to retrieve
    from threatconnect.Config.IndicatorType import IndicatorType

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
