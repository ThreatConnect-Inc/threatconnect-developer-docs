Update Victims
--------------

The example below demonstrates how to update a Victim Resource in the ThreatConnect platform:

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    victims = tc.victims()

    owner = 'Example Community'

    # create a victim object with the name: 'Updated Victim'
    victim = victims.add('Updated Victim', owner)

    # set the id of the new victim object to that of an existing victim
    victim.set_id(20)

    try:
        # this will change the name of the victim with id 20 to: 'Updated Victim'
        victim.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

**Code Highlights**

+----------------------------------------------+-------------------------------------------------------------------+
| Snippet                                      | Description                                                       |
+==============================================+===================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                             |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victims = tc.victims()``                   | Instantiate a Victims container object.                           |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victim = victims.add('Updated Victim'...`` | Add a Resource object setting the name and Owner.                 |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victim.set_id(20)``                        | Set the ID of the Victim to the **EXISTING** Victim ID to update. |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victim.commit()``                          | Trigger API calls to write all added, deleted, or modified data.  |
+----------------------------------------------+-------------------------------------------------------------------+
