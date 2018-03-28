Update Campaigns
^^^^^^^^^^^^^^^^

The example below demonstrates how to update a Campaign Resource in the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,20-21

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Campaigns object
    campaigns = tc.campaigns()

    owner = 'Example Community'

    # create Campaign with updated name
    campaign = campaigns.add('Updated Campaign', owner)
    # set the ID of the new Campaign to the ID of the existing Campaign you want to update
    campaign.set_id(123456)

    # you can update the Campaign metadata as described here: https://docs.threatconnect.com/en/latest/python/groups/groups.html#group-metadata

    try:
        # update the Campaign
        campaign.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
