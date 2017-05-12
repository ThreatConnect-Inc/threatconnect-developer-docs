Retrieve Group Security Labels
""""""""""""""""""""""""""""""

The code snippet below demonstrates how to retrieve the security label from an Incident. This example assumes there is an Incident with an ID of ``123456``. To test this code snippet, change the ``incident_id`` variable to the ID of an incident in your owner. This same process also applies to all group types. Simply change ``tc.incidents()`` to the group type you would like to retrieve. The available group types are: ``tc.<adversaries|campaigns|documents|emails|incidents|signatures|threats>()``. This snippet also assumes that the target owner has a 'TLP Green' security label (security labels are not case sensitive when using the Python SDK).

.. code-block:: python
    :emphasize-lines: 24-25

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

        # load the Incident's security label
        incident.load_security_label()

        # if this Incident has a security label, print some information about the sec. label
        if incident.security_label is not None:
            print(incident.security_label.name)
            print(incident.security_label.description)
            print(incident.security_label.date_added)

.. warning:: Currently, the ThreatConnect Python SDK does not support multiple security labels. If an Incident has multiple security labels, the Python SDK will only return one of them.
