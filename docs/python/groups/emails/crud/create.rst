Create Emails
^^^^^^^^^^^^^

The example below demonstrates how to create an Email Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-10,12-17,27-28

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate an Emails object
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

+-----------------+----------------------+------------+
| Property Name   | Method               | Required   |
+=================+======================+============+
| body            | set\_body            | True       |
+-----------------+----------------------+------------+
| from\_address   | set\_from\_address   | False      |
+-----------------+----------------------+------------+
| header          | set\_header          | True       |
+-----------------+----------------------+------------+
| score           | set\_score           | False      |
+-----------------+----------------------+------------+
| subject         | set\_subject         | True       |
+-----------------+----------------------+------------+
| to              | set\_to              | False      |
+-----------------+----------------------+------------+

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``emails = tc.emails()``                     | Instantiate an Emails container object.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``email = emails.add('New Email', ...``      | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_body('This is an email body...`` | **(REQUIRED)** Set the Email body.                               |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_from_address('bad_guy@examp...`` | **(OPTIONAL)** Set the Email from address.                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_header('This is an improper...`` | **(REQUIRED)** Set the Email header.                             |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_subject('This is an email s...`` | **(REQUIRED)** Set the Email subject.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_to('victim@example.com')``       | **(OPTIONAL)** Set the Email to address.                         |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.add_attribute('Description', 'D...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.add_tag('EXAMPLE')``                 | Add a Tag to the Email.                                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_security_label('TLP Green')``    | Add a Security Label to the Email.                               |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.commit()``                           | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+
