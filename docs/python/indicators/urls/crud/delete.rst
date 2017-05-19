Delete URLs
^^^^^^^^^^^

The example below demonstrates how to delete a URL Indicator from the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 25-26

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    owner = 'Example Community'

    # specify a specific URL from a specific owner (in this case 'http://example.com/test/clickme.html' from the 'Example Community')
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_indicator('http://example.com/test/clickme.html')

    # retrieve the Indicator
    indicators.retrieve()

    # prove there is only one Indicator retrieved
    assert len(indicators) == 1

    # iterate through the retrieved Indicators and delete them
    for indicator in indicators:
        # delete the Indicator
        indicator.delete()


.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.
