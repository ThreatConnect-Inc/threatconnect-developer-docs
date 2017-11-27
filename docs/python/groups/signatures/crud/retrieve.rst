Retrieve Signatures
^^^^^^^^^^^^^^^^^^^

Retrieving a Single Signature
"""""""""""""""""""""""""""""

This example demonstrates how to retrieve a specific Signature using the Signature's ID. The ``add_id`` filter specifies the ID of the Signature which you would like to retrieve.

.. code-block:: python
   :emphasize-lines: 10-12,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Signatures object
    signatures = tc.signatures()

    # set a filter to retrieve only the Signature with ID: 123456
    filter1 = signatures.add_filter()
    filter1.add_id(123456)

    try:
        # retrieve the Signature
        signatures.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Signatures (in this case there should only be one) and print its properties
    for signature in signatures:
        print(signature.id)
        print(signature.name)
        print(signature.date_added)
        print(signature.weblink)

        # Signature specific property
        print(signature.type)

        print('')

Downloading a Signature's Content
+++++++++++++++++++++++++++++++++

Example Python code for downloading the Signature contents for the Signature Resource:

.. 
    no-test

.. code-block:: python

    signature.download()

    if signature.contents is not None:
        print(signature.contents)

Retrieving Multiple Signatures
""""""""""""""""""""""""""""""

This example will demonstrate how to retrieve Signatures while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Signatures in the **Example Community** Owner that has a Tag
of **EXAMPLE**.

.. code-block:: python
    :emphasize-lines: 12-15,18-19

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Signatures object
    signatures = tc.signatures()

    owner = 'Example Community'

    # set a filter to only retrieve Signatures in the 'Example Community' tagged: 'Nation State'
    filter1 = signatures.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('Nation State')

    try:
        # retrieve the Signatures
        signatures.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    # iterate through the retrieved Signatures and print their properties
    for signature in signatures:
        print(signature.id)
        print(signature.name)
        print(signature.date_added)
        print(signature.weblink)
        print('')

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial <https://docs.threatconnect.com/en/latest/python/advanced.html#advanced-filtering>`__.
