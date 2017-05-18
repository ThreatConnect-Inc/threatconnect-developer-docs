Create Threats
^^^^^^^^^^^^^^

The example below demonstrates how to create a Threat Resource in the
ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-13,23-24

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Threat object
    threats = tc.threats()

    owner = 'Example Community'

    # create a new Threat in 'Example Community' with the name: 'New Threat'
    threat = threats.add('New Threat', owner)

    # add a description attribute
    threat.add_attribute('Description', 'Description Example')
    # add a tag
    threat.add_tag('Example')
    # add a security label
    threat.set_security_label('TLP Green')

    try:
        # create the Threat
        threat.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
