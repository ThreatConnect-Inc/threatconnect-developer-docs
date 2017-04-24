Create Email Addresses
^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to create an Email Address Indicator in the ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 10-11,25-26

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate an Indicators container
    indicators = tc.indicators()

    owner = 'Example Community'

    # create a new Indicator in the given owner
    indicator = indicators.add('badguy@example.com', owner)
    # set the confidence rating for the Indicator
    indicator.set_confidence(75)
    # set the threat rating for the Indicator
    indicator.set_rating(2.5)

    # add a description attribute
    adversary.add_attribute('Description', 'Description Example')
    # add a tag
    adversary.add_tag('Example')
    # add a security label
    adversary.set_security_label('TLP Green')

    try:
        # create the Indicator
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
