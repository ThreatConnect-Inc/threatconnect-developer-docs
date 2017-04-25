Update Victims
--------------

The example below demonstrates how to update a Victim Resource in the ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 10-11,13-14

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate a Victims object
    victims = tc.victims()

    owner = 'Example Community'

    # create a Victim object with the name: 'Updated Victim'
    victim = victims.add('Updated Victim', owner)

    # set the id of the new Victim object to that of an existing Victim
    victim.set_id(123456)

    try:
        # this will change the name of the Victim with id 123456 to: 'Updated Victim'
        victim.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
