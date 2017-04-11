Retrieve Group Tags
"""""""""""""""""""

The code snippet below demonstrates how to retrieve the tags from an Incident. This example assumes there is an Incident with an ID of ``123456``. To test this code snippet, change the ``group_id`` variable to the ID of an incident in your owner. This same process also applies to all group types. Simply change ``tc.incidents()`` to the group type you would like to retrieve. The available group types are: ``tc.<adversaries|campaigns|documents|emails|incidents|signatures|threats>()``.

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # define the ID of the group we would like to retrieve
    group_id = 123456

    # create an incidents object
    incidents = tc.incidents()

    # set a filter to retrieve the incident with the id: 123456
    filter1 = incidents.add_filter()
    filter1.add_id(group_id)

    try:
        incidents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for incident in incidents:
        print(incident.name)

        # load the incident's tags
        incident.load_tags()

        # print details about each tag on the incident
        for tag in incident.tags:
            print(tag.name)
            print(tag.weblink)
