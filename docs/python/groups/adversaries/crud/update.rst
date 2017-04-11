Update Adversaries
^^^^^^^^^^^^^^^^^^

The example below demonstrates how to update an Adversary Resource in
the ThreatConnect platform:

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    adversaries = tc.adversaries()

    owner = 'Example Community'
    adversary = adversaries.add('Updated Adversary', owner)
    adversary.set_id(20)

    adversary.load_attributes()
    for attribute in adversary.attributes:
        if attribute.type == 'Description':
            adversary.delete_attribute(attribute.id)

    adversary.add_attribute('Description', 'Updated Description')

    adversary.load_tags()
    for tag in adversary.tags:
        adversary.delete_tag(tag.name)

    adversary.add_tag('EXAMPLE')

    try:
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
