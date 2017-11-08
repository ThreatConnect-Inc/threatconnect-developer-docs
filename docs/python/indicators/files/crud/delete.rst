Delete Files
^^^^^^^^^^^^

The example below demonstrates how to delete a File Indicator from the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 34-35

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    owner = 'Example Community'
    indicator = '8743b52063cd84097a65d1633f5c74f5'

    # specify a specific file hash from a specific owner (in this case '8743b52063cd84097a65d1633f5c74f5' from the 'Example Community')
    filter1 = indicators.add_filter()
    filter1.add_owner(owner)
    filter1.add_indicator(indicator)

    # retrieve the Indicator
    indicators.retrieve()

    try:
        # prove there is only one Indicator retrieved
        assert len(indicators) == 1
    except AssertionError as e:
        # if the indicator doesn't exist in the given owner, raise an error
        print("AssertionError: The indicator {0} was not found in the '{1}' owner. ".format(indicator, owner) +
              "Try changing the `owner` variable to the name of an owner in your instance of ThreatConnect " +
              "or make sure that the {0} indicator specified by the `indicator` ".format(indicator) +
              "variable exists in that owner.")
        sys.exit(1)

    # iterate through the retrieved Indicators and delete them
    for indicator in indicators:
        # delete the Indicator
        indicator.delete()

.. note:: If you get an ``AssertionError`` when running this code, you likely need to change the name of the ``owner`` variable so that it is the name of an owner in your instance of ThreatConnect and/or you need to change the ``indicators`` variable so that it is an Indicator that exists in the given owner.

Deleting File Occurrences
"""""""""""""""""""""""""

A file occurrence can be deleted from File Indicators using the ``delete_file_occurrence`` function which takes the ID of the file occurrence to be deleted as an argument.

.. code-block:: python
    :emphasize-lines: 30-31

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
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

    # if the File was found, print some information about it
    for indicator in indicators:
        print(indicator.indicator)

        # load the file occurrences
        indicator.load_file_occurrence()

        # iterate through the Indicator's file occurrences
        for file_occurrence in indicator.file_occurrences:
            # delete the file occurrence
            indicator.delete_file_occurrence(file_occurrence.id)

        # commit the changes
        indicator.commit()
