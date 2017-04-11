Update Tasks
------------

The example below demonstrates how to update a Task Resource in the ThreatConnect platform:

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    tasks = tc.tasks()

    task = tasks.add('Updated Task')
    task.set_id(20)

    task.load_attributes()
    for attribute in task.attributes:
        if attribute.type == 'Description':
            task.delete_attribute(attribute.id)

    task.add_attribute('Description', 'Updated Description')

    task.load_tags()
    for tag in task.tags:
        task.delete_tag(tag.name)

    task.add_tag('EXAMPLE')

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
| ``task = Tasks.add('Updated task'...``       | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.set_id(20)``                          | Set the ID of the task to the **EXISTING** task ID to update.  |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.load_attributes()``                   | Load existing Attributes into the task object.                   |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.delete_attribute(attribute.id)``      | Add a delete flag to the Attribute with type **Description**.    |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.add_attribute('Description', '...``   | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.load_tags()``                         | Load existing Tags into the task object.                         |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.delete_tag(tag.name)``                | Add a delete flag to all Tags.                                   |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.add_tag('EXAMPLE')``                  | Add a Tag to the Resource.                                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``task.commit()``                            | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+
