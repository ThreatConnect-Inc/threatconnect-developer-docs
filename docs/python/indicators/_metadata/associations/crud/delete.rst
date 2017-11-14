Delete Indicator Associations
"""""""""""""""""""""""""""""

The code snippet below demonstrates how to remove an association between an Indicator and a Group in ThreatConnect. This example assumes a Host Indicator ``example.com`` exists in the target owner and an Incident with the ID ``123456``.

.. code-block:: python
    :emphasize-lines: 1,27-28,30-31,33-34,36-37

    from threatconnect.Config.ResourceType import ResourceType

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    # define variables
    host_name = 'example.com'
    incident_id = 123456

    # set a filter to retrieve a specific host indicator: example.com
    filter1 = indicators.add_filter()
    filter1.add_indicator(host_name)

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Indicators
    for indicator in indicators:
        print(indicator.indicator)

        # remove the association between this indicator and the incident
        indicator.disassociate_group(ResourceType.INCIDENTS, incident_id)

        # commit the changes to ThreatConnect
        indicator.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
