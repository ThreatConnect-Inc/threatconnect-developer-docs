Retrieve Incidents
^^^^^^^^^^^^^^^^^^

Retrieving a Single Incident
""""""""""""""""""""""""""""

This example demonstrates how to retrieve a specific Incident using the Incident's ID. The ``add_id`` filter specifies the ID of the Incident which you would like to retrieve.

.. code-block:: python
    :emphasize-lines: 10-12,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Incidents object
    incidents = tc.incidents()

    # set a filter to retrieve only the Incident with ID: 123456
    filter1 = incidents.add_filter()
    filter1.add_id(123456)

    try:
        # retrieve the Incident
        incidents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Incidents (in this case there should only be one) and print its properties
    for incident in incidents:
        print(incident.id)
        print(incident.name)
        print(incident.date_added)
        print(incident.weblink)

        # Incident specific property
        print(incident.event_date)

Retrieving Multiple Incidents
"""""""""""""""""""""""""""""

This example will demonstrate how to retrieve Incidents while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Incidents in the **Example Community** Owner that has a Tag
of **EXAMPLE**.

.. code-block:: python
    :emphasize-lines: 12-15,18-19

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Incidents object
    incidents = tc.incidents()

    owner = 'Example Community'

    # set a filter to only retrieve Incidents in the 'Example Community' tagged: 'APT'
    filter1 = incidents.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')

    try:
        # retrieve the Incidents
        incidents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    # iterate through the retrieved Incidents and print their properties
    for incident in incidents:
        print(incident.id)
        print(incident.name)
        print(incident.date_added)
        print(incident.weblink)

        # Incident specific property
        print(incident.event_date)

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial <https://docs.threatconnect.com/en/latest/python/advanced.html#advanced-filtering>`__.
