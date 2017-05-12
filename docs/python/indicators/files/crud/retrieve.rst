Retrieve Files
^^^^^^^^^^^^^^

Retrieving a Single File Indicator
""""""""""""""""""""""""""""""""""

This example demonstrates how to retrieve a File Indicator from the ThreatConnect platform. The ``add_indicator`` filter allows us to specify the specific Indicator we would like to retrieve. If a File Indicator exists in ThreatConnect and has all three types of hashes (md5, sha1, and sha256), you can pass any one of those hashes into the ``add_indicator`` filter and it will return the File Indicator with that hash.

.. code-block:: python
    :emphasize-lines: 8-10,13-14

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific File Indicator
    filter1 = indicators.add_filter()
    filter1.add_indicator('8743b52063cd84097a65d1633f5c74f5')

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # prove there is only one Indicator retrieved
    assert len(indicators) == 1

    # if the File Indicator was found, print some information about it
    for indicator in indicators:
        print(indicator.indicator)
        print(indicator.weblink)

        # File Indicator specific property giving the file size (in bytes)
        print(indicator.size)

Retrieving File Occurrences
+++++++++++++++++++++++++++

The code snippet below demonstrates how to retrieve a File Indicator's occurrences:

.. code-block:: python
    :emphasize-lines: 22-23,25-30

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific File Indicator
    filter1 = indicators.add_filter()
    filter1.add_indicator('8743b52063cd84097a65d1633f5c74f5')

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # if the File was found, print some information about it
    for indicator in indicators:
        print(indicator.indicator)

        # load the file occurrences
        indicator.load_file_occurrence()

        # iterate through the Indicator's file occurrences
        for file_occurrence in indicator.file_occurrences:
            print(file_occurrence.date)
            print(file_occurrence.file_name)
            print(file_occurrence.id)
            print(file_occurrence.path)

Retrieving Multiple File Indicators
"""""""""""""""""""""""""""""""""""

This example demonstrates how to retrieve all File Indicators in the default organization. The ``IndicatorType.FILES`` which is passed into the filter specifies which Indicator type we want to retrieve.

.. code-block:: python
    :emphasize-lines: 1-2,11-12,15-16

    # this import allows us to specify which Indicator type we want to retrieve
    from threatconnect.Config.IndicatorType import IndicatorType

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    # set a filter to retrieve File Indicators
    filter1 = indicators.add_filter(IndicatorType.FILES)

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Files and print them
    for indicator in indicators:
        print(indicator)
