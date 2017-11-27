Retrieve Victims
----------------

Retrieving a Single Victim
^^^^^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to retrieve a specific Victim Resource from the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 13-16,19-20

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Victims object
    victims = tc.victims()

    owner = 'Example Community'
    victim_id = 123456

    # set a filter to retrieve the Victim with the id: 123456
    filter1 = victims.add_filter()
    filter1.add_owner(owner)
    filter1.add_id(victim_id)

    try:
        # retrieve the Victim
        victims.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        # prove there is only one Victim retrieved
        assert len(victims) == 1
    except AssertionError as e:
        # if the Victim doesn't exist in the given owner, raise an error
        print('AssertionError: The victim with ID {0} was not found in the "{1}" owner. '.format(victim_id, owner) +
              'Try changing the `owner` variable to the name of an owner in your instance of ThreatConnect ' +
              'and/or set the `victim_id` variable to the ID of a Victim that exists in the given owner.')
        sys.exit(1)

    # if the Victim was found, print some information about it
    for victim in victims:
        print(victim.id)
        print(victim.name)
        print(victim.nationality)
        print(victim.org)
        print(victim.suborg)
        print(victim.work_location)
        print(victim.weblink)
        print('')

.. note:: If you get an ``AssertionError`` when running this code, you likely need to change the name of the ``owner`` variable so that it is the name of an owner in your instance of ThreatConnect and/or you need to change the ``victim_id`` variable so that it is the ID of a Victim that exists in the given owner.

For details on how to retrieve victim assets, refer to the `Victim Asset retrieval <https://docs.threatconnect.com/en/latest/python/victims/victims.html#retrieve-victim-assets>`_ section.

Retrieving Multiple Victims
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to retrieve multiple Victim Resources from the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,18-19

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Victims object
    victims = tc.victims()

    owner = 'Example Community'

    # set a filter to retrieve all Victims from the given owner that have the tag: 'Example'
    filter1 = victims.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('Example')

    try:
        # retrieve the Victims
        victims.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Victims and print their properties
    for victim in victims:
        print(victim.id)
        print(victim.name)
        print(victim.nationality)
        print(victim.org)
        print(victim.suborg)
        print(victim.work_location)
        print(victim.weblink)
        print('')
