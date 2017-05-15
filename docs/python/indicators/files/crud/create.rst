Create Files
^^^^^^^^^^^^

The example below demonstrates how to create a File Indicator in the ThreatConnect platform:

.. code-block:: python
    :emphasize-lines: 12-15,29-30

    # replace the line below with the standard, TC script heading described here:
    # https://docs.threatconnect.com/en/dev/python/python_sdk.html#standard-script-heading
    ...

    tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

    # instantiate Indicators object
    indicators = tc.indicators()

    owner = 'Example Community'

    # create a new Indicator in the given owner
    indicator = indicators.add('8743b52063cd84097a65d1633f5c74f5', owner) # MD5 hash of string 'hashcat'
    indicator.set_indicator('b89eaac7e61417341b710b727768294d0e6a277b') #SHA1 hash of same string
    indicator.set_indicator('127e6fbfe24a750e72930c220a8e138275656b8e5d8f48a98c3c92df2caba935') # SHA256 hash of same string
    # set the confidence rating for the Indicator
    indicator.set_confidence(75)
    # set the threat rating for the Indicator
    indicator.set_rating(2.5)

    # add a description attribute
    indicator.add_attribute('Description', 'Description Example')
    # add a tag
    indicator.add_tag('Example')
    # add a security label
    indicator.set_security_label('TLP Green')

    try:
        # create the Indicator
        indicator.commit()
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)

.. note:: In the prior example, no API calls are made until the ``commit()`` method is invoked.

.. note:: File Indicators in ThreatConnect support MD5, SHA1, and SHA256 hashes.

Adding File Occurrences
"""""""""""""""""""""""

A File occurrence can be added to File Indicators using the ``add_file_occurrence`` function which takes parameters in the following format: ``add_file_occurrence(<file_name>, <run_path>, <date>)``. Inserting the example code below into the previous code snippet before the ``indicator.commit()`` method will add a File occurrence.

.. 
    no-test

.. code-block:: python

    from datetime import datetime

    # set the date of the file occurrence (this example uses the current datetime stamp)
    fo_date = (datetime.isoformat(datetime.today())) + 'Z'

    # add a file occurrence with the following data: add_file_occurrence(<file_name>, <run_path>, <date>)
    indicator.add_file_occurrence('badfile.exe', 'C:\windows', fo_date)

.. note:: A File occurrence will only be added to a File Indicator if the ``indicator.add_file_occurrence(...)`` function is followed by an ``indicator.commit()``.
