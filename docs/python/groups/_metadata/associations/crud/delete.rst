Delete Group Associations
"""""""""""""""""""""""""

The code snippet below demonstrates how to remove an association between an Incident and another Group, Indicator, and Victim. This example is designed to remove the associations from an Incident with an ID of ``123456``. To test this code snippet, change the ``incident_id`` variable to the ID of an incident in your owner. This same process also applies to all group types. Simply change ``tc.incidents()`` to the group type you would like to retrieve. The available group types are: ``tc.<adversaries|campaigns|documents|emails|incidents|signatures|threats>()``.

.. code-block:: python
    :emphasize-lines: 1,28-29,31-32,34-35

    from threatconnect.Config.ResourceType import ResourceType

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
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

        # remove the association between this incident and the incident with the ID: 654321
        incident.disassociate_group(ResourceType.INCIDENTS, 654321)

        # remove the association between this incident and the URL indicator: http://example.com/
        incident.disassociate_indicator(ResourceType.URLS, 'http://example.com/')

        # remove the association between this incident and the victim with the ID: 333333
        incident.disassociate_victim(333333)

        # commit the changes to ThreatConnect
        incident.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
