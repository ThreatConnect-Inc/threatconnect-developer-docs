Create Tasks
------------

The example below demonstrates how to create a Task Resource in the ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 8-9,19-20

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate a Tasks object
    tasks = tc.tasks()

    # create a new Task in the given owner
    task = tasks.add('New Task')

    # add a description attribute
    task.add_attribute('Description', 'Description Example')
    # add a tag
    task.add_tag('EXAMPLE')
    # add a security label
    task.add_security_label('TLP Green')

    try:
        # create the Task
        task.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

.. note:: Other task-specific data such as ``Assignee`` or ``Escalation Date`` can be `modified using built-in library functions <https://github.com/ThreatConnect-Inc/threatconnect-python/blob/master/examples/commit/tasks_commit.py#L175>`__
