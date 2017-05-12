Update Incidents
^^^^^^^^^^^^^^^^

The example below demonstrates how to update an Incident Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-12,35-36

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Incidents object
    incidents = tc.incidents()

    owner = 'Example Community'
    # create an Incident with an updated name
    incident = incidents.add('Updated Incident', owner)
    # set the ID of the new Incident to the ID of the existing Incident you want to update
    incident.set_id(123456)

    # load Incident attributes
    incident.load_attributes()
    for attribute in incident.attributes:
        # if the attribute is a description, delete it
        if attribute.type == 'Description':
            # delete the attribute
            incident.delete_attribute(attribute.id)

    # add a new description attribute
    incident.add_attribute('Description', 'Updated Description')

    # load Incident tags
    incident.load_tags()
    # delete all of the Incident's tags
    for tag in incident.tags:
        incident.delete_tag(tag.name)

    # add a tag
    incident.add_tag('EXAMPLE')

    try:
        # update the Incident
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
