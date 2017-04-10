Delete Email Addresses
^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to delete an Email Address Indicator from the ThreatConnect platform:

.. code-block:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()
    owner = 'Example Community'

    # specify a specific email address from a specific owner (in this case 'badguy@example.com' from the 'Example Community')
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_indicator('badguy@example.com')

    # retrieve the indicator
    indicators.retrieve()

    try:
        # delete the indicator (there will be at most one indicator)
        for indicator in indicators:
            indicator.delete()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.
