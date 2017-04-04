Delete Adversaries
^^^^^^^^^^^^^^^^^^

The example below demonstrates how to delete an Adversary Resource in
the ThreatConnect platform:

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    adversaries = tc.adversaries()

    adversary = adversaries.add('', owner)
    adversary.set_id(20)

    try:
        adversary.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------------+
| Snippet                                      | Description                                                             |
+==============================================+=========================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                   |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``adversaries = tc.adversaries()``           | Instantiate an Adversaries container object.                            |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``adversary = adversaries.add('', owner)``   | Add a resource object setting the name and Owner.                       |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``adversary.set_id(20)``                     | Set the ID of the Adversary to the **EXISTING** Adversary ID to delete. |
+----------------------------------------------+-------------------------------------------------------------------------+
| ``adversary.delete()``                       | Trigger API calls to write all added, deleted, or modified data.        |
+----------------------------------------------+-------------------------------------------------------------------------+
