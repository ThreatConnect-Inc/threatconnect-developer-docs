Retrieve Victims
----------------

Retrieving a Single Victim
^^^^^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to retrieve a specific Victim Resource from the ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 8-10,13-14

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Victims object
    victims = tc.victims()

    # set a filter to retrieve the Victim with the id: 123456
    filter1 = victims.add_filter()
    filter1.add_id(123456)

    try:
        # retrieve the Victim
        victims.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # prove there is only one Victim retrieved
    assert len(victims) == 1

    # if the Victim was found, print some information about it
    for victim in victims:
        print(obj.id)
        print(obj.name)
        print(obj.nationality)
        print(obj.org)
        print(obj.suborg)
        print(obj.work_location)
        print(obj.weblink)

For details on how to retrieve victim assets, refer to the `Victim Asset retrieval <https://docs.threatconnect.com/en/latest/python/python_sdk.html#retrieve-victim-assets>`_ section.

Retrieving Multiple Victims
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The example below demonstrates how to retrieve multiple Victim Resources from the ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 10-12,16-17

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
        print(obj.id)
        print(obj.name)
        print(obj.nationality)
        print(obj.org)
        print(obj.suborg)
        print(obj.work_location)
        print(obj.weblink)
