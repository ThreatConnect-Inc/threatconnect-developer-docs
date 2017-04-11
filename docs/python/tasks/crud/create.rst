Create Tasks
------------

The example below demonstrates how to create a Task Resource in the ThreatConnect platform:

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    tasks = tc.tasks()

    task = tasks.add('New Task')
    task.add_attribute('Description', 'Description Example')
    task.add_tag('EXAMPLE')
    task.add_security_label('TLP Green')

    try:
        task.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

**Code Highlights**

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``tasks = tc.tasks()``                       | Instantiate a Tasks container object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``task = tasks.add('New task' own...``       | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.add_attribute('Description' 'D...``   | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.add_tag('EXAMPLE')``                  | Add a Tag to the Task.                                           |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.add_security_label('TLP Green')``     | Add a Security Label to the task.                                |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.commit()``                            | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+

.. note:: Other task-specific data such as ``Assignee`` or ``Escalation Date`` can be `modified using built-in library functions <https://github.com/ThreatConnect-Inc/threatconnect-python/blob/master/examples/commit/tasks_commit.py#L175>`__
