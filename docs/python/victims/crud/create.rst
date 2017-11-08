Create Victims
--------------

The example below demonstrates how to create a Victim Resource in the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-13,16-17

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Victims object
    victims = tc.victims()

    owner = 'Example Community'

    # create a new victim named 'Robin Scherbatsky' in the given owner
    victim = victims.add('Robin Scherbatsky', owner)

    try:
        # create the Victim
        victim.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
