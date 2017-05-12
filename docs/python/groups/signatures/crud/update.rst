Update Signatures
^^^^^^^^^^^^^^^^^

The example below demonstrates how to update a Signature Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-12,35-36

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Signatures object
    signatures = tc.signatures()

    owner = 'Example Community'
    # create a Signature with an updated name
    signature = signatures.add('Updated Signature', owner)
    # set the ID of the new Signature to the ID of the existing Signature you want to update
    signature.set_id(123456)

    # load Signature attributes
    signature.load_attributes()
    for attribute in signature.attributes:
        # if the attribute is a description, delete it
        if attribute.type == 'Description':
            # delete the attribute
            signature.delete_attribute(attribute.id)

    # add a new description attribute
    signature.add_attribute('Description', 'Updated Description')

    # load Signature tags
    signature.load_tags()
    # delete all of the Signature's tags
    for tag in signature.tags:
        signature.delete_tag(tag.name)

    # add a tag
    signature.add_tag('EXAMPLE')

    try:
        # update the Signature
        signature.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

Code Highlights

+----------------------------------------------+---------------------------------------------------------------------------+
| Snippet                                      | Description                                                               |
+==============================================+===========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                     |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signatures = tc.signatures()``             | Instantiate a Signatures container object.                                |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature = signatures.add('Updated D...`` | Add a Resource object setting the name and Owner.                         |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.set_id(20)``                     | Set the ID of the Signature to the ***EXISTING*** Signature ID to update. |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.load_attributes()``              | Load existing Attributes into the Signature object.                       |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.delete_attribute(attribute.id)`` | Add a delete flag to the Attribute with type **Description**.             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.add_attribute('Description'...`` | Add an Attribute of type **Description** to the Resource.                 |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.load_tags()``                    | Load existing Tags into the Signature object.                             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.delete_tag(tag.name)``           | Add a delete flag to all Tags.                                            |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.add_tag('EXAMPLE')``             | Add a Tag to the Resource.                                                |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``signature.commit()``                       | Trigger API calls to write all added, deleted, or modified data.          |
+----------------------------------------------+---------------------------------------------------------------------------+
