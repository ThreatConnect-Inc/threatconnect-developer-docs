Update Victims
--------------

The example below demonstrates how to update a Victim Resource in the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-13,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Victims object
    victims = tc.victims()

    owner = 'Example Community'

    # create a Victim object with the name: 'Updated Victim'
    victim = victims.add('Updated Victim', owner)

    # set the id of the new Victim object to that of an existing Victim
    victim.set_id(123456)

    # you can update the Victim metadata as described here: https://docs.threatconnect.com/en/latest/python/victims/victims.html#victim-metadata

    try:
        # this will change the name of the Victim with id 123456 to: 'Updated Victim'
        victim.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
