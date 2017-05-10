Delete Indicator Associations
"""""""""""""""""""""""""""""

The code snippet below demonstrates how to remove an association between an Indicator and a Group, Indicator, or Victim in ThreatConnect. This example assumes a host indicator ``example.com`` exists in the target owner.

.. code-block:: python
    :linenos:
    :emphasize-lines: 1,24-25,27-28,30-31

    from threatconnect.Config.ResourceType import ResourceType

    ...

    from threatconnect.Config.ResourceType import ResourceType

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

        # remove the association between this indicator and the incident with the ID: 123456
        indicator.disassociate_group(ResourceType.INCIDENTS, 123456)

        # remove the association between this indicator and the URL indicator: http://example.com/
        indicator.disassociate_indicator(ResourceType.URLS, 'http://example.com/')

        # remove the association between this indicator and the victim with the ID: 123456
        indicator.disassociate_victim(123456)

        # commit the changes to ThreatConnect
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
