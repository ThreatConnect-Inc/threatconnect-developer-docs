Retrieve Victim Assets
^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to pull all Assets for the current Victim Resource from the ThreatConnect platform:

.. code-block:: python

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
            print(asset.id)
            print(asset.name)
            print(asset.type)
            print(asset.weblink)

**Code Highlights**

+---------------------------------+-----------------------------------------------------------+
| Snippet                         | Description                                               |
+=================================+===========================================================+
| ``victim.load_assets()``        | Trigger API call to load Assets into the Resource object. |
+---------------------------------+-----------------------------------------------------------+
| ``for asset in victim.assets:`` | Iterate over the Assets object generator.                 |
+---------------------------------+-----------------------------------------------------------+
| ``print(asset.id)``             | Display the **id** property of the Asset object.          |
+---------------------------------+-----------------------------------------------------------+
