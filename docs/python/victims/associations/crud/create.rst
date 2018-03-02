Create Victim Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^

The code snippet below demonstrates how to create an association between a Victim and another Group in ThreatConnect. This example assumes there is a Victim with an ID of ``123456`` and an Incident with an ID of ``654321`` in the target owner. To test this code snippet, change the ``victim_id`` and ``incident_id`` variables.

.. code-block:: python
    :emphasize-lines: 1,32-33,35-36

    from threatconnect.Config.ResourceType import ResourceType

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # define the ID of the victim we would like to retrieve
    victim_id = 123456
    # define the ID of the incident we would like to associate with the victim
    incident_id = 654321

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

        # create an association between this victim and the incident
        victim.associate_group(ResourceType.INCIDENTS, incident_id)

        # commit the changes to ThreatConnect
        victim.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
