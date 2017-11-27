Create Documents
^^^^^^^^^^^^^^^^

The example below demonstrates how to create a Document Resource in the ThreatConnect platform.

.. code-block:: python
    :emphasize-lines: 12-14,16-20,30-31

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
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

**Supported Properties**

+---------------+-----------------+----------+
| Property Name | Method          | Required |
+===============+=================+==========+
| file\_name    | set\_file\_name | True     |
+---------------+-----------------+----------+
| malware       | set\_malware    | False    |
+---------------+-----------------+----------+
| password      | set\_password   | False    |
+---------------+-----------------+----------+

Create Malware Document
^^^^^^^^^^^^^^^^^^^^^^^

To `create a malware document <http://kb.threatconnect.com/customer/en/portal/articles/2171402-uploading-malware>`_  in ThreatConnect, make use of the ``set_malware`` and ``set_password`` functions as demonstrated below:

.. code-block:: python
    :emphasize-lines: 22-24

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Documents object 
    documents = tc.documents()

    owner = 'Example Community'

    # create a new Document in 'Example Community' with the name: 'New Document'
    document = documents.add('Malicious File', owner)
    document.set_file_name('bad.exe')

    # open a file handle for a local file and read the contents thereof
    fh = open('./bad.exe.zip', 'rb')
    contents = fh.read()
    # upload the contents of the file into the Document
    document.upload(contents)

    document.set_malware(True)
    # set the archive password for the zip (the default is "TCinfected")
    document.set_password("TCinfected")

    try:
        # create the Document
        document.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.
