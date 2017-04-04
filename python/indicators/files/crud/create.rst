Create Files
^^^^^^^^^^^^

The example below demonstrates how to create a File Indicator
Resource in the ThreatConnect platform:

.. code:: python

    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    indicators = tc.indicators()
        
    owner = 'Example Community'
    indicator = indicators.add('8743b52063cd84097a65d1633f5c74f5', owner) # MD5 hash of string `hashcat`
    indicator.set_indicator('b89eaac7e61417341b710b727768294d0e6a277b') #SHA1 hash of same string
    indicator.set_indicator('127e6fbfe24a750e72930c220a8e138275656b8e5d8f48a98c3c92df2caba935') # SHA256 hash of same string
    indicator.set_confidence(75)
    indicator.set_rating(2.5)
    indicator.set_size(112)

    indicator.add_attribute('Description', 'Example Attribute')
    indicator.add_tag('EXAMPLE')
    indicator.set_security_label('TLP Green')

    try:
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

The example demonstrates how to create a File Hash Indicator Resource in
the ThreatConnect platform. File Indicators support MD5, SHA1, and
SHA256 hashes. For more information on the purpose of each
line of code, see the **Code Highlights** section below.

Code Highlights

+---------------------------------------------+---------------------------------------------------------------------------------------+
| Snippet                                     | Description                                                                           |
+=============================================+=======================================================================================+
| ``tc = ThreatConnect(api_access_id,...``    | Instantiate the ThreatConnect object.                                                 |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator = indicators.add('8743b520...`` | Add an Indicator object setting the value and Owner.                                  |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_indicator('b89eaac7e61...`` | Add File addition File Hashes for this Indicator.                                     |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_indicator('127e6fbfe24...`` | Add File addition File Hashes for this Indicator.                                     |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_confidence(75)``            | Set the Confidence value for this Indicator.                                          |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_rating(2.5)``               | Set the Rating value for this Indicator.                                              |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_size(112)``                 | Set the File size property of the Indicator.                                          |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.add_attribute('Description...`` | Add an Attribute of type **Description** to the Resource.                             |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.add_tag('EXAMPLE')``            | Add a Tag to the Indicator.                                                           |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.set_security_label('TLP Gre..`` | Add a Security Label to the Indicator.                                                |
+---------------------------------------------+---------------------------------------------------------------------------------------+
| ``indicator.commit()``                      | Trigger multiple API calls to write Indicator, Attributes, Security Labels, and Tags. |
+---------------------------------------------+---------------------------------------------------------------------------------------+

Adding File Occurrences
"""""""""""""""""""""""

A File occurrence can be added to File Indicators by inserting the
example code below into the previous code snippet before the ``indicator.commit()`` method is called:

.. code:: python

    fo_date = (datetime.isoformat(datetime(2015, 3, 29))) + 'Z'
    indicator.add_file_occurrence('badfile.exe', 'C:\windows', fo_date)
