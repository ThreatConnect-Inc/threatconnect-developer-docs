Create Emails
^^^^^^^^^^^^^

The example below demonstrates how to create an Email Resource in the
ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-13,15-20,30-31

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Emails object
    emails = tc.emails()

    owner = 'Example Community'

    # create a new Email in 'Example Community' with the name: 'New Email'
    email = emails.add('New Email', owner)

    # set Email specific properties
    email.set_body('This is an email body.')  # REQUIRED
    email.set_from_address('bad_guy@example.com')  # OPTIONAL
    email.set_header('This is an improper email header.')  # REQUIRED
    email.set_subject('This is an email subject.')  # REQUIRED
    email.set_to('victim@example.com')  # OPTIONAL

    # add a description attribute
    email.add_attribute('Description', 'Description Example')
    # add a tag
    email.add_tag('EXAMPLE')
    # add a security label
    email.set_security_label('TLP Green')

    try:
        # create the Email
        email.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

**Supported Properties**

+---------------+--------------------+----------+
| Property Name | Method             | Required |
+===============+====================+==========+
| body          | set\_body          | True     |
+---------------+--------------------+----------+
| header        | set\_header        | True     |
+---------------+--------------------+----------+
| subject       | set\_subject       | True     |
+---------------+--------------------+----------+
| from\_address | set\_from\_address | False    |
+---------------+--------------------+----------+
| score         | set\_score         | False    |
+---------------+--------------------+----------+
| to            | set\_to            | False    |
+---------------+--------------------+----------+
