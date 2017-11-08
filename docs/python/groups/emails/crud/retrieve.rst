Retrieve Emails
^^^^^^^^^^^^^^^

Retrieving a Single Email
"""""""""""""""""""""""""

This example demonstrates how to retrieve a specific Email using the Email's ID. The ``add_id`` filter specifies the ID of the Email which you would like to retrieve.

.. code-block:: python
    :emphasize-lines: 10-12,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Emails object
    emails = tc.emails()

    # set a filter to retrieve only the Email with ID: 123456
    filter1 = emails.add_filter()
    filter1.add_id(123456)

    try:
        # retrieve the Email
        emails.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    # iterate through the retrieved Emails (in this case there should only be one) and print its properties
    for email in emails:
        print(email.id)
        print(email.name)
        print(email.date_added)
        print(email.weblink)

        # Email specific properties
        print(email.header)
        print(email.subject)
        print(email.from_address)
        print(email.to)
        print(email.body)
        print(email.score)

Retrieving Multiple Emails
""""""""""""""""""""""""""

This example will demonstrate how to retrieve emails while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any emails in the **Example Community** Owner that has a Tag of
**EXAMPLE**.

.. code-block:: python
    :emphasize-lines: 12-15,18-19

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Emails object
    emails = tc.emails()

    owner = 'Example Community'

    # set a filter to only retrieve Emails in the 'Example Community' tagged: 'APT'
    filter1 = emails.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')

    try:
        # retrieve the Emails
        emails.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    # iterate through the retrieved Emails and print their properties
    for email in emails:
        print(email.id)
        print(email.name)
        print(email.date_added)
        print(email.weblink)

        # Email specific property
        print(email.score)

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial <https://docs.threatconnect.com/en/latest/python/advanced.html#advanced-filtering>`__.
