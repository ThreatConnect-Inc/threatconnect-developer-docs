Delete Documents
^^^^^^^^^^^^^^^^

The example below demonstrates how to delete a Document Resource from the
ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,18-19

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Documents object
    documents = tc.documents()

    owner = 'Example Community'

    # create an empty Document
    document = documents.add('', owner)
    # set the ID of the new Document to the ID of the Document you would like to delete
    document.set_id(123456)

    try:
        # delete the Document
        document.delete()
    except RuntimeError as e:
        print(e)
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``delete()`` method is invoked.
