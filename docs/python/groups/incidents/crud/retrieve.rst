Retrieve Incidents
^^^^^^^^^^^^^^^^^^

Retrieving a Single Incident
""""""""""""""""""""""""""""

The import statement and reading of the configuration files have been replaced with ``...`` for brevity.

.. code-block:: python
    :emphasize-lines: 8-10,13-14

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

This example demonstrates how to retrieve a specific Incident using the Incident's ID. The ``add_id`` filter specifies the ID of the Incident which you would like to retrieve.

Code Highlights

+----------------------------------------------+-----------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                             |
+==============================================+=========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                   |
+----------------------------------------------+-----------------------------------------------------------------------------------------+
| ``incidents = tc.incidents()``               | Instantiate an Incident container object.                                               |
+----------------------------------------------+-----------------------------------------------------------------------------------------+
| ``filter1 = incidents.add_filter()``         | Add a filter object to the Incident container object (support multiple filter objects). |
+----------------------------------------------+-----------------------------------------------------------------------------------------+
| ``filter1.add_id(123456)``                   | Add API filter to retrieve the Incident with the ID: 123456                             |
+----------------------------------------------+-----------------------------------------------------------------------------------------+
| ``incidents.retrieve()``                     | Trigger the API request and retrieve the Incident intelligence data.                    |
+----------------------------------------------+-----------------------------------------------------------------------------------------+
| ``for incident in incidents:``               | Iterate over the Incident container object generator.                                   |
+----------------------------------------------+-----------------------------------------------------------------------------------------+
| ``print(incident.id)``                       | Display the **'id'** property of the Incident object.                                   |
+----------------------------------------------+-----------------------------------------------------------------------------------------+

Retrieving Multiple Incidents
"""""""""""""""""""""""""""""

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code-block:: python
    :emphasize-lines: 9-12,15-16

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
        print(incident.event_date)

This example will demonstrate how to retrieve Incidents while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Incidents in the **Example Community** Owner that has a Tag
of **EXAMPLE**.

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial <#advanced-filtering>`__.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                              |
+==============================================+==========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``incidents = tc.incidents()``               | Instantiate an Incidents container object.                                               |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1 = incidents.add_filter()``         | Add a filter object to the Incidents container object (support multiple filter objects). |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1.add_tag('APT')``                   | Add API filter to retrieve Incidents with the 'APT' tag.                                 |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``incidents.retrieve()``                     | Trigger the API request and retrieve the Incidents intelligence data.                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``for incident in incidents:``               | Iterate over the Incidents container object generator.                                   |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``print(incident.id)``                       | Display the **'id'** property of the Incidents object.                                   |
+----------------------------------------------+------------------------------------------------------------------------------------------+
