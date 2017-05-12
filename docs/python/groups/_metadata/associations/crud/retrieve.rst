Retrieve Group Associations
"""""""""""""""""""""""""""

The code snippet below demonstrates how to view Groups, Indicators, and Victims which are associated with a given Group in ThreatConnect. This example is designed to retrieve the associations from an Incident with an ID of ``123456``. To test this code snippet, change the ``incident_id`` variable to the ID of an incident in your owner. This same process also applies to all group types. Simply change ``tc.incidents()`` to the group type you would like to retrieve. The available group types are: ``tc.<adversaries|campaigns|documents|emails|incidents|signatures|threats>()``.

.. code-block:: python
    :emphasize-lines: 25,35,49

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # define the ID of the group we would like to retrieve
    incident_id = 123456

    # create an incidents object
    incidents = tc.incidents()

    # set a filter to retrieve the incident with the id: 123456
    filter1 = incidents.add_filter()
    filter1.add_id(incident_id)

    try:
        # retrieve the Incidents
        incidents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Incidents
    for incident in incidents:
        print(incident.name)

        # iterate through all associated Groups
        for associated_group in incident.group_associations:
            # print details about the associated Group
            print(associated_group.id)
            print(associated_group.name)
            print(associated_group.resource_type)
            print(associated_group.owner_name)
            print(associated_group.date_added)
            print(associated_group.weblink)

        # iterate through all associated Indicators
        for associated_indicator in incident.indicator_associations:
            # print details about the associated Indicator
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

        # iterate through all associated Victims
        for associated_victim in incident.victim_associations:
            # print details about the associated Victim
            print(associated_victim.id)
            print(associated_victim.name)
            print(associated_victim.description)
            print(associated_victim.owner_name)
            print(associated_victim.nationality)
            print(associated_victim.org)
            print(associated_victim.suborg)
            print(associated_victim.work_location)
            print(associated_victim.weblink)

.. note:: When the ``group_associations``, ``indicator_associations``, and ``victim_associations`` methods are called, an API request is invoked immediately.
