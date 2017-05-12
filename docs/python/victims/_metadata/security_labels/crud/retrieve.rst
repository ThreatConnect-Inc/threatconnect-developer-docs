Retrieve Victim Security Labels
"""""""""""""""""""""""""""""""

The code snippet below demonstrates how to retrieve the security label from a Victim. This example assumes there is a Victim with an ID of ``123456`` in the target owner. To test this code snippet, change the ``victim_id`` variable to the ID of a victim in your owner.

.. code-block:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # define the ID of the victim we would like to retrieve
    victim_id = 123456

    # create a victims object
    victims = tc.victims()

    # set a filter to retrieve the victim with the id: 123456
    filter1 = victims.add_filter()
    filter1.add_id(victim_id)

    try:
        victims.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for victim in victims:
        print(victim.name)

        # load the victim's security label
        victim.load_security_label()

        # if this victim has a security label, print some information about the sec. label
        if victim.security_label is not None:
            print(victim.security_label.name)
            print(victim.security_label.description)
            print(victim.security_label.date_added)

.. warning:: Currently, the ThreatConnect Python SDK does not support multiple security labels. If a Victim has multiple security labels, the Python SDK will only return one of them.
