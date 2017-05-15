Retrieve Indicator Associations
"""""""""""""""""""""""""""""""

The code snippet below demonstrates how to view Groups, Indicators, and Victims which are associated with a given Indicator in ThreatConnect. This example assumes a Host Indicator ``example.com`` exists in the target owner.

.. code-block:: python
    :emphasize-lines: 22-23,32-33,46-47

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    # set a filter to retrieve a specific host indicator: example.com
    filter1 = indicators.add_filter()
    filter1.add_indicator('example.com')

    try:
        # retrieve the Indicators
        indicators.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Indicators
    for indicator in indicators:
        print(indicator.indicator)

        # iterate through all associated groups
        for associated_group in indicator.group_associations:
            # print details about the associated group
            print(associated_group.id)
            print(associated_group.name)
            print(associated_group.resource_type)
            print(associated_group.owner_name)
            print(associated_group.date_added)
            print(associated_group.weblink)

        # iterate through all associated indicators
        for associated_indicator in indicator.indicator_associations:
            # print details about the associated indicator
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

        # iterate through all associated victims
        for associated_victim in indicator.victim_associations:
            # print details about the associated victim
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

**Indicator Associations Properties**

+----------------+------+
| Property Name  | Type |
+================+======+
| id             | int  |
+----------------+------+
| indicator      | str  |
+----------------+------+
| type           | str  |
+----------------+------+
| description    | str  |
+----------------+------+
| owner\_name    | str  |
+----------------+------+
| rating         | str  |
+----------------+------+
| confidence     | str  |
+----------------+------+
| date\_added    | str  |
+----------------+------+
| last\_modified | str  |
+----------------+------+
| weblink        | str  |
+----------------+------+
