Update Emails
^^^^^^^^^^^^^

The example below demonstrates how to update an Email Resource in the
ThreatConnect platform:

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    emails = tc.emails()

    owner = 'Example Community'
    email = emails.add('Updated Email', owner)
    email.set_id(20)

    email.load_attributes()
    for attribute in email.attributes:
        if attribute.type == 'Description':
            email.delete_attribute(attribute.id)

    email.add_attribute('Description', 'Updated Description')

    email.load_tags()
    for tag in email.tags:
        email.delete_tag(tag.name)

    email.add_tag('EXAMPLE')

    try:
        email.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------+
| Snippet                                      | Description                                                       |
+==============================================+===================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                             |
+----------------------------------------------+-------------------------------------------------------------------+
| ``emails = tc.emails()``                     | Instantiate an Emails container object.                           |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email = emails.add('Updated Email', o...`` | Add a Resource object setting the name and Owner.                 |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.set_id(20)``                         | Set the ID of the Email to the ***EXISTING*** Email ID to update. |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.load_attributes()``                  | Load existing Attributes into the Email object.                   |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.delete_attribute(attribute.id)``     | Add a delete flag on the Attribute with type **Description**.     |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.add_attribute('Description', 'U...`` | Add an Attribute of type **Description** to the Resource.         |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.load_tags()``                        | Load existing Tags into the Email object.                         |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.delete_tag(tag.name)``               | Add a delete flag to all Tags.                                    |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.add_tag('EXAMPLE')``                 | Add a Tag to the Resource.                                        |
+----------------------------------------------+-------------------------------------------------------------------+
| ``email.commit()``                           | Trigger API calls to write all added, deleted, or modified data.  |
+----------------------------------------------+-------------------------------------------------------------------+
