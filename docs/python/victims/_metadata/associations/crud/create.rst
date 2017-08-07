Create Victim Associations
""""""""""""""""""""""""""

The code snippet below demonstrates how to create an association between a Victim and another Group, Indicator, and Victim in ThreatConnect. This example assumes there is a Victim with an ID of ``123456`` in the target owner. To test this code snippet, change the ``victim_id`` variable to the ID of a victim in your owner.

.. code-block:: python
    :emphasize-lines: 28-29,31-32,34-35,37-38

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # define the ID of the victim we would like to retrieve
    victim_id = 123456

    # create a victims object
    victims = tc.victims()

    # set a filter to retrieve the victim with the id: 123456
    filter1 = victims.add_filter()
    filter1.add_id(victim_id)

    try:
        # retrieve the Victims
        victims.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Victims
    for victim in victims:
        print(victim.name)

        # create an association between this victim and the incident with the ID: 654321
        victim.associate_group(ResourceType.INCIDENTS, 654321)

        # create an association between this victim and the URL indicator: http://example.com/
        victim.associate_indicator(ResourceType.URLS, 'http://example.com/')

        # create an association between this victim and the victim with the ID: 333333
        victim.associate_victim(333333)

        # commit the changes to ThreatConnect
        victim.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
