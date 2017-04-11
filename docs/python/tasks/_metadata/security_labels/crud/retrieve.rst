Retrieve Task Security Labels
"""""""""""""""""""""""""""""

The code snippet below demonstrates how to retrieve the security label from a Task. This example assumes there is a Task with an ID of ``123456`` in the target owner. To test this code snippet, change the ``task_id`` variable to the ID of a task in your owner.

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

        # load the task's security label
        task.load_security_label()

        # if this task has a security label, print some information about the sec. label
        if task.security_label is not None:
            print(task.security_label.name)
            print(task.security_label.description)
            print(task.security_label.date_added)

.. warning:: Currently, the ThreatConnect Python SDK does not support multiple security labels. If a Task has multiple security labels, the Python SDK will only return one of them.
