Retrieve Indicator Security Labels
""""""""""""""""""""""""""""""""""

The code snippet below demonstrates how to retrieve the security label from an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner and has a security label.

.. code-block:: python
    :emphasize-lines: 25-26

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

        # load the indicator's security label
        indicator.load_security_label()

        # if this indicator has a security label, print some information about the sec. label
        if indicator.security_label is not None:
            print(indicator.security_label.name)
            print(indicator.security_label.description)
            print(indicator.security_label.date_added)

.. warning:: Currently, the ThreatConnect Python SDK does not support multiple security labels. If an Indicator has multiple security labels, the Python SDK will only return one of them.
