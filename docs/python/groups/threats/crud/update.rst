Update Threats
^^^^^^^^^^^^^^

The example below demonstrates how to update a Threat Resource in the
ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,20-21

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Threats object
    threats = tc.threats()

    owner = 'Example Community'

    # create a Threat with an updated name
    threat = threats.add('Updated Threat', owner)
    # set the ID of the new Threat to the ID of the existing Threat you want to update
    threat.set_id(123456)

    # you can update the Threat metadata as described here: https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-metadata

    try:
        # update the Threat
        threat.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
