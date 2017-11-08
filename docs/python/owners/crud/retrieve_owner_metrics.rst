Retrieve Owner Metrics
----------------------

It is possible to retrieve various metrics for a given owner such as Indicator and Group counts, average Indicator threat and confidence ratings, and more. The example below demonstrates how to retrieve this data for the owner with the given ID:

.. code-block:: python

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # specify the id of the owner for which you would like to get metrics
    owner_id = 1

    # instantiate Owners object
    owners = tc.owners()

    # filter for a specific owner based on the owner's id
    filter1 = owners.add_filter()
    filter1.add_id(owner_id)

    try:
        # retrieve owners
        owners.retrieve()
    except RuntimeError as e:
        print('Error: {0!s}'.format(e))
        sys.exit(1)

    for owner in owners:
        for metric in owner.metrics:
            print(metric)

It is also possible to retrieve the metrics for all of the owners to which you have access as demonstrated below:

.. code-block:: python

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Owners object
    owners = tc.owners()

    # get the metrics
    metrics = owners.retrieve_metrics()

    # display the metrics
    for metric in metrics:
        print(metric)
