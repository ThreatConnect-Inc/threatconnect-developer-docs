Retrieve Adversaries
^^^^^^^^^^^^^^^^^^^^

Retrieving a Single Adversary
"""""""""""""""""""""""""""""

This example demonstrates how to retrieve a specific Adversary using the Adversary's ID. The ``add_id`` filter specifies the ID of the Adversary which you would like to retrieve.

.. code-block:: python
    :emphasize-lines: 8-10,13-14

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Adversaries object
    adversaries = tc.adversaries()

    # set a filter to retrieve only the Adversary with ID: 123456
    filter1 = adversaries.add_filter()
    filter1.add_id(123456)

    try:
        # retrieve the Adversary
        adversaries.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Adversary (in this case there should only be one) and print its properties
    for adversary in adversaries:
        print(adversary.id)
        print(adversary.name)
        print(adversary.date_added)
        print(adversary.weblink)

Retrieving Multiple Adversaries
"""""""""""""""""""""""""""""""

This example demonstrates how to retrieve Adversaries while applying filters. Two filters are added: one for the Owner and another for a Tag. The result set returned from this example will contain all Adversaries in the "Example Community" Owner that have the **APT** Tag.

.. code-block:: python
    :emphasize-lines: 9-12,15-16

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Adversaries object
    adversaries = tc.adversaries()

    owner = 'Example Community'
    # set a filter to only retrieve Adversaries in the 'Example Community' tagged: 'APT'
    filter1 = adversaries.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('APT')

    try:
        # retrieve the Adversaries
        adversaries.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Adversaries and print their properties
    for adversary in adversaries:
        print(adversary.id)
        print(adversary.name)
        print(adversary.date_added)
        print(adversary.weblink)

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial <#advanced-filtering>`__.
