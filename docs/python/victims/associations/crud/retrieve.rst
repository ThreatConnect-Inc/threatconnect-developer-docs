Retrieve Victim Associations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The code snippet below demonstrates how to view Groups and Indicators which are associated with a given Victim in ThreatConnect. This example assumes there is a Victim with an ID of ``123456`` in the target owner. To test this code snippet, change the ``victim_id`` variable.

.. note:: It is not possible to associate an Indicator directly with a Victim in ThreatConnect. The code below returns Indicators that share a Group association with the given Victim. In the image below, the Victim and Indicator are not directly associated, but are both associated with the same Group. Therefore, the Indicator would be returned when iterating through ``victim.indicator_associations``.

.. figure:: ../../_static/victim-to-indicator-associations.png
    :alt: Victim to Indicator Associations

.. code-block:: python
    :emphasize-lines: 28-29,39-40

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
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

        # iterate through all associated groups
        for associated_group in victim.group_associations:
            # print details about the associated group
            print(associated_group.id)
            print(associated_group.name)
            print(associated_group.resource_type)
            print(associated_group.owner_name)
            print(associated_group.date_added)
            print(associated_group.weblink)
            print('')

        # iterate through all associated indicators
        for associated_indicator in victim.indicator_associations:
            # print details about the associated indicator
            print(associated_indicator.id)
            print(associated_indicator.indicator)
            print(associated_indicator.type)
            print(associated_indicator.description)
            print(associated_indicator.owner_name)
            print(associated_indicator.rating)
            print(associated_indicator.confidence)
            print(associated_indicator.date_added)
            print(associated_indicator.last_modified)
            print(associated_indicator.weblink)
            print('')

.. note:: When the ``group_associations`` and ``indicator_associations`` properties are referenced, an API request is immediately invoked.
