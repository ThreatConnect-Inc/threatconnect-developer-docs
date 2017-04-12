Update Adversaries
^^^^^^^^^^^^^^^^^^

The example below demonstrates how to update an Adversary Resource in
the ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 10,12

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)
    owner = 'Example Community'

    # instantiate Adversaries container
    adversaries = tc.adversaries()

    # create an empty adversary
    adversary = adversaries.add('Updated Adversary', owner)
    # set the ID of the new adversary to the ID of the adversary you would like to update
    adversary.set_id(123456)

    # load adversary attributes
    adversary.load_attributes()
    for attribute in adversary.attributes:
        # if the attribute is a description, delete it
        if attribute.type == 'Description':
            # delete the attribute
            adversary.delete_attribute(attribute.id)

    # add a new description attribute
    adversary.add_attribute('Description', 'Updated Description')

    # load adversary tags
    adversary.load_tags()
    # delete all of the adversary's tags
    for tag in adversary.tags:
        adversary.delete_tag(tag.name)

    # add a tag
    adversary.add_tag('EXAMPLE')

    try:
        # update the adversary
        adversary.commit()
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
| ``adversaries = tc.adversaries()``           | Instantiate an Adversaries container object.                              |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary = adversaries.add('Updated ...`` | Add a resource object setting the name and Owner.                         |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.set_id(20)``                     | Set the ID of the Adversary to the ***EXISTING*** Adversary ID to update. |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.load_attributes()``              | Load existing Attributes into the Adversary object.                       |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.delete_attribute(attribute.id)`` | Add a delete flag on the Attribute with type **Description**.             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.add_attribute('Description'...`` | Add an Attribute of type **Description** to the Resource.                 |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.load_tags()``                    | Load existing Tags into the Adversary object.                             |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.delete_tag(tag.name)``           | Add a delete flag to all Tags.                                            |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.add_tag('EXAMPLE')``             | Add a Tag to the Resource.                                                |
+----------------------------------------------+---------------------------------------------------------------------------+
| ``adversary.commit()``                       | Trigger API calls to write all added, deleted, or modified data.          |
+----------------------------------------------+---------------------------------------------------------------------------+
