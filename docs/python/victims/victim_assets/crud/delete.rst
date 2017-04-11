Delete Victim Assets
^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to delete Victim Assets from an existing Victim with an ID of ``123456``:

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    victims = tc.victims()

    # set a filter to retrieve the victim with the id: 123456
    filter1 = victims.add_filter()
    filter1.add_id(123456)

    try:
        victims.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for victim in victims:
        print(victim.id)
        print(victim.name)

        # retrieve the assets from ThreatConnect
        victim.load_assets()

        # iterate through the victim's assets
        for asset in victim.assets:
            # if the asset is a phone number asset, delete it
            if asset.type == "Phone":
                victim.delete(asset.id, asset)

        try:
            victim.commit()
        except RuntimeError as e:
            print('Error: {0}'.format(e))
            sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
