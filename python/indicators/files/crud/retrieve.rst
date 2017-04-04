Retrieve Files
^^^^^^^^^^^^^^

Retrieving a Single File Indicator
""""""""""""""""""""""""""""""""""

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific file indicator
    filter1 = indicators.add_filter()
    filter1.add_indicator('8743b52063cd84097a65d1633f5c74f5')

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # if the file was found, print some information about it
    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

This example demonstrates how to retrieve a specific file indicator. The ``add_indicator`` filter allows us to specify the file hash which we would like to retrieve. If a file exists in ThreatConnect, you can pass the md5, sha1, or sha256 of that file into the ``add_indicator`` filter and it will work.

Retrieving Multiple File Indicators
"""""""""""""""""""""""""""""""""""

.. code:: python

    # this import allows us to specify which indicator type we want to import
    from threatconnect.Config.IndicatorType import IndicatorType

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()

    # set a filter to retrieve file indicators
    filter1 = indicators.add_filter(IndicatorType.FILES)

    try:
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

This example demonstrates how to retrieve all file indicators in the default organization. The ``IndicatorType.FILES`` which is passed into the filter specifies which indicator type we want to retrieve.
