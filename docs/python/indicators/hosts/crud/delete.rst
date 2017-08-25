Delete Hosts
^^^^^^^^^^^^

The example below demonstrates how to delete a Host Indicator from the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 34-35

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    owner = 'Example Community'
    indicator = 'example.com'

    # specify a specific host from a specific owner (in this case 'example.com' from the 'Example Community')
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
