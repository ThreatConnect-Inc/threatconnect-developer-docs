Delete Victims
--------------

The example below demonstrates how to delete a Victim Resource in the ThreatConnect platform:

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    victims = tc.victims()

    owner = 'Example Community'

    # create an empty victim object
    victim = victims.add('', owner)

    # set the id of the empty victim object to the id of an existing victim to delete
    victim.set_id(20)

    try:
        victim.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------+
| Snippet                                      | Description                                                       |
+==============================================+===================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                             |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victims = tc.victims()``                   | Instantiate a Victims container object.                           |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victim = victims.add('', owner)``          | Add a Resource object setting the name and Owner.                 |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victim.set_id(20)``                        | Set the ID of the Victim to the **EXISTING** Victim ID to delete. |
+----------------------------------------------+-------------------------------------------------------------------+
| ``victim.delete()``                          | Trigger API calls to write all added, deleted, or modified data.  |
+----------------------------------------------+-------------------------------------------------------------------+
