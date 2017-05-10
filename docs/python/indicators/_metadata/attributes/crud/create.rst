Create Indicator Attributes
"""""""""""""""""""""""""""

The code snippet below demonstrates how to create an attribute on an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner.

.. code-block:: python
    :linenos:
    :emphasize-lines: 20-21,23-24

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()

    # set a filter to retrieve a specific host indicator: example.com
    filter1 = indicators.add_filter()
    filter1.add_indicator('example.com')

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for indicator in indicators:
        print(indicator.indicator)

        # add a description attribute that is displayed at the top of the indicator's page in ThreatConnect
        indicator.add_attribute('Description', 'Description Example', True)

        # add a description attribute that is not displayed at the top of the indicator's page in ThreatConnect
        indicator.add_attribute('Description', 'Description Example')

        # commit the changes
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
