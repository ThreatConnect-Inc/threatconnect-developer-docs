Update Threats
^^^^^^^^^^^^^^

The example below demonstrates how to update a Threat Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-12,35-36

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Threats object
    threats = tc.threats()

    owner = 'Example Community'
    # create an empty Threat
    threat = threats.add('Updated Threat', owner)
    # set the ID of the new Threat to the ID of the existing Threat you want to update
    threat.set_id(123456)

    # load Threat attributes
    threat.load_attributes()
    for attribute in threat.attributes:
        # if the attribute is a description, delete it
        if attribute.type == 'Description':
            # delete the attribute
            threat.delete_attribute(attribute.id)

    # add a new description attribute
    threat.add_attribute('Description', 'Updated Description')

    # load Threat tags
    threat.load_tags()
    # delete all of the Threat's tags
    for tag in threat.tags:
        threat.delete_tag(tag.name)

    # add a tag
    threat.add_tag('EXAMPLE')

    try:
        # update the Threat
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
