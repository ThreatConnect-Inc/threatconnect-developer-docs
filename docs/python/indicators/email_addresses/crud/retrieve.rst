Retrieve Email Addresses
^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a Single Email Address
"""""""""""""""""""""""""""""""""

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific email address indicator
    filter1 = indicators.add_filter()
    filter1.add_indicator('badguy@example.com')

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # if the email address was found, print some information about it
    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

This example demonstrates how to retrieve a specific email address indicator. The ``add_indicator`` filter allows us to specify the email address which we would like to retrieve.

Retrieving Multiple Email Addresses
"""""""""""""""""""""""""""""""""""

.. code-block:: python
    :linenos:

    # this import allows us to specify which indicator type we want to import
    from threatconnect.Config.IndicatorType import IndicatorType

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()

    # set a filter to retrieve email address indicators
    filter1 = indicators.add_filter(IndicatorType.EMAIL_ADDRESSES)

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

This example demonstrates how to retrieve all email address indicators in the default organization. The ``IndicatorType.EMAIL_ADDRESSES`` which is passed into the filter specifies which indicator type we want to retrieve.
