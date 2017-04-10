Delete Tasks
------------

The example below demonstrates how to delete a Task Resource from the ThreatConnect platform:

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    tasks = tc.tasks()

    owner = 'Example Community'
    task = tasks.add('', owner)
    task.set_id(20)

    try:
        task.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.

**Code Highlights**

+----------------------------------------------+---------------------------------------------------------------+
| Snippet                                      | Description                                                   |
+==============================================+===============================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                         |
+----------------------------------------------+---------------------------------------------------------------+
| ``tasks = tc.tasks()``                       | Instantiate a Tasks container object.                         |
+----------------------------------------------+---------------------------------------------------------------+
| ``task = tasks.add('', owner)``              | Add a Task Resource setting the name and Owner.               |
+----------------------------------------------+---------------------------------------------------------------+
| ``task.set_id(20)``                          | Set the ID of the task to the **EXISTING** task ID to delete. |
+----------------------------------------------+---------------------------------------------------------------+
| ``task.delete()``                            | Trigger API calls to delete the task.                         |
+----------------------------------------------+---------------------------------------------------------------+
