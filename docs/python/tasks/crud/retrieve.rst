Retrieve Tasks
--------------

Retrieving a Single Task
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :emphasize-lines: 10-12,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Tasks object
    tasks = tc.tasks()

    # set a filter to retrieve only the Task with ID: 123456
    filter1 = tasks.add_filter()
    filter1.add_id(123456)

    try:
        # retrieve the Task
        tasks.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # prove there is only one Task retrieved
    assert len(tasks) == 1

    # iterate through the retrieved Task (in this case there should only be one) and print its properties
    for task in tasks:
        print(task.id)
        print(task.name)
        print(task.date_added)
        print(task.weblink)

Retrieving Multiple Tasks
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :emphasize-lines: 10-12,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
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
