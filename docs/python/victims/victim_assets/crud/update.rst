Update Victim Assets
^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to update the Victim Assets of an existing Victim with an ID of ``123456``:

.. code-block:: python

    from threatconnect.Config.ResourceType import ResourceType

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Victims object
    victims = tc.victims()

    # set a filter to retrieve the victim with the id: 123456
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

        # iterate through the victim's assets
        for asset in victim.assets:
            # if the asset is an email address asset, update it
            if asset.type == "EmailAddress":
                # create a new victim asset object
                new_asset = VictimAssetObject(ResourceType.VICTIM_EMAIL_ADDRESSES)
                new_asset.set_address('victim2@example.com')
                new_asset.set_address_type('Personal')

                # update the existing asset with the new one
                victim.update(asset.id, new_asset)

        try:
            # commit the Victim with the updated Victim Asset
            victim.commit()
        except RuntimeError as e:
            print('Error: {0}'.format(e))
            sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
