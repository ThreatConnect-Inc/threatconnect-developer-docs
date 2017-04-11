Create Emails
^^^^^^^^^^^^^

The example below demonstrates how to create an Email Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    emails = tc.emails()
        
    owner = 'Example Community'
    email = emails.add('New Email', owner)

    email.set_body('This is an email body.')
    email.set_from_address('bad_guy@badguys.com')
    email.set_header('This is an improper email header.')
    email.set_subject('This is an email subject.')
    email.set_to('victim@goodguys.com')

    email.add_attribute('Description', 'Description Example')
    email.add_tag('EXAMPLE')
    email.set_security_label('TLP Green')
    try:
        email.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

Supported Properties

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

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

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
| ``email.set_from_address('bad_guy@badgu...`` | **(OPTIONAL)** Set the Email from address.                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_header('This is an improper...`` | **(REQUIRED)** Set the Email header.                             |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_subject('This is an email s...`` | **(REQUIRED)** Set the Email subject.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_to('victim@goodguys.com')``      | **(OPTIONAL)** Set the Email to address.                         |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.add_attribute('Description', 'D...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.add_tag('EXAMPLE')``                 | Add a Tag to the Email.                                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_security_label('TLP Green')``    | Add a Security Label to the Email.                               |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.commit()``                           | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+
