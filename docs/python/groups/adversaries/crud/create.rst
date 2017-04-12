Create Adversaries
^^^^^^^^^^^^^^^^^^

Example Python SDK creating an adversary resource in the ThreatConnect
platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 10,12,14,16,20

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)
    owner = 'Example Community'

    # instantiate Adversaries container
    adversaries = tc.adversaries()

    # create a new adversary in 'Example Community' with the name: 'New Adversary'
    adversary = adversaries.add('New Adversary', owner)
    # add a description attribute
    adversary.add_attribute('Description', 'Description Example')
    # add a tag
    adversary.add_tag('EXAMPLE')
    # add a security label
    adversary.set_security_label('TLP Green')

    try:
        # create the adversary
        adversary.commit()
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
| ``adversaries = tc.adversaries()``           | Instantiate an Adversaries container object.                     |
+----------------------------------------------+------------------------------------------------------------------+
| ``adversary = adversaries.add('New Adve...`` | Add a resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``adversary.add_attribute('Description'...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``adversary.add_tag('EXAMPLE')``             | Add a Tag to the Adversary.                                      |
+----------------------------------------------+------------------------------------------------------------------+
| ``adversary.set_security_label('TLP Gre...`` | Add a Security Label to the Adversary.                           |
+----------------------------------------------+------------------------------------------------------------------+
| ``resource.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+
