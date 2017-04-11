Update Incidents
^^^^^^^^^^^^^^^^

The example below demonstrates how to update an Incident Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    incidents = tc.incidents()

    owner = 'Example Community'
    incident = incidents.add('Updated Incident', owner)
    incident.set_id(20)

    incident.load_attributes()
    for attribute in incident.attributes:
        if attribute.type == 'Description':
            incident.delete_attribute(attribute.id)

    incident.add_attribute('Description', 'Updated Description')

    incident.load_tags()
    for tag in incident.tags:
        incident.delete_tag(tag.name)

    incident.add_tag('EXAMPLE')

    try:
        incident.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------------+
| Snippet                                      | Description                                                             |
+==============================================+=========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                   |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incidents = tc.incidents()``               | Instantiate an Incidents container object.                              |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident = incidents.add('Updated Inc...`` | Add a Resource object setting the name and Owner.                       |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.set_id(20)``                      | Set the ID of the Incident to the ***EXISTING*** Incident ID to update. |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.load_attributes()``               | Load existing Attributes into the Incident object.                      |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.delete_attribute(attribute.id)``  | Add a delete flag to the Attribute with type **Description**.           |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.add_attribute('Description' ...`` | Add an Attribute of type **Description** to the Resource.               |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.load_tags()``                     | Load existing Tags into the Incident object.                            |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.delete_tag(tag.name)``            | Add a delete flag to all Tags.                                          |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.add_tag('EXAMPLE')``              | Add a Tag to the Resource.                                              |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``incident.commit()``                        | Trigger API calls to write all added, deleted, or modified data.        |
+----------------------------------------------+-------------------------------------------------------------------------+
