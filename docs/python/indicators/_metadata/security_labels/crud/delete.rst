Delete Indicator Security Labels
""""""""""""""""""""""""""""""""

The code snippet below demonstrates how to delete a security label from an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner and that the host has the 'TLP Green' security label (security labels are not case sensitive when using the Python SDK).

.. code-block:: python
    :emphasize-lines: 25-26

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

        # remove the 'TLP Green' label from the indicator
        indicator.delete_security_label('TLP Green')

        # commit the indicator with the removed security label to ThreatConnect
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
