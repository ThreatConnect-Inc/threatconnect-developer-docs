Retrieve Task Associations
""""""""""""""""""""""""""

The code snippet below demonstrates how to view Groups, Indicators, and Victims which are associated with a given Task in ThreatConnect. This example assumes there is a Task with an ID of ``123456`` in the target owner. To test this code snippet, change the ``task_id`` variable to the ID of a task in your owner.

.. code-block:: python
    :linenos:
    :emphasize-lines: 25-26,35-36,49-50

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # define the ID of the task we would like to retrieve
    task_id = 123456

    # instantiate Tasks object
    tasks = tc.tasks()

    # set a filter to retrieve the task with the id: 123456
    filter1 = tasks.add_filter()
    filter1.add_id(task_id)

    try:
        tasks.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Tasks and print their associations
    for task in tasks:
        print(task.name)

        # iterate through all associated groups
        for associated_group in task.group_associations:
            # print details about the associated group
            print(associated_group.id)
            print(associated_group.name)
            print(associated_group.resource_type)
            print(associated_group.owner_name)
            print(associated_group.date_added)
            print(associated_group.weblink)

        # iterate through all associated indicators
        for associated_indicator in task.indicator_associations:
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
        for associated_victim in task.victim_associations:
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
