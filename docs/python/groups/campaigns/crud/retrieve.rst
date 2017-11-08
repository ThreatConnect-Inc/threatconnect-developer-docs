Retrieve Campaigns
^^^^^^^^^^^^^^^^^^

Retrieving a Single Campaign
""""""""""""""""""""""""""""

This example demonstrates how to retrieve a specific Campaign using the Campaign's ID. The ``add_id`` filter specifies the ID of the Campaign which you would like to retrieve.

.. code-block:: python
    :emphasize-lines: 10-12,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Campaigns object
    campaigns = tc.campaigns()

    # set a filter to retrieve only the Campaign with ID: 123456
    filter1 = campaigns.add_filter()
    filter1.add_id(123456)

    try:
        # retrieve the Campaign
        campaigns.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Campaign (in this case there should only be one) and print its properties
    for campaign in campaigns:
        print(campaign.id)
        print(campaign.name)
        print(campaign.date_added)
        print(campaign.weblink)

Retrieving Multiple Campaigns
"""""""""""""""""""""""""""""

This example demonstrates how to retrieve Campaigns while applying filters. Two filters are added: one for the Owner and another for a Tag. The result set returned from this example will contain all Campaigns in the "Example Community" Owner that have the **APT** Tag.

.. code-block:: python
    :emphasize-lines: 12-15,18-19

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Campaigns object
    campaigns = tc.campaigns()

    owner = 'Example Community'

    # set a filter to only retrieve Campaigns in the 'Example Community' tagged: 'APT'
    filter1 = campaigns.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')

    try:
        # retrieve the Campaigns
        campaigns.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Campaigns and print their properties
    for campaign in campaigns:
        print(campaign.id)
        print(campaign.name)
        print(campaign.date_added)
        print(campaign.weblink)

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial <https://docs.threatconnect.com/en/latest/python/advanced.html#advanced-filtering>`__.
