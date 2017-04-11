Generic Group Retrieval
-----------------------

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # create a groups object
    groups = tc.groups()
    owner = 'Example Community'

    try:
        filter1 = groups.add_filter()
        # only retrieve groups from the owner named: 'Example Community'
        filter1.add_owner(owner)
        # only retrieve groups tagged with: 'APT'
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        groups.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for group in groups:
        print(group.id)
        print(group.name)
        print(group.date_added)
        print(group.weblink)

        # group specific property
        print(group.type)

This example will demonstrate how to retrieve Groups while applying filters. In this example two filters will be added, one for the Owner and another for a Tag. The result set returned from this example will contain any Groups in the **Example Community** Owner that has a Tag of **APT**.

**Code Highlights**

+----------------------------------------------+---------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                           |
+==============================================+=======================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                 |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``groups = tc.groups()``                     | Instantiate a Groups container object.                                                |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``filter1 = groups.add_filter()``            | Add a filter object to the Groups container object (support multiple filter objects). |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``filter1.add_tag('APT')``                   | Add API filter to retrieve Groups with the 'Example' tag.                             |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``groups.retrieve()``                        | Trigger the API request and retrieve the Groups intelligence data.                    |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``for group in groups:``                     | Iterate over the Groups container object generator.                                   |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``print(group.id)``                          | Display the **'id'** property of the Group object.                                    |
+----------------------------------------------+---------------------------------------------------------------------------------------+
