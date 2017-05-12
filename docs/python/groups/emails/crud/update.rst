Update Emails
^^^^^^^^^^^^^

The example below demonstrates how to update an Email Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-12,35-36

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Emails object
    emails = tc.emails()

    owner = 'Example Community'
    # create an Email with an updated name
    email = emails.add('Updated Email', owner)
    # set the ID of the new Email to the ID of the existing Email you want to update
    email.set_id(123456)

    # load Email attributes
    email.load_attributes()
    for attribute in email.attributes:
        # if the attribute is a description, delete it
        if attribute.type == 'Description':
            # delete the attribute
            email.delete_attribute(attribute.id)

    # add a new description attribute
    email.add_attribute('Description', 'Updated Description')

    # load Email tags
    email.load_tags()
    # delete all of the Email's tags
    for tag in email.tags:
        email.delete_tag(tag.name)

    # add a tag
    email.add_tag('EXAMPLE')

    try:
        # update the Email
        email.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
