Delete URLs
^^^^^^^^^^^

The example below demonstrates how to delete a URL Indicator from the ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 23-24

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate an Indicators container
    indicators = tc.indicators()

    owner = 'Example Community'

    # specify a specific url from a specific owner (in this case 'http://example.com/test/clickme.html' from the 'Example Community')
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_indicator('http://example.com/test/clickme.html')

    # retrieve the Indicator
    indicators.retrieve()

    # prove that there is only one Indicator retrieved
    assert len(indicators) == 1

    try:
        for indicator in indicators:
            # delete the Indicator
            indicator.delete()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.
