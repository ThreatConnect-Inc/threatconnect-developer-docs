Retrieve Group Attributes
"""""""""""""""""""""""""

The code snippet below demonstrates how to retrieve the attributes from an Incident. This example is designed to delete attributes from an Incident with an ID of ``123456``. To test this code snippet, change the ``incident_id`` variable to the ID of an incident in your owner. This same process also applies to all group types. Simply change ``tc.incidents()`` to the group type you would like to retrieve. The available group types are: ``tc.<adversaries|campaigns|documents|emails|incidents|signatures|threats>()``.

.. code-block:: python
    :emphasize-lines: 28-29

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # define the ID of the Incident we would like to retrieve
    incident_id = 123456

    # create an Incidents object
    incidents = tc.incidents()

    # set a filter to retrieve the Incident with the id: 123456
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

        # load the Incident's attributes
        incident.load_attributes()

        # iterate through the attributes and print out their properties
        for attribute in incident.attributes:
            print(attribute.id)
            print(attribute.type)
            print(attribute.value)
            print(attribute.date_added)
            print(attribute.last_modified)
            print(attribute.displayed)
            print('')
