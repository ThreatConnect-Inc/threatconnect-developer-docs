Create Victims
--------------

The example below demonstrates how to create a Victim Resource in the ThreatConnect platform:

.. code:: python

    from threatconnect.Config.ResourceType import ResourceType
    from threatconnect import VictimAssetObject

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    victims = tc.victims()

    owner = 'Example Community'
    victim = victims.add('Robin Scherbatsky', owner)

    victim.set_nationality('Canadian')
    victim.set_org('Royal Canadian Mounted Police')
    victim.set_suborg('Quebec Office')
    victim.set_work_location('Quebec')

    # email address assets can be added to new victim
    asset = VictimAssetObject(ResourceType.VICTIM_EMAIL_ADDRESSES)
    asset.set_address('victim@victimsareus.com')
    asset.set_address_type('Personal')
    victim.add_asset(asset)

    # network account assets can be added to new victim
    asset = VictimAssetObject(ResourceType.VICTIM_NETWORK_ACCOUNTS)
    asset.set_account('victim')
    asset.set_network('victimsareus Active Directory')
    victim.add_asset(asset)

    # phone assets can be added to new victim
    asset = VictimAssetObject(ResourceType.VICTIM_PHONES)
    asset.set_phone_type('555-555-5555')
    victim.add_asset(asset)

    # social network assets can be added to new victim
    asset = VictimAssetObject(ResourceType.VICTIM_SOCIAL_NETWORKS)
    asset.set_account('@victim')
    asset.set_network('Twitter')
    victim.add_asset(asset)

    # website assets can be added to new victim
    asset = VictimAssetObject(ResourceType.VICTIM_WEBSITES)
    asset.set_website('www.victimsareus.com')
    victim.add_asset(asset)

    try:
        victim.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

**Code Highlights**

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``victims = tc.victims()``                   | Instantiate a Victims container object.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim = victims.add('Robin Scherbats...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim.set_nationality('Canadian')``       | *(OPTIONAL)* Set Victim nationality.                             |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim.set_org('Royal Canadian Mounte...`` | *(OPTIONAL)* Set Victim Organization.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim.set_suborg('Quebec Office')``       | *(OPTIONAL)* Set Victim Sub-Organization.                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim.set_work_location('Quebec')``       | *(OPTIONAL)* Set Victim location.                                |
+----------------------------------------------+------------------------------------------------------------------+
| ``victim.commit()``                          | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+
