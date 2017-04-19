Create Group Attributes
"""""""""""""""""""""""

The code snippet below demonstrates how to create an attribute on an Incident. This example is designed to create attributes on an Incident with an ID of ``123456``. To test this code snippet, change the ``incident_id`` variable to the ID of an incident in your owner. This same process also applies to all group types. Simply change ``tc.incidents()`` to the group type you would like to retrieve. The available group types are: ``tc.<adversaries|campaigns|documents|emails|incidents|signatures|threats>()``.

.. code-block:: python
    :linenos:
    :emphasize-lines: 24-25,27-28

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # create an Incidents object
    incidents = tc.incidents()

    # define the ID of the Incident we would like to retrieve
    incident_id = 123456

    # set a filter to retrieve the Incidents with the id: 123456
    filter1 = incidents.add_filter()
    filter1.add_id(incident_id)

    try:
        incidents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for incident in incidents:
        print(incident.name)

        # add a description attribute that is displayed at the top of the Incidents's page in ThreatConnect
        incident.add_attribute('Description', 'Description Example', True)

        # add a description attribute that is not displayed at the top of the Incidents's page in ThreatConnect
        incident.add_attribute('Description', 'Description Example')

        # commit the changes
        incident.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
