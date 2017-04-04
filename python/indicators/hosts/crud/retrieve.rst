Retrieve Hosts
^^^^^^^^^^^^^^

Retrieving a Single Host
""""""""""""""""""""""""

.. code:: python

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

    # if the host was found, print some information about it
    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

This example demonstrates how to retrieve a specific host indicator. The ``add_indicator`` filter allows us to specify the host which we would like to retrieve.

Retrieving DNS Resolutions
++++++++++++++++++++++++++

The example below demonstrates how to retrieve a Host Indicator's DNS Resolutions:

.. code:: python

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

        indicator.load_dns_resolutions()
        for dns in indicator.dns_resolutions:
            print(dns.ip)
            print(dns.owner_name)
            print(dns.resolution_date)
            print(dns.weblink)

.. note:: DNS Resolutions are only supported for the Host Indicator type.

**Code Highlights**

+-------------------------------------------+---------------------------------------------------------------------+
| Snippet                                   | Description                                                         |
+===========================================+=====================================================================+
| ``indicator.load_dns_resolutions()``      | Trigger API call to load DNS Resolutions into the Indicator object. |
+-------------------------------------------+---------------------------------------------------------------------+
| ``for dns in indicator.dns_resolutions:`` | Iterate over the DNS Resolutions property object generator.         |
+-------------------------------------------+---------------------------------------------------------------------+
| ``print(dns.ip)``                         | Display the **'ip'** property of the Attribute object.              |
+-------------------------------------------+---------------------------------------------------------------------+

Retrieving Multiple Hosts
"""""""""""""""""""""""""

.. code:: python

    # this import allows us to specify which indicator type we want to import
    from threatconnect.Config.IndicatorType import IndicatorType

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()

    # set a filter to retrieve file indicators
    filter1 = indicators.add_filter(IndicatorType.HOSTS)

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

This example demonstrates how to retrieve all host indicators in the default organization. The ``IndicatorType.HOSTS`` which is passed into the filter specifies which indicator type we want to retrieve.
