Update Tasks
------------

The example below demonstrates how to update a Task Resource in the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 10-13,18-19

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Tasks object
    tasks = tc.tasks()

    # create a new Task object with an updated name
    task = tasks.add('Updated Task')
    # set the ID of the new Task to the ID of the existing Task you want to update
    task.set_id(123456)

    # you can update the Task metadata as described here: https://docs.threatconnect.com/en/latest/python/tasks/tasks.html#task-metadata

    try:
        # update the Task
        task.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
