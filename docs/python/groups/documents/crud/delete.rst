Delete Documents
^^^^^^^^^^^^^^^^

The example below demonstrates how to delete a Document Resource from the
ThreatConnect platform:

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-12,15-16

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Documents container
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

Code Highlights

+----------------------------------------------+-----------------------------------------------------------------------+
| Snippet                                      | Description                                                           |
+==============================================+=======================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``documents = tc.documents()``               | Instantiate a Documents container object.                             |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``document = documents.add('', owner)``      | Add a Resource object setting the name and Owner.                     |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``document.set_id(20)``                      | Set the ID of the Document to the **EXISTING** Document ID to delete. |
+----------------------------------------------+-----------------------------------------------------------------------+
| ``document.delete()``                        | Trigger API calls to write all added, deleted, or modified data.      |
+----------------------------------------------+-----------------------------------------------------------------------+
