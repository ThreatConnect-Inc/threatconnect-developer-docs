Retrieve Emails
^^^^^^^^^^^^^^^

Retrieving a Single Email
"""""""""""""""""""""""""

The import statement and reading of the configuration files have been replaced with ``...`` for brevity.

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    emails = tc.emails()
    owner = 'Example Community'

    try:
        filter1 = emails.add_filter()
        filter1.add_id(123456)
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        emails.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for email in emails:
        print(email.id)
        print(email.name)
        print(email.date_added)
        print(email.weblink)
        
        # email specific properties
        print(email.header)
        print(email.subject)
        print(email.from_address)
        print(email.to)
        print(email.body)
        print(email.score)

This example demonstrates how to retrieve a specific Email using the Email's ID. The ``add_id`` filter specifies the ID of the Email which you would like to retrieve.

Code Highlights

+----------------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                          |
+==============================================+======================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``emails = tc.emails()``                     | Instantiate an Email container object.                                               |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``filter1 = emails.add_filter()``            | Add a filter object to the Email container object (support multiple filter objects). |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``filter1.add_id(123456)``                   | Add API filter to retrieve the Email with the ID: 123456                             |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``emails.retrieve()``                        | Trigger the API request and retrieve the Emails intelligence data.                   |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``for email in emails:``                     | Iterate over the Emails container object generator.                                  |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``print(email.id)``                          | Display the **'id'** property of the Email object.                                   |
+----------------------------------------------+--------------------------------------------------------------------------------------+

Retrieving Multiple Emails
""""""""""""""""""""""""""

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    emails = tc.emails()
    owner = 'Example Community'

    try:
        filter1 = emails.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        emails.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for email in emails:
        print(email.id)
        print(email.name)
        print(email.date_added)
        print(email.weblink)
        
        # email specific properties
        print(email.header)
        print(email.subject)
        print(email.from_address)
        print(email.to)
        print(email.body)
        print(email.score)

This example will demonstrate how to retrieve emails while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any emails in the **Example Community** Owner that has a Tag of
**EXAMPLE**.

To retrieve the headers and body for a single email, include a filter
for its ID. (Make an individual query for each email.)

``filter1.add_id($email_id)``

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial </python/advanced/filtering/>`__.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                           |
+==============================================+=======================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                 |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``emails = tc.emails()``                     | Instantiate an Emails container object.                                               |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``filter1 = emails.add_filter()``            | Add a Filter object to the Emails container object (support multiple filter objects). |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``filter1.add_tag('APT')``                   | Add API Filter to be applied to the API request.                                      |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``emails.retrieve()``                        | Trigger the API request and retrieve the Emails intelligence data.                    |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``for email in emails:``                     | Iterate over the Emails container object generator.                                   |
+----------------------------------------------+---------------------------------------------------------------------------------------+
| ``print(email.id)``                          | Display the **'id'** property of the Email object.                                    |
+----------------------------------------------+---------------------------------------------------------------------------------------+
