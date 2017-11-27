Retrieve Victim Assets
^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to pull all Assets for the current Victim Resource from the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 26-27

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
            print(asset.id)
            print(asset.name)
            print(asset.type)
            print(asset.weblink)
            print('')
