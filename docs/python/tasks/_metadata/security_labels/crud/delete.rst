Delete Task Security Labels
"""""""""""""""""""""""""""

The code snippet below demonstrates how to delete a security label from a Task. This example assumes there is a Task with an ID of ``123456`` in the target owner. To test this code snippet, change the ``task_id`` variable to the ID of a task in your owner.

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # define the ID of the task we would like to retrieve
    task_id = 123456

    # create a tasks object
    tasks = tc.tasks()

    # set a filter to retrieve the task with the id: 123456
    filter1 = tasks.add_filter()
    filter1.add_id(task_id)

    try:
        tasks.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for task in tasks:
        print(task.name)

        # remove the 'TLP Green' label from the task
        task.delete_security_label('TLP Green')

        # commit the task with the removed security label to ThreatConnect
        task.commit()

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
