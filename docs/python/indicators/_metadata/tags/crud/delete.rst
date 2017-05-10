Delete Indicator Tags
"""""""""""""""""""""

The code snippet below demonstrates how to delete a tag from an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner and is tagged 'Test'.

.. code-block:: python
    :linenos:
    :emphasize-lines: 20-21

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

        # remove the 'Test' tag from the indicator
        indicator.delete_tag('Test')

        # commit the indicator with the removed tag to ThreatConnect
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
