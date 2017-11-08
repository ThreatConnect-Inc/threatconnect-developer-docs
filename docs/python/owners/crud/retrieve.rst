Retrieve Owners
---------------

The example below demonstrates how to retrieve Owners from the ThreatConnect platform:

.. code-block:: python

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Owners object
    owners = tc.owners()

    try:
        # retrieve the Owners
        owners.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Owners
    for owner in owners:
        print(owner.id)
        print(owner.name)
        print(owner.type)
