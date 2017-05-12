Delete Emails
^^^^^^^^^^^^^

The example below demonstrates how to delete an Email Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-12,15-16

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Emails object
    emails = tc.emails()

    owner = 'Example Community'
    # create an empty Email
    email = emails.add('', owner)
    # set the ID of the new Email to the ID of the Email you would like to delete
    email.set_id(123456)

    try:
        # delete the Email
        email.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``emails = tc.emails()``                     | Instantiate an Emails container object.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``email = emails.add('', owner)``            | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.set_id(20)``                         | Set the ID of the Email to the **EXISTING** Email ID to delete.  |
+----------------------------------------------+------------------------------------------------------------------+
| ``email.delete()``                           | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+
