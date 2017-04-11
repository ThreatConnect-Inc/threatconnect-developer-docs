Update Threats
^^^^^^^^^^^^^^

The example below demonstrates how to update a Threat Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    threats = tc.threats()

    owner = 'Example Community'
    threat = threats.add('Updated Threat', owner)
    threat.set_id(20)

    threat.load_attributes()
    for attribute in threat.attributes:
        if attribute.type == 'Description':
            threat.delete_attribute(attribute.id)

    threat.add_attribute('Description', 'Updated Description')

    threat.load_tags()
    for tag in threat.tags:
        threat.delete_tag(tag.name)

    threat.add_tag('EXAMPLE')

    try:
        threat.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------+
| Snippet                                      | Description                                                         |
+==============================================+=====================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                               |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threats = tc.threats()``                   | Instantiate a Threats container object.                             |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat = threats.add('Updated Threat'...`` | Add a Resource object setting the name and Owner.                   |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.set_id(20)``                        | Set the ID of the Threat to the ***EXISTING*** Threat ID to update. |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.load_attributes()``                 | Load existing Attributes into the Threat object.                    |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.delete_attribute(attribute.id)``    | Add a delete flag to the Attribute with type **Description**.       |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.add_attribute('Description', '...`` | Add an Attribute of type **Description** to the Resource.           |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.load_tags()``                       | Load existing Tags into the Threat object.                          |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.delete_tag(tag.name)``              | Add a delete flag to all Tags.                                      |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.add_tag('EXAMPLE')``                | Add a Tag to the Resource.                                          |
+----------------------------------------------+---------------------------------------------------------------------+
| ``threat.commit()``                          | Trigger API calls to write all added, deleted, or modified data.    |
+----------------------------------------------+---------------------------------------------------------------------+
