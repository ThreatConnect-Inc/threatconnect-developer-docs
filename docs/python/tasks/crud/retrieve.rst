Retrieve Tasks
--------------

Retrieving a Single Task
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :emphasize-lines:  13-16,19-20

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Tasks object
    tasks = tc.tasks()

    owner = 'Example Community'
    task_id = 123456

    # set a filter to retrieve only the Task with ID: 123456
    filter1 = tasks.add_filter()
    filter1.add_owner(owner)
    filter1.add_id(task_id)

    try:
        # retrieve the Task
        tasks.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        # prove there is only one Task retrieved
        assert len(tasks) == 1
    except AssertionError as e:
        # if the Task doesn't exist in the given owner, raise an error
        print('AssertionError: The task with id {0} was not found in the "{1}" owner. '.format(task_id, owner) +
              'Try changing the `owner` variable to the name of an owner in your instance of ThreatConnect ' +
              'and/or set the `task_id` variable to the ID of a task that exists in the given owner.')
        sys.exit(1)

    # iterate through the retrieved Task (in this case there should only be one) and print its properties
    for task in tasks:
        print(task.id)
        print(task.name)
        print(task.date_added)
        print(task.weblink)
        print('')

.. note:: If you get an ``AssertionError`` when running this code, you likely need to change the name of the ``owner`` variable so that it is the name of an owner in your instance of ThreatConnect and/or you need to change the ``task_id`` variable so that it is the ID of a Task that exists in the given owner.

Retrieving Multiple Tasks
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :emphasize-lines: 10-12,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Tasks object
    tasks = tc.tasks()

    # set a filter to retrieve only Tasks with the tag: "Nation State"
    filter1 = tasks.add_filter()
    filter1.add_tag('Nation State')

    try:
        # retrieve the Tasks
        tasks.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    # iterate through the retrieved Tasks and print their properties
    for task in tasks:
        print(task.id)
        print(task.name)
        print(task.date_added)
        print(task.weblink)
        print('')
