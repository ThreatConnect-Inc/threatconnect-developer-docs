Retrieve Threats
^^^^^^^^^^^^^^^^

Retrieving a Single Threat
""""""""""""""""""""""""""

The import statement and reading of the configuration files have been replaced with ``...`` for brevity.

.. code-block:: python
    :linenos:
    :emphasize-lines: 8-10,13-14

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Threats container
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

This example demonstrates how to retrieve a specific Threat using the Threat's ID. The ``add_id`` filter specifies the ID of the Threat which you would like to retrieve.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                           |
+==============================================+=======================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                 |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``threats = tc.threats()``                   | Instantiate an Threat container object.                                               |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``filter1 = threats.add_filter()``           | Add a filter object to the Threat container object (support multiple filter objects). |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``filter1.add_id(123456)``                   | Add API filter to retrieve the Threat with the ID: 123456                             |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``threats.retrieve()``                       | Trigger the API request and retrieve the Threat intelligence data.                    |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``for threat in threats:``                   | Iterate over the Threat container object generator.                                   |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``print(threat.id)``                         | Display the **'id'** property of the Threat object.                                   |
+----------------------------------------------+---------------------------------------------------------------------------------------+

Retrieving Multiple Threats
"""""""""""""""""""""""""""

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-12,15-16

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Threats container
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

This example will demonstrate how to retrieve Threats while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Threats in the **Example Community** Owner that has a Tag of
**EXAMPLE**.

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial <#advanced-filtering>`__.

Code Highlights

+----------------------------------------------+----------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                            |
+==============================================+========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                  |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``threats = tc.threats()``                   | Instantiate a Threats container object.                                                |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``filter1 = threats.add_filter()``           | Add a filter object to the Threats container object (support multiple filter objects). |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``filter1.add_tag('APT')``                   | Add API filter to retrieve Threats with the 'APT' tag.                                 |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``threats.retrieve()``                       | Trigger the API request and retrieve the Threats intelligence data.                    |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``for threat in threats:``                   | Iterate over the Threats container object generator.                                   |
+----------------------------------------------+----------------------------------------------------------------------------------------+
| ``print(threat.id)``                         | Display the **id** property of the Threat object.                                      |
+----------------------------------------------+----------------------------------------------------------------------------------------+
