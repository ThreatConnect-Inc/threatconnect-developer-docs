Create Indicator Threat and Confidence Ratings
""""""""""""""""""""""""""""""""""""""""""""""

The code snippet below demonstrates how to add/change the threat and/or confidence rating on an Indicator. This example assumes a host indicator ``example.com`` exists in the target owner.

.. code-block:: python
    :linenos:

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

        # set the indicator's threat rating
        indicator.set_rating(2.5)

        # set the indicator's confidence rating
        indicator.set_confidence(100)

        # commit the changes
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
