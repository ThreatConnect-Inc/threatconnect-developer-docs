Retrieving Custom Indicator Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before you can find custom Indicators of a certain type, you need to identify which types are available on your instance of ThreatConnect and find the ``api_entity`` of the Indicator type you are interested in retrieving. The example below demonstrates how to do this.

.. code-block:: python
    :emphasize-lines: 1-2,10-11,13-14,16-24

    # this import allows us to initialize the IndicatorObjectParser class
    from threatconnect.IndicatorObjectParser import IndicatorObjectParser

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate an IndicatorObjectParser object
    indicatorParser = IndicatorObjectParser(tc)

    # initialize the parser (which tunes it for your instance of ThreatConnect)
    indicatorParser.init();

    # iterate through the custom indicator types and 
    for indicatorType in indicatorParser.custom_indicator_types:
        print('Name: {}'.format(indicatorType.name))
        print('API Entity: {}'.format(indicatorType.api_entity))

        # print the fields returned for the given indicator type (and the fields required to create it)
        print('API Fields:')
        for field in indicatorType.fields:
            print('    - {} (type: {})'.format(field.label, field.type))
        print('')

Running the script above on the ThreatConnect public cloud (`https://app.threatconnect.com/ <https://app.threatconnect.com/>`_) returns the following:

.. code-block:: shell

   Name: ASN
   API Entity: asn
   API Fields:
       - AS Number (type: text)

   Name: CIDR
   API Entity: cidrBlock
   API Fields:
       - Block (type: text)

   Name: Mutex
   API Entity: mutex
   API Fields:
       - Mutex (type: text)

   Name: Registry Key
   API Entity: registryKey
   API Fields:
       - Key Name (type: text)
       - Value Name (type: text)
       - Value Type (type: selectone)

   Name: User Agent
   API Entity: userAgent
   API Fields:
       - User Agent String (type: text)

Retrieving Custom Indicators of a Specific Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to retrieve all custom Indicators of a specific type. Before you do this, however, you need to know the API entity of the custom Indicator type you would like to retrieve. Refer to the section above this for more information regarding how you can find this value.

.. code-block:: python
    :emphasize-lines: 1-2,13-16,19-20

    # this import allows us to specify which Indicator type we want to retrieve
    from threatconnect.Config.IndicatorType import IndicatorType

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    # set a filter to retrieve ASN (Autonomous System Number) custom Indicators
    filter1 = indicators.add_filter(IndicatorType.CUSTOM_INDICATORS, api_entity='asn')
    # The `api_entity` argument above could be replaced with `cidrBlock`, `mutex`, 
    # `registryKey`, or `userAgent` to retrieve indicators of those respective types.

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Indicators and print them
    for indicator in indicators:
        print(indicator)
        print('')
