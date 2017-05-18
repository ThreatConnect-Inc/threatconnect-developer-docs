Create Signatures
^^^^^^^^^^^^^^^^^

The example below demonstrates how to create a Signature Resource in the
ThreatConnect platform.

.. code-block:: python
    :emphasize-lines: 11-12,14-22,24-29,39-40

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Signatures object
    signatures = tc.signatures()
        
    owner = 'Example Community'
    # create a new Signature in 'Example Community' with the name: 'New Signature'
    signature = signatures.add('New Signature', owner)

    # define Signature's content
    file_text = 'rule example_sig : example\n{\n'
    file_text += 'meta:\n        description = "This '
    file_text += 'is just an example"\n\n '
    file_text += 'strings:\n        $a = {6A 40 68 00 '
    file_text += '30 00 00 6A 14 8D 91}\n        $b = '
    file_text += '{8D 4D B0 2B C1 83 C0 27 99 6A 4E '
    file_text += '59 F7 F9}\n    condition:\n '
    file_text += '$a or $b\n}'

    # set the file name of the Signature
    signature.set_file_name('bad_file.txt')  # REQUIRED
    # set the type of the Signature
    signature.set_file_type('YARA')  # REQUIRED
    # set the contents of the signature
    signature.set_file_text(file_text)  # REQUIRED

    # add a description attribute
    signature.add_attribute('Description', 'Description Example')
    # add a tag
    signature.add_tag('Example')
    # add a security label
    signature.set_security_label('TLP Green')

    try:
        # create the Signature
        signature.commit()
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
| file\_text    | set\_file\_text | True     |
+---------------+-----------------+----------+
| file\_type    | set\_file\_type | True     |
+---------------+-----------------+----------+
