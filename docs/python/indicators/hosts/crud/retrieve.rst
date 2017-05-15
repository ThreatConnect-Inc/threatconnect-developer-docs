Retrieve Hosts
^^^^^^^^^^^^^^

Retrieving a Single Host
""""""""""""""""""""""""

This example demonstrates how to retrieve a Host Indicator from the ThreatConnect platform. The ``add_indicator`` filter allows us to specify the specific Indicator we would like to retrieve.

.. code-block:: python
    :emphasize-lines: 10-12,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific Host Indicator
    filter1 = indicators.add_filter()
    filter1.add_indicator('example.com')

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # prove there is only one Indicator retrieved
    assert len(indicators) == 1

    # if the Host was found, print some information about it
    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

Retrieving DNS Resolutions
++++++++++++++++++++++++++

The example below demonstrates how to retrieve a Host Indicator's DNS Resolutions:

.. code-block:: python
    :emphasize-lines: 24-25,27-32

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific host indicator
    filter1 = indicators.add_filter()
    filter1.add_indicator('example.com')

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # if the host was found, print the dns resolutions
    for indicator in indicators:
        print(indicator.indicator)

        # load the DNS resolutions
        indicator.load_dns_resolutions()

        # iterate through the Host Indicator's DNS resolutions
        for dns in indicator.dns_resolutions:
            print(dns.ip)
            print(dns.owner_name)
            print(dns.resolution_date)
            print(dns.weblink)

.. note:: DNS Resolutions are only supported for the Host Indicator type.

Retrieving Multiple Hosts
"""""""""""""""""""""""""

This example demonstrates how to retrieve all Host Indicators in the default organization. The ``IndicatorType.HOSTS`` which is passed into the filter specifies which Indicator type we want to retrieve.

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

    # set a filter to retrieve Host Indicators
    filter1 = indicators.add_filter(IndicatorType.HOSTS)

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Hosts and print them
    for indicator in indicators:
        print(indicator)
