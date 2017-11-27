Retrieve Documents
^^^^^^^^^^^^^^^^^^

Retrieving a Single Document
""""""""""""""""""""""""""""

This example demonstrates how to retrieve a specific Document using the Document's ID. The ``add_id`` filter specifies the ID of the Document which you would like to retrieve.

.. code-block:: python
    :emphasize-lines: 10-12,15-16

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Documents object
    documents = tc.documents()

    # set a filter to retrieve only the Document with ID: 123456
    filter1 = documents.add_filter()
    filter1.add_id(123456)

    try:
        # retrieve the Document
        documents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    # iterate through the retrieved Documents (in this case there should only be one) and print its properties
    for document in documents:
        print(document.id)
        print(document.name)
        print(document.date_added)
        print(document.owner_name)
        print(document.weblink)

        # Document specific property
        print(document.file_name)

Downloading a Document's Contents
+++++++++++++++++++++++++++++++++

Python SDK example of downloading the contents of the document stored
with the Document Resource:

.. 
    no-test

.. code-block:: python

    document.download()
    if document.contents is not None:
        print(document.contents)

Retrieving Multiple Documents
"""""""""""""""""""""""""""""

This example will demonstrate how to retrieve documents while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any documents in the **Example Community** Owner that has a Tag
of **EXAMPLE**.

.. code-block:: python
    :emphasize-lines: 12-15,18-19

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Documents object
    documents = tc.documents()

    owner = 'Example Community'

    # set a filter to only retrieve Documents in the 'Example Community' tagged: 'Nation State'
    filter1 = documents.add_filter()
    filter1.add_owner(owner)
    filter1.add_tag('Nation State')

    try:
        # retrieve the Documents
        documents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    # iterate through the retrieved Documents and print their properties
    for document in documents:
        print(document.id)
        print(document.name)
        print(document.date_added)
        print(document.owner_name)
        print(document.weblink)

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial <https://docs.threatconnect.com/en/latest/python/advanced.html#advanced-filtering>`__.
