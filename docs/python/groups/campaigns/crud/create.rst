Create Campaigns
^^^^^^^^^^^^^^^^

The example below demonstrates how to create a Campaign Resource in the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,25-26

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Campaigns object
    campaigns = tc.campaigns()

    owner = 'Example Community'

    # create a new Campaign in 'Example Community' with the name: 'New Campaign'
    campaign = campaigns.add('New Campaign', owner)
    # set the first seen date for the Campaign
    campaign.set_first_seen('2017-05-21T00:00:00Z')  # OPTIONAL

    # add a description attribute
    campaign.add_attribute('Description', 'Description Example')
    # add a tag
    campaign.add_tag('Example')
    # add a security label
    campaign.set_security_label('TLP Green')

    try:
        # create the Campaign
        campaign.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

**Supported Properties**

+---------------+------------------+----------+
| Property Name | Method           | Required |
+===============+==================+==========+
| first\_seen   | set\_first\_seen | False    |
+---------------+------------------+----------+

