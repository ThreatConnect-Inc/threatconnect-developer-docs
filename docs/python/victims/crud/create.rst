Create Victims
--------------

The example below demonstrates how to create a Victim Resource in the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 1-2,13-14,51-52

    from threatconnect.Config.ResourceType import ResourceType
    from threatconnect.VictimAssetObject import VictimAssetObject

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Victims object
    victims = tc.victims()

    owner = 'Example Community'

    # create a new victim named 'Robin Scherbatsky' in the given owner
    victim = victims.add('Robin Scherbatsky', owner)

    # set victim details (all are OPTIONAL)
    victim.set_nationality('Canadian')
    victim.set_org('Royal Canadian Mounted Police')
    victim.set_suborg('Quebec Office')
    victim.set_work_location('Quebec')

    # add an email address asset to new victim (OPTIONAL)
    asset = VictimAssetObject(ResourceType.VICTIM_EMAIL_ADDRESSES)
    asset.set_address('victim@victimsareus.com')
    asset.set_address_type('Personal')
    victim.add_asset(asset)

    # add a network account asset to the new victim (OPTIONAL)
    asset = VictimAssetObject(ResourceType.VICTIM_NETWORK_ACCOUNTS)
    asset.set_account('victim')
    asset.set_network('victimsareus Active Directory')
    victim.add_asset(asset)

    # add a phone asset to the new victim (OPTIONAL)
    asset = VictimAssetObject(ResourceType.VICTIM_PHONES)
    asset.set_phone_type('1-800-867-5309')
    victim.add_asset(asset)

    # add a social network asset to the new victim (OPTIONAL)
    asset = VictimAssetObject(ResourceType.VICTIM_SOCIAL_NETWORKS)
    asset.set_account('@victim')
    asset.set_network('Twitter')
    victim.add_asset(asset)

    # add a website asset to the new victim (OPTIONAL)
    asset = VictimAssetObject(ResourceType.VICTIM_WEBSITES)
    asset.set_website('www.victimsareus.com')
    victim.add_asset(asset)

    try:
        # create the Victim
        victim.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
