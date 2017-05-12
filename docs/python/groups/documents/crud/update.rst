Update Documents
^^^^^^^^^^^^^^^^

The example below demonstrates how to update a Document Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-12,35-36

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Documents container
    documents = tc.documents()

    owner = 'Example Community'
    # create an empty Document
    document = documents.add('Updated Document', owner)
    # set the ID of the new Document to the ID of the existing Document you want to update
    document.set_id(123456)

    # load Document attributes
    document.load_attributes()
    for attribute in document.attributes:
        # if the attribute is a description, delete it
        if attribute.type == 'Description':
            # delete the attribute
            document.delete_attribute(attribute.id)

    # add a new description attribute
    document.add_attribute('Description', 'Updated Description')

    # load Document tags
    document.load_tags()
    # delete all of the Document's tags
    for tag in document.tags:
        document.delete_tag(tag.name)

    # add a tag
    document.add_tag('EXAMPLE')

    try:
        # update the Document
        document.commit()
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
| ``documents = tc.documents()``               | Instantiate a Documents container object.                               |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document = documents.add('Updated Doc...`` | Add a Resource object setting the name and Owner.                       |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.set_id(20)``                      | Set the ID of the Document to the ***EXISTING*** Document ID to update. |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.load_attributes()``               | Load existing Attributes into the Document object.                      |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.delete_attribute(attribute.id)``  | Add a delete flag on the Attribute with type **Description**.           |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.add_attribute('Description',...`` | Add an Attribute of type **Description** to the Resource.               |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.load_tags()``                     | Load existing Tags into the Document object.                            |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.delete_tag(tag.name)``            | Add a delete flag to all Tags.                                          |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.add_tag('EXAMPLE')``              | Add a Tag to the Resource.                                              |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``document.commit()``                        | Trigger API calls to write all added, deleted, or modified data.        |
+----------------------------------------------+-------------------------------------------------------------------------+
