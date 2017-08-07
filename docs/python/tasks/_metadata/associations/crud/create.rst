Create Task Associations
""""""""""""""""""""""""

The code snippet below demonstrates how to create an association between a Task and another Group, Indicator, and Victim in ThreatConnect. This example assumes there is a Task with an ID of ``123456`` in the target owner. To test this code snippet, change the ``task_id`` variable to the ID of a task in your owner.

.. code-block:: python
    :emphasize-lines: 1,30-31,33-34,36-37,39-40

    from threatconnect.Config.ResourceType import ResourceType

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
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
        # retrieve the Tasks
        tasks.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the Tasks
    for task in tasks:
        print(task.name)

        # create an association between this task and the incident with the ID: 654321
        task.associate_group(ResourceType.INCIDENTS, 654321)

        # create an association between this task and the URL indicator: http://example.com/
        task.associate_indicator(ResourceType.URLS, 'http://example.com/')

        # create an association between this task and the victim with the ID: 333333
        task.associate_victim(333333)

        # commit the changes to ThreatConnect
        task.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
