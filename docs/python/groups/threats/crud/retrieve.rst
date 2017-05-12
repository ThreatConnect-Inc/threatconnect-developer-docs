Retrieve Threats
^^^^^^^^^^^^^^^^

Retrieving a Single Threat
""""""""""""""""""""""""""

This example demonstrates how to retrieve a specific Threat using the Threat's ID. The ``add_id`` filter specifies the ID of the Threat which you would like to retrieve.

.. code-block:: python
    :emphasize-lines: 8-10,13-14

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Threats object
    threats = tc.threats()

    # set a filter to retrieve only the Threat with ID: 123456
    filter1 = threats.add_filter()
    filter1.add_id(123456)

    try:
        # retrieve the Threat
        threats.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Threats (in this case there should only be one) and print its properties
    for threat in threats:
        print(threat.id)
        print(threat.name)
        print(threat.date_added)
        print(threat.weblink)

Retrieving Multiple Threats
"""""""""""""""""""""""""""

This example will demonstrate how to retrieve Threats while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Threats in the **Example Community** Owner that has a Tag of
**EXAMPLE**.

.. code-block:: python
    :emphasize-lines: 9-12,15-16

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Threats object
    threats = tc.threats()

    owner = 'Example Community'
    # set a filter to only retrieve Threats in the 'Example Community' tagged: 'APT'
    filter1 = threats.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')

    try:
        # retrieve the Threats
        threats.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Threats and print their properties
    for threat in threats:
        print(threat.id)
        print(threat.name)
        print(threat.date_added)
        print(threat.weblink)

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial <#advanced-filtering>`__.
