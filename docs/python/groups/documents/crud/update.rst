Update Documents
^^^^^^^^^^^^^^^^

The example below demonstrates how to update a Document Resource in the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 10-13,18-19

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Documents object
    documents = tc.documents()

    owner = 'Example Community'

    # create a Document with an updated name
    document = documents.add('Updated Document', owner)
    # set the ID of the new Document to the ID of the existing Document you want to update
    document.set_id(123456)

    # you can update the Document metadata as described here: https://docs.threatconnect.com/en/latest/python/python_sdk.html#group-metadata

    try:
        # update the Document
        document.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
