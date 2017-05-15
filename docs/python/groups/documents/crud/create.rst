Create Documents
^^^^^^^^^^^^^^^^

The example below demonstrates how to a Document Resource in the
ThreatConnect platform.

.. code-block:: python
    :emphasize-lines: 11-13,15-19,29-30

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Documents object 
    documents = tc.documents()

    owner = 'Example Community'
    # create a new Document in 'Example Community' with the name: 'New Document'
    document = documents.add('New Document', owner)
    document.set_file_name('New File.txt')

    # open a file handle for a local file and read the contents thereof
    fh = open('./sample1.zip', 'rb')
    contents = fh.read()
    # upload the contents of the file into the Document
    document.upload(contents)

    # add a description attribute
    document.add_attribute('Description', 'Description Example')
    # add a tag
    document.add_tag('Example')
    # add a security label
    document.set_security_label('TLP Green')

    try:
        # create the Document
        document.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

Adding Document Resources
+++++++++++++++++++++++++

The example demonstrates how to a Document Resource in the ThreatConnect
platform. The Document Resource has a special method ``upload()`` that
allows you to upload files to the platform. For more information on the
purpose of each line of code, see the **Code Highlights** section below.

**Supported Properties**

+-----------------+-------------------+------------+
| Property Name   | Method            | Required   |
+=================+===================+============+
| file\_name      | set\_file\_name   | True       |
+-----------------+-------------------+------------+

Code Highlights

+----------------------------------------------+------------------------------------------------------------------+
| Snippet                                      | Description                                                      |
+==============================================+==================================================================+
| ``tc = ThreatConnect(api_access_id, api...`` | Instantiate the ThreatConnect object.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``documents = tc.documents()``               | Instantiate a Documents container object.                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``document = documents.add('New Documen...`` | Add a resource object setting the name and Owner.                |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.set_file_name('New File.txt')``   | **(REQUIRED)** Set the Document file name.                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``fh = open('./sample1.zip', 'rb')``         | Open the file handle.                                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``contents = fh.read()``                     | Read contents of file from file handle.                          |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.upload(contents)``                | **Upload** file contents.                                        |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.add_attribute('Description',...`` | Add an Attribute of type **Description** to the Resource.        |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.add_tag('EXAMPLE')``              | Add a Tag to the Document.                                       |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.set_security_label('TLP Green')`` | Add a Security Label to the Document.                            |
+----------------------------------------------+------------------------------------------------------------------+
| ``document.commit()``                        | Trigger API calls to write all added, deleted, or modified data. |
+----------------------------------------------+------------------------------------------------------------------+
