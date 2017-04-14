Retrieve Documents
^^^^^^^^^^^^^^^^^^

Retrieving a Single Document
""""""""""""""""""""""""""""

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    documents = tc.documents()
    owner = 'Example Community'

    try:
        filter1 = documents.add_filter()
        filter1.add_id(123456)
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        documents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for document in documents:
        print(document.id)
        print(document.name)
        print(document.date_added)
        print(document.owner_name)
        print(document.weblink)
        
        # document specific property
        print(document.file_name)

This example demonstrates how to retrieve a specific Document using the Document's ID. The ``add_id`` filter specifies the ID of the Document which you would like to retrieve.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                              |
+==============================================+==========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``documents = tc.documents()``               | Instantiate a Documents container object.                                                |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1 = documents.add_filter()``         | Add a filter object to the Documents container object (support multiple filter objects). |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1.add_tag('EXAMPLE')``               | Add API filter to retrieve Documents with the 'Example' tag                              |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``documents.retrieve()``                     | Trigger the API request and retrieve the Documents intelligence data.                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``for document in documents:``               | Iterate over the Documents container object generator.                                   |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``print(document.id)``                       | Display the **'id'** property of the Document object.                                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+

Downloading a Document's Contents
+++++++++++++++++++++++++++++++++

Python SDK example of downloading the contents of the document stored
with the Document Resource:

.. code-block:: python
    :linenos:
    :no-test:

    document.download()
    if document.contents is not None:
        print(document.contents)

Continuing from the `Filter Example <#filter-example>`__, the example
will download the contents of the document stored with the Document
Resource.

Code Highlights

+---------------------------------------+--------------------------------------------------------------------------------------+
| Snippet                               | Description                                                                          |
+=======================================+======================================================================================+
| ``document.download()``               | Trigger API request to download the Document contents.                               |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``if document.contents is not None:`` | Validate the Document has downloaded before displaying.                              |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``print(document.contents)``          | Display the contents of the Document. (This should only be done for ASCII contents.) |
+---------------------------------------+--------------------------------------------------------------------------------------+

Retrieving Multiple Documents
"""""""""""""""""""""""""""""

The import statement and reading of the configuration files have been
replaced with ``...`` for brevity.

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    documents = tc.documents()
    owner = 'Example Community'

    try:
        filter1 = documents.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        documents.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for document in documents:
        print(document.id)
        print(document.name)
        print(document.date_added)
        print(document.owner_name)
        print(document.weblink)
        
        # document specific property
        print(document.file_name)

This example will demonstrate how to retrieve documents while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any documents in the **Example Community** Owner that has a Tag
of **EXAMPLE**.

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial </python/advanced/filtering/>`__.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                              |
+==============================================+==========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``documents = tc.documents()``               | Instantiate a Documents container object.                                                |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1 = documents.add_filter()``         | Add a filter object to the Documents container object (support multiple filter objects). |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1.add_tag('APT')``                   | Add API filter to retrieve Documents with the 'APT' tag                                  |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``documents.retrieve()``                     | Trigger the API request and retrieve the Documents intelligence data.                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``for document in documents:``               | Iterate over the Documents container object generator.                                   |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``print(document.id)``                       | Display the **'id'** property of the Document object.                                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
