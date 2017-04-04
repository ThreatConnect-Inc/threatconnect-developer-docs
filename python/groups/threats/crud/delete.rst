Delete Threats
^^^^^^^^^^^^^^

The example below demonstrates how to delete an Threat Resource in the
ThreatConnect platform:

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    threats = tc.threats()

    threat = threats.add('', owner)
    threat.set_id(20)

    try:
        threat.delete()
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
| ``threats = tc.threats()``                   | Instantiate a Threats container object.                           |
+----------------------------------------------+-------------------------------------------------------------------+
| ``threat = threats.add('', owner)``          | Add a Resource object setting the name and Owner.                 |
+----------------------------------------------+-------------------------------------------------------------------+
| ``threat.set_id(20)``                        | Set the ID of the Threat to the **EXISTING** Threat ID to delete. |
+----------------------------------------------+-------------------------------------------------------------------+
| ``threat.delete()``                          | Trigger API calls to write all added, deleted, or modified data.  |
+----------------------------------------------+-------------------------------------------------------------------+
