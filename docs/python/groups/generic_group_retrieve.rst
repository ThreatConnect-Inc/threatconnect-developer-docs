Generic Group Retrieval
-----------------------

This example demonstrates how to retrieve Groups while applying filters. In this example two filters will be added: one for the Owner and another for a Tag. The result set returned from this example will contain all Groups in the **Example Community** Owner that have the **APT** Tag.

.. code-block:: python
    :emphasize-lines: 12-16,19-20

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # create a Groups object
    groups = tc.groups()

    owner = 'Example Community'

    filter1 = groups.add_filter()
    # only retrieve groups from the owner named: 'Example Community'
    filter1.add_owner(owner)
    # only retrieve groups tagged with: 'APT'
    filter1.add_tag('APT')

    try:
        # retrieve Groups
        groups.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    # iterate through the Groups
    for group in groups:
        print(group.id)
        print(group.name)
        print(group.date_added)
        print(group.weblink)

        # Group specific property
        print(group.type)
