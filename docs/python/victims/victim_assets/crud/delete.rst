Delete Victim Assets
^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to delete Victim Assets from an existing Victim with an ID of ``123456``:

.. code-block:: python
    :emphasize-lines: 33,36-37

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Victims object
    victims = tc.victims()

    # set a filter to retrieve the Victim with the id: 123456
    filter1 = victims.add_filter()
    filter1.add_id(123456)

    try:
        # retrieve the Victims
        victims.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Victims
    for victim in victims:
        print(victim.id)
        print(victim.name)

        # retrieve the assets from ThreatConnect
        victim.load_assets()

        # iterate through the Victim's assets
        for asset in victim.assets:
            # if the asset is a phone number asset, delete it
            if asset.type == 'Phone':
                victim.delete(asset.id, asset)

        try:
            # commit the Victim with the Victim Asset(s) deleted
            victim.commit()
        except RuntimeError as e:
            print('Error: {0}'.format(e))
            sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
