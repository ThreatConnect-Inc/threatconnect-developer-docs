Create Threats
^^^^^^^^^^^^^^

The example below demonstrates how to create a Threat Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    threats = tc.threats()
        
    owner = 'Example Community'
    threat = threats.add('New Threat', owner)
    threat.add_attribute('Description', 'Description Example')
    threat.add_tag('EXAMPLE')
    threat.set_security_label('TLP Green')
    try:
        threat.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``threats = tc.threats()``                   | Instantiate a Threats container object.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``threat = threats.add('New Threat' own...`` | Add a Resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``threat.add_attribute('Description' 'D...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``threat.add_tag('EXAMPLE')``                | Add a Tag to the Threat.                                         |
+----------------------------------------------+------------------------------------------------------------------+
| ``threat.set_security_label('TLP Green')``   | Add a Security Label to the Threat.                              |
+----------------------------------------------+------------------------------------------------------------------+
| ``threat.commit()``                          | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+
