Retrieve Tasks
--------------

Retrieving a Single Task
""""""""""""""""""""""""

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    tasks = tc.tasks()

    # set a filter to retrieve the task with the id: 123456
    filter1 = tasks.add_filter()
    filter1.add_id(123456)

    try:
        tasks.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    for task in tasks:
        print(task.id)
        print(task.name)
        print(task.date_added)
        print(task.weblink)

**Code Highlights**

+----------------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                          |
+==============================================+======================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``Tasks = tc.Tasks()``                       | Instantiate a Tasks container object.                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``filter1 = Tasks.add_filter()``             | Add a filter object to the Tasks container object (support multiple filter objects). |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``filter1.add_id(123456)``               | Add an API filter to be applied to the API request.                                  |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``Tasks.retrieve()``                         | Trigger the API request and retrieve the Tasks-intelligence data.                    |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``for task in Tasks:``                       | Iterate over the Tasks container object generator.                                   |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``print(task.id)``                           | Display the **id** property of the Task object.                                      |
+----------------------------------------------+--------------------------------------------------------------------------------------+

Retrieving Multiple Tasks
"""""""""""""""""""""""""

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    tasks = tc.tasks()

    # set a filter to retrieve all tasks with the tag: "APT"
    filter1 = tasks.add_filter()
    filter1.add_tag('APT')

    try:
        tasks.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for task in tasks:
        print(task.id)
        print(task.name)
        print(task.date_added)
        print(task.weblink)

**Code Highlights**

+----------------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                          |
+==============================================+======================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``Tasks = tc.Tasks()``                       | Instantiate a Tasks container object.                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``filter1 = Tasks.add_filter()``             | Add a filter object to the Tasks container object (support multiple filter objects). |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``filter1.add_tag('APT')``                   | Add an API filter to be applied to the API request.                                  |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``Tasks.retrieve()``                         | Trigger the API request and retrieve the Tasks-intelligence data.                    |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``for task in Tasks:``                       | Iterate over the Tasks container object generator.                                   |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``print(task.id)``                           | Display the **id** property of the Task object.                                      |
+----------------------------------------------+--------------------------------------------------------------------------------------+
