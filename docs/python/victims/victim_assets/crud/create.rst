Create Victim Assets
^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to create Victim Assets for an existing Victim with an ID of ``123456``:

.. code-block:: python

    from threatconnect.Config.ResourceType import ResourceType

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
        # add email address asset to victim
        asset = VictimAssetObject(ResourceType.VICTIM_EMAIL_ADDRESSES)
        asset.set_address('victim@example.com')
        asset.set_address_type('Personal')
        victim.add_asset(asset)

        # add network account asset to victim
        asset = VictimAssetObject(ResourceType.VICTIM_NETWORK_ACCOUNTS)
        asset.set_account('victim')
        asset.set_network('victimsareus Active Directory')
        victim.add_asset(asset)

        # add phone asset to victim
        asset = VictimAssetObject(ResourceType.VICTIM_PHONES)
        asset.set_phone_type('555-555-5555')
        victim.add_asset(asset)

        # add social network asset to victim
        asset = VictimAssetObject(ResourceType.VICTIM_SOCIAL_NETWORKS)
        asset.set_account('@victim')
        asset.set_network('Twitter')
        victim.add_asset(asset)

        # add website asset to victim
        asset = VictimAssetObject(ResourceType.VICTIM_WEBSITES)
        asset.set_website('www.example.com')
        victim.add_asset(asset)

        try:
            victim.commit()
        except RuntimeError as e:
            print('Error: {0}'.format(e))
            sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
