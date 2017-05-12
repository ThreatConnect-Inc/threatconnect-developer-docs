Create Hosts
^^^^^^^^^^^^

The example below demonstrates how to create a Host Indicator in the ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 10-11,25-26

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    owner = 'Example Community'

    # create a new Indicator in the given owner
    indicator = indicators.add('example.com', owner)
    # set the confidence rating for the Indicator
    indicator.set_confidence(75)
    # set the threat rating for the Indicator
    indicator.set_rating(2.5)

    # add a description attribute
    indicator.add_attribute('Description', 'Description Example')
    # add a tag
    indicator.add_tag('Example')
    # add a security label
    indicator.set_security_label('TLP Green')

    try:
        # create the Indicator
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

Optionally, turn on DNS resolution and/or ownership information for the host.

.. 
    no-test

.. code-block:: python
    :linenos:

    # Query PTR record for a given host
    indicator.set_dns_active(True)

    # Look up host ownership information
    indicator.set_whois_active(True)
