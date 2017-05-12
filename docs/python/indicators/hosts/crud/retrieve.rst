Retrieve Hosts
^^^^^^^^^^^^^^

Retrieving a Single Host
""""""""""""""""""""""""

This example demonstrates how to retrieve a Host Indicator from the ThreatConnect platform. The ``add_indicator`` filter allows us to specify the specific Indicator we would like to retrieve.

.. code-block:: python
    :emphasize-lines: 8-10,13-14

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
    :emphasize-lines: 22-23,25-30

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific host indicator
    filter1 = indicators.add_filter()
    filter1.add_indicator('example.com')

    try:
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
    :emphasize-lines: 1-2,11-12,15-16

    # this import allows us to specify which Indicator type we want to retrieve
    from threatconnect.Config.IndicatorType import IndicatorType

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
