Update Emails
^^^^^^^^^^^^^

The example below demonstrates how to update an Email Resource in the
ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,20-21

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Emails object
    emails = tc.emails()

    owner = 'Example Community'

    # create an Email with an updated name
    email = emails.add('Updated Email', owner)
    # set the ID of the new Email to the ID of the existing Email you want to update
    email.set_id(123456)

    # you can update the Email metadata as described here: https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-metadata

    try:
        # update the Email
        email.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
