Retrieve Signatures
^^^^^^^^^^^^^^^^^^^

Retrieving a Single Signature
"""""""""""""""""""""""""""""

The import statement and reading of the configuration files have been replaced with ``...`` for brevity.

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    signatures = tc.signatures()
    owner = 'Example Community'

    try:
        filter1 = signatures.add_filter()
        filter1.add_id(123456)
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        signatures.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for signature in signatures:
        print(signature.id)
        print(signature.name)
        print(signature.date_added)
        print(signature.weblink)

This example demonstrates how to retrieve a specific Signature using the Signature's ID. The ``add_id`` filter specifies the ID of the Signature which you would like to retrieve.

Code Highlights

+----------------------------------------------+------------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                              |
+==============================================+==========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``signatures = tc.signatures()``             | Instantiate an Signature container object.                                               |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1 = signatures.add_filter()``        | Add a filter object to the Signature container object (support multiple filter objects). |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``filter1.add_id(123456)``                   | Add API filter to retrieve the Signature with the ID: 123456                             |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``signatures.retrieve()``                    | Trigger the API request and retrieve the Signature intelligence data.                    |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``for signature in signatures:``             | Iterate over the Signature container object generator.                                   |
+----------------------------------------------+------------------------------------------------------------------------------------------+
| ``print(signature.id)``                      | Display the **'id'** property of the Signature object.                                   |
+----------------------------------------------+------------------------------------------------------------------------------------------+

Downloading a Signature's Content
+++++++++++++++++++++++++++++++++

Example Python SDK downloading the Signature contents for the Signature
Resource:

.. code-block:: python
    :linenos:

    signature.download()
    if signature.contents is not None:
        print(signature.contents)

Download the Signature contents for the Signature Resource.

Code Highlights

+----------------------------------------+---------------------------------------------------------------+
| Snippet                                | Description                                                   |
+========================================+===============================================================+
| ``signature.download()``               | Trigger API request to download the Signature contents.       |
+----------------------------------------+---------------------------------------------------------------+
| ``if signature.contents is not None:`` | Validate that the Signature has downloaded before displaying. |
+----------------------------------------+---------------------------------------------------------------+
| ``print(signature.contents)``          | Display the contents of the Signature.                        |
+----------------------------------------+---------------------------------------------------------------+

Retrieving Multiple Signatures
""""""""""""""""""""""""""""""

The import statement and reading of the configuration files have been replaced with ``...`` for brevity.

.. code-block:: python
    :linenos:

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    signatures = tc.signatures()
    owner = 'Example Community'

    try:
        filter1 = signatures.add_filter()
        filter1.add_owner(owner)
        filter1.add_tag('APT')
    except AttributeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

    try:
        signatures.retrieve()
    except RuntimeError as e:
        print('Error: {0}'.format(e))

    for signature in signatures:
        print(signature.id)
        print(signature.name)
        print(signature.date_added)
        print(signature.weblink)

This example will demonstrate how to retrieve Signatures while applying
filters. In this example, two filters will be added, one for the Owner
and another for a Tag. The result set returned from this example will
contain any Signatures in the **Example Community** Owner that has a Tag
of **EXAMPLE**.

.. note:: The ``filter1`` object contains a ``filters`` property that provides a list of supported filters for the resource type being retrieved. To display this list, ``print(filter1.filters)`` can be used. For more on using filters see the `Advanced Filter Tutorial </python/advanced/filtering/>`__.

Code Highlights

+----------------------------------------------+-------------------------------------------------------------------------------------------+
| Snippet                                      | Description                                                                               |
+==============================================+===========================================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                                     |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``signatures = tc.signatures()``             | Instantiate an Signatures container object.                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``filter1 = signatures.add_filter()``        | Add a filter object to the Signatures container object (support multiple filter objects). |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``filter1.add_tag('APT')``                   | Add API filter to retrieve Signatures with the 'APT' tag.                                 |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``signatures.retrieve()``                    | Trigger the API request and retrieve the Signatures intelligence data.                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``for signature in signatures:``             | Iterate over the Signatures container object generator.                                   |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``print(signature.id)``                      | Display the **'id'** property of the Signature object.                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
