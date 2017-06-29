Retrieve Indicator ThreatAssess Threat and Confidence Ratings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The ThreatAssess Threat and Confidence ratings can be accessed via an Indicator's ``threat_assess_rating`` and ``threat_assess_confidence`` properties, respectively. The example below demonstrates how to retrieve these properties.

.. code-block:: python
    :emphasize-lines: 19-21

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # print the Indicator and ThreatAssess Threat rating for each Indicator
    for indicator in indicators:
        print("\nIndicator: {}\n".format(indicator.indicator) +
              "ThreatAssess Threat rating: {}\n".format(indicator.threat_assess_rating) +
              "ThreatAssess Confidence rating: {}\n".format(indicator.threat_assess_confidence))
