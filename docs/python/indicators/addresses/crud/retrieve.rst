Retrieve IP Addresses
^^^^^^^^^^^^^^^^^^^^^

Retrieving a Single Address
"""""""""""""""""""""""""""

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific address indicator
    filter1 = indicators.add_filter()
    filter1.add_indicator('192.168.0.1')

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # if the address was found, print some information about it
    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

This example demonstrates how to retrieve a specific IP address indicator. The ``add_indicator`` filter allows us to specify the address which we would like to retrieve.

Retrieving Multiple Addresses
"""""""""""""""""""""""""""""

.. code-block:: python
    :linenos:

    # this import allows us to specify which indicator type we want to import
    from threatconnect.Config.IndicatorType import IndicatorType

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()

    # set a filter to retrieve file indicators
    filter1 = indicators.add_filter(IndicatorType.ADDRESSES)

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

This example demonstrates how to retrieve all IP address indicators in the default organization. The ``IndicatorType.ADDRESSES`` which is passed into the filter specifies which indicator type we want to retrieve.
